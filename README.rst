==============================================================
 Example Django project BCNTourist
==============================================================

Contents
========

``BCNTourist/``
---------

This is the project iself, created using
``django-admin.py startproject BCNTourist``

``tourist/``
----------

This module contains the Tourist application instance for this project.

``api/``
------------

This module contains the API application instance for this project.

Installing requirements
=======================

The settings file assumes that ``rabbitmq-server`` is running on ``localhost``
using the default ports. More information here:

http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

In addition, some Python requirements must also be satisfied:

.. code-block:: bash

    $ pip install -r requirements.txt

API
===
The Simple API receives a HTTP POST on

.. code-block:: bash
    /api/update/location
    
With the parameters:

card_id = <card_id>
latitude = <latitude>
longitude = <longitude>

API requests are put into a queue with Celery.

Page administrator
==================
The Page administrator was done using django's admin which was moved to the home url.

If using the default sqlite db sent the admin credentials are root::root
Else create a new superuser
    


