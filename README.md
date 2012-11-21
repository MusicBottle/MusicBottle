Installing MusicBottle
----------------------

First obtain latest sources:

  *git clone https://github.com/Freso/MusicBottle.git*

Enter the directory:

  *cd MusicBottle*

Create a virtual environment and install dependencies:

  *virtualenv venv*
  *. venv/bin/activate*
  *pip install Flask Flask-Babel pymongo Flask-Script*

Run the server:

  *python manage.py runserver*
  
If the above gives an error, try to use "python2" instead of "python".

Finally, in a web browser, navigate to:
 
  *http://localhost:19048*
