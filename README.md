# Python initial web development model

This is a simple code for understanding python web development.
And this application is specifically developed for deploying on AWS Lightsail using ubuntu 18.04.

- Python Framework : [_Flask_](http://flask.pocoo.org/)
- DB Toolkit(ORM) : [_SQLAlchemy_](https://www.sqlalchemy.org/)
- DB Type : [_PostgreSQL_](https://help.ubuntu.com/community/PostgreSQL)
- Web Server : [_Apache2_](https://httpd.apache.org/)
- OS Type : [_Ubuntu 18.04_](https://www.ubuntu.com/)
- Hosting : [_AWS Lightsail_](https://aws.amazon.com/lightsail/)
- WSGI : [_mod_wsgi_](https://modwsgi.readthedocs.io/en/develop/)


## The database

The database has 2 tables. And database_setup.py contains the definition of it.

- Category
- CategoryItem

You need to create a new user called "garder" and set password.
And replace the password in database_setup.py, samplecategory.py, category.py with the password you created.

# Google oauth

You need to download your google oauth client_secret file to use google login.
Also you need to setup google oauth credentials properly.
Save it to in the same directory with app.py file and name it client_secret.json.
`Replace the client_secret.json path in the catalog.py file with yours`

# Using WSGI

You need to create file for using WSGI
Here is an sample code of wsgi.py
```
import sys
sys.path.insert(0, '/var/www/catalog')

from catalog import app as application
```
`Replace the path and module name if necessary`


## Installation & Usage

Clone the GitHub repository
```
$ git clone https://github.com/brokolidev/catalog-final.git catalog
$ cd catalog
```

And then simply use your command line tool to generate tables and some sample data.
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
