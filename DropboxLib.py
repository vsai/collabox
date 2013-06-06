#DropboxLib.py
import webbrowser
import private
from dropbox import client, rest, session

#refer to 
# https://www.dropbox.com/static/developers/dropbox-python-sdk-1.5-docs/index.html#dropbox.session.DropboxSession.build_authorize_url


class DropboxServer():
	def __init__(self):
		APP_KEY = private.APP_KEY
		APP_SECRET = private.APP_SECRET
		ACCESS_TYPE = private.ACCESS_TYPE
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

	def search(self):
		#look into client.search(path, query, file_limit=1000, include_deleted=False)
		pass

	def file_copy(self, from_path, to_path):
		#client.file_copy
		pass

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
		# self.client.file_create_folder
		raise NotImplementedError("Should implement this")

	def deleteFolder(self, dir_path):
		#delete folder
		# self.client.file_delete(dir_path)
		raise NotImplementedError("Should implement this")

	def renamePath(self, oldpath, newpath):
		#rename path
		# self.client.file_move
		raise NotImplementedError("Should implement this")

	def deleteFile(self, file_path):
		#delete file
		# self.client.file_delete(file_path)

	def ls(self, dir_path=None, onlyDirectories=False):
		#list files of dir_path
		if not dir_path:
			dir_path = "/"
		lst = self.client.metadata(dir_path).get("contents")
		if onlyDirectories:
			return filter(self.isDir, lst)
		else:
			return lst

	def isDir(self, path):
		#boolean function to check if something is a directory
		#list=false so it does not load the contents array
		metadata = self.client.metadata(path, list=False)
		print type(metadata)
		print metadata
		isdir = metadata.get('is_dir')
		if not isdir: #false or None
			return False
		return True

	def close(self):
		#close connections to account
		raise NotImplementedError("Should implement this")

