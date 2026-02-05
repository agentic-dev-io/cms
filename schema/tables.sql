-- CMS Schema for synapticore web properties

CREATE TABLE IF NOT EXISTS sites (
    site_id VARCHAR PRIMARY KEY,
    domain VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    theme_bg VARCHAR,
    theme_primary VARCHAR,
    theme_secondary VARCHAR
);

CREATE TABLE IF NOT EXISTS ecosystem_orgs (
    org_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    role VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    color VARCHAR NOT NULL,
    icon VARCHAR,
    href VARCHAR,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS hero_sections (
    site_id VARCHAR PRIMARY KEY REFERENCES sites(site_id),
    title VARCHAR NOT NULL,
    subtitle VARCHAR,
    description VARCHAR,
    cta_text VARCHAR,
    cta_href VARCHAR,
    features JSON
);

CREATE TABLE IF NOT EXISTS content_blocks (
    block_id VARCHAR PRIMARY KEY,
    site_id VARCHAR NOT NULL REFERENCES sites(site_id),
    block_type VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    description VARCHAR,
    icon VARCHAR,
    features JSON,
    tags JSON,
    metadata JSON,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS case_studies (
    case_id VARCHAR PRIMARY KEY,
    site_id VARCHAR NOT NULL REFERENCES sites(site_id),
    brand VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    tags JSON,
    stats JSON,
    color_gradient VARCHAR,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS timeline_events (
    event_id VARCHAR PRIMARY KEY,
    site_id VARCHAR NOT NULL REFERENCES sites(site_id),
    year INTEGER NOT NULL,
    category VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    description VARCHAR,
    sort_order INTEGER NOT NULL DEFAULT 0
);
