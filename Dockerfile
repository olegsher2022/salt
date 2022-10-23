FROM python:3.10
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
# ENTRYPOINT [ "python3" ]
EXPOSE 5000
# CMD ["flask" "--app server.py" "run" "--host 0.0.0.0" "--port 5000"]
CMD ["python3" , "./server.py" ]