FROM python:3.10.12 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.12

ENV PYTHONFAULTHANDLER=1 \
        PYTHONUNBUFFERED=1 \
        PYTHONHASHSEED=random \
        PIP_NO_CACHE_DIR=off \
        PIP_DISABLE_PIP_VERSION_CHECK=on \
        PIP_DEFAULT_TIMEOUT=100 \
        PYTHONDONTWRITEBYTECODE=1

RUN apt-get update    
RUN apt-get -y install \
        wget \
        libxft-dev \
        libffi-dev \
        libssl-dev

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

# colocar esse comando no compose e criar um entrypoint.sh para rodar migrações do DB (alembic)
CMD exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload 