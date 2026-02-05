import json

import typer
from rich import print as rprint

from cms.db import get_connection
from cms.main import app


def _seed_sites(con):
    con.execute("DELETE FROM sites")
    sites = [
        ("agentic-dev", "agentic-dev.io", "agentic-dev.io", "#050508", "#ff6b35", "#26ffd4"),
        ("synapticore-io", "synapticore.io", "SYNAPTICORE.IO", "#020617", "#22d3ee", "#0ea5e9"),
        ("synapticore-studio", "synapticore.studio", "SYNAPTICORE.STUDIO", "#020202", "#22d3ee", "#f97316"),
    ]
    con.executemany(
        "INSERT INTO sites VALUES (?, ?, ?, ?, ?, ?)", sites
    )


def _seed_ecosystem(con):
    con.execute("DELETE FROM ecosystem_orgs")
    orgs = [
        (
            "agentic-dev",
            "agentic-dev.io",
            "AI Development",
            "Agentic Systems, MCP Tools und AI-Infrastruktur. Wir bauen die intelligenten Systeme.",
            "#ff6b35",
            "Cpu",
            "https://agentic-dev.io",
            1,
        ),
        (
            "synapticore-io",
            "synapticore.io",
            "Research Lab",
            "Neuromorphic Computing, Spatial Intelligence und experimentelle Architekturen. Hier entsteht das Neue.",
            "#22d3ee",
            "FlaskConical",
            "https://synapticore.io",
            2,
        ),
        (
            "synapticore-studio",
            "synapticore.studio",
            "Production & Product Owner",
            "Content, DCC Pipelines, Virtual Production und Games. Der Product Owner, der alles zusammenführt.",
            "#ffa726",
            "Layers",
            "https://synapticore.studio",
            3,
        ),
    ]
    con.executemany(
        "INSERT INTO ecosystem_orgs VALUES (?, ?, ?, ?, ?, ?, ?, ?)", orgs
    )


def _seed_hero_sections(con):
    con.execute("DELETE FROM hero_sections")
    heroes = [
        (
            "agentic-dev",
            "Lokale AI\nohne Cloud, ohne API-Kosten",
            None,
            "Ollama, n8n, ComfyUI – bei dir installiert, von dir kontrolliert. Für Freelancer, Agenturen und kleine Teams.",
            "15 Min Gespräch buchen",
            "https://calendly.com/bjoern-bethge/15min",
            json.dumps(["DSGVO-konform", "Keine monatlichen Kosten", "Offline nutzbar"]),
        ),
        (
            "synapticore-io",
            "Rethink\nComputation",
            None,
            "Wir verschmelzen physikalischen Raum mit neuronaler Logik.\nEin dezentrales Nervensystem für die Industrie.",
            "Infrastruktur starten",
            None,
            json.dumps(["Neuromorphic Computing", "Spatial LiDAR Cloud", "Nexus Topology"]),
        ),
        (
            "synapticore-studio",
            "Invisible\nArchitects.",
            "Ghost Architecture // Hands-On Forge",
            "Synapticore ist ein spezialisiertes Studio für Deep-Tech Architecture. Wir entwerfen und implementieren die unsichtbare Logik hinter globalen Systemen – von VW Pixel Streaming bis zu autonomen Rust AI Agenten.",
            "STUDIO ARCHIVES",
            "#projects",
            json.dumps(["Engineering the Invisible Core since 2004"]),
        ),
    ]
    con.executemany(
        "INSERT INTO hero_sections VALUES (?, ?, ?, ?, ?, ?, ?)", heroes
    )


