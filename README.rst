=====================
www.pytosquatting.org
=====================

This is a Django project.

It's bare bones without any magic.

To run it:

#. Create a virtualenv
#. Install `django 1.11`
#. Write something in local.py (see below)
#. ``python manage.py migrate``
#. ``python manage.py runserver``


``pythosquatting/settings/local.py``

.. ::
  python
  from .base import *  # @UnusedWildImport

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'SOMETHING SECRET FOR A DEV ENV'

