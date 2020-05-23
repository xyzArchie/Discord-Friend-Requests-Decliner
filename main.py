import requests, sys, re, os

os.system('title [Discord Auto Friend Requests Decliner]')
token = '' # Your Discord token.
ids = []
success = 0
headers = {
    'authorization': token,
}

friends = requests.get('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)
if '401: Unauthorized' not in friends.text:
    types = re.findall(r'"id": "\w{18}", "type": \w{1}', friends.text)
else:
    sys.stdout.write('> Invalid token.\n')
    os.system('pause')
    os._exit(0)

for type_ in types:
    if ': 3' in type_:
        ids.append(type_)

if len(ids) != 0:
    for id_ in ids:
        id_raw = id_.split('"id": "')[1].split('", "')[0]
        decline = requests.delete('https://discord.com/api/v6/users/@me/relationships/%s' % (id_raw), headers=headers)
        if decline.status_code == 204:
            sys.stdout.write('Successfully declined user | %s\n' % (id_raw))
            success += 1
        else:
            sys.stdout.write('Error.\n')
    
    if success != 1:
        sys.stdout.write('\n> Declined %s friend requests.\n' % (success))
    else:
        sys.stdout.write('\n> Declined %s friend request.\n' % (success))
else:
    sys.stdout.write('> You have no friend requests incoming.\n')

os.system('pause')
