CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  summary TEXT NOT NULL,
  topic TEXT NOT NULL,
  observed_at TEXT NOT NULL,
  valid_from TEXT NOT NULL,
  valid_to TEXT,
  time_precision TEXT NOT NULL,
  geo_label TEXT NOT NULL,
  country TEXT,
  region TEXT,
  geometry_geojson TEXT NOT NULL CHECK (json_valid(geometry_geojson)),
  centroid_lat REAL NOT NULL CHECK (centroid_lat >= -90 AND centroid_lat <= 90),
  centroid_lon REAL NOT NULL CHECK (centroid_lon >= -180 AND centroid_lon <= 180),
  precision_m INTEGER CHECK (precision_m IS NULL OR precision_m >= 0),
  risk TEXT NOT NULL CHECK (risk IN ('low', 'medium', 'high', 'unknown')),
  confidence TEXT NOT NULL CHECK (confidence IN ('confirmed', 'signal', 'rumor', 'unknown')),
  provenance_json TEXT NOT NULL CHECK (json_valid(provenance_json)),
  relations_json TEXT NOT NULL CHECK (json_valid(relations_json)),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_events_topic ON events(topic);
CREATE INDEX IF NOT EXISTS idx_events_region ON events(region);
CREATE INDEX IF NOT EXISTS idx_events_observed_at ON events(observed_at);
CREATE INDEX IF NOT EXISTS idx_events_risk ON events(risk);
