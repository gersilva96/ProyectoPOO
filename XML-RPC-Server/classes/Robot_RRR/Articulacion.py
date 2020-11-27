
class ArticulacionC:
	Velocidad=25
	AnguloMax=0.0
	AnguloMin=0.0
	VelocidadMax=0
	Angulo=0.0

	def __init__(self, AnguloMax, AnguloMin, VelocidadMax):
		self.AnguloMax=AnguloMax
		self.AnguloMin=AnguloMin
		self.VelocidadMax=VelocidadMax
		
	
	def getVelocidad(self):
		return self.Velocidad

	def getAngulo(self):
		return self.Angulo
		
	def setVelocidad(self, NuevaVelocidad):
		a=float(NuevaVelocidad)
		b=float(self.VelocidadMax)
		if a > b:
			return True
		else:
			self.Velocidad=NuevaVelocidad
			return False

	def setAngulo(self, NuevoAngulo, Sentido):
		a=float(self.Angulo)
		b=float(NuevoAngulo)
		d=float(self.AnguloMax)
		if Sentido == True:
			c = a + b
		else:
			c = a - b

		if c < d:
			self.Angulo=c
			return False
		else:
			return True











