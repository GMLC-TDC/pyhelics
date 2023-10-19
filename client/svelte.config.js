import adapter from "@sveltejs/adapter-static";
import {vitePreprocess} from "@sveltejs/kit/vite";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: [vitePreprocess({})],

  kit: {
    adapter: adapter({
      fallback: "index.html",
    }),
    alias: {
      '~': './src',
      '~/*': './src/*',
      $components: './src/lib/components',
      '$components/*': './src/lib/components/*',
    },
    prerender: {
      handleHttpError: ({ path, message }) => {
        // Allow routing to
        const allowed_routes = ['/helics'];
        if (allowed_routes.some((prefix) => path.toLowerCase().startsWith(prefix.toLowerCase()))) {
          return;
        }

        throw new Error(message);
      }
    }
  },
};

export default config;
