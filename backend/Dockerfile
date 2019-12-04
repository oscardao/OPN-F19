FROM python:latest

ENV FLASK_APP server.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN pip3 install Flask
RUN pip3 install mysql-connector-python==8.0.11
COPY server.py server.py
CMD ["flask", "run"]
