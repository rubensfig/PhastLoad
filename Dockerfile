FROM fedora:27

RUN mkdir /phastload
WORKDIR /phastload

ADD requirements.txt /phastload/requirements.txt

RUN dnf -y install httpd python3-pip gcc && dnf clean all; systemctl enable httpd.service

RUN pip3 install -r requirements.txt

EXPOSE 80
ADD . /phastload
