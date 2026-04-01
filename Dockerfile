FROM  mcr.microsoft.com/playwright/python:v1.50.0-noble

WORKDIR .

COPY pyproject.toml

RUN pip install hatch

RUN pip install -e .

RUN playwright install --with-deps


