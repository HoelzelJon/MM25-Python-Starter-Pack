FROM python:3.7.0-alpine
COPY . .
RUN pip install flask
CMD python Server.py Strategy
