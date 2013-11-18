
''' Author:Polina Soshnin
    Date: Nov 17, 2013 
    Description: Draws one dustbunny using several different glut objects
'''

### ================================================================
import sys
import random
from TW import *
import scene 

### ================================================================
'''Global variables'''

cornflower = (100.0/255, 149.0/255, 237.0/255)
purple = (102.0/255, 0.0/255, 102.0/255)
black=(0.0, 0.0, 0.0)
white= (1.0, 1.0, 1.0)

### ================================================================

'''Dust Bunny is made out of a sphere and cylinders protruding from the sphere'''
def dust_bunny(radius, color):
 	'''Draws the body of a dust bunny of given radius and color.
    The color is a 3 RBG tuple'''

    #draws the body consisting of a cylinder 
	s=25
	twColor(color,0.7, 10)
	glPushMatrix()
	#glRotate(-90,0,1,0)
	glutSolidSphere(radius,s,s)
	glPopMatrix()

	#draws the eyes. the eyes are going to be tubes
	#and there will be a circle on the tubes  

	glPushMatrix()
	glRotate(70,0,1,0)
	drawEye(radius,s)
	glPopMatrix()

	glPushMatrix()
	glRotate(110,0,1,0)
	drawEye(radius,s)
	glPopMatrix()

	#draws the tentacles
	#the length of each tentacle is between 1/2 the radius and 3/2 the radius
	#the tentacles are spaced 10 to 20 degrees apart 
	#the width of each tentacle is 1/15 of the radius
	angle=0
	
	while angle<360:
		glPushMatrix()
		glRotatef(angle,1,0,0)
		twColor(black, 0.7, 10)
		rand_height= random.uniform(radius*1.5, radius*2.5)
		twCylinder(radius/15.0, radius/15.0, rand_height, 32, 32)
		glPopMatrix()
		randnum= random.randint(10,30)
		angle= angle+randnum
		
def drawEye(radius,s):
	twColor(white,0.7,10)
	twTube(radius/3.5, radius/3.5, radius*1.10,s,s)
	twColor(black,0.7,10)
	glPushMatrix()
	twTube(radius/10.0,radius/10.0, radius*1.15, s,s)
	glPopMatrix()   

### ================================================================

# Display
def display():
    twDisplayInit()
    
    twCamera()
    
    glPushMatrix()
    glTranslate(0,0,0)
    glRotatef(-90,0,1,0)
    dust_bunny(1, black)
    glPopMatrix()

    glFlush()
    glutSwapBuffers() 	
    
### ================================================================
# Main
def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0, 5, 0, 5, 0, 5)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()