#import argparse
#from wakeonlan import send_magic_packet

#def main():
    #parser = argparse.ArgumentParser() 
    #parser.add_argument('mac', help='MAC address') 
    #args = parser.parse_args() 
    #print(f'Sending magic wakeup packet to {args.mac}')
    #send_magic_packet(args.mac)
#
#if __name__ == "__main__":
    #main()


#import os
#from flask import Flask
#from markupsafe import escape
#
#app = Flask(__name__)
#
#@app.route("/<mac>")
#def home(mac):
    #send_magic_packet(mac)
    #return f"Waking up {escape(mac)}"
#
#if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    #app.run(debug=True, host='0.0.0.0', port=port)


from wakeonlan import send_magic_packet
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(mac):
    send_magic_packet(mac)
    return f"Waking up {escape(mac)}"

