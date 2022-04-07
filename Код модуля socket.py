class socket:  # Да, да, имя класса с маленькой буквы :(
    def __init__(self, sock_familty, sock_type, proto):
        self._fd = system_socket(sock_family, sock_type, proto)

    def write(self, data):
        # на самом деле вместо write используется send, но об этом ниже
        system_write(self._fd, data)

    def fileno(self):
        return self._fd
