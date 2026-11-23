import { sveltekit } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

export default defineConfig({
    server: { proxy: { '/api': 'http://127.0.0.1:8000' } },
    plugins: [sveltekit({
        adapter: adapter({ fallback: 'index.html' }),
        preprocess: vitePreprocess()
    })]
});
