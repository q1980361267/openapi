FROM python:3.7.3
WORKDIR /auto_openapi
ENV REFRESHED_AT 2020 08 20
COPY . .
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN apt-get update && apt-get install -y vim