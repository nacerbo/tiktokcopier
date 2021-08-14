from TikTokApi import TikTokApi
import mysql.connector


mydb = mysql.connector.connect(
  host="5.189.176.126",
  user="admin",
  password="CMFB8LXQG7ADF2b",
  database="Amir_tiktok_downloads"
)

def getHashtag(tag):
    verifyFp = "verify_ksbysoz5_IHaavI7S_0WJz_4v7F_Ay8p_eDhJv8K7bEku"
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    count = 1000
    videos = []
    hashtag = tag
    hashtag_videos = api.by_hashtag(hashtag, count=count)

    for vid in hashtag_videos:
        videos.append({'id': vid['id'], 'title': vid['desc'], 'user': vid['author']['uniqueId'], 'thumbnail': vid['video']['cover']})
        
    return videos


def get_vids(tag, num):
    videos = getHashtag(tag)
    needed_vids = []
    for vid in videos:
        if len(needed_vids)>= num:
            break
        
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT id FROM tiktoks WHERE tiktok_id = {}".format(vid['id']))
        row_count = mycursor.rowcount
        if row_count == 0:
            needed_vids.append(vid)
        else:
            continue
        
    return needed_vids

def insert_vid(id, tag):
    mycursor        = mydb.cursor()
    sql = "INSERT INTO tiktoks (tiktok_id, tag) VALUES (%s, %s)"
    val = (id, tag)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount

