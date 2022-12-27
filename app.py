import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://github.com/Jnanesh124/newhop0 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
