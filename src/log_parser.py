"""
SentinelForge
Log Parser Module

Phase 1: Basic JSON log ingestion and failed login detection.
"""

import json


def load_logs(file_path):
    """Load JSON log data from file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def count_failed_logins(logs):
    """Count events marked as failed_login."""
    failed_count = 0

    for entry in logs:
        if entry.get("event_type") == "failed_login":
            failed_count += 1

    return failed_count


def main():
    logs = load_logs("../logs/sample_logs.json")
    failed_attempts = count_failed_logins(logs)

    print(f"Total failed login attempts: {failed_attempts}")


if __name__ == "__main__":
    main()
