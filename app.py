#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response
from flask import session as login_session
import sqlalchemy
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from http.server import BaseHTTPRequestHandler, HTTPServer
from pprint import pprint
import httplib2
import random
import string
import json
import requests

engine = create_engine('sqlite:///database.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template("login.html", client_id=CLIENT_ID)


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # Login
        if self.path.endswith('/login'):
            self.send_response(200)
            return

        # Categories Form
        if self.path.endswith("/categories/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Make A New Category</h1>"
            output += "<form method = 'POST' enctype='multipart/form-data' action = '/categories/new'>"
            output += "<input name = 'title' type = 'text' placeholder = 'Category Title' > "
            output += "<input type='submit' value='Create'>"
            output += "</form></body></html>"
            self.wfile.write(output)
            return

        # Categories Index
        if(self.path.endswith("/categories")):
            categories = session.query(Category).all()
            output = ""
            output += """
                <a href = '/categories/new'>Make a New Category here</a>
                <br>"
            """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output += "<html><body>"
            for category in categories:
                output += category.title
                output += "</br>"
                output += "<a href='#'>Edit</a>"
                output += "</br>"
                output += "<a href='#'>Delete</a>"
            output += "</body></html>"
            self.wfile.write(output)
            return

            # Log

    def do_POST(self):
        try:
            if self.path.endswith("/categories/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('title')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8005)
