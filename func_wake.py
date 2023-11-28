from paramiko import SSHClient, AutoAddPolicy
from ngrok import Client

def ngrok_check(): # проверяет наличие ключа нгрок k1-ключ успешно запущен  k2-ключ был добавлен и запущен
    with open("key.txt", "r+") as f:
        global ng_client
        key = f.readline()
        if not key:
            key = input("please inter your ngrok authtoken: ")
            print(key , file=f)
            ng_client = Client(key)
            return "ng2"
        else:
            ng_client = Client(key[:len(key) - 1:])
        return "ng1"

def mac_check(): # проверяет наличие ключа нгрок k1-ключ успешно запущен  k2-ключ был добавлен и запущен
    with open("mac.txt", "r+") as f:
        mac = f.readline()
        if not mac:
            mac = input("please inter your pc mac address: ")
            print(mac , file=f)
            return mac, "m2"
        return mac[:len(mac) - 1:].replace("-", ":", 5), "m1"

def ip_s():  # ip промежуточного устройства
    for i in ng_client.tunnels.list():   # getting all ngrok connections in "i"
        if i.forwards_to == "localhost:22":         
            return str(i.public_url)[6::]

def wake_up(ip, mac):   # включает устройство использую айпи для подключения
    print(ip, mac)
    host = ip[:ip.find(":"):] # подкдючается к промежуточному устройства и отправляет пакет для включения
    with open("intermediate_device_data.txt", "r+") as f: # логин пароль промежуточного устройства
        
        data = f.readline().split()

        if not data:
            user = str(input("Please inter intermediate device user name: "))
            pw = str(input("Please inter intermediate device password: "))

            f.write(user + " ")
            f.write(pw)

        else: 

            user = data[0]
            pw = data[1]

        username = user
        password = pw
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(hostname=host, username=username, password=password, port=int(ip[ip.find(':') + 1::]))   # подключение к промежуточному устройству
        _stdin, stdout,_stderr = ssh_client.exec_command(f"wakeonlan {mac[0]}")    # отправка команды
        print(str(stdout.read())[2:-3:])    # выход
        ssh_client.close()  # отключение
    return

ngrok_check()

wake_up(ip_s(), mac_check())