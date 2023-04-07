FROM python:3.9
WORKDIR /app
COPY pyproject.toml ./
COPY poetry.lock ./
COPY ./ ./
RUN pip install poetry
RUN poetry install
CMD ["poetry", "run", "flask", "--app", "src/roomie_api", "run", "--host=0.0.0.0"]