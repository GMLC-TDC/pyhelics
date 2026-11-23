import { expect, test } from '@playwright/test';

test('index page exposes the combined HELICS UI', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle('HELICS Web Interface');
    for (const route of ['/run', '/observe', '/profile', '/broker']) {
        await expect(page.locator(`a[href="${route}"]`).first()).toBeVisible();
    }
});

test('broker controls reach the managed broker through the packaged UI', async ({ page, request }) => {
    const name = 'ui-' + crypto.randomUUID();
    const brokers = '/api/v1/brokers';
    const created = await request.post(brokers, { data: { name, core_type: 'inproc' } });
    expect(created.status(), await created.text()).toBe(201);
    try {
        await page.goto('/');
        await page.getByRole('link', { name: 'Broker', exact: true }).first().click();
        await expect(page.getByRole('heading', { name: 'Name: ' + name })).toBeVisible();
        await page.getByRole('button', { name: 'Set Barrier' }).click();
        const dialog = page.getByRole('dialog').filter({ has: page.locator('#broker-barrier-time-input') });
        await expect(dialog).toBeVisible();
        await dialog.locator('input').fill('4');
        const barrier = page.waitForResponse(r => r.url().endsWith('/time-barrier') && r.request().method() === 'PUT');
        await dialog.getByRole('button', { name: /set|save/i }).click();
        expect((await barrier).status()).toBe(200);
        await expect(page.getByRole('button', { name: 'Clear Barrier' })).toBeVisible();
    } finally {
        await request.delete(brokers + '/' + name);
    }
});

test('runner, observer, and profiler load from direct links', async ({ page }) => {
    for (const route of ['/run', '/observe', '/profile']) {
        const response = await page.goto(route);
        expect(response.status()).toBe(200);
        await expect(page.locator('input[type=file]')).toHaveCount(1);
    }
});

test('profiler draws a recorded federate interval', async ({ page }) => {
    await page.route('**/api/v1/profile', route => route.fulfill({
        json: { sender: [{ name: 'sender', s_enter: 1, s_end: 2, r_enter: 3, r_end: 4 }] }
    }));
    await page.goto('/profile');
    await expect(page.locator('svg rect title')).toHaveText(/sender.*1\.00s/);
});
