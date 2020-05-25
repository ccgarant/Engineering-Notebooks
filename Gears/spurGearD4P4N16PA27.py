#spur gear design
'''
d = 4, [in] pitch circle diameter
P = 4, [in] diametral pitch
N = 16, # of gear teeth
PA = 27, [deg] pressure angle
'''

#imports
from numpy import pi, sin, cos, tan, deg2rad, arange
import pandas as pd
import numpy as np


#####d
# dims
#####

#all dimensions in inches
d = 4  #pitch diameter
P = 4  #diametral pitch
N = round(P*d,3) #number of teeth
p = round(pi*d/N,3)
pa = 27 #[deg] common is 20, but going for exagerated
r_pitch= d/2 #pitch radius
r_base = round((r_pitch)*cos(deg2rad(pa)),3)
addendum = 1.00/P  #addendum
dedendum = 1.25/P  #dedendum
clearance = .125
r_addendum = r_pitch + addendum
r_dedendum = r_pitch - dedendum
r_clearance = r_pitch - dedendum + clearance
tooth_thickness = p/2 #circular pitch divided by two

#tooth thickness arc
s = tooth_thickness  #arc
r = r_pitch
theta_tooth_thickness_rad = s/r_pitch
theta_tooth_thickness_deg = round(np.rad2deg(theta_tooth_thickness_rad),3)
theta_tooth_thickness_lineofsymmetry_deg = theta_tooth_thickness_deg/2     #line of symmetry about which to mirrow the invlute curve

print('gear design input parameters:')
print('')
print(f'{d}, pitch diameter')
print(f'{P}, diametral pitch')
print(f'{N}, number of teeth')
print(f'{p}, circular pitch')
print(f'{pa}, pressure angle')
print('')
print('gear design output design parameters:')
print('')
print('design info:')
print(f'{addendum}, addendum, radial distance from pitch radius')
print(f'{dedendum}, dedendum, radial distance from pitch radius')
print(f'{clearance}, clearance')
print('')
print('radii info:')
print(f'{r_pitch}, pitch radius')
print(f'{r_base}, base radius')
print(f'{r_addendum}, addendum radius')
print(f'{r_dedendum}, dedendum radius')
print(f'{r_clearance}, clearance radius')
print('')
print('tooth thickness info:')
print(f'{tooth_thickness}, tooth thickness')
print(f'{theta_tooth_thickness_deg} tooth thickness angle [deg]')
print(f'{theta_tooth_thickness_lineofsymmetry_deg} tooth thickness line of symmetry [deg]')

#####
# involute
#####

theta_deg = arange(0,70,5)  #0 to 70 degress in 5 degree intervals
theta_rad = np.deg2rad(theta_deg)
s = theta_rad*r_base

theta_deg = list(theta_deg)
theta_rad = list(theta_rad)
s = list(s)

inv = pd.DataFrame(index=theta_deg, columns=['theta_rad','s arc length'])
inv.index.name = 'deg'

inv['theta_rad'] = theta_rad
inv['s arc length'] = s

print(inv)