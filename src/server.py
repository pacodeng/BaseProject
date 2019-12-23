import socket
from _thread import *
from player import Player , projectile
import pickle
from config import IP, PORT, maxPlayer
import packet
import json

class Server():
    def __init__(self, ip = IP, port = PORT, maxPlayer = maxPlayer):
        self.ip = IP
        self.port = PORT
        self.Maxplayer = maxPlayer
        self.Playerlist = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Preset_pos = [(30,560),(100,560)]
        self.newJoined = False

    def update(self):
        client, addr = self.sock.accept()
        print("Connected to:", addr)

        data = client.recv(4096).decode('utf-8')
        payload = json.loads(data)
        print('payload: ', payload)
        if payload['event'] == packet.Event_joingame:
            print('Player {} join!'.format(addr[0]))
            self.newJoined = True
            start_new_thread(self.update_player, (client, str(addr[1]), payload))


    def update_player(self, sock, addr, payload):
        self.newJoined = False
        sock.setblocking(False)
        moving = False
        while True:
            try:
                data = sock.recv(4096).decode('utf-8')
                if data:
                    payload = json.loads(data)
            except socket.error:
                pass
            else:
                break
            if payload['event'] == packet.Event_joingame and not(addr in self.Playerlist.keys()):
                x, y = self.Preset_pos[len(self.Playerlist)]
                newplayer = Player(x, y,40,60, sock)
                self.Playerlist[addr] = newplayer
                print('通知其他玩家')
                for p in self.Playerlist.values():
                    packet.sendpack(p.sock, packet.Event_joingame, {'addr': addr, 'x': x, 'y': y})

            player = self.Playerlist[addr]
            if payload['event'] == packet.Event_jump:
                player.jumped = True
                moving = True
            if player.jumped:
                if player.jumpCount >= -10:
                    neg = 1
                    if player.jumpCount < 0:
                        neg = -1
                    player.y -= (player.jumpCount ** 2) * 0.5 * neg
                    player.jumpCount -= 1
                else:
                    player.jumped = False
                    player.jumpCount = 10

            if payload['event'] == packet.Event_move:
                moving = True
                if not payload['payload'] == standing:
                    if payload['payload'] == left:
                        player.walkCount += 1
                        player.x -= player.vel
                    else:
                        player.walkCount += 1
                        player.x += player.vel
            if moving:
                self.updateposition(sock)
        self.Playerlist.pop(addr)
        print('player'+playerID+'left')


    def start(self):
        try:
            self.sock.bind((IP, PORT))
        except socket.error as e:
            print(e)
        self.sock.listen(2)

    def updateposition(self, conn):
        for playeraddr in self.Playerlist.keys():
            p = self.Playerlist[playeraddr]
            packet.sendpack(conn, packet.Event_poschange,{'addr':playeraddr, 'x': p.x, 'y': p.y})

if __name__ == '__main__':
    server = Server()
    server.start()
    print("Waiting for a connection, Server Started")
    while True:
        server.update()