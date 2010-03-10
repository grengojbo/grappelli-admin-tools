.. _quickstart:

Quick start guide
=================

Before installing django-admin-tools, you'll need to have a copy of
`Django <http://www.djangoproject.com>`_ already installed. For the
|version| release, Django 1.1 or newer is required.


Installing django-admin-tools
-----------------------------

django-admin-tools requires Django version 1.1 or superior, optionally, 
if you want to display feed modules, you'll also need the 
`Universal Feed Parser module <http://www.feedparser.org/>`_.

There are several ways to install django-admin-tools, this is explained 
in :ref:`the installation section <installation>`.

For the impatient, the easiest method is to install django-admin-tools via  
`easy_install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_ 
or `pip <http://pip.openplans.org/>`_. 

Using ``easy_install``, type::

    easy_install -Z django-admin-tools

Note that the ``-Z`` flag is required, to tell ``easy_install`` not to
create a zipped package; zipped packages prevent certain features of
Django from working properly.

Using ``pip``, type::

    pip install django-admin-tools


Basic configuration
-------------------

For a more detailed guide on how to configure django-admin-tools, please
consult :ref:`the configuration section <configuration>`.

Prerequisite
~~~~~~~~~~~~

In order to use django-admin-tools you obviously need to have configured
your Django admin site. If you didn't, please refer to the 
`relevant Django documentation <http://docs.djangoproject.com/en/1.1/intro/tutorial02/#activate-the-admin-site>`_.

.. important::
    It is required that you use the Django 1.1 syntax to declare the 
    Django admin urls, e.g.::

        urlpatterns = patterns('',
            (r'^admin/', include(admin.site.urls)),
        )

    The old url style ``(r'^admin/(.*)', admin.site.root)`` won't work.

Required settings
~~~~~~~~~~~~~~~~~

First make sure you have the following template context processors 
installed::

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.auth',
        'django.core.context_processors.request',
    )

Then, add admin_tools and its modules to the ``INSTALLED_APPS`` like 
this::

    INSTALLED_APPS = (
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.auth',
        'django.contrib.sites',
        'django.contrib.admin'
        # ...other installed applications...
    )

.. important::
    it is very important that you put the admin_tools modules **before** 
    the ``django.contrib.admin module``, because django-admin-tools
    overrides the default Django admin templates, and this will not work 
    otherwise.

django-admin-tools is modular, so if you want to disable a particular 
module, just remove or comment it out in your ``INSTALLED_APPS``, note 
that ``admin_tools`` is required for i18n.


Setting up the database
~~~~~~~~~~~~~~~~~~~~~~~

To set up the tables that django-admin-tools uses you'll need to type::

    python manage.py syncdb

Adding django-admin-tools to your urls.py file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll need to add django-admin-tools to your urls.py file::

    urlpatterns = patterns('',
        url(r'^admin_tools/', include('admin_tools.urls')),
        #...other url patterns...
    )

Setting up the django-admin-tools media files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To do this you have two options:

* create a symbolic link to the django-admin-tools media files to your 
  ``MEDIA_ROOT`` directory, for example::

      ln -s /usr/local/lib/python2.6/dist-packages/admin_tools/media/admin_tools /path/to/yourproject/media/

* copy the django-admin-tools media files to your ``MEDIA_ROOT`` directory, 
  for example::
  
      cp -r /usr/local/lib/python2.6/dist-packages/admin_tools/media/admin_tools /path/to/yourproject/media/


Testing your new shiny admin interface
--------------------------------------

Congrats! At this point you should have a working installation of 
django-admin-tools. Now you can just login to your admin site and see what 
changed.

django-admin-tools is fully customizable, but this is out of the scope of 
this quickstart. To learn how to customize django-admin-tools modules 
please read :ref:`the customization section<customization>`.

