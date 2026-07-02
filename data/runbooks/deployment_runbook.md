# Deployment Failure Runbook

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

