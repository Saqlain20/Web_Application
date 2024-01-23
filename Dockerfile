FROM python:3.8-alpine           
#virtual os

# RUN apk update && apk add git 

WORKDIR /flask-loan-app
#working directory inside the container

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY .  .
# Copy everything from the current directory to the PWD (Present Working Directory) inside the container

# CMD ["python", "-m","flask", "run", "--host=0.0.0.0"]

CMD ["python", "-m","flask", "--app", "app.py", "run", "--host=0.0.0.0"]



# codes used
# 1) docker build -t "imagefilename" .
# 2) docker image ls
# 3) docker run -p 5000:5000 "imagename" / docker run -d -p 5000:5000 "imagename"    (-d is used to let the container keep running in the background)
# 4) docker tag "imagename" maverickmindset10/loan_prediction_app:"tagname"
# 5) docker push maverickmindset10/loan_prediction_app:"tagname"