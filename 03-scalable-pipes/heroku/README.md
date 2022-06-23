# Heroku

## Simple Workflow

```
git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started/
heroku apps:create --buildpack heroku/python
git push heroku main
heroku ps:scale web=1
heroku open
heroku run bash
```
