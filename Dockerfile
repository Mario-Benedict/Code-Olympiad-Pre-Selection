FROM python:latest

WORKDIR /usr/src/app

RUN python3 -m venv env
RUN source env/bin/activate

COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

COPY . .

CMD [ "make", "run" ]