#!/usr/bin/env python3
#
# usage: python test.py < follow_salonS_H.csv
# 卒論　サロン垢のfollow取得　対象はCSV 読み込み
#
import tweepy
import sys
import time
import csv
import datetime



auth = tweepy.OAuthHandler(CK1,CS1)
auth.set_access_token(AT1, AS1)
api = tweepy.API(auth)

d = datetime.datetime.now()

# open a file to save follower data

outfile = open('follow_data' + d.strftime('%Y%m%d') + '.csv', 'w')

# get the list of salon members from input file
salon_members_list = []
for line in sys.stdin:
  salon_member_name = line.replace("\r\n", "")
  #print(salon_member_name)
  salon_members_list.append( salon_member_name )
#print(salon_members_list)
#sys.exit(0)

for screen_name in salon_members_list:
  # wait for 5 seconds
  time.sleep(5)

  print("### start getting ", screen_name, "data... ###")

  # プロフィール情報を手に入れたい Twitter User ID
  friends_ids = []
  ids=[]

  # ユーザー情報の取得
  try:
    user = api.followers_ids(screen_name=screen_name)
  except:
    print("api.followers_ids cannot get data of ", screen_name, ". continue...")
    time.sleep(100)
    continue
 

  try:
    friend_ids_list = tweepy.Cursor(api.friends_ids, screen_name=screen_name).items()
    for friend_id in friend_ids_list:
      friends_ids.append(friend_id)
  except:
    print("tweepy.Cursor cannot get data of ", screen_name, ". continue...")
    continue

  # 100IDsずつに詳細取得
  for i in range(0, len(friends_ids), 100):
    for user in api.lookup_users(user_ids=friends_ids[i:i+100]):
      print(str(screen_name.replace('\n',''))+","+str(user.screen_name))
      outfile.write(str(screen_name.replace('\n',''))+","+str(user.screen_name)+"\n")
      ids.append(user.screen_name)

  #print("### getting ", screen_name, "data ended ###")

# close the file
outfile.close()
