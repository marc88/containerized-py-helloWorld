FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt
RUN pip install -r requirements.txt
COPY hello_world.py
EXPOSE 5000
CMD python hello_world.py
