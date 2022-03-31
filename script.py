import requests
from sys import argv

def main():
    pokeName = argv[1]
    pokeDic = retrievePokeDic(pokeName)
    pokeTB = pasteBinFormat(pokeDic)
    pasteURL = mkpasteBin(pokeTB[0], pokeTB[1])
    print(pasteURL)
    
def retrievePokeDic(pokeName):
        
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokeName)

    print("Connecting to PokeAPI . . .", end = "")
    
    if response.status_code == 200:
        print(' Success!')
        pokeInfo = response.json()
    else:
        print(' Error', sep = "")

    return pokeInfo

def pasteBinFormat(pokeDic):
    
    title = (pokeDic['name'] + "'s Abilities")
    body = ""

    for n in pokeDic['abilities']:
        body += '- ' + n['ability']['name'] + '\n'

    return (title, body)

def mkpasteBin(title, body):
    
    print('Posting to PasteBin . . . ', end="")

    parameters = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }
    
    response = requests.post('https://pastebin.com/api/api_post.php', data=parameters)

    if response.status_code == 200:
        print(' Success!')
        return response.text
    else:
        print(' Error', sep = "")
        return response.status_code

main()