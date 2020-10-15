from flask import render_template, send_from_directory, request
from app import app
import json

# Main site pages

@app.route('/')
def homepage():
    return render_template('pages/index.html')

@app.route('/about')
def aboutpage():
    
    with open('app/members.json') as membersfile:
        members = json.load(membersfile)

    return render_template('pages/about.html', members=members)

@app.route('/events')
def eventspage():
    return render_template('pages/events.html')

@app.route('/contact')
def contactpage():
    return render_template('pages/contact.html')

@app.route('/resources')
def resourcespage():
    return render_template('pages/resources.html')

# Static resources

@app.route('/robots.txt')
def robotstxtpage():
    return send_from_directory('static', filename='robots.txt')

@app.route('/favicon.ico')
def faviconpage():
    return send_from_directory('static', filename='favicon.ico')

@app.route('/qa.pdf')
def qapdfpage():
    return send_from_directory('static', filename='qa.pdf')

# Error handling

@app.errorhandler(404)
def pagenotfounderror(error):
    return(render_template('error/404.html')) # Return a nice and pretty custom 404 error page