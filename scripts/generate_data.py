"""
Grounded RAG Log Analyzer
Enterprise Synthetic Data Generator

Generates:
- application_logs.csv
- deployment_logs.csv
- kubernetes_logs.csv
- incident_history.csv
- deployment_runbook.md
- sample_questions.json
"""

from pathlib import Path
import csv
import json
import random
from datetime import datetime, timedelta

# ------------------------------------------------------
# Configuration
# ------------------------------------------------------

random.seed(42)

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"

LOG_DIR = DATA_DIR / "logs"
INCIDENT_DIR = DATA_DIR / "incidents"
RUNBOOK_DIR = DATA_DIR / "runbooks"

LOG_DIR.mkdir(parents=True, exist_ok=True)
INCIDENT_DIR.mkdir(parents=True, exist_ok=True)
RUNBOOK_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------
# Enterprise Environment
# ------------------------------------------------------

SERVICES = [
    "payment-api",
    "order-service",
    "inventory-service",
    "auth-service",
    "notification-service"
]

HOSTS = [
    "prod-app-01",
    "prod-app-02",
    "prod-app-03"
]

SEVERITY = [
    "INFO",
    "WARN",
    "ERROR"
]

DEPLOYMENTS = [
    "v2.0.1",
    "v2.1.0",
    "v2.1.3",
    "v2.2.0"
]

# ------------------------------------------------------
# Incident Templates
# ------------------------------------------------------

INCIDENTS = [

    {
        "title": "Database Connection Timeout",
        "root_cause":
            "PostgreSQL stopped accepting new client connections.",
        "resolution":
            "Increase connection pool and restart database.",
        "messages": [
            "Database connection refused",
            "Connection timeout",
            "Migration failed due to timeout",
            "Rollback initiated",
            "Deployment marked FAILED"
        ]
    },

    {
        "title": "Redis Cache Failure",
        "root_cause":
            "Redis became unavailable because of memory pressure.",
        "resolution":
            "Restart Redis and warm cache.",
        "messages": [
            "Redis unavailable",
            "Cache miss rate increased",
            "Switching to database reads",
            "Latency increased",
            "Redis recovered"
        ]
    },

    {
        "title": "Out Of Memory",
        "root_cause":
            "Application exceeded Kubernetes memory limit.",
        "resolution":
            "Increase memory limit and fix memory leak.",
        "messages": [
            "Pod restarted",
            "OOMKilled",
            "Container terminated",
            "Restart policy activated",
            "Service recovered"
        ]
    },

    {
        "title": "Image Pull Failure",
        "root_cause":
            "Docker registry authentication failed.",
        "resolution":
            "Refresh registry credentials.",
        "messages": [
            "ImagePullBackOff",
            "Registry authentication failed",
            "Deployment waiting",
            "Retrying image pull",
            "Deployment failed"
        ]
    }

]

# ------------------------------------------------------
# Timestamp Generator
# ------------------------------------------------------

START_TIME = datetime(2026, 6, 18, 10, 0, 0)


def next_timestamp(counter):

    return (
        START_TIME +
        timedelta(seconds=counter * random.randint(5, 15))
    ).strftime("%Y-%m-%d %H:%M:%S")


# ------------------------------------------------------
# CSV Helpers
# ------------------------------------------------------

