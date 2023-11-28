# Wake_up_app
Программа для дистанционного включения компьютера

ДЛЯ РАБОТЫ НЕОБХОДИМО УСТРОЙСТВО, КОТОРОЕ БУДЕТ ВСЁ ВРЕМЯ НАХОДИТЬСЯ В ЛОКАЛЬНОЙ СЕТИ С ВАШИМ КОМПЬЮТЕРОМ

            УСТАНОВКА 

Скайте ВСЕ файлы (в том числе txt)

Для запуска необходимы следующте библиотеки для python:
 - paramiko
 - ngrok


             ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ 

Перед запуском необходимо выполнить несколько действий:

1. Зарегистрируйтесь на сайте https://ngrok.com/
2. Срздайте API ключ и вставьте его в первую строчку файла key.txt
3. На устройстве которое всегда будет в сети создайте пользователя и вставьте логин и пароль через пробел в перую строчку файла intermediate_device_data (например если логин user а пароль 123, то в файле должно быть: "user 123")
4. На этом же устройстве включите tcp соединение на 22 порт через ngrok
5. Любым доступным способом узнайте mac адресс устройства которое вы хотите включать и вставьте его в первую строчку файла mac.txt в формате XX-XX-XX-XX-XX-XX
6. В настройках bios вам необходимо включить функцию включения компьютера через устройство в локальной сети (Способ включения и название данной функции различаяется в зависимость от материнской платы поэтому инструкцию лучше поискать в интернете)

Ставите программу на флешку или любой другой переносной носитель и при запуске файла func_wake.py вне зависимость от вашего местоположения при наличии интернет соединения устройство, которое вы указали в файлах, будет дистанционно включено.
