# astronomy-stuff

Astronomer docs: https://www.astronomer.io/docs/astro/cli/overview

## Setup

Installing Astronomer CLI:
```bash
curl -sSL install.astronomer.io | sudo bash -s

astro version
```

Installing Docker: https://docs.docker.com/desktop/install/ubuntu/

Handling permissions:
```bash
cd astro
bash permissions.sh
```

## Running Airflow

To start airflow:
```bash
astro dev start
```

To stop airflow:
```bash
astro dev stop
```

## Package Docs

XMM Newton: https://astroquery.readthedocs.io/en/latest/esa/xmm_newton/xmm_newton.html