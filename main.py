from hashtag import downloadHashtag, getHashtag
import sys
headers_dict = {
    "Accept" : 'application/json, text/plain, */*',
    "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": 'en-US,en;q=0.9,fr;q=0.8,ar;q=0.7,ko;q=0.6',
    "Connection" : 'keep-alive',
    "Host" : '178.18.242.66',
    "Referer" : 'http://178.18.242.66/',
    "TOKEN" : '287bcb01-0792-4bcf-a3ff-88ad78a165a7',
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}
       
downloadHashtag(sys.argv[1], int(sys.argv[2]), headers_dict=headers_dict)
