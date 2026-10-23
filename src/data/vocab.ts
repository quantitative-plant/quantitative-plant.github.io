// Vocabulaires contrôlés : un seul endroit pour les libellés affichés et l'ordre des filtres.
export const ORGANS: Record<string, string> = {
  'root-system': 'Root system', 'single-root': 'Single root', leaf: 'Leaf', rosette: 'Rosette',
  shoot: 'Shoot', canopy: 'Canopy', hypocotyl: 'Hypocotyl', stem: 'Stem', tissue: 'Tissue', flower: 'Flower', fruit: 'Fruit',
  seed: 'Seed', pollen: 'Pollen', cell: 'Cell', fungi: 'Fungi', plant: 'Whole plant', general: 'General', simulation: 'Simulation',
};
export const PLATFORMS: Record<string, string> = {
  windows: 'Windows', macos: 'macOS', linux: 'Linux', web: 'Web', ios: 'iOS', android: 'Android',
};
export const LICENSES: Record<string, string> = {
  'open-source': 'Open source', freeware: 'Free', commercial: 'Commercial', 'on-request': 'On request',
};
export const AUTOMATION: Record<string, string> = {
  automated: 'Automated', 'semi-automated': 'Semi-automated', manual: 'Manual',
};
export const STATUS: Record<string, string> = {
  active: 'Active', unverified: 'Not verified recently', unmaintained: 'Unmaintained', deprecated: 'Deprecated',
};
export const label = (dict: Record<string, string>, k: string) =>
  dict[k] ?? k.replace(/-/g, ' ').replace(/^\w/, (c) => c.toUpperCase());
export const SCALES: Record<string, string> = {
  cell: 'Cell', organ: 'Organ', 'whole-plant': 'Whole plant', field: 'Field', regional: 'Regional', global: 'Global',
};
export const MODEL_CATEGORIES: Record<string, string> = {
  FSPM: 'Functional–structural plant model', FSM: 'Functional–structural model', FPM: 'Functional plant model',
  SPM: 'Structural plant model', CSM: 'Crop simulation model', gbCSM: 'Gene-based crop model',
  ODE: 'Ordinary differential equations', PDE: 'Partial differential equations',
};
