#!flask/bin/python
from flask import Flask, Response
import json
import threading
from funciones_scrap import *

app = Flask(__name__)
app.debug=True
cookies = {}

def reload_cookies():
  global cookies
  print 'Updating cookies'
  threading.Timer(300.0, reload_cookies).start()
  cookies=get_cookies('http://civil.poderjudicial.cl/CIVILPORWEB/')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/rut/<string:rut>')
def get_info(rut):
  global cookies
  dv = rut[-1]
  rutnum = rut[:-1]
  # resultados=rut_scraper(rutnum,dv,cookies)
  array = [{'rol': 'CT556644', 'algo': 'algo'}, {'rol': 'CT553344', 'algo': 'algo'}]
  return Response(json.dumps(array),  mimetype='application/json')

@app.route('/cookies')
def cookies():
  
  return get_cookies('http://civil.poderjudicial.cl/CIVILPORWEB/')

if __name__ == '__main__':
  # reload_cookies()
  # app.run(debug=True)
  app.run(host='0.0.0.0')