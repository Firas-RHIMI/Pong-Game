FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip install requirements.txt
COPY objects/ objects/
COPY scripts/ scripts/
RUN chmod +x /scripts/entrypoint.sh
ENTRYPOINT ["scripts/entrypoint.sh"]
