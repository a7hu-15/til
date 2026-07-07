# Docker Compose Detached Mode

To run your docker-compose services in the background without tying up your terminal, use the `-d` (detached) flag:

```bash
docker-compose up -d
```
You can later view logs with `docker-compose logs -f`.