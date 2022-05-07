#!/usr/bin/env python3
import getpass
import os
import friend
from sender import UI
from server import Server
from friend import Friend

user_info = {"name": getpass.getuser(), "nodename": os.uname().nodename}
srv_cfg = {"port": 3939, "size": 1024}
FRIENDS_LIST = [
    Friend(
        name=user_info["name"], ip="0.0.0.0", port=srv_cfg["port"], size=srv_cfg["size"]
    )
]

ui = UI(name=user_info["name"], pc=user_info["nodename"])

inbox = Server(srv_cfg["port"], srv_cfg["size"])
# TODO: Find some way to get an input of i from user
outbox = friend.connect_to(FRIENDS_LIST[i])

while True:
    read = inbox.recv()
    if read.data:
        ui.print_message(read.data, FRIENDS_LIST[i])
    wrote = ui.get_message()
    outbox.send(wrote)
