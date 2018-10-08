from abc import ABCMeta,abstractmethod

class Images:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def load(self):
        return("loaded")
    
    #abstractmethod
    def save(self):
        print("saved")

class Songs(Images):
	
	def load(self):
		s=super(Songs, self).load()
		print(s,"opened")
	
	#@abc.abstractmethod
	#def Close(self):
		#print ("closed")

a=Songs()
a.load()
a.save()

