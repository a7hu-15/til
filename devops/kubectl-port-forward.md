# Kubectl Port Forwarding

You can access internal Kubernetes services or pods directly from your local machine.

```bash
kubectl port-forward svc/my-service 8080:80
```
This forwards your local port 8080 to the service's port 80.