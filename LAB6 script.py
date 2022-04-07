import requests
from sys import argv

def main():
    pokeName = argv[1]
    pokeDic = retrievePokeDic(pokeName)
    pokeTB = pasteBinFormat(pokeDic)
    pasteURL = mkpasteBin(pokeTB[0], pokeTB[1])
    print(pasteURL)
    
def retrievePokeDic(pokeName):

    # connects to the PokeAPI page for the pokemon specified as a command line parameter for main()
    # and makes a GET request    
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokeName)

    print("Connecting to PokeAPI . . .", end = "")
    
    # if connection is successful assign the pokemon info to a dictionary
    if response.status_code == 200:
        print(' Success!')
        pokeInfo = response.json()
    else:
        print(' Error', sep = "")

    return pokeInfo

def pasteBinFormat(pokeDic):
    
    # format the pastebin title with the pokemons name from the pokeDic dictionary
    title = (pokeDic['name'] + "'s Abilities")
    body = ""
    # format the pastebin body with the pokemons abilities from the pokeDic dictionary
    for n in pokeDic['abilities']:
        body += '- ' + n['ability']['name'] + '\n'

    return (title, body)

def mkpasteBin(title, body):
    
    print('Posting to PasteBin . . . ', end="")

    # parameters for the connection to the pastebin API and the formatting of the paste
    parameters = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }
    
    # connects to the pastebinAPI and makes a POST request
    response = requests.post('https://pastebin.com/api/api_post.php', data=parameters)

    # if connection is successful return response.text which is a link to the paste
    if response.status_code == 200:
        print(' Success!')
        return response.text
    else:
        print(' Error', sep = "")
        return response.status_code

main()