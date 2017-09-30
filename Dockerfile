From python:3.5
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["sh","/app/run.sh"]
CMD []
