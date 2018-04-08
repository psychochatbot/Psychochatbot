#!/usr/bin/env python

import urllib
import json
import os
import pickle
import io
from flask import Flask
from flask import request
from flask import make_response
from flask import session



# Flask app should start in global layout
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'
with open('filename.pkl', 'rb') as f:
    model = pickle.load(f,encoding='latin1')
    
with io.open('data.json', 'w', encoding='utf8') as outfile:
    entry = {}
    entry['name'] = 'happy'
    str_=json.dumps(entry,ensure_ascii=False)
    outfile.write((str_))
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


#with open('record.txt','w') as ef:
 #   ef.write('ephimerel testing')
#print(model.predict([[2,0,0,1]]))

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

def dump_value(key,value):
    with open('data.json', 'r') as data_file:
        data_loaded =json.loads(data_file.read())
    with io.open('data.json', 'w', encoding='utf8') as outfile:
        #data_loaded =json.loads(outfile)
     #   abc=eval(data_loaded)
        data_loaded[key]=value
        str_=json.dumps(data_loaded,ensure_ascii=False)
        outfile.write((str_))

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
    
    
    if req.get("result").get("action") == "action_welcome":
        result = req.get("result")
        session.clear()
        with io.open('data.json', 'w', encoding='utf8') as outfile:
            entry = {}
            entry['name'] = 'happy'
            str_=json.dumps(entry,ensure_ascii=False)
            outfile.write((str_))
        return {}
      #  return {
       #  "speech": "apka swagat h",
        #"displayText": "apka swagat h"
        #}
    
    
    if req.get("result").get("action") == "action_welcome_good_day":
        result = req.get("result")
        print(model.predict([[2,0,0,1]]))
       # parameters = result.get("parameters")
        #for key in session.keys():
         #   session.pop(key)
        session.clear()
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
        dump_value('father_occupation',father_occupation)
        #with io.open('data.json', 'a', encoding='utf8') as outfile:
         #   entry = {}
         #   entry['father_occupation']=father_occupation
          #  str_=json.dumps(entry,ensure_ascii=False)
           # outfile.write((str_))
        with open('data.json', 'r') as data_file:
            data_loaded =json.loads(data_file.read())
            print(data_loaded['father_occupation'])
           # data_file.close()
        if('mother_occupation' not in data_loaded):
            speech="your father is "+data_loaded['father_occupation']+" what does your mother do?"
            return {
            "speech": speech,
            "displayText": speech,
            "source": "apiai-psychochatbot"
     }
        #speech="Okay, let's talk about your family"
        else:    
            speech="your father is "+father_occupation+"and maa is "+session['mother_occupation']
            return {
            "speech": speech,
            "displayText": speech,
            "source": "apiai-psychochatbot",
            "followupEvent": {
            "name": "event_ask_be_like"
            }
     }
        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot"
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
            return {
            "speech": speech,
            "displayText": speech,
            "source": "apiai-psychochatbot"
     }
        #speech="Okay, let's talk about your family"
        else:    
            speech="your mother is "+mother_occupation+" and your father is "+session['father_occupation']
            return {
            "speech": speech,
            "displayText": speech,
            "source": "apiai-psychochatbot",
            "followupEvent": {
            "name": "event_ask_be_like"
            }
     }
          
          
    if req.get("result").get("action") == "action_ask_be_like_father":
        result = req.get("result")
        session['ask_be_like']="father"
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_hobbies_interests"
        }
    }
       
       
    if req.get("result").get("action") == "action_ask_be_like_mother":
        result = req.get("result")
        session['ask_be_like']="mother"
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_hobbies_interests"
        }
    }
    
    
    if req.get("result").get("action") == "action_hobbies_interests_art":
        result = req.get("result")
        session['hobby']="arts"
        session['duration']=duration
        session['certis']= certifications
        session['as_career']=as_career
        session['parents_support']=parents_support
        parameters = result.get("parameters")
        duration=parameters.get("duration")
        certifications=parameters.get("certifications")
        as_career=parameters.get("as_career")
        parents_support=parameters.get("parents_support")
        return {
       # "speech": "arts",
        #"displayText": "arts",
        "source": "apiai-psychochatbot",
       # "followupEvent": {
        #   "name": "event_hobbies_interests"
        #}
    }
    
    if req.get("result").get("action") == "action_hobbies_interests_sports":
        result = req.get("result")
        parameters = result.get("parameters")
        duration=parameters.get("duration")
        achievements=parameters.get("achievements")
        as_career=parameters.get("as_career")
        parents_support=parameters.get("parents_support")
        return {
        "source": "apiai-psychochatbot",
       # "followupEvent": {
        #   "name": "event_hobbies_interests"
        #}
    }
    
    if req.get("result").get("action") == "action_hobbies_interests_misc":
        result = req.get("result")
        parameters = result.get("parameters")
        duration=parameters.get("duration")
        certification=parameters.get("certification")
        as_career=parameters.get("as_career")
        parents_support=parameters.get("parents_support")
        return {
        "source": "apiai-psychochatbot",
       # "followupEvent": {
        #   "name": "event_hobbies_interests"
        #}
    }
    
    
    #if req.get("result").get("action") == "action_hobbies_interests_arts_no" or "action_hobbies_interests_sports_no" or "action_hobbies_interests_misc_no" or "action_hobbies_interests_extras_no":
     #   return{
      #    "followupEvent": {
       #   "name": "event_ask_about_family"
        #}
        #}
          
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
