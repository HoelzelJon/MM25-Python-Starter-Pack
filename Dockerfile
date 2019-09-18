FROM python:3.7.0-alpine
COPY . .
CMD python Server.py Strategy 5000
