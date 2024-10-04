FROM python:3.12-slim

COPY . /home/apps
WORKDIR /home/apps

RUN apt update && apt install -y sqlite3
RUN pip install --upgrade pip && pip install -r requirements.txt
# Remove existing DB if exist, and Execute SQL file and exit
RUN rm -f dict.db && sqlite3 -init init_db.sql dict.db ".exit"

ENTRYPOINT ["python", "main.py"]