def write_csv(path, headers, rows):

    with open(path, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(headers)

        writer.writerows(rows)


# ------------------------------------------------------
# Application Logs
# ------------------------------------------------------

def generate_application_logs():

    rows = []

    counter = 0

    for _ in range(200):

        incident = random.choice(INCIDENTS)

        rows.append([
            next_timestamp(counter),
            random.choice(SERVICES),
            random.choice(HOSTS),
            random.choice(SEVERITY),
            random.choice(incident["messages"]),
            "production"
        ])

        counter += 1

    write_csv(
        LOG_DIR / "application_logs.csv",
        [
            "timestamp",
            "service",
            "host",
            "severity",
            "message",
            "environment"
        ],
        rows
    )

    print("✔ application_logs.csv generated")

# ------------------------------------------------------
# Deployment Logs
# ------------------------------------------------------

def generate_deployment_logs():

    rows = []

    for deployment_id in range(1, 81):

        incident = random.choice(INCIDENTS)

        version = random.choice(DEPLOYMENTS)

        status = random.choice([
            "SUCCESS",
            "FAILED",
            "ROLLED_BACK"
        ])

        duration = random.randint(60, 900)

        rows.append([
            f"DEP-{deployment_id:04d}",
            version,
            status,
            duration,
            incident["title"]
        ])

    write_csv(
        LOG_DIR / "deployment_logs.csv",
        [
            "deployment_id",
            "version",
            "status",
            "duration_seconds",
            "reason"
        ],
        rows
    )

    print("✔ deployment_logs.csv generated")


# ------------------------------------------------------
# Kubernetes Logs
# ------------------------------------------------------

def generate_kubernetes_logs():

    rows = []

    counter = 0

    events = [
        "Pod Started",
        "Container Created",
        "Container Restarted",
        "ImagePullBackOff",
        "CrashLoopBackOff",
        "OOMKilled",
        "Liveness Probe Failed",
        "Readiness Probe Failed"
    ]

    namespaces = [
        "production",
        "payments",
        "orders"
    ]

    nodes = [
        "worker-node-01",
        "worker-node-02",
        "worker-node-03"
    ]

    for i in range(80):

        rows.append([
            next_timestamp(counter),
            f"payment-api-{100+i}",
            random.choice(namespaces),
            random.choice(nodes),
            random.choice(events),
            random.choice(SEVERITY)
        ])

        counter += 1

    write_csv(
        LOG_DIR / "kubernetes_logs.csv",
        [
            "timestamp",
            "pod",
            "namespace",
            "node",
            "event",
            "severity"
        ],
        rows
    )

    print("✔ kubernetes_logs.csv generated")


# ------------------------------------------------------
# Historical Incidents
# ------------------------------------------------------

def generate_incidents():

    rows = []

    for i in range(25):

        incident = random.choice(INCIDENTS)

        rows.append([
            f"INC-{1000+i}",
            incident["title"],
            incident["root_cause"],
            incident["resolution"],
            "Improve monitoring and add preventive alerts."
        ])

    write_csv(
        INCIDENT_DIR / "incident_history.csv",
        [
            "incident_id",
            "title",
            "root_cause",
            "resolution",
            "lessons_learned"
        ],
        rows
    )

    print("✔ incident_history.csv generated")


# ------------------------------------------------------
# Runbook
# ------------------------------------------------------

def generate_runbook():

    content = """# Deployment Failure Runbook

## Symptoms

- Deployment marked FAILED
- Database timeout
- Pod restart loop
- ImagePullBackOff

## Investigation Steps

1. Verify deployment status.
2. Check Kubernetes events.
3. Review application logs.
4. Verify PostgreSQL connectivity.
5. Check Redis availability.

## Resolution

- Restart failed services.
- Increase DB connection pool.
- Fix failed migration.
- Redeploy application.

## Verification

- Deployment completed successfully.
- Pods are healthy.
- No ERROR logs observed.
"""

    with open(
        RUNBOOK_DIR / "deployment_runbook.md",
        "w"
    ) as f:

        f.write(content)

    print("✔ deployment_runbook.md generated")


# ------------------------------------------------------
# Sample Questions
# ------------------------------------------------------

def generate_questions():

    questions = [

        "Why did deployment fail?",

        "Why was the application rolled back?",

        "What caused the database timeout?",

        "Why are Kubernetes pods restarting?",

        "What caused ImagePullBackOff?",

        "Why is Redis unavailable?",

        "What is the root cause of incident INC-1001?",

        "Suggest a resolution for deployment failure.",

        "Show evidence for deployment failure.",

        "Which service experienced the highest failures?"

    ]

    with open(
        DATA_DIR / "sample_questions.json",
        "w"
    ) as f:

        json.dump(
            questions,
            f,
            indent=4
        )

    print("✔ sample_questions.json generated")


# ------------------------------------------------------
# Main
# ------------------------------------------------------

def main():

    print("=" * 60)
    print("Generating Enterprise Synthetic Dataset")
    print("=" * 60)

    generate_application_logs()

    generate_deployment_logs()

    generate_kubernetes_logs()

    generate_incidents()

    generate_runbook()

    generate_questions()

    print("\nDataset generation completed successfully.")
    print(f"\nData location: {DATA_DIR}")


if __name__ == "__main__":
    main()
