from flask import Flask, render_template, request

from google.appengine.api import memcache

app = Flask(__name__)
app.config['DEBUG'] = True

cronNum = 0

@app.route('/cronjob')
def addCron():
    global cronNum
    cronNum = cronNum + 1
    return render_template('cron.html', cronNum = cronNum)
