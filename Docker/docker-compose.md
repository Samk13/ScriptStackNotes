
<video src="https://www.youtube.com/watch?v=KDh8aIwfIac">full video</video>

Quick way to see if you did something wrong:

```bash
# list your docker compose
docker compose config

# list all images used
docker compose config --images 

# list all services
docker compose config --services

# list all volumes
docker compose config --volumes
```

## Pass SSH key to your docker image

If you pass ssh key from you agent
if you want private dependecy from a private repo,
ssh can be made securlly in docker compose

```yml
services
  web:
    build:
      context:
      ssh: ["default"]
      
RUN --mount=type=ssh,id=default git clone ...
```

## dockerfile inline

Another option if to have the possiblity to write a dockerfile in a dockerfile!

```yml
services
  web:
    build:
      context:
      dockerfile_inline: |
        FROM nginx
        COPY static/ /usr/share/nginx/html

```

# depends_on > condition

This only apply when creating services, has no affect after creation in case of restart or fail.
default: service_started
there is also: service_exited_succesfully

```yml
services
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres

```

# depends > restart

```yml
services
  web:
    build: .
    depends_on:
      db:
        restart: true
  db:
    image: postgres
```

# depends_on > required

```yml
services
  web:
    build: .
    depends_on:
      jaeger:
        required: false
  jaeger:
    image: jaegertracing/all-in-one
    profiles: ["tracing"]
```

Yaml Anchors
This will merge these 2 services, basically it's a pointer to the same file so you don't need to write it twice

```yml
services
  app:
    environment:
      <<: *common-env
      POSTGRES_USER: postgres
x-common-env: &common-env
  LOG_LEVEL: debug
  NODE_ENV: development
  TZ: Europe/Stockholm
  LANG: sv_SE.UTF-8
```

you can check if it's correct by running: `docker compose config`
the `x-` in `x-common-env` that's a compose specific feature that it dosnt' know about field it will show an error,
so x- wil allow to pass the key before it know it.

# compose specific featrue

## !reset

compose.yaml

```yml
services
  web:
    build: .
    depends_on:
      jaeger:
        required: false
  jaeger:
    image: jaegertracing/all-in-one
    profiles: ["tracing"]
```

Yaml Anchors
This will merge these 2 services, basically it's a pointer to the same file so you don't need to write it twice

```yml
services
  app:
    build:
      <<: *common-env
      POSTGRES_USER: postgres
x-common-env: &common-env
  LOG_LEVEL: debug
  NODE_ENV: development
  TZ: Europe/Stockholm
  LANG: sv_SE.UTF-8
```

## !reset

compose.yaml

```yml
services
  app:
    build:
      context: .
      target: dev
      pull: true
    port:
      - 8080:80
```

compose.override.yaml

```yml
services
  app:
    image: docker.io/milas/app
    build: !reset null
    ports: !reset []
```

when override and you want to clear this field you pass `!reset null` if it's a list you pass `!reset []`

result will be:

```yml
services
  app:
    image: docker.io/milas/app
```

```bash
docker compose alpha viz
```

```digraph
digraph "voc-test" {
        layout=dot;
        "search" [style="filled" label=<<font point-size="15">search</font>>];
        "opensearch-dashboards" [style="filled" label=<<font point-size="15">opensearch-dashboards</font>>];
        "pgadmin" [style="filled" label=<<font point-size="15">pgadmin</font>>];
        "cache" [style="filled" label=<<font point-size="15">cache</font>>];
        "db" [style="filled" label=<<font point-size="15">db</font>>];
        "mq" [style="filled" label=<<font point-size="15">mq</font>>];

}

```

you can visualize your docker compose connections if you paste the results in [digraph visulizer like:] (<https://dreampuf.github.io/GraphvizOnline/#digraph>)

# Tracing

see the whole picture on how you project is been built, you can take a snapshot as waterfall in services like Jaeger UI
<https://www.jaegertracing.io/docs/1.51/>

```bash
export COMPOSE_EXPERIMENTAL_OTEL=1
export OTEL_EXPORTER_OTLP_ENPOINT='http://localhost:5000'
docker compose up
```

# include

```bash
export COMPOSE_EXPERIMENTAL_GIT_REMOTE=1
include:
  - https://github.com/dockersamples/avatares.git#main
```

# x-develop

Make it watch as you are on your development env

```yaml
services:
  web:
    pull_policy: build
    build: .
    develop:
      watch:
        - path: web/
          target: /app
          action: sync
        - path: web/package.json
          action: rebuild
```
