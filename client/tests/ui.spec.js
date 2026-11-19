import { expect, test } from '@playwright/test';

test('index page exposes the combined HELICS UI', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle('HELICS Web Interface');
    for (const route of ['/run', '/observe', '/profile', '/broker']) {
        await expect(page.locator(`a[href="${route}"]`).first()).toBeVisible();
    }
});
