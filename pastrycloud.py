''' Author:Polina Soshnin
    Date: Nov 17, 2013 
    Description: Draws one pastrycloud
'''

import sys
from TW import *
import math


### ================================================================
'''CLOUD CONTROL POINTS'''
#equations for the 3 circles and 1 ellipse I'm using to 
#determine my control points

#ellipse: (x^2)/9 + y^2=1
#top circle: x^2+ (y^2-2)=1
#middle circle: (x^2-1)+ (y^2-1)=1
#bottom circle: (x^2-2)+y^2=1

def top_circle_y(xcoord):
    return math.sqrt(1-math.pow(xcoord,2))+2

def middle_circle_y(xcoord):
    return math.sqrt(1-math.pow(xcoord-1,2))+1

def bottom_circle_y(xcoord):
    return math.sqrt(1-math.pow(xcoord-2,2))

def ellipse_y(xcoord):
    return -math.sqrt(1-(math.pow(xcoord,2)/9))


top_circle_1= ( (0.0, top_circle_y(0.0), 0.0),
            (0.2, top_circle_y(0.2), 0.0),
            (0.4, top_circle_y(0.4), 0.0),
            (0.6,  top_circle_y(0.6), 0.0)
            )


top_circle_2 = ((0.6,  top_circle_y(0.6), 0.0),
            (0.7,  top_circle_y(0.7), 0.0),
            (0.8, top_circle_y(0.8), 0.0),
            (1.0, top_circle_y(1.0), 0.0)
            )

middle_circle_1= ( (1.0, middle_circle_y(1.0), 0.0),
            (1.2, middle_circle_y(1.2), 0.0),
            (1.4, middle_circle_y(1.4), 0.0),
            (1.6,  middle_circle_y(1.6), 0.0)
            )


middle_circle_2 = ((1.6,  middle_circle_y(1.6), 0.0),
            (1.7,  middle_circle_y(1.7), 0.0),
            (1.8, middle_circle_y(1.8), 0.0),
            (2.0, middle_circle_y(2.0), 0.0)
            )

bottom_circle_1= ( (2.0, bottom_circle_y(2.0), 0.0),
            (2.2, bottom_circle_y(2.2), 0.0),
            (2.4, bottom_circle_y(2.4), 0.0),
            (2.6,  bottom_circle_y(2.6), 0.0)
            )


bottom_circle_2 = ((2.6,  bottom_circle_y(2.6), 0.0),
            (2.7,  bottom_circle_y(2.7), 0.0),
            (2.8, bottom_circle_y(2.8), 0.0),
            (3.0, bottom_circle_y(3.0), 0.0)
            )

### ================================================================
'''ELLIPSE CONTROL POINTS'''

ellipse_1= ( (0.0, ellipse_y(0.0), 0.0),
            (0.2, ellipse_y(0.2), 0.0),
            (0.4, ellipse_y(0.4), 0.0),
            (0.6,  ellipse_y(0.6), 0.0)
            )

ellipse_2 = ((0.6,  ellipse_y(0.6), 0.0),
            (0.7,  ellipse_y(0.7), 0.0),
            (0.8, ellipse_y(0.8), 0.0),
            (1.0, ellipse_y(1.0), 0.0)
            )

ellipse_3= ( (1.0, ellipse_y(1.0), 0.0),
            (1.2, ellipse_y(1.2), 0.0),
            (1.4, ellipse_y(1.4), 0.0),
            (1.6,  ellipse_y(1.6), 0.0)
            )


ellipse_4 = ((1.6,  ellipse_y(1.6), 0.0),
            (1.7,  ellipse_y(1.7), 0.0),
            (1.8, ellipse_y(1.8), 0.0),
            (2.0, ellipse_y(2.0), 0.0)
            )

ellipse_5= ( (2.0, ellipse_y(2.0), 0.0),
            (2.2, ellipse_y(2.2), 0.0),
            (2.4, ellipse_y(2.4), 0.0),
            (2.6,  ellipse_y(2.6), 0.0)
            )


ellipse_6= ((2.6,  ellipse_y(2.6), 0.0),
            (2.7,  ellipse_y(2.7), 0.0),
            (2.8, ellipse_y(2.8), 0.0),
            (3.0, ellipse_y(3.0), 0.0)
            )

### ================================================================

# The silhouette is a 1D curve in z=0 plane; this rounds it out to a
# 2D surface with a circular cross-section.

