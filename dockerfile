
FROM python:3.10
RUN pip install pdm
RUN pdm config python.use_venv false
RUN pdm install --prod --no-lock --no-editable
ENV PYTHONPATH=__pypackages__/3.10/lib
COPY . ./
CMD python3 clustering_test.py