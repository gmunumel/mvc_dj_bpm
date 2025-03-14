FROM python:3.12.6-slim AS base

# Install wget for integration tests
RUN apt-get update && apt-get install -y \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv

WORKDIR /app

RUN pip install virtualenv
RUN virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy all files we need. At some point we should use a multistage build for test and prod (and exclude test code from prod image)
COPY pyproject.toml requirements.txt main.py ./
COPY src/ ./src/

# need to be in this order
RUN pip install .

EXPOSE 5000
ENTRYPOINT ["python", "main.py"]