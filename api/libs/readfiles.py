

class read_file:

	@staticmethod
	def read_uploads(file):
		data = file.read().decode("utf-8")
		return data.strip().split('\n')
