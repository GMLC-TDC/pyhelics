import { browser } from "$app/env";
import type { Writable } from "svelte/store";
import { writable, get, derived } from "svelte/store";

const storage = <T>(key: string, initValue: T): Writable<T> => {
  const store = writable(initValue);
  if (!browser) return store;

  const storedValueStr = localStorage.getItem(key);
  if (storedValueStr != null) store.set(JSON.parse(storedValueStr));

  store.subscribe((val) => {
    if ([null, undefined].includes(val)) {
      localStorage.removeItem(key);
    } else {
      localStorage.setItem(key, JSON.stringify(val));
    }
  });

  window.addEventListener("storage", () => {
    const storedValueStr = localStorage.getItem(key);
    if (storedValueStr == null) return;

    const localValue: T = JSON.parse(storedValueStr);
    if (localValue !== get(store)) store.set(localValue);
  });

  return store;
};

export default storage;

export const DEFAULT = {
  profile: [],
  runner: {},
  federates: [],
  cores: [],
  systeminfo: {},
  graphs: {},
  publications: [],
  inputs: [],
  table: [],
  table_columns: [],
  cores_columns: [
    {
      field: "id",
      sortName: "id",
      title: "ID",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "name",
      sortName: "name",
      title: "Name",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "address",
      sortName: "address",
      title: "Address",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
  ],
  federates_columns: [
    {
      field: "id",
      sortName: "id",
      title: "ID",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "name",
      sortName: "name",
      title: "Name",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "core_name",
      sortName: "core_name",
      title: "Core Name",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
  ],
  inputs_columns: [
    {
      field: "id",
      sortName: "id",
      title: "ID",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "source_name",
      sortName: "source_name",
      title: "Source",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "target_name",
      sortName: "target_name",
      title: "Target",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
  ],
  publications_columns: [
    {
      field: "id",
      sortName: "id",
      title: "ID",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "name",
      sortName: "name",
      title: "Name",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "source_name",
      sortName: "source_name",
      title: "Source",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
    {
      field: "target_name",
      sortName: "target_name",
      title: "Target",
      show: true,
      sort: "ascending",
      sortColor: "#fff",
      sortActive: true,
      text_center: false,
    },
  ],
};

export const data = storage("data", DEFAULT);
