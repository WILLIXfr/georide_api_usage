# William Alloul
# william.alloul@gmail.com

import requests
import json
import sys
import argparse

g_tracker_id=None
g_tracker_name=None

def login():
  email=''
  password=''
  log_info={'email': email, 'password': password}
  log_request = requests.post("https://api.georide.fr/user/login", data=log_info).json()
  authToken="Bearer " + log_request["authToken"]
  return authToken

def get_trackers(token):
  auth_head = { 'Authorization': token}
  result = requests.get("https://api.georide.fr/user/trackers", headers=auth_head).json()

  return result

def get_first_tracker_info(token):
  auth_head = { 'Authorization': token}
  result = requests.get("https://api.georide.fr/user/trackers", headers=auth_head).json()

  return result[0]["trackerId"],result[0]["trackerName"]

def check_tracker_exist(token, trackerId, trackerName):
  auth_head = { 'Authorization': token}
  result = requests.get("https://api.georide.fr/user/trackers", headers=auth_head).json()
  for tracker in result:
    if (str(tracker['trackerId']) == trackerId or str(tracker['trackerName']) == trackerName):
      global g_tracker_id
      g_tracker_id=tracker['trackerId']
      global g_tracker_name
      g_tracker_name=tracker['trackerName']
      return True
  return False

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

def display_trackers(trackers_list):
  for tracker in trackers_list:
    print ('Tracker Name:\t' + str(tracker['trackerName']) + '\nTracker Id:\t' + str(tracker['trackerId']) + '\n')

def main():
  parser = argparse.ArgumentParser(description='Action required')
  parser.add_argument('--action', dest='action', choices=['lock', 'unlock', 'list'], help='action desired')
  parser.add_argument('--id', dest='tracker_id', nargs='?', help='tracker_id')
  parser.add_argument('--name', dest='tracker_name', nargs='*', help='tracker_name')
  args = parser.parse_args()


  if (args.action == 'unlock' and (args.tracker_id == None and args.tracker_name == None)):
    print ('Unlocking 1st tracker')
    token=login()
    trackerId,trackerName=get_first_tracker_info(token)
    unlock(token,trackerId)
    print (trackerName + ' is unlocked')
  elif (args.action == 'unlock' and (args.tracker_id != None or args.tracker_name != None)):
    print ('Unlocking selected tracker')
    token=login()
    if (check_tracker_exist(token,args.tracker_id,args.tracker_name)):
      unlock(token,g_tracker_id)
      print (g_tracker_name + ' is unlocked')
  elif (args.action == 'lock' and (args.tracker_id == None and args.tracker_name == None)):
    print ('Locking 1st tracker')
    token=login()
    trackerId,trackerName=get_first_tracker_info(token)
    lock(token,trackerId)
    print (trackerName + ' is locked')
  elif (args.action == 'lock' and (args.tracker_id != None or args.tracker_name != None)):
    print ('Locking selected tracker')
    token=login()
    if (check_tracker_exist(token,args.tracker_id,args.tracker_name)):
      lock(token,g_tracker_id)
      print (g_tracker_name + ' is locked')
  elif (args.action == 'list'):
    token=login()
    trackers_list=get_trackers(token)
    display_trackers(trackers_list)
  else:
    print ("Wrong Argument")

if __name__== "__main__":
  main()

