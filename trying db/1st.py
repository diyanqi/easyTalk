from persistent import Persistent
		
class Host(Persistent):
	def __init__(self, hostname, ip, interfaces):
		self.hostname = hostname
		self.ip = ip
		self.interfaces = interfaces