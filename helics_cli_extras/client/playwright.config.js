/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    webServer: {
        command: 'npm run build && npx vite preview --outDir build --port 3000',
        port: 3000
    }
};

export default config;
