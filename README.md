# JOB-CRUD

## Description

An app built with Flask, Python, HTML, and JavaScript to create, list, update, and delete your job applications.

## Local Installation

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

## Technologies and programming languages 

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **JavaScript** [Source](https://developer.mozilla.org/es/docs/Web/JavaScript)
* **Flask** (v. 2.3.2)  [Source](https://flask.palletsprojects.com/en/2.2.x/)
* **Flask-SQLAlchemy** (v. 3.0.3) [Source](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)
* **Flask-Bootstrap** (v. 3.3.7.1) [Source](https://pythonhosted.org/Flask-Bootstrap/)
* **python-dotenv** (v. 1.0.0) [Source](https://pypi.org/project/python-dotenv/)
* **SweetAlert2** (v. 11.7.5) [Source](https://sweetalert2.github.io/)
* **mysqlclient** (v. 2.1.1) [Source](https://pypi.org/project/mysqlclient/)

## Author

- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)