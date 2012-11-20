#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""Manage the MusicBottle server."""
from musicbottle import app
from flask.ext.script import Manager, Server

manager = Manager(app)
manager.add_command("runserver", Server(port=app.config['PORT']))

if __name__ == "__main__":
    manager.run()
