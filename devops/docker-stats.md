# Checking Resource Usage of Docker Containers

To view a live stream of container resource usage statistics (CPU, memory, network I/O, etc.), use:

```bash
docker stats
```
To get stats for a specific running container:
```bash
docker stats container_name
```
To format the output to show only specific fields:
```bash
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```