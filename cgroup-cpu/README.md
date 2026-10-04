# cgroups made visible: CPU limits under load

Prometheus + Grafana + cAdvisor watching a container that burns CPU, with a `cpus` limit applied through Docker.

## Run

```
docker compose up -d --build
```

- cAdvisor: http://localhost:8080
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin / admin)

## Set up Grafana

1. Add a Prometheus data source pointing at `http://prometheus:9090`.
2. New dashboard, new panel, query:

```
rate(container_cpu_usage_seconds_total{name=~"cgroup-cpu-demo-stress.*"}[1m])
```

This is CPU-seconds used per second by the `stress` container — with a 0.5 `cpus` limit, it should flatten out around 0.5 regardless of how many workers are spinning.

## Experiment

1. With the stack running as-is (`cpus: 0.5`, `WORKERS=4`), watch the graph plateau near 0.5.
2. Edit `docker-compose.yml`, remove the `cpus: 0.5` line, then:

```
docker compose up -d --build stress
```

3. Watch the same graph climb toward the number of workers instead of staying capped — that's the cgroup CPU quota being enforced (or not).
4. Try changing `WORKERS` and `mem_limit` and repeat.
