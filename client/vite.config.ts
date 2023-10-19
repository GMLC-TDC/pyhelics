import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';
import { searchForWorkspaceRoot } from 'vite';

export default defineConfig({
    plugins: [sveltekit()],
    test: {
        include: ['src/**/*.{test,spec}.{js,ts}']
    },
    server: {
        proxy: {
            '/helics': { target: 'http://localhost:43542', changeOrigin: true }
        },
        fs: {
            allow: [
                // search up for workspace root
                searchForWorkspaceRoot(process.cwd())
                // your custom rules
                // '/path/to/custom/allow',
            ]
        }
    }
});
