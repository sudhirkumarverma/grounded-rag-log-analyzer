"""
Grounded RAG Log Analyzer
Enterprise Synthetic Dataset Generator

This script generates:

1. enterprise_logs.csv
2. incident_history.csv
3. deployment_runbook.md
4. sample_questions.json

Author: Sudhir Kumar Verma
"""

from __future__ import annotations

import csv
import json
import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

random.seed(42)

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = DATA_DIR / "logs"
INCIDENT_DIR = DATA_DIR / "incidents"
RUNBOOK_DIR = DATA_DIR / "runbooks"

LOG_DIR.mkdir(parents=True, exist_ok=True)
INCIDENT_DIR.mkdir(parents=True, exist_ok=True)
RUNBOOK_DIR.mkdir(parents=True, exist_ok=True)

ENTERPRISE_LOG_FILE = LOG_DIR / "enterprise_logs.csv"

INCIDENT_FILE = INCIDENT_DIR / "incident_history.csv"

RUNBOOK_FILE = RUNBOOK_DIR / "deployment_runbook.md"

QUESTION_FILE = DATA_DIR / "sample_questions.json"

START_TIME = datetime(2026, 6, 18, 10, 0, 0)

# ----------------------------------------------------------
# Enterprise Environment
# ----------------------------------------------------------

SERVICES = [
    "payment-api",
    "order-service",
    "inventory-service",
    "auth-service",
    "notification-service",
]

ENVIRONMENTS = [
    "production",
    "staging",
]

SOURCES = [
    "Jenkins",
    "Docker",
    "Kubernetes",
    "PostgreSQL",
    "Redis",
    "Application",
]

SEVERITIES = [
    "INFO",
    "WARN",
    "ERROR",
]

# ----------------------------------------------------------
# Incident Definition
# ----------------------------------------------------------


@dataclass
class IncidentTemplate:

    title: str

    root_cause: str

    resolution: str

    lessons: str

    timeline: list[tuple[str, str, str]]


# ----------------------------------------------------------
# Incident Templates
# ----------------------------------------------------------

INCIDENT_TEMPLATES = [

    IncidentTemplate(

        title="Deployment Failure",

        root_cause="PostgreSQL connection pool exhausted during schema migration.",

        resolution="Increase PostgreSQL connection pool, rerun migration and redeploy.",

        lessons="Monitor connection pool usage before deployment.",

        timeline=[

            ("Jenkins", "INFO", "Deployment started"),

            ("Docker", "INFO", "Docker image pulled"),

            ("Kubernetes", "INFO", "Deployment initiated"),

            ("PostgreSQL", "WARN", "Connection pool nearing capacity"),

            ("PostgreSQL", "ERROR", "Database connection refused"),

            ("Application", "ERROR", "Migration timed out"),

            ("Jenkins", "ERROR", "Rollback initiated"),

            ("Jenkins", "ERROR", "Deployment failed"),

        ],

    ),

    IncidentTemplate(

        title="Redis Failure",

        root_cause="Redis exhausted available memory and stopped serving requests.",

        resolution="Restart Redis and increase memory allocation.",

        lessons="Enable Redis memory alerts.",

        timeline=[

            ("Redis", "INFO", "Cache warming completed"),

            ("Redis", "WARN", "Memory usage exceeded 90%"),

            ("Redis", "ERROR", "Redis unavailable"),

            ("Application", "WARN", "Fallback to database"),

            ("Application", "WARN", "API latency increased"),

            ("Redis", "INFO", "Redis restarted"),

            ("Application", "INFO", "Service recovered"),

        ],

    ),

    IncidentTemplate(

        title="Container CrashLoop",

        root_cause="Application crashed repeatedly because of an unhandled exception.",

        resolution="Fix application startup exception and redeploy.",

        lessons="Improve startup health checks.",

        timeline=[

            ("Docker", "INFO", "Container started"),

            ("Application", "ERROR", "Unhandled exception during startup"),

            ("Kubernetes", "ERROR", "CrashLoopBackOff detected"),

            ("Kubernetes", "WARN", "Restarting container"),

            ("Application", "ERROR", "Startup failed"),

            ("Kubernetes", "ERROR", "Pod unhealthy"),

        ],

    ),

    IncidentTemplate(

        title="Image Pull Failure",

        root_cause="Container registry authentication failed.",

        resolution="Refresh registry credentials and retry deployment.",

        lessons="Rotate registry credentials before expiration.",

        timeline=[

            ("Jenkins", "INFO", "Deployment started"),

            ("Docker", "ERROR", "Registry authentication failed"),

            ("Kubernetes", "ERROR", "ImagePullBackOff"),

            ("Kubernetes", "WARN", "Retrying image pull"),

            ("Jenkins", "ERROR", "Deployment failed"),

        ],

    ),

]

