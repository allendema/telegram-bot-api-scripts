# Text will be passed to a engine like Wikipedia and there will be an instant answer.

import requests
from time import sleep

global OFFSET
OFFSET = 0

# Your Bot Token from Botfather comes below
botToken = ""

requestURL = "https://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "https://api.telegram.org/bot" + botToken + "/sendMessage"

# Best option is to use your own Instance
# You could use a Public Searx instance too
searx_instance = ""

# Which engines with Infoboxes should be used
# !wikipedia or !wp
# !wikidata or !wd
# Duckduckgo Definitions - !ddd
# Two engines could be used at the same time too

searx_parameter = "?q=!wp+"


def update (url):
    global OFFSET

    try:
        update_raw = requests.get(url + "?offset=" + str(OFFSET))
        update = update_raw.json()
        result = extract_result(update)

        if result != False:
            OFFSET = result['update_id'] + 1
            return result
        else:
            return False

    except requests.exceptions.ConnectionError:
        pass

def extract_result (dict):
    result_array = dict['result']

    if result_array == []:
        return False
    else:
        result_dic = result_array[0]
        return result_dic


def send_message (chatId, message, print_response = False):

    data = {
        'chat_id': chatId,
        'text': message
        }

    #response = requests.post(sendURL + "?chat_id=" + str(chatId) + "&text=" + message)     #Direkt in URL platzieren
    #response = requests.post(sendURL, params = data)                                       #Ueber post() in URL platzieren
    response = requests.post(sendURL, data = data)                                          #application/x-www-form-urlencoded (ins body der POST)
    #response = requests.post(sendURL, json = data)                                         #application/json (ins body der POST, in Form einer JSON)

    if print_response == True:
        print("----------")
        print(response.request.url)
        print(response.request.headers)
        print(response.request.body)
        print("----------")

while True:
    newmessage = update(requestURL)

    try:

        if newmessage != False:
            userchatid = newmessage['message']['chat']['id']
            usertext = newmessage['message']['text']
            username = newmessage['message']['chat']['first_name']

            if usertext.lower() == "hello":
                send_message(userchatid, "Hi " + username)
            else:
                mix = searx_instance + searx_parameter + usertext + "&format=json"
                jsondata = requests.get(mix).json()

                for i in jsondata["infoboxes"]:
                      wiki_infobox = i["content"]
                      send_message(userchatid, wiki_infobox)

    except Exception as e:
        print ("There was an error, the script will continue:", e)


    sleep(1)
