#!/usr/bin/env python3
# multithreading
import getpass
import os
import friend
from sender import UI
from server import Server
from friend import Friend
from friendlist import FRIENDS_LIST
import sys
import select
import argparse

parser = argparse.ArgumentParser(description="Talk to friends")
parser.add_argument(
    "inbox_port", metavar="N", type=int, nargs=1, help="set port for the inbox"
)
args = parser.parse_args()
print(f"{args.inbox_port[0]}")

user_info = {"name": getpass.getuser(), "nodename": os.uname().nodename}
srv_cfg = {"port": int(args.inbox_port[0]), "size": 1024}

ui = UI(name=user_info["name"], pc=user_info["nodename"])

inbox = Server(srv_cfg["port"], srv_cfg["size"])
inbox.start()
i = UI.chooseFriend(FRIENDS_LIST)
outbox = friend.connect_to(FRIENDS_LIST[i])
outbox.start()

try:
    while True:
        read_socks, write_socks, err_socks = select.select(
            [inbox.socket, sys.stdin], [], []
        )
        for sock in read_socks:
            if sock == inbox.socket:
                read = inbox.recv().decode()
                ui.print_message(read, FRIENDS_LIST[i])
            else:
                wrote = ui.get_message()
                outbox.send(wrote)
except KeyboardInterrupt:
    print("Ok, going away")
finally:
    inbox.close()
    outbox.close()
