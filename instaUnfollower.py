__author__ = 'Abhishek Srivastava'

import json
import os
import time
import requests


def isSet(next_url):
    if next_url == '':
        return False
    else:
        return True


def setAccessToken():
    global access_token
    if os.path.exists('config.txt'):
        access_token = ''
        config_file = open('config.txt', 'r')
        for line in config_file.readlines():
            if 'access_token' in line:
                access_token = line.split('=')[1]
                print('Token found...')
            else:
                print("Error in config file. No access_token found.")
                raw_input("Enter any key to exit...")
                exit("Exiting, issue with getting token.")
        config_file.close()
    else:
        print("No access token found. Please create a config file with access token...\nP.S: Details are in Readme file")
        raw_input("Enter any key to exit...")
        exit()


def core():
    '''
    Setting up data
    '''
    global unfollow_count
    unfollow_count = 0
    url = 'https://api.instagram.com/v1/users/self/follows?access_token='+str(access_token)+'&count=20'
    response = requests.get(url)
    json_data = json.loads(response.text)
    json_length = len(json_data['data'])
    '''
    Looping through the fetched users to get current relationship
    '''
    for itr in range(0, json_length, 1):
            user_id = (json_data['data'][itr]['id'])
            #print user_id
            user_name = (json_data['data'][itr]['username'])
            print(user_name)
            '''
            Check if the user is following you or not. Un-follow only when they are not following you
            '''
            chkfollow_url = 'https://api.instagram.com/v1/users/%s/relationship?access_token=%s' % (user_id, access_token)
            chkfollow_response = requests.get(chkfollow_url)
            chkfollow_json_data = json.loads(chkfollow_response.text)
            if chkfollow_json_data['data']['incoming_status'] == "none":
                unfollow_url = 'https://api.instagram.com/v1/users/%s/relationship?access_token=%s' % (user_id, access_token)
                r = requests.post(unfollow_url, data = {"action":"unfollow"})
                if r.status_code == 200:
                    print 'Unfollowed %s' % user_name
                    unfollow_count += 1
                else:
                    print '\n!!!Error in un-following!!!'
                    print json.loads(r.text)['meta']['error_message']
                    print '\nSleeping for one hour. Keep the window open, will retry...'
                    time.sleep(3601)
            else:
                print 'User %s follows you, not un-following' % (user_name)
            time.sleep(2)

    if 'next_url' in json_data['pagination']:
            next_url = (json_data['pagination']['next_url'])
    else:
            next_url = ''

    '''
    Loop through the pagination, if available
    '''
    while isSet(next_url):
        print 'Fetching next url data'
        response = requests.get(next_url)
        json_data = json.loads(response.text)
        json_length = len(json_data['data'])
        if 'next_url' in json_data['pagination']:
            next_url = (json_data['pagination']['next_url'])
        else:
            next_url = ''

        for itr in range(0, json_length, 1):
            user_id = (json_data['data'][itr]['id'])
            user_name = (json_data['data'][itr]['username'])
            print(user_name)
            '''
            Check if the user is following you or not. Un-follow only when they are not following you
            '''
            chkfollow_url = 'https://api.instagram.com/v1/users/%s/relationship?access_token=%s' % (user_id, access_token)
            chkfollow_response = requests.get(chkfollow_url)
            chkfollow_json_data = json.loads(chkfollow_response.text)
            if chkfollow_json_data['data']['incoming_status'] == "none":
                unfollow_url = 'https://api.instagram.com/v1/users/%s/relationship?access_token=%s' % (user_id, access_token)
                r = requests.post(unfollow_url, data = {"action":"unfollow"})
                ##below to be printed only when 200 response code is received
                if r.status_code == 200:
                    print 'Unfollowed %s' % user_name
                    unfollow_count += 1
                else:
                    print '\n!!!Error in un-following!!!'
                    print json.loads(r.text)['meta']['error_message']
                    print '\nSleeping for one hour. Keep the window open, will retry...'
                    time.sleep(3601)
            else:
                print 'User %s follows you, not un-following' % (user_name)
            time.sleep(2)



if __name__ == '__main__':
    print('\t\t####################################')
    print('\t\t####################################')
    print('\t\t####### Insta User Unfollower ######')
    print('\t\t####################################')
    print('\t\t# Developed by Abhishek Srivastava #')
    print('\t\t####################################')
    print('\t\t####################################\n\n')

    setAccessToken()
    print('Started Un-following')
    core()
    print("Unfollowed %s users" % unfollow_count)
    raw_input("Ended the unfollow process...enter any key to exit")