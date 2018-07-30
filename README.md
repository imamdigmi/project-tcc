# Django on Heroku
This is for exam on my college

## Running Locally
```bash
$ git clone git@github.com:imamdigmi/project-tcc.git
$ cd project-tcc

$ pipenv install

$ createdb project_tcc

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```bash
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
