from wakeonlan import send_magic_packet
from markupsafe import escape
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/wakeup/<mac>")
def wakeup(mac):
    print(mac)
    send_magic_packet(mac)
    return render_template('index.html', mac=escape(mac))
    #return f"Waking up {escape(mac)}"

