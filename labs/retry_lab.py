#!/usr/bin/env python3
"""Deterministic local SQLite exercise; no network, sleep, credentials or Azure."""
import argparse
import json
import sqlite3


class ResponseLost(Exception):
    pass


class PermanentFailure(Exception):
    pass


def exercise(*, idempotent, attempts=3, permanent=False):
    if not 1 <= attempts <= 10:
        raise ValueError("attempts must be 1..10")
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE documents (id INTEGER PRIMARY KEY, request_key TEXT, title TEXT)")
    if idempotent:
        connection.execute("CREATE UNIQUE INDEX request_once ON documents(request_key)")
    waits = []
    completed = False
    calls = 0
    error = None
    try:
        for attempt in range(attempts):
            calls += 1
            try:
                if permanent:
                    raise PermanentFailure("invalid request")
                sql = "INSERT OR IGNORE" if idempotent else "INSERT"
                connection.execute(
                    sql + " INTO documents(request_key,title) VALUES (?,?)",
                    ("request-001", "Synthetic notes"),
                )
                connection.commit()
                if attempt == 0:
                    raise ResponseLost("commit succeeded; response was lost")
                completed = True
                break
            except PermanentFailure as failure:
                error = str(failure)
                break  # Permanent errors are not retried.
            except ResponseLost as failure:
                error = str(failure)
                if attempt + 1 < attempts:
                    waits.append(2 ** attempt)  # Record planned delays; do not sleep.
        rows = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        return {
            "idempotent": idempotent, "completed": completed,
            "requests": calls, "stored_documents": rows,
            "planned_waits": waits, "error": None if completed else error,
        }
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, default=3)
    args = parser.parse_args()
    if not 1 <= args.attempts <= 10:
        parser.error("--attempts must be 1..10")
    print(json.dumps({
        "naive": exercise(idempotent=False, attempts=args.attempts),
        "idempotent": exercise(idempotent=True, attempts=args.attempts),
        "permanent": exercise(idempotent=True, attempts=args.attempts, permanent=True),
    }, indent=2))


if __name__ == "__main__":
    main()
