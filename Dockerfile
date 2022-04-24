FROM python:3.8-slim-buster
RUN mkdir /project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY objects/ objects/
COPY scripts/entrypoint.sh entrypoint.sh
COPY main.py main.py
RUN chmod +x entrypoint.sh
ENTRYPOINT ["bash", entrypoint.sh"]
