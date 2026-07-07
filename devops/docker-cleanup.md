# Cleaning Up Docker Resources

To free up space by removing all stopped containers, unused networks, dangling images, and build cache, use:

```bash
docker system prune
```

To also remove all unused images (not just dangling ones) and volumes:

```bash
docker system prune -a --volumes
```