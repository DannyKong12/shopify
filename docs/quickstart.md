# Quickstart

Pull the project to get started, we'll be using `python 3.6` for this project

```bash
git clone https://github.com/DannyKong12/shopify
```

Install some dependencies, if you need

```bash
pip install django django-filter django-toolbelt graphene-django
```

## Initialize

Once you've pulled the repo, go ahead and migrate the database

```bash
python manage.py makemigrations products
python manage.py migrate
```

Let's populate our tables with some test data. Install the fixture included in the repo.

```bash
python manage.py loaddata products
```

If everything is installed properly, go ahead and run this line to deploy a local test server.

```bash
python manage.py runserver
```

Navigate to localhost on the port specified by Django, to the route `'/graphql'`. This should bring up the GraphIQL view.
