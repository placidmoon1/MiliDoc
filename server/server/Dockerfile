# 1 
#mecab installation reference: https://github.com/litsynp/flask-g2pk/blob/main/Dockerfile
FROM python:3.7

# 2
RUN pip install Flask gunicorn pyrebase4 flask_cors flask_sqlalchemy pandas 
RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ git curl
RUN apt-get install -y g++ default-jdk default-jre
# 3
COPY src/ /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install nltk
RUN pip install konlpy

RUN cd . && \
  curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s

RUN export LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app