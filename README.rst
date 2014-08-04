###################
Django Social Links
###################

Allow to create social link (facebook, twitter, others...) and assing them
to groups or any other object in your project.

*******
Install
*******

It is strongly recommanded to install this app from GIT with PIP onto you project virtualenv.


.. code-block::  shell-session

   pip install -e git+https://github.com/tomaszroszko/django-social-links.git#egg=django-social-links


Add app to you settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'sociallinks'
        ...
    )


Run syncdb and migrate command

.. code-block::  shell-session

    python manage.py syncdb
    python manage.py migrate


*******
Usage
*******


Example of getting all social links for 'user'

.. code-block::  python

    {% load sociallink_tags %}

    {% obj_social_links user as user_links %}
    {% for link in user_links %}
        <a href="{{ link.link }}" class="{{ link.link_type.css_class }}">
            {{ link.link_type.name }}
        </a>
    {% endfor %}
