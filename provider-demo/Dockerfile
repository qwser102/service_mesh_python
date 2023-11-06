FROM 192.168.183.144/devops/builder-python:3.6-debian-ac120cff
RUN mkdir -p /app
ADD ./provider-demo /app
RUN pip install -r /app/requirements.txt
CMD ["sh","-c","cd /app ; python3 app.py"]
EXPOSE 8081
