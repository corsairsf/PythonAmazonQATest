from operator import itemgetter

# we can store test data in this module like users

users = [

	{'name' : 'user_1', 'email' : 'email@gmail.com', 'password' : '123456aa' }
	{'name' : 'user_2', 'email' : 'email_2@gmail.com', 'password' : 'aa123456'}
]

def get_user(name)
		try:
			return (user for user in users if user['name'] == name).text()

			exept:
				print "\n     User %s is not defined, enter a valid user.\n" %name