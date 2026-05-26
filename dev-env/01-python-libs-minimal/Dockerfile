FROM python:3.14-slim

ARG NB_USER=jupyter
ARG NB_UID=1000
ARG NB_GID=100

RUN useradd -m -u ${NB_UID} -g ${NB_GID} -s /bin/bash ${NB_USER}

RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-dejavu \
    python3-tk \
    tini \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --only-binary=:all: \
    ipykernel \
    ipywidgets \
    jupyterlab \
    matplotlib \
    notebook \
    numpy \
    pandas \
    scikit-learn \
    scipy \
    seaborn \
    statsmodels

USER ${NB_USER}
WORKDIR /workspace
EXPOSE 8888

ENV JUPYTER_TOKEN=""

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["sh", "-c", "jupyter notebook --ServerApp.token=\"${JUPYTER_TOKEN}\" --ip=0.0.0.0 --no-browser --port=8888"]
