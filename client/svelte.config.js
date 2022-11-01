import preprocess from "svelte-preprocess";
import adapterStatic from "@sveltejs/adapter-static";

function adapter(options) {
  const baseStatic = adapterStatic(options);
  return {
    name: "svelte-adapter-static",
    async adapt(builder) {
      await baseStatic.adapt(builder);
    },
  };
}

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: [
    preprocess({
      postcss: true,
    }),
  ],

  kit: {
    adapter: adapter({
      fallback: "index.html",
    }),
  },
};

export default config;
