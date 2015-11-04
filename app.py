from flask import Flask
from redis import Redis, RedisError
import os
import socket

app = Flask(__name__)

# Connect to Redis
redis = Redis(host="redis")

@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "<i>counter disabled. Cannot connect to Redis.</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>" \
           "<img src=http://bit.ly/1Cry9PX>"
    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
