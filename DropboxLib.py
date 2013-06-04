#DropboxLib.py
import webbrowser
from dropbox import client, rest, session


class DropboxServer():

	def __init__(self):
		APP_KEY = 'bwprdal6wpnd0ql'
		APP_SECRET = 'pdczqfzsxnczx6q'
		ACCESS_TYPE = 'dropbox'
		sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
		request_token = sess.obtain_request_token()
		url = sess.build_authorize_url(request_token)
		webbrowser.open_new(url)
		print "Please authorize in the browser. After you're done, press enter."
		raw_input()
		# This will fail if the user didn't visit the above URL and hit 'Allow'
		access_token = sess.obtain_access_token(request_token)
		self.client = client.DropboxClient(sess)

	def getAccountInfo(self):
		return self.client.account_info()

	def pwd(self):
		#find currently working directory
		raise NotImplementedError("Should implement this")

	def download(self, source_file, destination_file):
		#download file
		f, metadata = self.client.get_file_and_metadata(source_file)
		out = open(destination_file, 'w')
		out.write(f.read())
		f.close()
		out.close()
		return metadata
		
	def upload(self, source_file, destination_file):
		#upload file
		f = open(source_file)
		response = self.client.put_file(destination_file, f)
		print "uploaded:", response
		f.close()
		return response

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
		metadata = self.client.metadata(path)
		print type(metadata)
		print metadata
		isdir = metadata.get('is_dir')
		if not isdir: #false or None
			return False
		return True

		#boolean function to check if something is a directory
		# raise NotImplementedError("Should implement this")

	def close(self):
		#close connections to account
		raise NotImplementedError("Should implement this")

