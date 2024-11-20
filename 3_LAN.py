class Server:

    last_ip = 0

    def __init__(self):
        self.ip = Server.last_ip + 1
        Server.last_ip = self.ip
        self.buffer = []
        self.router = None

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        res = self.buffer
        self.buffer = []
        return res

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        self.servers.pop(server.get_ip())
        server.router = None

    def send_data(self):
        for data in self.buffer:
            server = self.servers[data.ip]
            server.buffer.append(data.data)
        self.buffer = []


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

# sv_from1 = Server()
# sv_from2 = Server()
# sv_to = Server()
# router = Router()
# router.link(sv_from1)
# router.link(sv_from2)
# router.link(sv_to)
# sv_from1.send_data(Data("hello", sv_to.get_ip()))
# sv_from2.send_data(Data("hi", sv_to.get_ip()))
# sv_to.send_data(Data("bye", sv_from1.get_ip()))
# router.send_data()
# print(sv_to.get_data())
# print(sv_from1.get_data())