# ----------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------

def write_csv(path: Path, headers: list[str], rows: list[list]) -> None:
    """Write rows to a CSV file."""

    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)


def build_timestamp(offset_seconds: int) -> str:
    """Return timestamp string."""

    return (
        START_TIME + timedelta(seconds=offset_seconds)
    ).strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------
# Enterprise Log Generator
# ----------------------------------------------------------

def generate_enterprise_logs():

    rows = []

    incident_history = []

    incident_number = 1001

    time_offset = 0

    # Generate 50 realistic incidents
    for _ in range(50):

        template = random.choice(INCIDENT_TEMPLATES)

        incident_id = f"INC-{incident_number}"

        service = random.choice(SERVICES)

        environment = random.choice(ENVIRONMENTS)

        # Store incident summary
        incident_history.append([
            incident_id,
            template.title,
            template.root_cause,
            template.resolution,
            template.lessons
        ])

        # Build timeline
        for source, severity, message in template.timeline:

            component = source

            rows.append([
                build_timestamp(time_offset),
                incident_id,
                source,
                service,
                component,
                severity,
                message,
                environment
            ])

            time_offset += random.randint(20, 90)

        # Small gap before next incident
        time_offset += random.randint(180, 600)

        incident_number += 1

    # Save enterprise log file
    write_csv(
        ENTERPRISE_LOG_FILE,
        [
            "timestamp",
            "incident_id",
            "source",
            "service",
            "component",
            "severity",
            "message",
            "environment"
        ],
        rows
    )

    # Save incident history
    write_csv(
        INCIDENT_FILE,
        [
            "incident_id",
            "title",
            "root_cause",
            "resolution",
            "lessons_learned"
        ],
        incident_history
    )

    print(f"Generated {len(rows)} enterprise log events")
    print(f"Generated {len(incident_history)} incidents")
# ----------------------------------------------------------
# Runbook Generator
# ----------------------------------------------------------

def generate_runbook():

    runbook = """# Deployment Failure Runbook

## Symptoms

- Deployment failed
- Database connection refused
- Migration timeout
- ImagePullBackOff
- CrashLoopBackOff

## Investigation

1. Check Jenkins deployment logs.
2. Verify Kubernetes events.
3. Verify PostgreSQL connectivity.
4. Check Redis health.
5. Review application logs.

## Resolution

- Increase PostgreSQL connection pool.
- Restart affected services.
- Retry schema migration.
- Redeploy application.

## Verification

- Deployment completed successfully.
- All pods are healthy.
- No ERROR logs present.
- Application health endpoint returns HTTP 200.

"""

    with open(RUNBOOK_FILE, "w", encoding="utf-8") as f:
        f.write(runbook)

    print("Generated deployment_runbook.md")


# ----------------------------------------------------------
# Sample Questions
# ----------------------------------------------------------

def generate_sample_questions():

    questions = [
        "Why did deployment fail?",
        "Show the timeline for INC-1001.",
        "What caused the PostgreSQL connection failure?",
        "Why did Kubernetes restart the pod?",
        "Summarize incident INC-1005.",
        "Which incidents involved Redis?",
        "How was the deployment failure resolved?",
        "Which services experienced the highest failures?",
        "Recommend a resolution for deployment failures.",
        "Show evidence supporting the root cause."
    ]

    with open(QUESTION_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4)

    print("Generated sample_questions.json")


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    print("=" * 60)
    print("Grounded RAG Log Analyzer")
    print("Enterprise Dataset Generator")
    print("=" * 60)

    generate_enterprise_logs()

    generate_runbook()

    generate_sample_questions()

    print("\nDataset generation completed successfully.\n")

    print(f"Enterprise Logs : {ENTERPRISE_LOG_FILE}")
    print(f"Incidents      : {INCIDENT_FILE}")
    print(f"Runbook         : {RUNBOOK_FILE}")
    print(f"Questions       : {QUESTION_FILE}")

    print("\nReady for ingestion.")


if __name__ == "__main__":
    main()
