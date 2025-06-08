FROM python:3.11

WORKDIR /app

COPY app.py .

RUN pip install flask psycopg2-binary

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
