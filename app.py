from wakeonlan import send_magic_packet
from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/wakeup/<mac>")
def wakeup(mac):
    send_magic_packet(mac)
    return render_template('wakeup.html', mac=escape(mac))

