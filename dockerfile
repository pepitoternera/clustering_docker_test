
FROM python:3.10
RUN pdm install
COPY . .
RUN python3 clustering_test.py