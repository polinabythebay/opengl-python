
''' Author:Polina Soshnin
    Name: scene.py
    Date: Nov 17, 2013 (using Lateness coupons)
    Description: Draw a scene of pastryclouds and a dustbunny
    Techniques used: Lighting, Bezier Curves, Textures, Glut Objects
'''

import sys
from TW import *
from pastrycloud import *
from dustbunny import *


### ================================================================
'''Global variables'''

cloudblue = (0.0/255, 102.0/255, 204.0/255)
purplered = (102.0/255, 0.0/255, 51.0/255)

## ================================================================

def drawGround():

	#sets the color properties of the ground
    twColor((1,1,1),0.1,0.1)

    #sets up the surface normal 
    glNormal3f(0,-1,0)

    #set up texture parameters, applicable to both textures utilized
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glEnable(GL_TEXTURE_2D)

    # Loads texture for ground
    twPPM_Tex2D(twPathname("stoneTile.ppm",False))
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glBegin(GL_POLYGON)

    glTexCoord2f(0,0); glVertex3fv((0,0,0));
    glTexCoord2f(0,1); glVertex3fv((12,0,0));
    glTexCoord2f(1,1); glVertex3fv((12,0,12));
    glTexCoord2f(1,0); glVertex3fv((0,0,12));

    glEnd()

    glDisable(GL_TEXTURE_2D)

 ### ================================================================

def display():
    twDisplayInit()
    twCamera()

    #sets the lighting

    lightPos = ( 5, 5, 5, 0 )
    twGrayLight(GL_LIGHT0,lightPos,0.2,0.8,0.8);
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);

    #draws the textured ground

    drawGround()

    #draws the dustbunny

    glPushMatrix()
    glTranslate(5,5,5)
    glRotatef(-90,0,1,0)
    dust_bunny(1.5, purplered)
    glPopMatrix()

    twColor(cloudblue,0.1,0.1)

    #draws the clouds

    glPushMatrix()
    glScalef(.75,.75,.75)
    glTranslate(12,6,10)
    draw_cloud()
    glPopMatrix()

    glPushMatrix()
    glScalef(.75,.75,.75)
    glTranslate(2,3,2)
    draw_cloud()
    glPopMatrix()

    glPushMatrix()
    glScalef(.75,.75,.75)
    glTranslate(8,4,2)
    draw_cloud()
    glPopMatrix()

    glPushMatrix()
    glScalef(.75,.75,.75)
    glTranslate(6,2,10)
    draw_cloud()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()


 ### ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(0, 10, 0, 10, 0, 10)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()


