import { fileURLToPath } from "node:url";
import js from "@eslint/js";
import typescript from "@typescript-eslint/eslint-plugin";
import prettier from "eslint-config-prettier";
import { defineConfig, globalIgnores, includeIgnoreFile } from "eslint/config";
import globals from "globals";

export default defineConfig([
  includeIgnoreFile(fileURLToPath(new URL(".gitignore", import.meta.url))),
  globalIgnores(["**/*.cjs"]),
  {
    files: ["**/*.{js,mjs,ts}"],
    extends: [js.configs.recommended, typescript.configs["flat/recommended"], prettier],
    languageOptions: {
      ecmaVersion: 2020,
      sourceType: "module",
      globals: { ...globals.browser, ...globals.node },
    },
  },
]);
