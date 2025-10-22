FROM python:3.12-slim AS python-base
ARG app_version=0.0.0+development-container
ARG POETRY_VERSION=2.1.1

# Set up environment variables for Poetry and the application
ENV POETRY_HOME="/opt/poetry" \
    POETRY_CACHE_DIR="/tmp/poetry-cache" \
    APP_DIR="/app"
ENV PATH="$APP_DIR/.venv/bin:$POETRY_HOME/bin:$PATH"
ENV UVICORN_PORT=8000 \
    UVICORN_HOST=0.0.0.0

# Set working directory
WORKDIR $APP_DIR

# ----- app-common-builder -----
FROM python-base AS app-common-builder

# Create a virtual environment for poetry and install
RUN python -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install --upgrade pip setuptools
RUN $POETRY_HOME/bin/pip install poetry==${POETRY_VERSION}
RUN $POETRY_HOME/bin/poetry config virtualenvs.create true
RUN $POETRY_HOME/bin/poetry config virtualenvs.in-project true

# Install main dependencies inside virtual environment
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=${POETRY_CACHE_DIR} $POETRY_HOME/bin/poetry install --no-ansi --no-root

# Copy the application source code
COPY --link me_ai ./me_ai

# Stamp the version file
RUN printf "__version__ = \"%s\"\n" "$app_version" > ./me_ai/version.py

EXPOSE "${UVICORN_PORT}/tcp"

# ----- development -----
FROM app-common-builder AS development

# Install dev dependencies inside virtual environment
RUN --mount=type=cache,target=${POETRY_CACHE_DIR} $POETRY_HOME/bin/poetry install --no-ansi --no-root --with dev

CMD ["/app/.venv/bin/python", "-m", "me_ai"]

# ----- production -----
FROM python-base AS production
COPY --link --from=app-common-builder $APP_DIR $APP_DIR

CMD ["/app/.venv/bin/python", "-m", "me_ai"]