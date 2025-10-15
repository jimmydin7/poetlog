# Poetlog is a simple IP logger that generates poet lyrics with AI based on your information

from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":

    port = int(os.getenv("PORT", 4040))
    app.run(host="0.0.0.0", port=port)