import sys
import _mysql
import apiclient.discovery
import httplib2
import pprint
import os.path
import time
import urllib
import json

#set up the basic stuff
db = _mysql.connect(host='127.0.0.1', user='djangoman', passwd='django', db='djangoman')
api_key = 'AIzaSyAAPuaXCEEUGGZe27ezqxP3sM4YvbRd5n0'
http = httplib2.Http()
service = apiclient.discovery.build('plus', 'v1', http=http, developerKey=api_key)

#retrive all the targets
db.query("SELECT id, google_id FROM trakc_target")
result_targets = db.store_result()

#loop condition
running = True

while running:
    row = result_targets.fetch_row(how = 1)
    if len(row) < 1:
        running = False
        continue
    row = row[0]
    
    #search for posts by specific user    
    result = service.activities().list(userId=row['google_id'], collection='public', maxResults=100).execute()

    if 'items' in result:
        my_count = 0
        for activity in result['items']:
            #verify if the posts is already in our db
            g_id = activity['id']
            db.query("SELECT * FROM trakc_post WHERE google_id='" + str(g_id) + "'")
            check_existance = db.store_result()
            if (check_existance.num_rows() > 0):
                continue
            my_count += 1
            published = activity['published']
            author_id = row['id']
            likes = activity['object']['plusoners']['totalItems']
            shares = activity['object']['resharers']['totalItems']
            comments = activity['object']['replies']['totalItems']
            content = '['
            if 'attachments' in activity['object']:
                for att_ment in activity['object']['attachments']:  
                    content += _mysql.escape_string(json.dumps(att_ment)) + ', '
            content += ']'
            db.query("INSERT INTO trakc_post(author_id, post_date, google_id, likes, shares, comments, content) VALUES('" + str(author_id) + "', '" + published + "', '" + str(g_id) + "', " + str(likes) + ", " + str(shares) + ", " + str(comments) + ", '" + str(content) + "')")
        print row['id'], 'had', my_count, 'posts.'
db.close()


