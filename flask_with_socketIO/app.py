from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'enigma'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( 'index.html' )

def logRec():
  print( 'message was received!!!' )

@socketio.on( 'default event' )
def handleEvent( json ):
  print( 'Message recieved: ' + str( json ) )
  socketio.emit( 'response', json, callback=logRec)

if __name__ == '__main__':
  socketio.run( app, debug = True )