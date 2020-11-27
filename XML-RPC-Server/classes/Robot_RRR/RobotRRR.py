from classes.Robot_RRR.Articulacion import ArticulacionC
from classes.Robot_RRR.EfectorF import Efector

class Robot:
	#Articulacion de la base, puede rotar 360 grados
	articulacion1=None 
	AnguloMax1=360
	AnguloMin1=0
	VelocidadMax=5
	#Articulacion del primer brazo, puede rotar entre 0 y 43 grados
	articulacion2=None 
	AnguloMax2=43
	AnguloMin2=0
	VelocidadMax=5
	#Articulacion del segundo brazo, puede rotar entre 0 y 69 grados(en este va colocado el efector final)
	articulacion3=None 
	AnguloMax3=69
	AnguloMin3=0
	VelocidadMax=5

	def __init__(self):
		self.articulacion1=ArticulacionC(self.AnguloMax1,self.AnguloMin1,self.VelocidadMax)	
		self.articulacion2=ArticulacionC(self.AnguloMax2,self.AnguloMin2,self.VelocidadMax)
		self.articulacion3=ArticulacionC(self.AnguloMax3,self.AnguloMin3,self.VelocidadMax)

	def RotarArticulacion(self):
		ArticulacionC().GirarArticulacion()

	def EfectorFinal(self, tiempo):
		Efector().ActivarEfector(tiempo)


	



