#!/usr/bin/env python3
import getpass
import os
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
