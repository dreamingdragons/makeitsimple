import os

# FOR PRODUCTION USE
class security():
	SECRET_KEY = os.environ['SECRET_KEY']