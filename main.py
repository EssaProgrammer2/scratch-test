from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')

def home():
  return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=7070)

def keep_alive():
  t = Thread(target=run)
  t.start()

keep_alive()

import scratchattach as scratch3

session = scratch3.Session(".eJxVkMFugzAQRP-Fc0uNsQHn1iJFag9pk0hVerIWew0uYCNwFKlV_71G4pLrzOzb2f1NrgvODkZMdknt_ausvcaZ5kXykATfo4u6Krkq0RCmM8qohgYNcgWKqRzQGLL7nIpLexownJvju-7OlwN87KF-8_tjxAy-te7RTpGUVSSlPE8LkVJSRU_CNXRy7SCtjgFREcqygkZLf4NrvQx2xB_v1n7PI85WwdMBb_LLz_39fAdLF0NlyZipCGYiQ2gKIgAF4aIEjpDzSpcccmqYWO_DJSjve7vCbxGI-h7ZgIofWHutGroQtwfrXboZS3rCadjEly389w9FRW5b:1rqTx8:jHNntVLrnYI8DyjQ_J46iBvvV2w", username="CooI_Coder236") #The username field is case sensitive

conn = session.connect_cloud("991864476") #replace with your project id
#conn = scratch3.CloudConnection(project_id = "991864476", username="CooI_Coder236", session_id=".eJxVkMFugzAQRP-Fc0uNsQHn1iJFag9pk0hVerIWew0uYCNwFKlV_71G4pLrzOzb2f1NrgvODkZMdknt_ausvcaZ5kXykATfo4u6Krkq0RCmM8qohgYNcgWKqRzQGLL7nIpLexownJvju-7OlwN87KF-8_tjxAy-te7RTpGUVSSlPE8LkVJSRU_CNXRy7SCtjgFREcqygkZLf4NrvQx2xB_v1n7PI85WwdMBb_LLz_39fAdLF0NlyZipCGYiQ2gKIgAF4aIEjpDzSpcccmqYWO_DJSjve7vCbxGI-h7ZgIofWHutGroQtwfrXboZS3rCadjEly389w9FRW5b:1rqTx8:jHNntVLrnYI8DyjQ_J46iBvvV2w")

client = scratch3.CloudRequests(conn, ignore_exceptions=True)

@client.request
def ping(): #called when client receives request
    print("Ping request received")
    return "pong" #sends back 'pong' to the Scratch project

@client.request
def following(argument1):
    user = scratch3.get_user(argument1)
    if user.is_followed_by("Cool_Coder236"):
        return "gakbisa"
    else:
        user.follow()
        return user.is_following("Cool_Coder236")

@client.event
def on_ready():
    print("Request handler is running")

client.run() #make sure this is ALWAYS at the bottom of your Python file