# William Alloul
# william.alloul@gmail.com

import requests
import json
import sys

def login():
  email=''
  password=''
  log_info={'email': email, 'password': password}
  log_request = requests.post("https://api.georide.fr/user/login", data=log_info).json()
  authToken="Bearer " + log_request["authToken"]
  return authToken

def tracker_info(token):
  auth_head = { 'Authorization': token}
  result = requests.get("https://api.georide.fr/user/trackers", headers=auth_head).json()

  return result[0]["trackerId"],result[0]["trackerName"]

def unlock(token, trackerId):
  auth_head = { 'Authorization': token}
  data = {'trackerId': trackerId}
  url = "https://api.georide.fr/tracker/" + str(trackerId) + "/unlock"
  requests.post(url, headers=auth_head, data=data)

def lock(token, trackerId):
  auth_head = { 'Authorization': token}
  data = {'trackerId': trackerId}
  url = "https://api.georide.fr/tracker/" + str(trackerId) + "/lock"
  requests.post(url, headers=auth_head, data=data)

if (sys.argv[1] and sys.argv[1] == 'unlock'):
  token=login()
  trackerId,trackerName=tracker_info(token)
  unlock(token,trackerId)
  print (trackerName + ' is unlocked')
elif (sys.argv[1] and sys.argv[1] == 'lock'):
  token=login()
  trackerId,trackerName=tracker_info(token)
  lock(token,trackerId)
  print (trackerName + ' is unlocked')
else:
  print ("Wrong Argument")


