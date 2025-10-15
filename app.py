# Poetlog is a simple IP logger that generates poet lyrics with AI based on your information

from flask import Flask, render_template, request
import os
from utils.geo import request_geo

app = Flask(__name__)

@app.route('/')
def index():

    ip = request.headers.get('X-Forwarded-For', request.remote_addr) #get ip
    geodata = request_geo(ip)

    return render_template('index.html', geodata=geodata)

if __name__ == "__main__":

    port = int(os.getenv("PORT", 4040))
    app.run(host="0.0.0.0", port=port)