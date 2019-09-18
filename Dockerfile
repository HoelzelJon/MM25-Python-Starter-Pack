FROM python:3.7.0-alpine
COPY . .
RUN pip install flask
EXPOSE 8080
CMD python Server.py Strategy
