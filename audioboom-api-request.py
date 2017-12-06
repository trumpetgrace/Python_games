import requests

import json
import sys


username = 'radio-x'
per_page = 100
page = 1
count = 0

def get_booms(p):
    global count
    r = requests.get("http://api.audioboom.com/users/185399/audio_clips.json")
    response = r.text
    parsed_json = r.json()
    body = parsed_json['body']
    totals = body['totals']
    if p == 1:
        print ('user: '+ username + ' -total: ' + str(totals['count']))
        print ('')
    for clip in body['audio_clips']:
        print ('-----------------------------------------------')
        mp3_url = clip['urls']['high_mp3']
        print ('TITLE   : ' + clip['title'])
        print ('mp3 url : ' + mp3_url)
        naming = mp3_url.split('/')
        mp3_name = naming[-1]
        name = mp3_name.split('mp3')
        json_name = name[0] + '.json'
        print ('mp3 name: ' + mp3_name)
        count = count + 1
    if count < totals['count']:
        get_booms(p + 1)


print('===== ArchiveBoom =============================')
get_booms(page)
print('ALL DONE!')
print('')
