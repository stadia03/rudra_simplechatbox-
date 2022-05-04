#Trying to build a class which prints recieved message and get messages 
# from the user

class UI:
	def __init__(self, name):
		self.name = name

	def get_message(self):
		return input(self.name + ":> ")

	def print_message(self, string):
		print(self.name+string)