def circular_slice(silhouette_cp):
    surface_cp = [ map(list,silhouette_cp),
                   map(list,silhouette_cp),
                   map(list,silhouette_cp),
                   map(list,silhouette_cp)
                    ]
    # the first list will stay unchanged, lying in z=0
    # the last list (#3) will lie in x=0, by swapping x and z for each one
      
    for i in range(4):
        surface_cp[3][i][0] = surface_cp[0][i][2] # x = z
        surface_cp[3][i][2] = surface_cp[0][i][0] # z = x


    # base list 1 on list 0 and list 2 on list 3.
    for i in range(4):
        # for list 1, x and y don't change, z gets the radius*0.552
        radius = silhouette_cp[i][0]
        #dist= radius
        dist = radius*0.552;    # distance of inner control points
        surface_cp[1][i][0] = surface_cp[0][i][0]
        surface_cp[1][i][2] = dist
        surface_cp[2][i][0] = dist
        surface_cp[2][i][2] = surface_cp[3][i][2]
    
    return surface_cp


def draw_silhouette():

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLineWidth(3.0)

    twDrawBezierCurve(top_circle_1,12)
    twDrawBezierCurve(top_circle_2,12)

    twDrawBezierCurve(middle_circle_1,12)
    twDrawBezierCurve(middle_circle_2,12)

    twDrawBezierCurve(bottom_circle_1,12)
    twDrawBezierCurve(bottom_circle_2,12)

    twDrawBezierCurve(ellipse_1,12)
    twDrawBezierCurve(ellipse_2,12)
    twDrawBezierCurve(ellipse_3,12)
    twDrawBezierCurve(ellipse_4,12)
    twDrawBezierCurve(ellipse_5,12)
    twDrawBezierCurve(ellipse_6,12)

    glPopAttrib()

## the 2D surface is just 1/4 of a circle/cylinder. This does 4 to
## make it complete.


'''THIS WILL DRAW THE TOP OF THE CLOUD'''
def draw_figure_of_revolution(cp):
    # q is the quadrant of the circular cross-section that we're drawing.
    glPushMatrix();
    for q in range(4):
        twDrawBezierSurface(cp,10,10)
        glRotatef(90,0,1,0);
    glPopMatrix();


'''draw_cloud creates one bezier surface that resembles a cloud'''
def draw_cloud():
    
    #need to draw 12 slices

    top_circle_1_slice= circular_slice(top_circle_1)
    draw_figure_of_revolution(top_circle_1_slice)

    top_circle_2_slice= circular_slice(top_circle_2)
    draw_figure_of_revolution(top_circle_2_slice)

    
    middle_circle_1_slice= circular_slice(middle_circle_1)
    draw_figure_of_revolution(middle_circle_1_slice)

    middle_circle_2_slice= circular_slice(middle_circle_2)
    draw_figure_of_revolution(middle_circle_2_slice)

    bottom_circle_1_slice= circular_slice(bottom_circle_1)
    draw_figure_of_revolution(bottom_circle_1_slice)

    bottom_circle_2_slice= circular_slice(bottom_circle_2)
    draw_figure_of_revolution(bottom_circle_2_slice)

    ellipse_1_slice= circular_slice(ellipse_1)
    draw_figure_of_revolution(ellipse_1_slice)

    ellipse_2_slice= circular_slice(ellipse_2)
    draw_figure_of_revolution(ellipse_2_slice)

    ellipse_3_slice= circular_slice(ellipse_3)
    draw_figure_of_revolution(ellipse_3_slice)

    ellipse_4_slice= circular_slice(ellipse_4)
    draw_figure_of_revolution(ellipse_4_slice)

    ellipse_5_slice= circular_slice(ellipse_5)
    draw_figure_of_revolution(ellipse_5_slice)

    ellipse_6_slice= circular_slice(ellipse_6)
    draw_figure_of_revolution(ellipse_6_slice)
    

def set_lighting():
    twGrayLight(GL_LIGHT0, (5,5,2,1), 0.2, 0.7, 0.2)
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);    

def display():
    twDisplayInit(1,1,1)
    twCamera()

    glDisable(GL_LIGHTING)

    set_lighting();
    glShadeModel(GL_SMOOTH);        # smooth shading 
    
    twColorName(TW_CYAN)

    draw_cloud()

    glFlush()
    glutSwapBuffers()

# ================================================================

def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    twBoundingBox(-1.5/2,5,0,5,-0.25,5)
    twInitWindowSize(500,500)
    glutCreateWindow(sys.argv[0])
    glutDisplayFunc(display)
    twMainInit()
    glutMainLoop()

if __name__ == '__main__':
    main()

