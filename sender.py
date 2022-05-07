# Trying to build a class which prints recieved message and get messages
# from the user


class UI:
    def __init__(self, name, pc):
        self.name = name
        self.pc = pc

    # method to get message from the user
    def get_message(self):
        return input(self.name + "@" + self.pc + ":> ")

    # method to print the recieved message to the terminal
    def print_message(string, friend):
        print(friend.name + ":> " + string)

    def chooseFriend(friendlist):
        for (i, f) in enumerate(friendlist):
            print(f"Enter {i} for {f}")

        i = int(input())
        while i not in range(len(friendlist)):
            print("No such friend.Try again")
            i = int(input())

        return i
