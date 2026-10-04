# The pull model, made visible

A tiny app increments a counter every 200ms. Prometheus scrapes it. Change the scrape interval and watch the graph lose resolution.

## Run

```
docker compose up -d --build
```

- App metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin / admin)

## Set up Grafana

1. Add a Prometheus data source pointing at `http://prometheus:9090`.
2. New dashboard, new panel, query:

```
rate(ticks_total[5s])
```

## Experiment

1. With `scrape_interval: 1s` (the default here), watch the panel track the underlying 200ms ticks closely.
2. Edit `prometheus.yml`, change `scrape_interval` to `30s`, then:

```
docker compose restart prometheus
```

3. Watch the same query over the same window — the line gets visibly blockier and loses the real shape of the underlying signal, since Prometheus only ever knows what the counter's value was at each scrape, never what happened between scrapes.
4. Try a few interval values (`5s`, `10s`, `30s`) and compare.
