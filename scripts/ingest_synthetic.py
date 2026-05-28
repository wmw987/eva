#!/usr/bin/env python3
"""Ingest a synthetic Eva event JSON file into the local SQLite store."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "db" / "migrations" / "001_init.sql"


def ensure_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(MIGRATION.read_text())


def event_to_row(event: dict) -> dict:
    geo = event["geo"]
    time = event["time"]
    assessment = event["assessment"]
    centroid = geo["centroid"]

    return {
        "id": event["id"],
        "title": event["title"],
        "summary": event["summary"],
        "topic": event["topic"],
        "observed_at": time["observed_at"],
        "valid_from": time["valid_from"],
        "valid_to": time["valid_to"],
        "time_precision": time["precision"],
        "geo_label": geo["label"],
        "country": geo.get("country"),
        "region": geo.get("region"),
        "geometry_geojson": json.dumps(geo["geometry"], separators=(",", ":")),
        "centroid_lat": centroid["lat"],
        "centroid_lon": centroid["lon"],
        "precision_m": geo.get("precision_m"),
        "risk": assessment["risk"],
        "confidence": assessment["confidence"],
        "provenance_json": json.dumps(event["provenance"], separators=(",", ":")),
        "relations_json": json.dumps(event["relations"], separators=(",", ":")),
    }


def ingest_event(connection: sqlite3.Connection, event: dict) -> None:
    row = event_to_row(event)
    connection.execute(
        """
        INSERT INTO events (
          id, title, summary, topic, observed_at, valid_from, valid_to,
          time_precision, geo_label, country, region, geometry_geojson,
          centroid_lat, centroid_lon, precision_m, risk, confidence,
          provenance_json, relations_json
        ) VALUES (
          :id, :title, :summary, :topic, :observed_at, :valid_from, :valid_to,
          :time_precision, :geo_label, :country, :region, :geometry_geojson,
          :centroid_lat, :centroid_lon, :precision_m, :risk, :confidence,
          :provenance_json, :relations_json
        )
        ON CONFLICT(id) DO UPDATE SET
          title = excluded.title,
          summary = excluded.summary,
          topic = excluded.topic,
          observed_at = excluded.observed_at,
          valid_from = excluded.valid_from,
          valid_to = excluded.valid_to,
          time_precision = excluded.time_precision,
          geo_label = excluded.geo_label,
          country = excluded.country,
          region = excluded.region,
          geometry_geojson = excluded.geometry_geojson,
          centroid_lat = excluded.centroid_lat,
          centroid_lon = excluded.centroid_lon,
          precision_m = excluded.precision_m,
          risk = excluded.risk,
          confidence = excluded.confidence,
          provenance_json = excluded.provenance_json,
          relations_json = excluded.relations_json
        """,
        row,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("event_json", type=Path)
    parser.add_argument("--db", type=Path, default=Path("eva.db"))
    args = parser.parse_args()

    event = json.loads(args.event_json.read_text())
    connection = sqlite3.connect(args.db)
    try:
        ensure_schema(connection)
        ingest_event(connection, event)
        connection.commit()
    finally:
        connection.close()

    print(f"ingested {event['id']} into {args.db}")


if __name__ == "__main__":
    main()
