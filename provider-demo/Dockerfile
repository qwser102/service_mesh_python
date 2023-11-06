FROM python/base:v1
RUN mkdir -p /app
ADD ./provider-demo /app
CMD ["sh","-c","cd /app ; python3 app.py"]
EXPOSE 8081
