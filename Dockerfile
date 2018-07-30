FROM django

ADD . /project-tcc
WORKDIR /project-tcc
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]