Basic MusicBottle documentation
===============================

MusicBottle is meant as a way to display data from MusicBrainz' webservice in a
more presentable format than what MusicBrainz itself can achieve while catering
to its most importants users' - the editors' - workflow of editing the data.

See more about the project at our WikiPage:
https://wiki.musicbrainz.org/MusicBottle

Installing MusicBottle
----------------------

First obtain latest sources:
    git clone https://github.com/Freso/MusicBottle.git

This will create a directory "MusicBottle". Navigate to it:
    cd MusicBottle

Create a virtual environment *(Note 1)* and install dependencies:
    virtualenv venv
    . venv/bin/activate</dd>
    pip install Flask Flask-Babel pymongo Flask-Script

Run the server:
    python manage.py runserver

If the above gives an error, try to use `python2` instead of `python`.

Finally, in a web browser, navigate to http://localhost:19048

---

**Note 1**

On Debian and Ubuntu Linux:
    sudo apt-get install python-virtualenv

This will also install python and pip.
