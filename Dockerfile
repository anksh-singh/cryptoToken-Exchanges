# 
FROM python:3.10.7

# 
WORKDIR /token

# 
COPY ./requirements.txt /code/requirements.txt

RUN pip install fastapi uvicorn 

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
