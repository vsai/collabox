#input
import paramiko
import getpass
from abstractAccount import *
from stat import S_ISDIR


class SFTPServer(AbstractAcct):
	def __init__(self, hostname, port=22):
		import getpass
		uname = getpass.getuser()
		pwd = getpass.getpass("password of %s: " % uname)
		self.transport = paramiko.Transport((hostname, port))
		self.transport.connect(username=uname, password=pwd)
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

	def ls(self, dir_path=None, onlyDirectories=False):
		if dir_path:
			lst = self.sftp.listdir(dir_path)
		else:
			lst = self.sftp.listdir()

		if onlyDirectories:
			return filter(self.isDir, lst)
		else:
			return lst

	def isDir(self, path):
		try:
			return S_ISDIR(self.sftp.stat(path).st_mode)
  		except IOError:
    		#Path does not exist, so by definition not a directory
			return False

	def close(self):
		if self.transport.is_active():
			self.sftp.close()
			self.transport.close()

