
FROM python:3.8
RUN pip install pdm
RUN pdm config python.use_venv false
RUN pdm install --prod --no-lock --no-editable
ENV PYTHONPATH=__pypackages__/3.8/lib
COPY . ./
CMD python3 docker_test.py