#!/usr/bin/env python3
from collections import namedtuple
from client import Client

Friend = namedtuple("Friend", ["name", "ip", "port", "size"])


def connect_to(friend):
    return Client(friend.ip, friend.port, friend.size)
