from flask import Flask
from flask import request

import json
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object( DevelopmentConfig )

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    if request.methods == 'GET':
        verify_token = request.args.get('hub.verify_token')
        if verify_token == app.config['SECRET_KEY']:
            return request.args.get('hub.challenge', '')
        return 'Error al validar el secreto'

    elif request.methods == 'POST':
        payload = request.get_data()
        data = json.loads(payload)

        for page_entry in data['entry']:

            for message_event in page_entry['messaging']:

                if 'message' in message_event:
                    evento = message_event['message']
                    print (evento['text'])

        return "ok"


@app.route('/', methods = ['GET'])
def index():
    return 'Hi DuckBot'

if __name__ == '__main__':
    app.run(port = 8000)
