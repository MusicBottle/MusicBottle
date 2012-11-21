Basic MusicBottle documentation
===============================

MusicBottle is a web application which aims to display MusicBrainz data in a
more presentable format that the MusicBrainz website does. MusicBrainz must
allow for both viewing and editing of data and because of this data isn't
always displayed in the clearest way.

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
    pip install Flask Flask-Babel pymongo Flask-Script pyyaml nltk

Run the server:
    python manage.py runserver

If the above gives an error, try to use `python2` instead of `python`.

Finally, in a web browser, navigate to http://localhost:19048

---

**Note 1**

On Debian and Ubuntu Linux:
    sudo apt-get install python-virtualenv

This will also install python and pip.
