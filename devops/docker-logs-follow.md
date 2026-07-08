# Following Docker Logs

To view continuous output from a running container, use the `-f` flag with `docker logs`.

```bash
docker logs -f container_name
```
It acts just like `tail -f`.