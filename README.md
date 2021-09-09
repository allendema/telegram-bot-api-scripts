# telegram-bot-api-scripts

Following dependency is needed:
 - requests

<details>
<summary>Saving this locally</summary>

```bash
$ cd ~/Downloads/
$ mkdir github && cd github
$ git clone https://github.com/allendema/telegram-bot-api-scripts.git
$ pip3 install -r requirements.txt
```

Go to the directory where the scripts are installed:

```bash
$ cd ~/Downloads/github
```
</details>
 
# Let the script you want run in the background:

```bash
python3 [BOT] &
```
Example:

```bash
python3 dictionary_bot.py & 
```
```bash
python3 wikipedia_bot.py & 
```
<details>
<summary>Dictionary Bot in Action</summary>
 
 ![Dictionary Bot in Action](https://github.com/allendema/telegram-bot-api-scripts/blob/main/dictionary_bot_example.png)

</details> 

<details>
<summary>Wikipedia Bot in Action</summary>
 
 ![Wikipedia Bot in Action](https://github.com/allendema/telegram-bot-api-scripts/blob/allendema-wikipedia_bot/wikipedia_bot_example.png)

<details>


# Stoping the script
Find the PID of the BOT then terminate it, like so:

```$ ps ax | grep bot ```

```$ sudo kill [PID from the command above] ```