def _seed_content_blocks(con):
    con.execute("DELETE FROM content_blocks")
    blocks = []

    # === agentic-dev: problems ===
    problems = [
        ("ad-prob-1", "💸", "Monatliche Kosten summieren sich", "ChatGPT Plus, Midjourney, Runway – schnell 100€+ pro Monat. Für immer."),
        ("ad-prob-2", "🔓", "Deine Daten liegen in der Cloud", "Kundendaten, Geschäftsideen, Texte – alles auf US-Servern. DSGVO-Problem."),
        ("ad-prob-3", "🚫", "Abhängig von Anbietern", "API-Limits, Preiserhöhungen, Ausfälle – du hast keine Kontrolle."),
        ("ad-prob-4", "📵", "Ohne Internet geht nichts", "Im Zug, im Flugzeug, beim Kunden ohne WLAN – keine AI."),
    ]
    for i, (bid, icon, title, desc) in enumerate(problems):
        blocks.append((bid, "agentic-dev", "problem", title, desc, icon, None, None, None, i))

    # === agentic-dev: solutions ===
    solutions = [
        ("ad-sol-1", "Lock", "100% Datenschutz", "Daten verlassen nie deinen Rechner. DSGVO? Erledigt."),
        ("ad-sol-2", "Shield", "0€ laufende Kosten", "Kein Abo, keine API-Kosten. Unbegrenzte Nutzung."),
        ("ad-sol-3", "Zap", "Volle Kontrolle", "Dein System, deine Modelle, deine Regeln."),
    ]
    for i, (bid, icon, title, desc) in enumerate(solutions):
        blocks.append((bid, "agentic-dev", "solution", title, desc, icon, None, None, None, i))

    # === agentic-dev: stack ===
    stack = [
        ("ad-stack-1", "Ollama", "LLMs lokal (Llama, Mistral, Qwen)"),
        ("ad-stack-2", "n8n", "Workflow-Automatisierung"),
        ("ad-stack-3", "ComfyUI", "Bildgenerierung (SDXL, Flux)"),
        ("ad-stack-4", "LTX Video", "Videogenerierung"),
    ]
    for i, (bid, title, desc) in enumerate(stack):
        blocks.append((bid, "agentic-dev", "stack", title, desc, None, None, None, None, i))

    # === agentic-dev: services ===
    services = [
        (
            "ad-svc-1", "🚀", "Quick Setup",
            "Lokaler AI-Stack, installiert und erklärt.",
            ["Ollama mit passenden Modellen", "n8n Basis-Installation", "Einweisung per Call", "Setup-Dokumentation"],
            False,
        ),
        (
            "ad-svc-2", "⚡", "Full Stack Setup",
            "Komplettes lokales AI-System für Produktion.",
            ["Alles aus Quick Setup", "ComfyUI für Bildgenerierung", "Custom n8n Workflows", "Workshop/Training", "Support nach Setup"],
            True,
        ),
        (
            "ad-svc-3", "🛠", "Workflows & Automation",
            "Individuelle Automatisierung für deinen Use Case.",
            ["n8n Workflow nach Bedarf", "ComfyUI Pipeline anpassen", "Integration in deine Tools", "Dokumentation inkl."],
            False,
        ),
    ]
    for i, (bid, icon, title, desc, features, featured) in enumerate(services):
        blocks.append((
            bid, "agentic-dev", "service", title, desc, icon,
            json.dumps(features), None, json.dumps({"featured": featured}), i
        ))

    # === agentic-dev: comparison ===
    cloud_items = [
        "20-200€ monatlich, für immer",
        "Daten auf US-Servern",
        "Abhängig von Anbieter",
        "API-Limits & Rate Limits",
        "Nur mit Internet",
    ]
    local_items = [
        "Einmal Setup, dann 0€",
        "Daten bleiben bei dir",
        "Du kontrollierst alles",
        "Unbegrenzte Nutzung",
        "Funktioniert offline",
    ]
    blocks.append((
        "ad-comp-cloud", "agentic-dev", "comparison", "Cloud-AI (ChatGPT, Midjourney...)",
        None, None, json.dumps(cloud_items), None, json.dumps({"side": "cloud"}), 0
    ))
    blocks.append((
        "ad-comp-local", "agentic-dev", "comparison", "Lokale AI (dein Stack)",
        None, None, json.dumps(local_items), None, json.dumps({"side": "local"}), 1
    ))

    # === agentic-dev: about ===
    blocks.append((
        "ad-about", "agentic-dev", "about", "Über mich",
        None, None, None, None,
        json.dumps({
            "paragraphs": [
                'Ich bin <strong class="text-[#f0f0f5]">Björn</strong> – Entwickler mit Fokus auf AI-Systeme, Automatisierung und Unreal Engine. Seit Jahren baue ich Lösungen, die lokal laufen und keine Cloud brauchen.',
                "Mein Hintergrund: Enterprise IT, Automotive, Software-Architektur. Ich weiß, wie Systeme in der echten Welt funktionieren müssen – nicht nur in Demos.",
                '<strong class="text-[#f0f0f5]">Warum lokal?</strong> Weil ich glaube, dass du die Kontrolle über deine Tools und Daten behalten solltest. Ohne monatliche Gebühren an US-Konzerne.',
            ],
            "links": [
                {"label": "GitHub", "href": "https://github.com/agentic-dev-io"},
                {"label": "LinkedIn", "href": "https://www.linkedin.com/in/bj%C3%B6rn-bethge-a0754a329"},
            ],
            "projects": [
                {"name": "agentic-dev.io", "desc": "Intelligente Automatisierung für Teams"},
                {"name": "synapticore.io", "desc": "Scientific Computing & Spatial Intelligence Lab"},
                {"name": "synapticore.studio", "desc": "Realtime GenAI & Agentic DCC"},
            ],
        }),
        0,
    ))

    # === synapticore-io: modes ===
    modes = [
        ("sio-mode-1", "Network", "Neuromorphic Computing", "Simulation biologischer Synapsenpfade."),
        ("sio-mode-2", "Box", "Spatial LiDAR Cloud", "Echtzeit-Analyse hochfrequenter Raumdaten."),
        ("sio-mode-3", "Globe", "Nexus Topology", "Globale dezentrale Mesh-Netzwerke."),
    ]
    for i, (bid, icon, title, desc) in enumerate(modes):
        blocks.append((bid, "synapticore-io", "mode", title, desc, icon, None, None, None, i))

    # === synapticore-io: stats ===
    blocks.append((
        "sio-stats", "synapticore-io", "stats", "Hardware-Software Nexus",
        "Synapticore nutzt neuromorphe Architektur-Prinzipien, um Latenzen in der räumlichen Intelligenz um 90% zu reduzieren. Wir verarbeiten Daten dort, wo sie entstehen.",
        None, None, None,
        json.dumps({
            "heading": "Berechnungen im Vektorfeld.",
            "metrics": [
                {"value": "0.08ms", "label": "Synaptische Latenz"},
                {"value": "12.4TB", "label": "Live Mesh Kapazität"},
            ],
        }),
        0,
    ))

    # === synapticore-studio: capabilities ===
    capabilities = [
        (
            "ss-cap-1", "Brain", "Autonomous Agent Systems",
            "Entwicklung von kognitiven Layern und autonomen Agenten-Frameworks in Unreal Engine 5. Wir nutzen Rust und C++, um Logik-Infrastrukturen zu schaffen, die über klassisches Scripting hinausgehen.",
        ),
        (
            "ss-cap-2", "Cloud", "Enterprise Cloud Streaming",
            "Architektur und Deployment globaler Pixel-Streaming-Lösungen. Wir orchestrieren GPU-Cluster für fotorealistische Konfiguratoren auf Enterprise-Level (VAG Group Standard).",
        ),
        (
            "ss-cap-3", "Wand2", "Generative Production Tools",
            "Bau von proprietären Plugins und intelligenten Generatoren. Wir automatisieren komplexe DCC-Pipelines durch 20 Jahre Erfahrung in der prozeduralen Asset-Erzeugung.",
        ),
    ]
    for i, (bid, icon, title, desc) in enumerate(capabilities):
        blocks.append((bid, "synapticore-studio", "capability", title, desc, icon, None, None, None, i))

    con.executemany(
        "INSERT INTO content_blocks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        blocks,
    )


