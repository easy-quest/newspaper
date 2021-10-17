#!/data/data/com.termux/files/usr/bin/bash

# git add -A
# git commit -m 'push first commit'
# git push 
# git status

curl -X POST \
https://api.telegram.org/bot2084711551:AAGV4Fmp2kZ_COs0UvEYTsh9d5oVm9w8Oe8/sendMessage?chat_id=2072707119&text=Hello%20World

ps -a > /home/darkfess/tg-log &&
curl --socks5-basic -x socks5h://<адрес:порт> -U <логин:пароль>
-X POST https://api.telegram.org/bot<токен>/sendMessage -d chat_id=<чат> -d
text="$(tail -n 10 /home/darkfess/tg-log)"