# JOB-CRUD

## Description

An app built with Flask, Python, HTML, and JavaScript to create, list, update, and delete your job applications.

## Getting Started

First clone the repository from Github and switch to the new directory:
```bash
  $ clone git https://github.com/Geffrerson7/JOB-CRUD.git
```

```bash
  $ cd JOB-CRUD
```

Activate the virtualenv for your project.

```sh
$ virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Install project dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Create the following environment variables in the .env file

`FLASK_APP`

`FLASK_DEBUG`

`FLASK_ENV`

`SECRET_KEY`

`SQLALCHEMY_DATABASE_URI`

Execute the migrations:

```sh
(env)$ flask db init
```

```sh
(env)$ flask db migrate
```

```sh
(env)$ flask db upgrade
```

You can now run the development server:
```sh
(env)$ flask run
```

And navigate to
```sh
http://127.0.0.1:5000/
```

## Author

- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)