# Deployment Failure Runbook

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
