#input
import paramiko
import getpass


class SFTPServer():
	def __init__(self, username, password, hostname, port=22):
		self.transport = paramiko.Transport((hostname, port))
		self.transport.connect(username=username, password=password)
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)


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
