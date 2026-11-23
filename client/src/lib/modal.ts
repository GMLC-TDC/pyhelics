// Runner and broker controls can appear after an API refresh. Register the
// delegated modal handlers when a trigger is mounted.
export function enableModal() {
  void import("tw-elements").then(({ Modal, initTWE }) => initTWE({ Modal }));
}
