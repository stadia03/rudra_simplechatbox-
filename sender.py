#Trying to build a class which prints recieved message and get messages 
# from the user

class UI:
	def __init__(self, name, pc):
		self.name = name
		self.pc = pc
	
	#method to get message from the user
	def get_message(self):
		return input(self.name + "@" + self.pc + ":> ")

	#method to print the recieved message to the terminal
	def print_message(string, sender_name, sender_pc):
		print(sender_name + "@" + sender.pc + ":> "+string)
