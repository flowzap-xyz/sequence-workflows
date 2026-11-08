from __future__ import annotations

import csv
import json
import os
import re
import shutil
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FLOWZAP_APP_ROOT = Path(
    os.environ.get('FLOWZAP_APP_ROOT') or (REPO_ROOT.parent / 'FlowZap-App-v5')
)
TEMPLATES_INDEX_PATH = FLOWZAP_APP_ROOT / 'src' / 'templateLibrary' / 'templatesIndex.json'
TEMPLATE_FILES_DIR = FLOWZAP_APP_ROOT / 'public' / 'template-files'
SITEMAP_URL = 'https://flowzap.xyz/sitemap-templates.xml'

USE_CASES = [
    {
        'id': 'handoff',
        'labels': {'en': 'Handoff', 'fr': 'Transfert', 'zh': '交接'},
        'keywords': ['handoff', 'handover', 'transfer', 'escalation', 'routing', 'handoff degradation'],
    },
    {
        'id': 'approval',
        'labels': {'en': 'Approval', 'fr': 'Approbation', 'zh': '审批'},
        'keywords': ['approval', 'approve', 'sign-off', 'review', 'authorize', 'authorization'],
    },
    {
        'id': 'incident',
        'labels': {'en': 'Incident', 'fr': 'Incident', 'zh': '事故'},
        'keywords': ['incident', 'outage', 'alert', 'on-call', 'monitoring', 'response'],
    },
    {
        'id': 'onboarding',
        'labels': {'en': 'Onboarding', 'fr': 'Intégration', 'zh': '入职'},
        'keywords': ['onboarding', 'onboard', 'welcome', 'setup', 'activation', 'registration'],
    },
    {
        'id': 'offboarding',
        'labels': {'en': 'Offboarding', 'fr': 'Départ', 'zh': '离职'},
        'keywords': ['offboarding', 'termination', 'account deletion', 'deprovision', 'deactivate'],
    },
    {
        'id': 'billing',
        'labels': {'en': 'Billing & Payments', 'fr': 'Facturation & paiements', 'zh': '计费与支付'},
        'keywords': ['billing', 'invoice', 'payment', 'subscription', 'dunning', 'refund', 'dispute', 'chargeback'],
    },
    {
        'id': 'security',
        'labels': {'en': 'Security & Access', 'fr': 'Sécurité & accès', 'zh': '安全与访问'},
        'keywords': ['security', 'auth', 'authentication', 'oauth', '2fa', 'two-factor', 'mfa', 'certificate', 'rotation', 'secret', 'vulnerability', 'patch'],
    },
    {
        'id': 'compliance',
        'labels': {'en': 'Compliance', 'fr': 'Conformité', 'zh': '合规'},
        'keywords': ['gdpr', 'audit', 'compliance', 'consent', 'policy', 'risk', 'controls'],
    },
    {
        'id': 'delivery',
        'labels': {'en': 'Delivery & DevOps', 'fr': 'Livraison & DevOps', 'zh': '交付与 DevOps'},
        'keywords': ['ci/cd', 'ci-cd', 'pipeline', 'deploy', 'deployment', 'rollback', 'migration', 'backup', 'restore', 'provisioning', 'infrastructure', 'load testing'],
    },
    {
        'id': 'support',
        'labels': {'en': 'Support', 'fr': 'Support', 'zh': '支持'},
        'keywords': ['support', 'ticket', 'knowledge base', 'knowledge-base'],
    },
    {
        'id': 'agentic',
        'labels': {'en': 'Agentic Teams', 'fr': 'Équipes Agentiques', 'zh': '智能体团队'},
        'keywords': ['agentic', 'supervisor-worker', 'swarm', 'hierarchical', 'team-of-rivals', 'multi-agent', 'ai-team', 'orchestrator', 'planner', 'critic'],
    },
    {
        'id': 'ai-orchestration',
        'labels': {'en': 'AI Orchestration', 'fr': 'Orchestration IA', 'zh': 'AI编排'},
        'keywords': ['ai-native', 'orchestration', 'single-agent', 'sequential-pipeline', 'parallel-fan-out', 'map-reduce', 'event-driven-mesh', 'competitive', 'generator-critic', 'coordinator'],
    },
    {
        'id': 'mcp',
        'labels': {'en': 'MCP Architecture', 'fr': 'Architecture MCP', 'zh': 'MCP架构'},
        'keywords': ['mcp', 'direct-connect', 'gateway', 'proxy', 'tool-router', 'agent-mesh', 'circuit-breaker', 'context-proxy', 'stdio', 'production-grade'],
    },
    {
        'id': 'context-management',
        'labels': {'en': 'Context Management', 'fr': 'Gestion de Contexte', 'zh': '上下文管理'},
        'keywords': ['context-management', 'session-memory', 'rolling-summary', 'profile-memory', 'semantic-memory', 'episodic-memory', 'hybrid-retrieval', 'shared-memory', 'vector-db', 'memory'],
    },
]

