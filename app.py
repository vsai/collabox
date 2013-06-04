import uuid

######### TODO #########
#should create an abstract class for accounts that are made
#download, upload, ls, mkdir, and other basic functionality
#############################

accounts = {}

def generateRandomString():
	return uuid.uuid4().hex


def addAccount():
	acct_id = generateRandomString()
	new_account = "create appropriate account object here"
	accounts[acct_id] = new_account
	return acct_id

def deleteAccount(acct_id):
	acct = accounts.get(acct_id)
	if not acct:
		return
	acct.close()
	return


