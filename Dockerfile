FROM python:latest

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN cd /bin
COPY ./geckodriver /bin/geckodriver
RUN chmod +x /bin/geckodriver
RUN export PATH=$PATH:/bin/geckodriver

# COPY ./firefox /firefox
# RUN chmod +x /firefox/firefox
# RUN mv firefox /opt
# RUN  ln -s /opt/firefox/firefox /usr/local/bin/firefox

# COPY ./firefox.desktop /usr/local/share/applications

RUN mkdir /app
COPY ./app /app
WORKDIR /app