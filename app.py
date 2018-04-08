#!/usr/bin/env python

import urllib
import json
import os
import pickle
import io
import pandas as pd
from flask import Flask
from flask import request
from flask import make_response
from flask import session
from sklearn.preprocessing import LabelEncoder


# Flask app should start in global layout
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'
with open('psycho.pkl', 'rb') as f:
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
           "name": "event_hobbies_interests"
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
           "name": "event_joke"
        }
    }
    
    if req.get("result").get("action") == "action_joke_no":
        result = req.get("result")
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_joke"
        }
    }
    
    if req.get("result").get("action") == "action_joke_yes":
        result = req.get("result")
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_hobbies_interests"
        }
    }
    
    #THIS IS NEW VERSION
    if req.get("result").get("action") == "action_father_occupation":
        result = req.get("result")
        parameters = result.get("parameters")
        father_occupation=parameters.get("f_o")
        dump_value('father_occupation',father_occupation)
        psycho_algo = pd.read_csv("psycho_data.csv")
        psycho_algo.head()
        number = LabelEncoder()
        psycho_algo['like_mother'] = number.fit_transform(psycho_algo['like_mother'])
        #print(psycho_algo['like_mother'])
       # print("this is  ")
        #print(number.transform(['y']))
  
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
            speech="your father is "+data_loaded['father_occupation']+"and maa is "+data_loaded['mother_occupation']
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
        dump_value('mother_occupation',mother_occupation)
        #if(session['father_occupation']==""):
        with open('data.json', 'r') as data_file:
            data_loaded =json.loads(data_file.read())
#            print(data_loaded['father_occupation'])
        if('father_occupation' not in data_loaded):
            speech="your mother is "+data_loaded['mother_occupation']+" what does your father do?"
            return {
            "speech": speech,
            "displayText": speech,
            "source": "apiai-psychochatbot"
     }
        #speech="Okay, let's talk about your family"
        else:    
            speech="your mother is "+data_loaded['mother_occupation']+" and your father is "+data_loaded['father_occupation']
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
        dump_value('ask_be_like_father','y')
        dump_value('ask_be_like_mother','n')
        #data_loaded['ask_be_like']="father"
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_result"
        }
    }
       
       
    if req.get("result").get("action") == "action_ask_be_like_mother":
        result = req.get("result")
        dump_value('ask_be_like_father','n')
        dump_value('ask_be_like_mother','y')
        #data_loaded['ask_be_like']="mother"
        return {
        "source": "apiai-psychochatbot",
        "followupEvent": {
           "name": "event_result"
        }
    }
    
    
    if req.get("result").get("action") == "action_hobbies_interests_art":
        result = req.get("result")
        data_loaded['hobby']="arts"
        parameters = result.get("parameters")
        duration=parameters.get("duration")
        certifications=parameters.get("certifications")
        as_career=parameters.get("as_career")
        parents_support=parameters.get("parents_support")
        dump_value('hobby','arts')
        dump_value('duration','n')
        dump_value('certifications',certifications)
        dump_value('as_career',as_career)
        dump_value('parents_support',parents_support)
        
     #   data_loaded['duration']=duration
      #  data_loaded['certis']= certifications
       # data_loaded['as_career']=as_career
        #data_loaded['parents_support']=parents_support
   
        return {
       # "speech": "arts",
        #"displayText": "arts",
        "source": "apiai-psychochatbot"
       # "followupEvent": {
        #   "name": "event_hobbies_interests"
        #}
    }
    
    if req.get("result").get("action") == "action_hobbies_interests_sports":
        result = req.get("result")
        parameters = result.get("parameters")
        duration=parameters.get("duration")   
        print(duration)
        achievements=parameters.get("achievements")
        as_career=parameters.get("as_career")
        parents_support=parameters.get("parents_support")
        dump_value('hobby','sports')
        dump_value('duration','n')
        dump_value('certifications',achievements)
        dump_value('as_career',as_career)
        dump_value('parents_support',parents_support)
        return {
        "speech": "Do you have any other hobbies or interests?",
        "displayText": "Do you have any other hobbies or interests?",
        "source": "apiai-psychochatbot"
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
        "source": "apiai-psychochatbot"
       # "followupEvent": {
        #   "name": "event_hobbies_interests"
        #}
    }
    
    
    if req.get("result").get("action") == "action_hobbies_interests_arts_no":
        return{
          "followupEvent": {
          "name": "event_ask_about_family"
        }
        }
    
    if req.get("result").get("action") == "action_hobbies_interests_sports_no":
        return{
          "followupEvent": {
          "name": "event_ask_about_family"
        }
        }
    
    if req.get("result").get("action") == "action_hobbies_interests_misc_no":
        return{
          "followupEvent": {
          "name": "event_ask_about_family"
        }
        }  
    
    if req.get("result").get("action") == "action_hobbies_interests_extras_no":
        return{
          "followupEvent": {
          "name": "event_ask_about_family"
        }
        } 
    
    if req.get("result").get("action") == "action_result":
        psycho_algo = pd.read_csv("psycho_data.csv")
        psycho_algo.head()
        number1 = LabelEncoder()
        psycho_algo['like_mother'] = number1.fit_transform(psycho_algo['like_mother'])
        number2 = LabelEncoder()
        psycho_algo['like_father'] = number2.fit_transform(psycho_algo['like_father'])
        number3 = LabelEncoder()
        psycho_algo['hobby_as_career'] = number3.fit_transform(psycho_algo['hobby_as_career'])
        number4 = LabelEncoder()
        psycho_algo['achieve_hobby'] = number4.fit_transform(psycho_algo['achieve_hobby'])
        number5 = LabelEncoder()
        psycho_algo['duration_passion'] = number5.fit_transform(psycho_algo['duration_passion'])
        number6 = LabelEncoder()
        psycho_algo['parent_support'] = number6.fit_transform(psycho_algo['parent_support'])
        number7 = LabelEncoder()
        psycho_algo['result'] = number7.fit_transform(psycho_algo['result'])
        with open('data.json', 'r') as data_file:
            data_loaded =json.loads(data_file.read())
        like_mother=str(data_loaded['ask_be_like_father'])
        like_father=str(data_loaded['ask_be_like_mother'])
        hobby_as_career=str(data_loaded['as_career'])
        achieve_hobby=str(data_loaded['certifications'])
        duration_passion='h'
        parent_support=str(data_loaded['parents_support'])
        
        like_mother=list(like_mother)
        like_father=list(like_father)
        hobby_as_career=list(hobby_as_career)
        achieve_hobby=list(achieve_hobby)
        duration_passion=list(duration_passion)
        parent_support=list(parent_support)
        
        lm=number1.transform(like_mother)
        lf=number2.transform(like_father)
        hc=number3.transform(hobby_as_career)
        ah=number4.transform(achieve_hobby)
        dp=number5.transform(duration_passion)
        ps=number6.transform(parent_support)
        
        print(ps)
        res=number7.inverse_transform(model.predict([[lm[0],lf[0],hc[0],ah[0],dp[0],ps[0]]]))
        r=res[0]
        print(r)
        speech=r
        return{
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot"
        }

        print(speech)
        return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "apiai-psychochatbot"
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
        "source": "apiai-psychochatbot"
        #"followupEvent": {
         #   "name": "I1"
     #   }
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
  #  app.secret_key="Sgsits2018"
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')
