# Scrapyd web service (with authentication)

FROM python:3.7

# install Ubuntu packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    git \
    # python3 support
    python3 python3-pip python3-setuptools \
    # scrapy dependencies
    build-essential python3-dev \
    libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev \
    # nginx and htpasswd
    nginx apache2-utils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# install Chaperone
# (Unofficial repo due to: https://github.com/garywiz/chaperone/issues/24)
#RUN pip3 install chaperone \
RUN pip3 install git+https://github.com/necrophcodr/chaperone.git \
 && mkdir /etc/chaperone.d

# install Scrapyd and dependencies
ADD requirements.txt /
RUN pip3 install -r /requirements.txt \
 && pip3 freeze > /pip3-freeze.txt

# configure
ADD chaperone.conf /etc/chaperone.d/chaperone.conf
ADD nginx.conf /etc/nginx/sites-enabled/default
ADD scrapyd.conf /etc/scrapyd/scrapyd.conf

# expose
ADD .. /code
RUN cd ./code && \
    python3 setup.py bdist_egg && \
    rm -rf /build /default.egg-info

# expose
EXPOSE 6800 6801
ENTRYPOINT ["/usr/local/bin/chaperone"]


VOLUME /scrapyd
EXPOSE 6800

ENTRYPOINT ["/usr/local/bin/chaperone"]
