#!/usr/bin/env python3
# multithreading
import getpass
import os
import friend
from sender import UI
from server import Server
from friend import Friend
import sys
import select

user_info = {"name": getpass.getuser(), "nodename": os.uname().nodename}
srv_cfg = {"port": 3939, "size": 1024}
FRIENDS_LIST = [
    Friend(
        name=user_info["name"], ip="0.0.0.0", port=srv_cfg["port"], size=srv_cfg["size"]
    )
]

ui = UI(name=user_info["name"], pc=user_info["nodename"])

inbox = Server(srv_cfg["port"], srv_cfg["size"])
inbox.start()
i = UI.chooseFriend(FRIENDS_LIST)
outbox = friend.connect_to(FRIENDS_LIST[i])

while True:
    read_socks, write_socks, err_socks = select.select(
        [inbox.socket, outbox.socket, sys.stdin], [], []
    )
    for sock in read_socks:
        if sock == inbox:
            read = inbox.recv()
            ui.print_message(read.data, FRIENDS_LIST[i])
        else:
            wrote = ui.get_message()
            outbox.send(wrote)
