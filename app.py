import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests

app = flask.Flask(__name__)
import models
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')
# all_numbers = []
@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    # all_numbers.append(data['number'])
    # socketio.emit('all numbers', {
    #     'numbers': all_numbers
    # })

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'

all_numbers = []
@socketio.on('new number')
def on_new_number(data):
    # print 'Got a new message with data: ', data
    
    response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json()
    
    all_numbers.append(data['number'])
    socketio.emit('all numbers', {
        'numbers': all_numbers
    })
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )