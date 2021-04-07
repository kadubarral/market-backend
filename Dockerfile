FROM python:3.8.5

RUN apt-get update && apt-get install
RUN python -m pip install --upgrade pip
RUN mkdir /usr/src/app/

COPY . /usr/src/app/

WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 5000

CMD ["./start.sh"]