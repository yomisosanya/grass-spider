FROM  mcr.microsoft.com/playwright/python:v1.50.0-noble

ARG APP_DIR
ARG APP_NAME
ARG FILE_DIR

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY README.md .
COPY pyproject.toml .
COPY .env .
COPY hatch.toml .
COPY src/ ./src/

RUN pip install hatch 

RUN pip install -e .

RUN playwright install --with-deps chromium

# WORKDIR $APP_DIR
CMD ["python", "-m", "spider"]

# CMD ["spider"]

