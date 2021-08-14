from TikTokApi import TikTokApi
import requests
import validators
from time import sleep
from random import randint
import os
import re
import mysql.connector
from get_hashtag import get_vids, insert_vid, getHashtag


def downloadHashtag(tag, n_videos, headers_dict):
    if not os.path.exists('./tags/{}'.format(tag)):
        os.makedirs('./tags/{}'.format(tag))
        os.makedirs('./tags/{}/thumbnails'.format(tag))
    videos = get_vids(tag, n_videos)
    print("\n\nthere is {} ids\n\n".format(len(videos)))
    for id in videos:
        username        = id['user']
        vid_id          = id['id']
        thumbnail       = id['thumbnail']
        title           = id['title']
        my_new_string   = re.sub('[^a-zA-Z0-9 \n\.]', '', title)
        title           = "{} - {} - {}".format(username, my_new_string, vid_id)
        
        if os.path.isfile('./tags/{}/{}.mp4'.format(tag, title)):
            print('First Firewall -------- File already Exists\n\n')
            # sleep(5)
            continue
        video_api_url  = "http://178.18.242.66/api/v1/fetch?url=https://www.tiktok.com/@{}/video/{}".format(id['user'], id['id'])
        response = requests.get(video_api_url, headers=headers_dict)
        rJson = response.json()
        if not isinstance(rJson,dict):
            print("problem with link response")
            # sleep(5)
            continue
        if not 'url_nwm' in rJson.keys():
            print('watermarked video doesn\'t exist for this video')
            # sleep(5)
            continue
        if not rJson['url_nwm']:
            print('url is empty watermarked video doesn\'t exist for this video')
            # sleep(5)
            continue
        if validators.url(rJson['url_nwm']):
            video = requests.get(rJson['url_nwm'], allow_redirects=True)
            if validators.url(thumbnail):
                thumbnail = requests.get(thumbnail, allow_redirects=True)
            
            try:
                print('downloading ./tags/{}/{}.mp4'.format(tag,title))
                if os.path.isfile('./tags/{}/{}.mp4'.format(tag,title)):
                    print('\n\nFile already Exists\n\n')
                else:
                    open('./tags/{}/{}.mp4'.format(tag,title), 'wb').write(video.content)
                    open('./tags/{}/thumbnails/{}.jpg'.format(tag,title), 'wb').write(thumbnail.content)
                    insert_vid(vid_id, tag)
            except:
                print("issue with file name")
            # sleep(randint(5, 30))
        
