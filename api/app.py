from flask import Flask, request
import logging
import json
from flask_cors import CORS
from getStatusId import test

app = Flask(__name__)
CORS(app)

@app.route("/sendToFlaskReturnToVue", methods=['POST'])
def returnTweetIDList():
    # Receive handle and term from Vue input
    target_handle = request.json['handle']
    termToSearch = request.json['term']
    
    # console log
    app.logger.warning(target_handle)
    app.logger.warning(termToSearch)
    
    # Produce list of tweets matching else return null
    tweetIDList = test(target_handle, termToSearch)



    # if tweetIDList is a null (not a list) return a fail object
    if (type(tweetIDList) is not list):
      app.logger.warning(type(tweetIDList))
      return {
          "1":"fail"
      }
    # else return JSON converted tweet list
    else:
      # console logs
      app.logger.warning(tweetIDList[0])
      app.logger.warning(type(json.dumps(tweetIDList)))
      app.logger.warning(json.dumps(tweetIDList))
      
      return json.dumps(tweetIDList)