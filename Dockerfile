FROM ubuntu:latest
RUN apt-get -y update  && apt-get install -y python3.10  python3-pip wget
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN rm -rf __pycache__
RUN rm -rf .pytest_cache
RUN rm -rf .venv
CMD ["python3" , "./server.py" ]
