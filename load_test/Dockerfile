FROM python:3.7
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
COPY locustfile.py locustfile.py
COPY mining_flotation_test.csv mining_flotation_test.csv
EXPOSE 8089
CMD ["locust", "-f", "locustfile.py", "--host", "http://127.0.0.1:5000"]