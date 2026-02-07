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
            "Agentic Systems & AI Development",
            "AI Agents, Automation & MCP Tools. Wir bauen die intelligenten Systeme.",
            "#ff6b35",
            "Cpu",
            "https://agentic-dev.io",
            1,
        ),
        (
            "synapticore-io",
            "synapticore.io",
            "Scientific Computing & Spatial Intelligence",
            "Experimentelle Architekturen und Open-Source-Forschung.",
            "#22d3ee",
            "FlaskConical",
            "https://synapticore.io",
            2,
        ),
        (
            "synapticore-studio",
            "synapticore.studio",
            "Agentic DCC Pipelines & Interactive AI Experiences",
            "Virtual Production, Games und interaktive Erlebnisse. Der Product Owner, der alles zusammenführt.",
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
            "Open-Source-Forschung an den Grenzen von Neural Networks, astronomischem Computing und Scientific Data.",
            "Forschung entdecken",
            None,
            json.dumps(["Neural Computing", "Space & Climate ML", "Scientific Data Engineering"]),
        ),
        (
            "synapticore-studio",
            "Invisible\nArchitects.",
            "Ghost Architecture // Hands-On Forge",
            "Spezialisiertes Studio für Agentic DCC Pipelines, Virtual Production und generative Content-Produktion. 20+ Jahre Enterprise-Erfahrung als Fundament – von Blender 2.4 bis Unreal Engine 5.",
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
        ("sio-mode-1", "Network", "Neural Computing", "Graph Neural Networks, Bio-inspired Architectures und Deep Learning Forschung."),
        ("sio-mode-2", "Globe", "Space & Climate ML", "Astronomische Datenanalyse, Weltraum-Wetter und Klima-Modelle."),
        ("sio-mode-3", "Database", "Scientific Data Engineering", "DuckDB Extensions, Spatial Computing und Research Tooling."),
    ]
    for i, (bid, icon, title, desc) in enumerate(modes):
        blocks.append((bid, "synapticore-io", "mode", title, desc, icon, None, None, None, i))

    # === synapticore-io: stats ===
    blocks.append((
        "sio-stats", "synapticore-io", "stats", "Open Source Research",
        "Experimentelle Architekturen, Open Source first. Wir erforschen neue Ansätze in Neural Computing, astronomischer Datenverarbeitung und Scientific Tooling – und teilen alles als Open Source.",
        None, None, None,
        json.dumps({
            "heading": "Open Source first.",
            "metrics": [
                {"value": "16 Repos", "label": "Open Source"},
                {"value": "PyTorch + DuckDB", "label": "Core Stack"},
            ],
        }),
        0,
    ))

    # === synapticore-studio: capabilities ===
    capabilities = [
        (
            "ss-cap-1", "Brain", "Agentic DCC Pipelines",
            "AI-gestützte Content-Produktion und automatisierte DCC Workflows. Autonome Agenten für Blender, Unreal Engine und prozedurale Asset-Erzeugung.",
        ),
        (
            "ss-cap-2", "Cloud", "Virtual Production & Streaming",
            "20+ Jahre Erfahrung in Pixel Streaming, Real-Time Rendering und Virtual Production. Von Automotive-Konfiguratoren bis interaktive Erlebnisse.",
        ),
        (
            "ss-cap-3", "Wand2", "Generative Production Tools",
            "Prozedurale Asset-Erzeugung, Blender/UE Integrations und intelligente Generatoren. Automatisierung komplexer DCC-Pipelines.",
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
            "Studio R&D",
            "Agentic DCC Pipelines",
            "Autonome Content-Produktion durch AI-gesteuerte DCC Workflows. Agentic Pipelines für Blender und Unreal Engine 5 – von prozeduraler Generierung bis zur automatisierten Post-Production.",
            json.dumps(["UE5", "Agentic DCC", "Production Pipeline"]),
            json.dumps(["Est. 2024", "Agentic Workflows", "DCC Automation"]),
            "from-orange-600 to-red-600",
            0,
        ),
        (
            "vw-streaming",
            "synapticore-studio",
            "Volkswagen Group",
            "20 Jahre Enterprise DCC",
            "Track Record über 20+ Jahre und dutzende Marken: Audi, Skoda, Seat, Bentley, Porsche u.v.m. Pixel Streaming, Motion Capture, Projection Mapping, AR/VR – Enterprise DCC auf höchstem Niveau.",
            json.dumps(["Pixel Streaming", "Motion Capture", "AR/VR"]),
            json.dumps(["Since 2004", "20+ Jahre", "Enterprise DCC"]),
            "from-blue-600 to-indigo-600",
            1,
        ),
        (
            "adidas-vr",
            "synapticore-studio",
            "Adidas / NVIDIA",
            "Virtual Photography & RTX Pipeline",
            "Virtual Asset Production für Adidas mit NVIDIA RTX Pipeline. Weiterentwicklung der DCC-Pipeline, Featured im NVIDIA Blog als Referenzprojekt.",
            json.dumps(["Virtual Photography", "RTX Pipeline", "Asset Production"]),
            json.dumps(["NVIDIA Featured", "Asset Production", "DCC Pipeline"]),
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
        ("ss-tl-1", "synapticore-studio", 2004, "DCC Legacy", "Blender Origin", "Erste Schritte mit Blender 2.4 – Beginn von 20 Jahren DCC-Erfahrung", 0),
        ("ss-tl-2", "synapticore-studio", 2008, "Enterprise", "VWAG Ökosystem", "Erste Projekte im Volkswagen Group Ökosystem – Audi, Skoda, Seat, Bentley u.v.m.", 1),
        ("ss-tl-3", "synapticore-studio", 2014, "Intelligence", "Neural Research", "Einstieg in Neural Networks und ML-Forschung", 2),
        ("ss-tl-4", "synapticore-studio", 2024, "Agentic", "Agentic DCC", "Agentic Systems und AI-gestützte DCC Pipelines", 3),
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
