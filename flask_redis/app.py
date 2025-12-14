import socket
import redis
import socket
from flask import Flask, make_response

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count() -> int:
    return int(cache.get('hits') or 0)


def incr_hit_count() -> int:
    return cache.incr('hits')


@app.route('/metrics')
def metrics():
    metrics_text = f'''
# HELP view_count Flask-Redis-App visit counter
# TYPE view_count counter
view_count{{service="Flask-Redis-App"}} {get_hit_count()}
'''
    response = make_response(metrics_text, 200)
    response.mimetype = "text/plain"
    return response


@app.route('/')
def hello():
    incr_hit_count()
    count = get_hit_count()
    return 'Hello World v.1.0.2! I have been seen {} times. My name is: {}\n'.format(count, socket.gethostname())
