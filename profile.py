import os

class Profile:
	"This is the basic profile created after submitting"

	def __init__(self, name, email, picture):
		self.name    = _name
		self.email   = _email
		self.picture = _picture
		self.sports  = []


def create():
	project_name = input("Name of new profile: ")
	directory = os.path.dirname(__file__) + "/" + new_profile
	if not os.path.exists(directory):
		os.makedirs(directory)
		new_profile = project_name + "_profile.txt"
		complete_name = directory + "/" + new_profile

def check_file(filename):
	try:
		print("opening", filename)
		return open(filename, 'r')

	except FileNotFoundError:
		print("Error: ", filename, " not found")
		print("Creating new profile file")
		create()
		return