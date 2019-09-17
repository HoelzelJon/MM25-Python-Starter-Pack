FROM python:3.7.0-alpine
RUN pip install flask
COPY . .
CMD python Server.py Strategy