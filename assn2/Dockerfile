FROM ubuntu

MAINTAINER neil castellino <neilcastellino@gmail.com>

RUN apt-get update

ADD server_persistent_storage server_storage/

RUN ls
RUN ls server_storage/

CMD ["echo", "Hello World! from my first Docker Image"]
