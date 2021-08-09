
import flask
from flask import request, jsonify
import random
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address
app = flask.Flask(__name__)

limiter = Limiter(app, key_func=get_remote_address) # Set the ratelimiting strategy (Uses IP adress)

@app.route('/api/message', methods=['put'])       # Define what method and url has to be used to get the response
@limiter.limit("2/hour")                          # Set the ratelimit
def replace():
    if 'newMessage' in request.json:              # Checks if the requests countains the newMessage parameter
        if len(request.json['newMessage']) < 100: # Checks if the message contains less that 100 characters sothat the databas ewont be spammed

          newMessage = request.json['newMessage'] # Grab the newMessage value from the request's json args
          token_file = open("message.txt", "a")   #--
          token_file.write(f"{newMessage} \n")    #  | Open a file and writes the message sothat it can be stored for the get request 
          token_file.close()                      #--
          
          return f"Updated message to {newMessage}!",200 # Inform the user that the request was successful 
        else:
          return f"Limit the amount of characters to 100! {len(request.json['newMessage'])}",400 # If the characters is more than 100, return an error
    else:
        return 'Error: Remember to send your message inside the "newMessage" field',400 # If the request doesn't contain the new message, return an error
@app.errorhandler(429)                                                                  # If error 429, do the following:
def ratelimit_handler(e):
     return '{\n"ErrorCode": "429"\n"message": "You have been ratelimited.\n}',429      # Send back a ratelimit message


@app.route('/api/message', methods=['get']) # Define what method and url has to be used to get the response
def get_message(): 
    message = open("message.txt").read().splitlines() # 
    LastLine = message[-1]                            #
    messageJSON = {                                   #
                                                      # Get the bottom line from the file and save it into the messageJSON variable
          "message": LastLine                         #
                                                      #
    }                                                 #
    
    return jsonify(messageJSON),200                   # Send messageJSON back to the user with statuscode 200

app.run(debug=True)                                   # Run the app
