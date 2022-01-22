FROM python:latest

ADD mydata.txt /server_storage/
ADD server.py /server_storage/

WORKDIR /server_storage/

EXPOSE 5002

CMD ["python3", "/server_storage/server.py"]
