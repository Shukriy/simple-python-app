# Simple Python App Documentation

## Overview

A lightweight Flask-based REST API service that provides health check and application information endpoints. This service is containerized and deployed on Kubernetes with Helm charts.

## Architecture

- **Framework**: Flask (Python)
- **Container**: Docker
- **Orchestration**: Kubernetes (via Helm)
- **Ingress**: Traefik/ArgoCD managed
- **Port**: 8080

## API Endpoints

### Health Check

```http
GET /api/v1/healthz
```

**Description**: Returns the health status of the application.

**Response**:
```json
{
  "status": "healthy"
}
```

**Status Codes**:
- `200 OK` - Service is healthy and operational

**Use Case**: Used by Kubernetes liveness and readiness probes to monitor application health.

---

### Application Information

```http
GET /api/v1/info
```

**Description**: Returns metadata and version information about the application.

**Response**:
```json
{
  "name": "simple-python-app",
  "version": "1.0.0",
  "description": "A simple Python Flask API",
  "environment": "development"
}
```

**Status Codes**:
- `200 OK` - Successfully retrieved application info

**Use Case**: Provides version tracking and environment identification for debugging and monitoring.

## Access

### Production URL
```
https://python-app.test.com/api/v1/healthz
```

### Local Development
```bash
# Run locally
python src/app.py

# Access at
http://localhost:8080/api/v1/healthz
http://localhost:8080/api/v1/info
```

### Docker
```bash
# Build
docker build -t simple-python-app .

# Run
docker run -p 8080:8080 simple-python-app

# Access at
http://localhost:8080/api/v1/healthz
```

### Kubernetes
```bash
# Deploy with Helm
helm install simple-python-app ./charts/simple-python-app

# Port forward for local access
kubectl port-forward svc/simple-python-app 8080:8080
```

## Monitoring

- **Health Checks**: Monitor `/api/v1/healthz` endpoint
- **Logs**: Available via `kubectl logs` or centralized logging solution
- **Metrics**: Application metrics exposed for Prometheus scraping (if configured)

## Development

### Prerequisites
- Python 3.9+
- Docker (for containerization)
- Kubernetes cluster (for deployment)
- Helm 3.x

### Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

### Testing
```bash
# Test health endpoint
curl http://localhost:8080/api/v1/healthz

# Test info endpoint
curl http://localhost:8080/api/v1/info
```

## Deployment

The application is deployed via ArgoCD and manages its own Helm chart located in `charts/simple-python-app/`.

### Configuration Files
- `Dockerfile` - Container image definition
- `requirements.txt` - Python dependencies
- `charts/simple-python-app/` - Helm chart for Kubernetes deployment
- `k8s/` - Raw Kubernetes manifests (alternative to Helm)

## Troubleshooting

### Application Won't Start
- Check if port 8080 is already in use
- Verify Python dependencies are installed
- Check logs for errors

### Health Check Failing
- Ensure the service is running
- Verify network connectivity
- Check Kubernetes pod status: `kubectl get pods`

### Cannot Access via Ingress
- Verify ingress configuration
- Check DNS resolution for `python-app.test.com`
- Ensure Traefik/ingress controller is running