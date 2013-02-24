=================================
 Basic MusicBottle documentation
=================================

MusicBottle is a web application which aims to display MusicBrainz data in a
more presentable format that the MusicBrainz website does. MusicBrainz must
allow for both viewing and editing of data and because of this data isn't
always displayed in the clearest way.

See more about the project at our WikiPage:
https://wiki.musicbrainz.org/MusicBottle

Installing MusicBottle
----------------------

Make sure you have a reasonably recent Python 2 installed. We're working with
compatibility for Python >= 2.6.3. It's recommended to use ``pip`` and
``virtualenv`` for dependencies. ``virtualenv`` is available as a package in
most distributions, e.g. as ``python-virtualenv`` in Ubuntu and Debian and
``python2-virtualenv`` in ArchLinux. Installing this should also pull in
Python 2 and PIP.

Obtain the latest sources and navigate to them::

    git clone https://github.com/Freso/MusicBottle.git
    cd MusicBottle

If you decided to go with with using ``virtualenv``, now is a good time to make a
virtual environment::

    virtualenv venv
    . venv/bin/activate

Install download and install the required dependencies::

    pip install -U --download-cache=/tmp/pip -I -r requirements.txt --no-install
    pip install -U --download-cache=/tmp/pip -I -r requirements.txt --no-download

Running MusicBottle
-------------------

Inside the project directory, run ``python manage.py runserver`` to start
the server.

You can run ``python manage.py runserver -h`` to see a list of options for
starting the server. E.g., if you need to run it on a different port than
the default.

If the commands above give errors, try using ``python2`` instead of ``python``.

Configuring MusicBottle
-----------------------

If you want to configure MusicBottle settings, copy
``musicbottle/default_settings.py`` somewhere, edit it and set the environment
variable ``MUSICBOTTLE_SETTINGS`` to point to the edited file.

Accessing MusicBottle
---------------------

Once you have the test server running, you should be able to access it at
http://127.0.0.1:19048/
