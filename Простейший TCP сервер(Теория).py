import socket

serv_sock = socket.socket(socket.AF_INET,  # задаем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)  # выбираем протокол 'по умолчанию' для TCP, т.е. IP
print(type(serv_sock))  # <class 'socket.socket'>


# ДОСТУП К ЦЕЛОЧИСЛЕННОМУ ФАЙЛОВОМУ ДЕСКРИПТОРУ МОЖНО ПОЛУЧИТЬ С ПОМОЩЬЮ:
print(serv_sock.fileno())  # 3 или другой int


# ПРИВЯЗКА СОЗДАННОГО СОКЕТА К ОДНОМУ ИЗ СЕТЕВЫХ АДАПТЕРОВ
serv_sock.bind(('127.0.0.1', 53210))  # чтобы привязать сразу ко всем, можно использовать ''


# ПЕРЕВОД СОКЕТА В СОСТОЯНИЕ ОЖИДАНИЯ ПОДКЛЮЧЕНИЯ
serv_sock.listen(10)  # 10 - это размер очереди входящих подключений, т.н. backlog


# ПОЛУЧЕНИЕ СОЕДИНЕНИЕ ИЗ ЭТОЙ ОЧЕРЕДИ
client_sock, client_addr = serv_sock.accept()


# НА ЭТОМ ЭТАПЕ НА СТОРОНЕ СЕРВЕРА МЫ ИМЕЕМ ДВА СОКЕТА.
# Первый, serv_sock, находится в состоянии LISTEN, т.е. принимает входящие соединения.
# Второй, client_sock, находится в состоянии ESTABLISHED, т.е. готов к приему и передаче данных.


# ПРИМЕР ЧТЕНИЯ И ЗАПИСИ ДАННЫХ В КЛИЕНТСКИЙ СОКЕТ:
while True:
    data = client_sock.recv(1024)
    if not data:
        break
    client_sock.sendall(data)
    print(data)


# АДРЕСАЦИЯ:
'''
serv_sock:
  laddr (ip=<server_ip>, port=53210)
  raddr (ip=0.0.0.0, port=*)  # т.е. любой

client_sock:
  laddr (ip=<client_ip>, port=51573)  # случайный порт, назначенный системой
  raddr (ip=<server_ip>, port=53210)  # адрес слушающего сокета на сервере
'''


# ПОДКЛЮЧЕНИЕ К СЕРВЕРУ

# Подключиться к этому серверу можно с использованием консольной утилиты telnet,
# предназначенной для текстового обмена информацией поверх протокола TCP:

'''
telnet 127.0.0.1 53210
> Trying 192.168.0.1...
> Connected to 192.168.0.1.
> Escape character is '^]'.
> Hello
> Hello
'''
