# Import Library
import json

# Memuat file json dari Followers
with open('./data/followers_1.json') as d:
    data = json.load(d)

# Ekstraksi username dari data followers
followers = []
for items in data:
    for i in items["string_list_data"]:
        followers.append(i["value"])
        
# Memuat file json dari following
with open('./data/following.json') as d:
    data = json.load(d)
   
# Ekstraksi username dari data following    
followings = []
for items in data["relationships_following"]:
    for i in items["string_list_data"]:
        followings.append(i["value"])
        
# Mengidentifikasi akun mutual
mutuals = []
for user in followings:
    if user in followers:
        mutuals.append(user)
        
# Menampilkan akun yang tidak mutual
for user in followings:
    if user not in mutuals:
        print(f'https://www.instagram.com/{user}')