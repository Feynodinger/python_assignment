import json, requests 

post_url =  'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
top = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
r = requests.get(top)
string = r[1:-2].split(',')
for i in range(len(string)):
    string[i] = string[i].strip(' ')
    resp = requests.get(post_url.format(string[i]))
    url = resp.json()['url']
    title = resp.json()['title']
    txt = 'New Story !! ' + '\nTitle = ' + title + ' \nurl = ' + url
    send_json = json.dumps({"text": text}
    send = requests.post(url='https://api.flock.com/hooks/sendMessage/c34dc160-62f4-4d89-94ab-82400a105bb7', data = send_json)
