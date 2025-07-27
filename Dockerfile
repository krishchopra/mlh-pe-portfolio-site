FROM quay.io/centos/centos:stream9

RUN dnf install -y python3.9 python3-pip

WORKDIR /mlh-pe-portfolio-site

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
