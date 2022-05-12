from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'enigma'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( 'index.html' )

def logRec():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'Message recieved: ' + str( json ) )
  socketio.emit( 'my response', json, callback=logRec)

if __name__ == '__main__':
  socketio.run( app, debug = True )