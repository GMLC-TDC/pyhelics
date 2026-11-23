/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    webServer: {
        command: 'helics server --no-open --port 8300',
        url: 'http://127.0.0.1:8300/api/v1/health'
    },
    use: { baseURL: 'http://127.0.0.1:8300' }
};

export default config;
