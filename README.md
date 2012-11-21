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

<i><dl>
<dd>git clone https://github.com/Freso/MusicBottle.git</dd>
</dl></i>

This will create a directory "MusicBottle". Navigate to it:

<i><dl>
<dd>cd MusicBottle</dd>
</dl></i>

Create a virtual environment *(Note 1)* and install dependencies:
<i><dl>
<dd>virtualenv venv</dd>
<dd>. venv/bin/activate</dd>
<dd>pip install Flask Flask-Babel pymongo Flask-Script</dd>
</dl></i>
Run the server:
<i><dl>
<dd>python manage.py runserver</dd>
</dl></i>

If the above gives an error, try to use "python2" instead of "python".

Finally, in a web browser, navigate to:
<i><dl>
<dd>http://localhost:19048</dd>
</dl></i>

---

**Note 1**

On Debian and Ubuntu Linux:
<i><dl>
<dd>sudo apt-get install python-virtualenv</dd>
</dl></i>

This will also install python and pip.