LEGACY_TOP_LEVEL_DIRS = [
    'business-operations',
    'devops',
    'edge-cases',
    'finance',
    'hr',
    'logistics',
    'patterns',
    'syntax-primitives',
    'handoff',
    'approval',
    'incident',
    'onboarding',
    'offboarding',
    'billing',
    'security',
    'compliance',
    'delivery',
    'support',
    'agentic',
    'ai-orchestration',
    'mcp',
    'context-management',
    'uncategorized',
    'indexes',
]


def normalize_text(value: str) -> str:
    return re.sub(r'\s+', ' ', value.lower().replace('_', ' ').replace('-', ' ')).strip()


def slugify(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-') or 'unknown'


def load_canonical_slugs() -> list[str]:
    with urllib.request.urlopen(SITEMAP_URL, timeout=30) as response:
        xml_text = response.read().decode('utf-8')
    root = ET.fromstring(xml_text)
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    slugs: list[str] = []
    seen: set[str] = set()
    for loc_node in root.findall('sm:url/sm:loc', ns):
        loc = (loc_node.text or '').strip()
        if '/fr/templates/' in loc or '/zh/templates/' in loc:
            continue
        marker = '/templates/'
        if marker not in loc:
            continue
        slug = loc.split(marker, 1)[1].strip('/').removesuffix('.html')
        if slug and slug not in seen:
            slugs.append(slug)
            seen.add(slug)
    return slugs


def load_app_index() -> dict[str, dict]:
    data = json.loads(TEMPLATES_INDEX_PATH.read_text(encoding='utf-8'))
    return {entry['slug']: entry for entry in data['templates']}


def detect_kind(entry: dict) -> str:
    tags = entry.get('tags') or []
    if entry.get('domain') == 'Architecture' or 'architecture-diagram' in tags:
        return 'architecture'
    return 'workflow'


def compute_use_cases(entry: dict) -> list[str]:
    haystack = normalize_text(
        ' '.join(
            str(part)
            for part in [entry.get('slug', ''), entry.get('domain', ''), entry.get('sourcePath', ''), *(entry.get('tags') or [])]
            if part
        )
    )
    matches: list[str] = []
    for use_case in USE_CASES:
        if any(normalize_text(keyword) in haystack for keyword in use_case['keywords']):
            matches.append(use_case['id'])
    return matches


def make_readme(entry: dict, primary_use_case: str, secondary_use_cases: list[str], relative_dir: str) -> str:
    title = entry['title']
    description = entry.get('description') or ''
    source_domain = entry.get('domain') or 'unknown'
    tags = entry.get('tags') or []
    lines = [
        f'# {title}',
        '',
        description,
        '',
        f'**Template ID:** `{entry["slug"]}`  ',
        f'**Kind:** {detect_kind(entry)}  ',
        f'**Source domain:** {source_domain}  ',
        f'**Primary use case:** {primary_use_case}  ',
        f'**Secondary use cases:** {", ".join(secondary_use_cases) if secondary_use_cases else "None"}  ',
        f'**Complexity:** {entry.get("complexity", "n/a")}/5  ',
        f'**Nodes:** {entry.get("numNodes", "n/a")}  ',
        f'**Lanes:** {entry.get("numLanes", "n/a")}  ',
        f'**Tags:** [{", ".join(tags)}]  ',
        f'**Source path:** `{entry.get("sourcePath", "")}`  ',
        f'**Repo path:** `{relative_dir}`',
        '',
        '## Files',
        '- `workflow.fz` — FlowZap Code source',
        '- `metadata.json` — Structured metadata',
    ]
    return '\n'.join(lines).strip() + '\n'


def clean_repo_root() -> None:
    for name in LEGACY_TOP_LEVEL_DIRS:
        path = REPO_ROOT / name
        if path.is_dir():
            shutil.rmtree(path)
    for name in ('metadata.csv', 'templates.index.json', 'use-cases.index.json', 'README.md', 'CONTRIBUTING.md'):
        path = REPO_ROOT / name
        if path.exists():
            path.unlink()


def write_root_docs(total_templates: int, counts: Counter) -> None:
    readme_lines = [
        '# sequence-workflows',
        '',
        f'A synchronized FlowZap template corpus with **{total_templates} canonical templates**, mirrored from the FlowZap template library and organized by **primary Use Case**.',
        '',
        '## Organization Model',
        '',
        '- Top-level folders are primary Use Cases from the FlowZap Templates dropdown.',
        '- Second-level folders preserve the original source domain from the FlowZap app index.',
        '- Each template keeps all matched Use Cases in `metadata.json` and the generated JSON/CSV indexes.',
        '- Templates that do not match any current dropdown Use Case are placed under `uncategorized/`.',
        '',
        '## Top-Level Folders',
        '',
    ]
    for use_case in USE_CASES:
        readme_lines.append(f'- `{use_case["id"]}/` — {use_case["labels"]["en"]} ({counts.get(use_case["id"], 0)})')
    readme_lines.append(f'- `uncategorized/` — Unmatched canonical templates ({counts.get("uncategorized", 0)})')
    readme_lines.extend([
        '',
        '## Generated Indexes',
        '',
        '- `templates.index.json` — Full machine-readable template index',
        '- `use-cases.index.json` — Use Case summary with counts and template paths',
        '- `metadata.csv` — Flat CSV export of core template metadata',
        '',
        '## Sync Source',
        '',
        '- Template library (source of truth): `src/templateLibrary/templatesIndex.json` in the FlowZap app',
        '- Template file source: `public/template-files/*.fz` in the FlowZap app',
        '- Public listing check: `https://flowzap.xyz/sitemap-templates.xml` — a template missing from the sitemap is still mirrored, this list only reports the gap',
    ])
    (REPO_ROOT / 'README.md').write_text('\n'.join(readme_lines).strip() + '\n', encoding='utf-8')

    contributing_lines = [
        '# Contributing',
        '',
        'This repository is synchronized from the FlowZap application template library.',
        '',
        '## Structure',
        '',
        '- `primary-use-case/source-domain/template-slug/`',
        '- `workflow.fz` contains the FlowZap Code source',
        '- `metadata.json` stores machine-readable metadata including primary and secondary Use Cases',
        '- `templates.index.json`, `use-cases.index.json`, and `metadata.csv` are generated artifacts',
        '',
        '## Sync Expectations',
        '',
        '- Keep the sitemap-driven template set aligned with `https://flowzap.xyz/sitemap-templates.xml`.',
        '- Preserve one canonical template copy per slug.',
        '- Use `primary_use_case` for folder placement and `use_cases` for the full taxonomy membership.',
        '- Preserve `source_domain` from the app index for traceability.',
    ]
    (REPO_ROOT / 'CONTRIBUTING.md').write_text('\n'.join(contributing_lines).strip() + '\n', encoding='utf-8')


def main() -> None:
    if not FLOWZAP_APP_ROOT.exists():
        raise SystemExit(f'FlowZap app not found at {FLOWZAP_APP_ROOT}')
    canonical_slugs = load_canonical_slugs()
    app_index = load_app_index()
    clean_repo_root()

    # The app index is the source of truth: it holds every template the product
    # ships. The sitemap only says which of them are publicly listed, so it can
    # lag behind a release and must never shrink the corpus.
    sitemap_slugs = set(canonical_slugs)
    app_order = list(app_index.keys())
    sitemap_only = [slug for slug in canonical_slugs if slug not in app_index]
    missing_from_sitemap = [slug for slug in app_order if slug not in sitemap_slugs]

    templates_index: list[dict] = []
    use_case_index = {use_case['id']: {'label': use_case['labels']['en'], 'count': 0, 'templates': []} for use_case in USE_CASES}
    use_case_index['uncategorized'] = {'label': 'Uncategorized', 'count': 0, 'templates': []}
    counts: Counter = Counter()

    for slug in app_order:
        entry = app_index[slug]
        template_file = TEMPLATE_FILES_DIR / f'{slug}.fz'
        if not template_file.exists():
            raise SystemExit(f'Missing template file: {template_file}')

        source_domain = entry.get('domain') or 'unknown'
        source_domain_slug = slugify(source_domain)
        use_cases = compute_use_cases(entry)
        primary_use_case = use_cases[0] if use_cases else 'uncategorized'
        secondary_use_cases = use_cases[1:]
        kind = detect_kind(entry)
        workflow_id = slug[:-9] if slug.endswith('-workflow') else slug

        relative_dir = f'{primary_use_case}/{source_domain_slug}/{slug}'
        target_dir = REPO_ROOT / relative_dir
        target_dir.mkdir(parents=True, exist_ok=True)

        shutil.copyfile(template_file, target_dir / 'workflow.fz')

        metadata = {
            'template_id': slug,
            'workflow_id': workflow_id,
            'title': entry['title'],
            'kind': kind,
            'source_domain': source_domain,
            'primary_use_case': primary_use_case,
            'secondary_use_cases': secondary_use_cases,
            'use_cases': use_cases,
            'complexity': entry.get('complexity'),
            'num_nodes': entry.get('numNodes'),
            'num_lanes': entry.get('numLanes'),
            'tags': entry.get('tags') or [],
            'description': entry.get('description') or '',
            'source_path': entry.get('sourcePath') or '',
            'repo_path': relative_dir,
        }
        (target_dir / 'metadata.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        (target_dir / 'README.md').write_text(make_readme(entry, primary_use_case, secondary_use_cases, relative_dir), encoding='utf-8')

        record = {
            'slug': slug,
            'title': entry['title'],
            'description': entry.get('description') or '',
            'kind': kind,
            'sourceDomain': source_domain,
            'primaryUseCase': primary_use_case,
            'secondaryUseCases': secondary_use_cases,
            'useCases': use_cases,
            'complexity': entry.get('complexity'),
            'numNodes': entry.get('numNodes'),
            'numLanes': entry.get('numLanes'),
            'tags': entry.get('tags') or [],
            'sourcePath': entry.get('sourcePath') or '',
            'repoPath': relative_dir,
        }
        templates_index.append(record)
        use_case_index[primary_use_case]['count'] += 1
        use_case_index[primary_use_case]['templates'].append({'slug': slug, 'title': entry['title'], 'repoPath': relative_dir})
        counts[primary_use_case] += 1

    (REPO_ROOT / 'templates.index.json').write_text(json.dumps({'templates': templates_index}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (REPO_ROOT / 'use-cases.index.json').write_text(json.dumps({'useCases': use_case_index}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    with (REPO_ROOT / 'metadata.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['template_id', 'workflow_id', 'title', 'kind', 'source_domain', 'primary_use_case', 'secondary_use_cases', 'use_cases', 'complexity', 'num_nodes', 'num_lanes', 'tags', 'description', 'source_path', 'repo_path'])
        writer.writeheader()
        for item in templates_index:
            writer.writerow({
                'template_id': item['slug'],
                'workflow_id': item['slug'][:-9] if item['slug'].endswith('-workflow') else item['slug'],
                'title': item['title'],
                'kind': item['kind'],
                'source_domain': item['sourceDomain'],
                'primary_use_case': item['primaryUseCase'],
                'secondary_use_cases': ';'.join(item['secondaryUseCases']),
                'use_cases': ';'.join(item['useCases']),
                'complexity': item['complexity'],
                'num_nodes': item['numNodes'],
                'num_lanes': item['numLanes'],
                'tags': ';'.join(item['tags']),
                'description': item['description'],
                'source_path': item['sourcePath'],
                'repo_path': item['repoPath'],
            })

    write_root_docs(len(templates_index), counts)
    print(f'Synchronized {len(templates_index)} templates into {REPO_ROOT}')
    if missing_from_sitemap:
        print(f'Not yet in sitemap-templates.xml ({len(missing_from_sitemap)}): {", ".join(missing_from_sitemap[:15])}')
    if sitemap_only:
        print(f'Sitemap entries without template metadata, skipped ({len(sitemap_only)}): {", ".join(sitemap_only[:10])}')


if __name__ == '__main__':
    main()
