import os
import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  html = ['<h1>Hello Flask, Docker and Kubernetes!</h1>']
  html.append('<p>The time is: %s</p>' % datetime.datetime.now())
  return "\n".join(html)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)


