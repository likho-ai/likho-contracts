// Checks that the event contracts are consistent:
//   1. every schema compiles (JSON Schema 2020-12);
//   2. every event in streams.yaml has a schema and an example;
//   3. every example is a valid CloudEvent and its data matches the schema of its type;
//   4. every event's subject is captured by exactly one stream, the one streams.yaml names.
import { readFileSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';
import { parse } from 'yaml';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const eventsDir = join(root, 'events');
const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'));

const ajv = new Ajv2020({ allErrors: true, strict: true });
addFormats(ajv);

const problems = [];
const fail = (message) => problems.push(message);

const envelope = ajv.compile(readJson(join(eventsDir, 'cloudevent.schema.json')));
const layout = parse(readFileSync(join(root, 'streams.yaml'), 'utf8'));

// NATS wildcard match: "*" is one token, ">" is the rest.
const matches = (pattern, subject) => {
  const p = pattern.split('.');
  const s = subject.split('.');
  for (let i = 0; i < p.length; i += 1) {
    if (p[i] === '>') return true;
    if (s[i] === undefined || (p[i] !== '*' && p[i] !== s[i])) return false;
  }
  return p.length === s.length;
};

const schemaFiles = readdirSync(eventsDir).filter((f) => f.endsWith('.schema.json') && f !== 'cloudevent.schema.json');
const known = new Set(Object.keys(layout.events));

for (const file of schemaFiles) {
  const type = file.replace('.schema.json', '');
  if (!known.has(type)) fail(`${file}: not listed in streams.yaml`);
}

for (const [type, spec] of Object.entries(layout.events)) {
  let validate;
  try {
    validate = ajv.compile(readJson(join(eventsDir, `${type}.schema.json`)));
  } catch (error) {
    fail(`${type}: schema missing or invalid (${error.message})`);
    continue;
  }

  const capturing = Object.entries(layout.streams)
    .filter(([, stream]) => stream.subjects.some((pattern) => matches(pattern, spec.subject)))
    .map(([name]) => name);
  if (capturing.length !== 1 || capturing[0] !== spec.stream) {
    fail(`${type}: subject ${spec.subject} is captured by [${capturing.join(', ')}], expected exactly [${spec.stream}]`);
  }

  let example;
  try {
    example = readJson(join(eventsDir, 'examples', `${type}.json`));
  } catch {
    fail(`${type}: no example in events/examples`);
    continue;
  }
  if (!envelope(example)) fail(`${type}: example envelope: ${ajv.errorsText(envelope.errors)}`);
  if (example.type !== type) fail(`${type}: example has type ${example.type}`);
  if (example.source !== spec.producer) fail(`${type}: example source ${example.source}, producer is ${spec.producer}`);
  if (!validate(example.data)) fail(`${type}: example data: ${ajv.errorsText(validate.errors)}`);
}

if (problems.length > 0) {
  console.error(problems.map((p) => `  x ${p}`).join('\n'));
  process.exit(1);
}
console.log(`ok: ${known.size} events, ${Object.keys(layout.streams).length} streams, examples valid`);
