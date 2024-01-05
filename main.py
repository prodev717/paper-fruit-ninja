from ursina import *
from ursina.prefabs import health_bar
from random import randint as ran
from random import uniform as uni

nf=20
nb=10

def update():
	score.text="score:"+str(15-fruit.no)
	if hb.value==0:
		out=Text(text="YOU LOST",color=color.red,scale=2.5,x=-0.15)
	if fruit.no==0:
		win=Text(text="YOU  WON",color=color.red,scale=2.5,x=-0.15)

class fruit(Button):
	no=0
	def __init__(self):
		fruit.no+=1
		self.f=ran(0,5)
		self.dx,self.dy=1,1
		self.sx,self.sy=round(uni(0.001,0.005),3),round(uni(0.001,0.005),3)
		super().__init__(parent=camera,model="quad",double_sided=True,texture="assets/"+fruits[self.f],highlight_color=color.red,color=color.white,
			             x=round(uni(-0.40,0.40),2),y=round(uni(-0.50,0.50),2),z=0.9,scale=0.1)
	def update(self):
		self.rotation_z+=1
		self.x+=self.sx*self.dx
		self.y+=self.sy*self.dy
		if (-0.40<self.x<0.40)==False:
			self.dx*=-1
		if (-0.50<self.y<0.50)==False:
			self.dy*=-1
	def input(self,key):
		if self.hovered:
			if key=="left mouse down":
				a=Audio("assets/sword",pitch=1)
				fruit.no-=1
				S=Entity(parent=camera,model="quad",scale=0.1,texture="assets/S"+fruits[self.f],x=self.x,y=self.y,z=0.95)
				destroy(self)

class bomb(Button):
	def __init__(self):
		self.dx,self.dy=1,1
		self.sx,self.sy=round(uni(0.001,0.005),3),round(uni(0.001,0.005),3)
		super().__init__(parent=camera,model="quad",double_sided=True,texture="assets/bomb.png",highlight_color=color.red,color=color.white,
			             x=round(uni(-0.40,0.40),2),y=round(uni(-0.50,0.50),2),z=0.9,scale=0.1)
	def update(self):
		self.rotation_z+=1
		self.x+=self.sx*self.dx
		self.y+=self.sy*self.dy
		if (-0.40<self.x<0.40)==False:
			self.dx*=-1
		if (-0.50<self.y<0.50)==False:
			self.dy*=-1
	def input(self,key):
		global hb
		if self.hovered:
			if key=="left mouse down":
				a=Audio("boom_1",pitch=1,volume=2)
				S=Entity(parent=camera,model="quad",scale=0.2,texture="assets/explosion.png",x=self.x,y=self.y,z=0.94)
				hb.value-=int(100/4)
				destroy(self)

fruits=("apple.png","banana.png","coconut.png","orange.png","pineapple.png","watermelon.png")
game=Ursina(borderless=False)
window.size=(600,800)
bg=Entity(parent=camera,model="quad",texture="assets/background.png",z=1)
hb=health_bar.HealthBar(bar_color=color.lime)
score=Text(text=0,color=color.black,scale=2,y=0.46,x=0.17)
for i in range(nf):
	f=fruit()
for i in range(nb):
	b=bomb()

game.run()