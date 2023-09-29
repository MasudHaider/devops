FROM python:3.8

WORKDIR /usr/src/app

RUN pip install flask
RUN mkdir -p /usr/src/app/logs

COPY . .

EXPOSE 8000

# since "python service2.py" gave error while testing locally
CMD ["python3", "service2.py"]