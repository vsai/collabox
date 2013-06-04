
class AbstractAcct():
	def pwd(self):
		#find currently working directory
		raise NotImplementedError("Should implement this")

	def download(self, source_file, destination_file):
		#download file
		raise NotImplementedError("Should implement this")

	def upload(self, source_file, destination_file):
		#upload file
		raise NotImplementedError("Should implement this")

	def createFolder(self, dir_path):
		#create folder
		raise NotImplementedError("Should implement this")

	def deleteFolder(self, dir_path):
		#delete folder
		raise NotImplementedError("Should implement this")

	def renamePath(self, oldpath, newpath):
		#rename path
		raise NotImplementedError("Should implement this")

	def deleteFile(self, file_path):
		#delete file
		raise NotImplementedError("Should implement this")

	def ls(self, dir_path, onlyDirectories):
		#list files of dir_path
		raise NotImplementedError("Should implement this")

	def isDir(self, path):
		#boolean function to check if something is a directory
		raise NotImplementedError("Should implement this")

	def close(self):
		#close connections to account
		raise NotImplementedError("Should implement this")

