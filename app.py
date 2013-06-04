import uuid

import SFTPLib
import DropboxLib

######### TODO #########
#should create an abstract class for accounts that are made
#download, upload, ls, mkdir, and other basic functionality
#############################

accounts = {}

def generateRandomString():
	return uuid.uuid4().hex

def addAccount(type):
	#type = "dropbox" or "sftp" or "box"
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


hname = '127.0.0.1'
port = 22

# s = SFTPLib.SFTPServer(username=uname, password=pwd, hostname=hname, port=port)
# s.createFolder("/Users/vishalsaidaswani/hello_world")
# s.download("/Users/vishalsaidaswani/Desktop/github keyart.png", "/Users/vishalsaidaswani/a.png")
# s.ls()
# s.close()

s = DropboxLib.DropboxServer()
s.isDir('/Documents')