#input
import paramiko
import getpass


class SFTPServer():
	def __init__(self, username, password, hostname, port=22):
		self.transport = paramiko.Transport((hostname, port))
		self.transport.connect(username=username, password=password)
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)
		self.homedirectory = self.sftp.getcwd()

	def pwd(self):
		return self.sftp.getcwd()

	def download(self, source_file, destination_file):
		self.sftp.get(source_file, destination_file)

	def upload(self, source_file, destination_file):
		self.sftp.put(source_file, destination_file)

	def createFolder(self, dir_path=None):
		self.sftp.mkdir(dir_path)

	def deleteFolder(self, dir_path=None):
		self.sftp.rmdir(dir_path)

	def renamePath(self, oldpath, newpath):
		self.sftp.rename(oldpath, newpath)

	def deleteFile(self, file_path):
		self.sftp.remove(file_path)

	def ls(self, dir_path=None):
		if dir_path:
			return self.sftp.listdir(dir_path)
		else:
			return self.sftp.listdir()

	def close(self):
		if self.transport.is_active():
			self.sftp.close()
			self.transport.close()



hname = '127.0.0.1'
port = 22
uname = getpass.getuser()
# uname = raw_input("username to connect to: ")
pwd = getpass.getpass("password of %s: " % uname)



s = SFTPServer(username=uname, password=pwd, hostname=hname, port=port)
# s.createFolder("/Users/vishalsaidaswani/hello_world")
# s.download("/Users/vishalsaidaswani/Desktop/github keyart.png", "/Users/vishalsaidaswani/a.png")
print s.ls()
s.close()







# print "Username: %s\nPassword: %s" % (username, password)

# def ls(args):
# 	print "yolo"
# 	print args
# 	s = paramiko.SSHClient()
# 	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 	s.load_system_host_keys()
# 	s.connect(hostname, port, username, password)
# 	command = "ls " + args[0]
# 	(stdin, stdout, stderr) = s.exec_command(command)
# 	for line in stdout.readlines():
# 		print line
# 	s.close()

# def mkdir(args):
# 	#args = [directory_name]
# 	print "swag"
# 	print args
# 	s = paramiko.SSHClient()
# 	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 	s.load_system_host_keys()
# 	s.connect(hostname, port, username, password)
# 	command = "mkdir " + args[0]
# 	(stdin, stdout, stderr) = s.exec_command(command)
# 	for line in stdout.readlines():
# 		print line
# 	s.close()

# def pwd(args):
# 	#args = []
# 	print "pwd"
# 	s = paramiko.SSHClient()
# 	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 	s.load_system_host_keys()
# 	s.connect(hostname, port, username, password)
# 	command = "pwd"
# 	(stdin, stdout, stderr) = s.exec_command(command)
# 	for line in stdout.readlines():
# 		print line
# 	s.close()

# def transferFile(args, direction):
# 	if (direction != 'download' or direction != 'upload'):
# 		raise Exception('Transfer file. Inapplication direction specified')
# 	if (len(args) < 2):
# 		raise Exception('Transfer file - requires at least 2 args')
# 	source_file = args[0]
# 	destination_file = args[1]

# 	transport = paramiko.Transport((hostname, port))
# 	transport.connect(username=username, password=password)
# 	sftp = paramiko.SFTPClient.from_transport(transport)

# 	if (direction == 'download'):
# 		sftp.get(source_file, destination_file)
# 	else: # upload
# 		sftp.put(source_file, destination_file)
# 	sftp.close()
# 	transport.close()


# def getFileList(args):
# 	# args = [directory_path_name]
# 	print getFileList
# 	transport = paramiko.Transport((hostname, port))
# 	transport.connect(username=username, password=password)
# 	sftp = paramiko.SFTPClient.from_transport(transport)
# 	if (len(args) == 0):
# 		print sftp.listdir()
# 	else:
# 		print sftp.listdir(args[0])
# 	sftp.close()
# 	transport.close()


# d = {"ls" : ls, "mkdir" : mkdir, "upload" : uploadFile, "download" : downloadFile, "pwd" : pwd}

# while True:
# 	x = raw_input("Command: ")
# 	print x
# 	x = x.split()
# 	args = []

# 	if (len(x) == 0):
# 		continue
# 	elif (len(x) > 1):
# 		args = x[1::]

# 	fnMap = d.get(x[0])
# 	if fnMap:
# 		fnMap(args)
# 	else:
# 		print "no such function mapping. try again"
# 		continue

