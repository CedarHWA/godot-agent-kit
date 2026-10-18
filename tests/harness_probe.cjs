// Run using the installed Desktop's Electron Node runtime (ELECTRON_RUN_AS_NODE=1),
// or Node with --module pointing at an installed Harness skill-filesystem module.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

(async () => {
  const [modulePath, project, isolatedHome, expectedRoot = project, expectedJson] = process.argv.slice(2);
  const expectedLocations = expectedJson ? JSON.parse(expectedJson) : undefined;
  if (!modulePath || !project || !isolatedHome) throw new Error('module path, project and isolated home required');
  const { FileSystemSkillProvider } = await import(pathToFileURL(modulePath).href);
  const warnings = [];
  const controller = new AbortController();
  const provider = new FileSystemSkillProvider(
    { get: () => undefined, logger: { warn: (value) => warnings.push(String(value)) } },
    { signal: controller.signal, invalidate: () => {} },
    { watch: false, dshHome: isolatedHome, agentsHome: path.join(isolatedHome, 'agents'),
      bundledSkillDir: path.join(isolatedHome, 'bundled') });
  try {
    const discovered = await provider.list({ cwd: project });
    const candidates = Array.isArray(discovered) ? discovered : discovered.candidates;
    const inRoot = candidate => {
      const relative = path.relative(expectedRoot, candidate.path);
      return !path.isAbsolute(relative) && relative !== '..' && !relative.startsWith('..' + path.sep);
    };
    const selected = candidates.filter(c => ['godot-project-init', 'godot-dev'].includes(c.name) && inRoot(c));
    const names = expectedLocations ? Object.keys(expectedLocations) : ['godot-project-init', 'godot-dev'];
    if (selected.length !== names.length) throw new Error(`Unexpected skill count: ${JSON.stringify(selected)}`);
    const rows = [];
    for (const name of names) {
      const candidate = selected.find(c => c.name === name);
      if (!candidate) throw new Error(`Skill not discovered from project: ${name}; ${JSON.stringify(warnings)}`);
      if (expectedLocations && path.relative(expectedLocations[name], candidate.path) !== '') {
        throw new Error(`Skill discovered from unexpected scope: ${name}; ${candidate.path}`);
      }
      const skill = await provider.get(candidate, { signal: controller.signal });
      if (!skill.content || !skill.description || !fs.existsSync(path.join(skill.resourceBase.path, 'references'))) {
        throw new Error(`Incomplete skill load: ${name}`);
      }
      rows.push({ name, source: candidate.source, bodyLoaded: true, resourcesPresent: true });
    }
    console.log(JSON.stringify({ passed: true, skills: rows, warnings }));
  } finally {
    await provider.dispose();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
