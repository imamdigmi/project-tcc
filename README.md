# Django on Heroku
This is just app for demo!

[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg?style=flat-square)](https://hub.docker.com/r/imamdigmi/project-tcc/)

## Setup
1. Clone the app
```bash
git clone git@github.com:imamdigmi/project-tcc.git && cd project-tcc
```

2. Install dependencies and activate envirounment
```bash
pipenv install && pipenv shell
```

3. Create database
```bash
createdb project_tcc
```

4. Migrate database and collecting static files
```bash
python manage.py migrate && python manage.py collectstatic
```

## Running Locally
```bash
python manage.py runserver
```
or
```bash
heroku local
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

1. Create app instance on heroku
```bash
heroku create
```

2. Deploy to heroku
```bash
git push heroku master
```

3. Launch the app
```bash
heroku run python manage.py migrate
heroku open
```


[![Deployment Demo](https://img.youtube.com/vi/HPrq7ZNSS-8/0.jpg)](https://www.youtube.com/watch?v=HPrq7ZNSS-8)
