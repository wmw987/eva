#!/usr/bin/env python3
"""Query synthetic Eva events from the local SQLite store."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


def build_event(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"],
        "title": row["title"],
        "summary": row["summary"],
        "topic": row["topic"],
        "time": {
            "observed_at": row["observed_at"],
            "valid_from": row["valid_from"],
            "valid_to": row["valid_to"],
            "precision": row["time_precision"],
        },
        "geo": {
            "label": row["geo_label"],
            "country": row["country"],
            "region": row["region"],
            "geometry": json.loads(row["geometry_geojson"]),
            "centroid": {
                "lat": row["centroid_lat"],
                "lon": row["centroid_lon"],
            },
            "precision_m": row["precision_m"],
        },
        "assessment": {
            "risk": row["risk"],
            "confidence": row["confidence"],
        },
        "provenance": json.loads(row["provenance_json"]),
        "relations": json.loads(row["relations_json"]),
    }


def query_events(
    db_path: Path,
    region: str | None,
    risk: str | None,
    limit: int,
    time_window: str,
) -> dict:
    conditions = []
    params: list[object] = []

    if region:
        conditions.append("(region = ? OR geo_label = ?)")
        params.extend([region, region])
    if risk:
        conditions.append("risk = ?")
        params.append(risk)

    where = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    params.append(limit)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            f"""
            SELECT *
            FROM events
            {where}
            ORDER BY observed_at DESC
            LIMIT ?
            """,
            params,
        ).fetchall()
    finally:
        connection.close()

    return {
        "query": {
            "region": region,
            "time_window": time_window,
            "risk": risk,
        },
        "results": [build_event(row) for row in rows],
        "limits": {
            "max_results": limit,
            "source_policy": "citations_required",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path("eva.db"))
    parser.add_argument("--region")
    parser.add_argument("--since", default="PT48H")
    parser.add_argument("--risk", choices=["low", "medium", "high", "unknown"])
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    print(
        json.dumps(
            query_events(args.db, args.region, args.risk, args.limit, args.since),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
