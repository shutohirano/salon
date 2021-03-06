import tweepy
import datetime

def twitter_api():
 CK = ""
 CS = ""
 AT = ""
 AS = ""   

 auth = tweepy.OAuthHandler(CK, CS)
 auth.set_access_token(AT, AS)
 api = tweepy.API(auth)
 return api


api = twitter_api()
api.trends_available()

woeid_dic = {'世界': 1, '日本': 23424856,
             '東京': 1118370, '京都': 15015372, '大阪': 15015370,
             '札幌': 1118108, '仙台': 1118129, '名古屋': 1117817, 
             '神戸': 1117545, '広島': 1117227, '福岡': 1117099,
             '埼玉': 1116753, '千葉': 1117034, '横浜': 1118550,
             '川崎': 1117502, '相模原': 1118072, '北九州': 1110809,
             '岡山': 90036018, '新潟': 1117881, '高松': 1118285,
             '浜松': 1117155, '熊本': 1117605, '沖縄': 2345896}

city   = '日本'
woeid  = woeid_dic[city]
trends = api.trends_place(woeid)
city2  = '東京' 
woeid2  = woeid_dic[city2]
trends2 = api.trends_place(woeid2)
city3  = '埼玉' 
woeid3  = woeid_dic[city3]
trends3 = api.trends_place(woeid3)

d = datetime.datetime.now()
outfile = open('trend.csv', 'a',encoding='utf-8', errors='ignore')

#トレンドの順位と内容だけプリント
for trend in trends:
    trend_l = 0
    for trend_id in trend['trends']:
        trend_n  = trend_id['name']
        created_at  = trend['created_at']
        as_of  = trend['as_of']
        trend_l += 1
        outfile.write(str(city)+","+str(trend_l)+","+str(trend_n)+","+str(created_at)+","+str(as_of)+"\n")
        
        
for trend in trends2:
    trend_l = 0
    for trend_id in trend['trends']:
        trend_n  = trend_id['name']
        created_at  = trend['created_at']
        as_of  = trend['as_of']
        trend_l += 1
        outfile.write(str(city2)+","+str(trend_l)+","+str(trend_n)+","+str(created_at)+","+str(as_of)+"\n")

        

for trend in trends3:
    trend_l = 0
    for trend_id in trend['trends']:
        trend_n  = trend_id['name']
        created_at  = trend['created_at']
        as_of  = trend['as_of']
        trend_l += 1
        outfile.write(str(city3)+","+str(trend_l)+","+str(trend_n)+","+str(created_at)+","+str(as_of)+"\n")
        

print("end")        
