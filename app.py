#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import session


# Flask app should start in global layout
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'

#@app.before_first_request
#def initiali():
 #  global father_occupation
  # global mother_occupation
   



@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res) 
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    #father_occupation=""
   # mother_occupation=""
    if req.get("result").get("action") == "how_are_you":
      #  return {}
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("how_r_u")
        speech="you are "+str(zone)
    #speech="you are bhoot"
        print(zone)
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
            "name": "event_occupation_father"
        }
    }
    
    
    if req.get("result").get("action") == "action_welcome_good_day":
        result = req.get("result")
       # parameters = result.get("parameters")
       
        speech="Okay, let's talk about your family"
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_ask_about_family"
        }
    }
    
    if req.get("result").get("action") == "action_welcome_bad_day":
        result = req.get("result")
       # parameters = result.get("parameters")
       
        speech="Okay, let's talk about your family"
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_ask_about_family"
        }
    }
    
    #THIS IS NEW VERSION
    if req.get("result").get("action") == "action_father_occupation":
        result = req.get("result")
        parameters = result.get("parameters")
        father_occupation=parameters.get("f_o")
        session['father_occupation']=father_occupation
        if('mother_occupation' not in session):
            speech="your father is "+session['father_occupation']+" what does your mother do?"
        #speech="Okay, let's talk about your family"
        else:    
            speech="your father is "+father_occupation
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
      #  "followupEvent": {
       #    "name": "event_ask_about_family"
        #}
    }
    
     #THIS IS NEW VERSION
    if req.get("result").get("action") == "action_mother_occupation":
        result = req.get("result")
        parameters = result.get("parameters")
        mother_occupation=parameters.get("m_o")
        session['mother_occupation']=mother_occupation
        #if(session['father_occupation']==""):
        if('father_occupation' not in session):
            speech="your mother is "+mother_occupation+" what does your father do?"
        #speech="Okay, let's talk about your family"
        else:    
            speech="your mother is "+mother_occupation+" and your father is "+session['father_occupation']
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
      #  "followupEvent": {
       #    "name": "event_ask_about_family"
        #}
    }
    
    
   # if req.get("result").get("action") == "action_ask_about_family_yes":
    #    result = req.get("result")
       # parameters = result.get("parameters")
       
   #     speech="Okay, let's talk about your family"
   #     print(speech)
    #    return {
     #   "speech": speech,
      #  "displayText": speech,
        #"data": {},
        #"contextOut": [],
      #  "source": "apiai-psychochatbot",
       # "followupEvent": {
        #   "name": "event_occupation_father"
        #}
    #}
    
    
        
    if req.get("result").get("action") == "action_occupation_father":
        result = req.get("result")
        parameters = result.get("parameters")
        occupation_father=parameters.get("f_o")
        speech="your father is "+str(occupation_father)
       # print(occup)
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_occupation_mother"
        }
    }
    
    
    if req.get("result").get("action") == "action_occupation_mother":
        result = req.get("result")
        parameters = result.get("parameters")
        occupation_mother=parameters.get("m_o")
        speech="your mother is "+str(occupation_mother)
      #  print(occup)
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
       # "data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_want_to_be_father"
        }
    }
    
    
    
        
        
    # if req.get("result").get("action") == "occupation_":
     #   result = req.get("result")
      #  parameters = result.get("parameters")
       # occup=parameters.get("abc")
        #speech="your father is "+str(occup)
        #print(occup)
        #print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-psychochatbot",
        "followupEvent": {
            "name": "I1"
        }
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
  #  app.secret_key="Sgsits2018"
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')
