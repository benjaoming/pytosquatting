=====================
www.pytosquatting.org
=====================

This is a Django project.

It's bare bones without any magic.

To run it:

 1. Create a virtualenv
 1. Install `django 1.11`
 1. Write something in local.py (see below)
 1. `python manage.py migrate`
 1. `python manage.py runserver`


`pythosquatting/settings/local.py`

```
from .base import *  # @UnusedWildImport

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SOMETHING SECRET FOR A DEV ENV'
```