def _seed_case_studies(con):
    con.execute("DELETE FROM case_studies")
    cases = [
        (
            "ai-rust",
            "synapticore-studio",
            "R&D / Cognitive Logic",
            "Neural Agent Frameworks 2024",
            "Unsere neueste Evolution: Hochperformante KI-Agenten basierend auf Rust-Backends. Memory-safe, ultra-schnell und nahtlos in UE5 integriert für autonome Simulations-Szenarien.",
            json.dumps(["Rust", "AI Agents", "C++ Plugin"]),
            json.dumps(["Est. 2024", "Rust Performance", "Agentic Logic"]),
            "from-orange-600 to-red-600",
            0,
        ),
        (
            "vw-streaming",
            "synapticore-studio",
            "Volkswagen / Audi / Skoda",
            "Global Pixel Streaming Lead",
            "Die technologische Basis für globale Automotive-Konfiguratoren. Seit 2008 entwerfen und implementieren wir die Cloud-Infrastruktur für die VAG-Gruppe weltweit.",
            json.dumps(["Cloud Infra", "Pixel Streaming", "Direct Supplier"]),
            json.dumps(["Since 2008", "Global Rollout", "Tier-1 Partner"]),
            "from-blue-600 to-indigo-600",
            1,
        ),
        (
            "adidas-vr",
            "synapticore-studio",
            "Adidas x NVIDIA",
            "Virtual Photography Studio",
            "Ein VR-integriertes Ökosystem zur virtuellen Asset-Produktion. Validiert durch NVIDIA als globaler Benchmark für High-Fidelity Performance und RTX-Optimierung.",
            json.dumps(["VR Studio", "NVIDIA Global", "Automation"]),
            json.dumps(["RTX Validated", "Asset-Gen", "DCC Mastery"]),
            "from-emerald-500 to-cyan-600",
            2,
        ),
    ]
    con.executemany(
        "INSERT INTO case_studies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", cases
    )


def _seed_timeline(con):
    con.execute("DELETE FROM timeline_events")
    events = [
        ("ss-tl-1", "synapticore-studio", 2004, "DCC Legacy", "Blender Origin", None, 0),
        ("ss-tl-2", "synapticore-studio", 2008, "Enterprise", "VAG Partner ID", None, 1),
        ("ss-tl-3", "synapticore-studio", 2014, "Intelligence", "Neural Research", None, 2),
        ("ss-tl-4", "synapticore-studio", 2024, "Performance", "Rust & Agents", None, 3),
    ]
    con.executemany(
        "INSERT INTO timeline_events VALUES (?, ?, ?, ?, ?, ?, ?)", events
    )


@app.command()
def seed():
    """Seed the database with content extracted from the App.jsx files."""
    con = get_connection()

    _seed_sites(con)
    rprint("[green]  Sites seeded[/green]")

    _seed_ecosystem(con)
    rprint("[green]  Ecosystem orgs seeded[/green]")

    _seed_hero_sections(con)
    rprint("[green]  Hero sections seeded[/green]")

    _seed_content_blocks(con)
    rprint("[green]  Content blocks seeded[/green]")

    _seed_case_studies(con)
    rprint("[green]  Case studies seeded[/green]")

    _seed_timeline(con)
    rprint("[green]  Timeline events seeded[/green]")

    con.close()
    rprint("[bold green]All content seeded successfully.[/bold green]")
