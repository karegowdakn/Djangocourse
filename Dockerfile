FROM python:3.13-bullseye
ENV PYTHONUNBUFFERED=1\
    PIP_NO_CACHE_DIR=1 \
    # Disable Poetry virtualenvs so packages install into the image env
    POETRY_VIRTUALENVS_CREATE=false

RUN mkdir /code

WORKDIR /code

RUN python -m pip install --upgrade pip \
    && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]