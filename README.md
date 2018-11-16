# Python initial web development model

This is a simple code for understanding python web development.
And this application is specifically developed for deploying on AWS Lightsail using ubuntu 18.04.

- Python Framework : [_Flask_](http://flask.pocoo.org/)
- DB Toolkit(ORM) : [_SQLAlchemy_](https://www.sqlalchemy.org/)
- DB Type : [_PostgreSQL_](https://www.postgresql.org/)
- Web Server : [_Apache2_](https://httpd.apache.org/)
- OS Type : [_Ubuntu 18.04_](https://www.ubuntu.com/)
- Hosting : [_AWS Lightsail_](https://aws.amazon.com/lightsail/)
- WSGI : [_mod_wsgi_](https://modwsgi.readthedocs.io/en/develop/)


## The database

The database has 2 tables. And database_setup.py contains the definition of it.

- Category
- CategoryItem

## Installation & Usage

Clone the GitHub repository
```
$ git clone https://github.com/brokolidev/catalog-final.git
$ cd catalog-final
```

And then simply use your command line tool to generate DB and insert some sample data.
```
$ python database_setup.py
$ python samplecategory.py
```

## JSON Endpoint

There are 4 JSON endpoint included.
- /category.json > All categories and information of it's containing items.
- /categories/JSON > All the categories only.
- /items/JSON > All the items only.
- /item/<int:item_id>/JSON > details of an item by providing item_id.

# About google oauth

You need to download your google oauth client_secret file to use google login.
Save it to in the same directory with app.py file and name it client_secret.json.
