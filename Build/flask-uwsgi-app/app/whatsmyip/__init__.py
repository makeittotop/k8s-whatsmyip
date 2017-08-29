#!/usr/bin/env python

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  if os.environ.has_key('POD_IP'):
    message=os.environ['POD_IP']
  else:
    message="Hello from minikube"

  return message

if __name__ == '__main__':
  app.run()
