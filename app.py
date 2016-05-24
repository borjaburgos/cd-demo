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
           "<img src=https://s3.amazonaws.com/f.cl.ly/items/3G0u1j1Y3z2H2M1z1M2A/docker_cloud.png>"
        #  "<img src=https://s3.amazonaws.com/f.cl.ly/items/0T2g2E1m2i0J272C2v2R/Image%202016-05-24%20at%2009.20.06.png>"
    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
