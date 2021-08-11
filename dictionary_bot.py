# Dictionary bot which returns links from urbandictionary.com,
# those links are previewed by the TG client i.e there will be instant answers.


import requests
from time import sleep

global OFFSET
OFFSET = 0

# Your Bot Token from Botfather comes below
botToken = ""

requestURL = "https://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "https://api.telegram.org/bot" + botToken + "/sendMessage"

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
    #response = requests.post(sendURL, params = data)                                       #Über post() in URL platzieren
    response = requests.post(sendURL, data = data)                                          #application/x-www-form-urlencoded (ins body der POST)
    #response = requests.post(sendURL, json = data)                                         #application/json (ins body der POST, in Form einer JSON)

    if print_response == True:
        print("----------")
        print(response.request.url)
        print(response.request.headers)
        print(response.request.body)
        print("----------")

while True:
    newmessage = update (requestURL)

    try:

        if newmessage != False:
            userchatid = newmessage['message']['chat']['id']
            usertext = newmessage['message']['text']
            username = newmessage['message']['chat']['first_name']

            if usertext.lower() == "hello":
                send_message(userchatid, "Hi " + username)
            else:
                send_message(userchatid, "https://www.urbandictionary.com/define.php?term=" + usertext)
    
    except Exception as e:
        print ("There was an error, the script will continue:", e)


    sleep (1)
