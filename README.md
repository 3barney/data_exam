# Data Engineer example

Task to test ETL process on a given exchange rates api

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

```
Python3
Postgresql
virtualenv
pip
```

Ensure python3 is available, if not install

```
    python3 -V
```

Install pip if not available

```
    easy_install pip3
```

Install virtualenv

```
    pip install virtualenv
```

### Setup database

Install `postgresdb` if not available

Create database, database user and password.

After cloning the project do set this values in the `database.ini` file

### Setup python

Create a virtualenv propject

```
    virtualenv data_engineer -p python3.7
```

Navigate to `data_engineer` folder created and clone project from github

```
    git clone git@github.com:3barney/data_exam.git
```

Activate python environment while in `data_engineer` folder

```
    source bin/activate
```

Install dependencies using

```
    pip install -r requirements.txt
```

## Running application

Execute

```
    python3 main.py
```

This download api data, transforms and stores in Postgress

To Load view: Execute sql in `summary_view.sql`
