import numpy as np
import bpy
import math
import time

def fingers (a,m):
    if m==1:
        side = "r"
    else:
        side = "l"
    if (a==0 or a==9 or a==1 or a==8):
        #pataka or tripataka or Ardhachandra or Dola
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(16),math.radians(14.4*m),math.radians(-59.2*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(-19.2),math.radians(4.91*m),math.radians(-47.3*m)]
        pb.location = [0.017015*m,-0.022855,-0.054315]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(-13.2),math.radians(-14.2*m),math.radians(4.88*m)]
        pb.location = [0.010108*m,0.003513,-0.046629]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(-6.62),math.radians(-6.61*m),math.radians(0.531*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.location = [0.000043*m,0.006383,0.01972]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(8.55),math.radians(4.64*m),math.radians(0.932*m)]
        pb.location = [0.002588*m,0.009492,0.0334464]
        
        if a==9 :
            pb = ob.pose.bones.get("ring2."+side)
            pb.rotation_euler = [math.radians(0.0435),math.radians(30.5*m),math.radians(74.8*m)]
            
        if a==1:
            #pb = ob.pose.bones.get("upperarm."+side)
            #pb.rotation_euler = [math.radians(6.78),math.radians(48.4*m),math.radians(5.33*m)]
        
            #pb = ob.pose.bones.get("forearm."+side)
            #pb.rotation_euler = [math.radians(-3.27),math.radians(39.6*m),math.radians(-2.08*m)]
            
            pb = ob.pose.bones.get("palm."+side)
            pb.rotation_euler = [0,0,0]
            
            pb = ob.pose.bones.get("thumb1."+side)
            pb.rotation_euler = [math.radians(24.6),math.radians(-16.8*m),math.radians(7.62*m)]
            pb.location = [-0.018362*m,-0.013661,-0.028176]
            
            pb = ob.pose.bones.get("thumb2."+side)
            pb.rotation_euler = [math.radians(14.2),math.radians(-6.72*m),math.radians(2.51*m)]
            
        if a==8:
            pb = ob.pose.bones.get("palm."+side)
            pb.rotation_euler = [math.radians(11.6),math.radians(24.9*m),math.radians(16*m)]
        
            pb = ob.pose.bones.get("thumb1."+side)
            pb.rotation_euler = [0,0,0]
            pb.location = [0,0,0]
            
            
    if a==2 :
        #Kartarimukha
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(20.2),math.radians(16.9*m),math.radians(-51.6*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(-50.4),math.radians(-8.92*m),math.radians(12*m)]
        pb.location = [0.005286*m,-0.038062,-0.044142]
        
        pb = ob.pose.bones.get("thumb2."+side)
        pb.rotation_euler = [math.radians(-38),math.radians(-3.26*m),math.radians(17.2*m)]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(-8.47),math.radians(-12.1*m),math.radians(-1.81*m)]
        pb.location = [0.000355*m,-0.003317,-0.029156]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(-6.61),math.radians(16*m),math.radians(29.3*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(-3.9),math.radians(22.9*m),math.radians(47.9*m)]
        pb.location = [0.001575*m,0.005462,0.022928]
        
        pb = ob.pose.bones.get("ring2."+side)
        pb.rotation_euler = [math.radians(-1.26),math.radians(28.2*m),math.radians(55.1*m)]
        
        pb = ob.pose.bones.get("ring3."+side)
        pb.rotation_euler = [math.radians(-32.4),math.radians(11*m),math.radians(81.5*m)]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(-1.78),math.radians(18.8*m),math.radians(46.2*m)]
        pb.location = [-0.006562*m,0.020608,0.072343]
        
        pb = ob.pose.bones.get("pinky2."+side)
        pb.rotation_euler = [math.radians(-3.72),math.radians(25.4*m),math.radians(49.2*m)]
        
        pb = ob.pose.bones.get("pinky3."+side)
        pb.rotation_euler = [math.radians(-24.7),math.radians(8.38*m),math.radians(65.1*m)]
        
    if a==3:
        #Kutukamukha
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(9.01),math.radians(1.73*m),math.radians(-72.1*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(-20.2),math.radians(-11*m),math.radians(8.74*m)]
        pb.location = [0.016017*m,0.018857,-0.007888]
        
        pb = ob.pose.bones.get("thumb2."+side)
        pb.rotation_euler = [math.radians(-46.6),math.radians(-60.3*m),math.radians(65.3*m)]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(3.81),math.radians(9.67*m),math.radians(61.3*m)]
        
        pb = ob.pose.bones.get("index2."+side)
        pb.rotation_euler = [math.radians(0.486),math.radians(2.59*m),math.radians(21.3*m)]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(8.73),math.radians(2.04*m),math.radians(50*m)]
        pb.location = [-0.004797*m,-0.000071,0.030914]
        
        pb = ob.pose.bones.get("middle2."+side)
        pb.rotation_euler = [math.radians(0.87),math.radians(2.36*m),math.radians(40.5*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(10),math.radians(3.45*m),math.radians(17.9*m)]
        pb.location = [0.002455*m,0.005537,0.028158]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(6.99),math.radians(13.8*m),math.radians(-22.9*m)]
        pb.location = [0.006588*m,0.004933,0.05633]
        
    if a==4 :
        #shikhara
        #pb = ob.pose.bones.get("upperarm."+side)
        #pb.rotation_euler = [math.radians(6.78),math.radians(48.4*m),math.radians(5.33*m)]
        
        #pb = ob.pose.bones.get("forearm."+side)
        #pb.rotation_euler = [math.radians(-3.27),math.radians(39.6*m),math.radians(-2.08*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(23.2),math.radians(3.21*m),math.radians(-3.98*m)]
        pb.location = [0.035344*m,-0.036544,-0.006086]
        
        pb = ob.pose.bones.get("thumb2."+side)
        pb.rotation_euler = [math.radians(20.9),math.radians(-5.05*m),math.radians(0.0151*m)]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(3.67),math.radians(10.2*m),math.radians(76.5*m)]
        pb.location = [-0.009969*m,-0.000854,-0.036625]
        
        pb = ob.pose.bones.get("index2."+side)
        pb.rotation_euler = [math.radians(6.53),math.radians(5.45*m),math.radians(76.9*m)]
        
        pb = ob.pose.bones.get("index3."+side)
        pb.rotation_euler = [math.radians(-14.6),math.radians(49.3*m),math.radians(66.2*m)]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(1.95),math.radians(-0.099*m),math.radians(71.7*m)]
        
        pb = ob.pose.bones.get("middle2."+side)
        pb.rotation_euler = [math.radians(4.26),math.radians(2.04*m),math.radians(82.6*m)]
        
        pb = ob.pose.bones.get("middle3."+side)
        pb.rotation_euler = [math.radians(4.4),math.radians(2.39*m),math.radians(81.5*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(3.75),math.radians(-2.78*m),math.radians(55.4*m)]
        pb.location = [0.000803*m,-0.00226,0.03448]
        
        pb = ob.pose.bones.get("ring2."+side)
        pb.rotation_euler = [math.radians(-0.0722),math.radians(-2.72*m),math.radians(83.3*m)]
        
        pb = ob.pose.bones.get("ring3."+side)
        pb.rotation_euler = [math.radians(2.97),math.radians(0.123*m),math.radians(90.5*m)]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(3.24),math.radians(-5*m),math.radians(46.3*m)]
        pb.location = [0.001553*m,-0.009744,0.071087]
        
        pb = ob.pose.bones.get("pinky2."+side)
        pb.rotation_euler = [math.radians(0.0524),math.radians(-2.63*m),math.radians(79.5*m)]
        
        pb = ob.pose.bones.get("pinky3."+side)
        pb.rotation_euler = [math.radians(-3.17),math.radians(-6.66*m),math.radians(77.7*m)]
        
    if (a==5):
        #suchi
        
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(6.58),math.radians(-8.7*m),math.radians(-74.1*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(-43.2),math.radians(-8.87*m),math.radians(16.4*m)]
        pb.location = [0.005732*m,-0.049,-0.0969]
        
        pb = ob.pose.bones.get("thumb2."+side)
        pb.rotation_euler = [math.radians(-24.3),math.radians(-22*m),math.radians(4.75*m)]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(0.267),math.radians(-2.56*m),math.radians(-11.9*m)]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(0.152),math.radians(0.603*m),math.radians(28.2*m)]
        
        pb = ob.pose.bones.get("middle2."+side)
        pb.rotation_euler = [math.radians(2.38),math.radians(3.41*m),math.radians(70*m)]
        
        pb = ob.pose.bones.get("middle3."+side)
        pb.rotation_euler = [math.radians(2.67),math.radians(3.83*m),math.radians(69.7*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(-0.251),math.radians(-1.24*m),math.radians(22.9*m)]
        pb.location = [-0.009325*m,-0.010571,0.039031]
        
        pb = ob.pose.bones.get("ring2."+side)
        pb.rotation_euler = [math.radians(6.65),math.radians(-10.6*m),math.radians(64.2*m)]
        
        pb = ob.pose.bones.get("ring3."+side)
        pb.rotation_euler = [math.radians(18.7),math.radians(-14.3*m),math.radians(57.8*m)]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(9.06),math.radians(0.45*m),math.radians(14.1*m)]
        pb.location = [-0.014573*m,-0.019191,0.056904]
        
        pb = ob.pose.bones.get("pinky2."+side)
        pb.rotation_euler = [math.radians(11),math.radians(-13*m),math.radians(68.2*m)]
        
        pb = ob.pose.bones.get("pinky3."+side)
        pb.rotation_euler = [math.radians(47.5),math.radians(55.9*m),math.radians(102*m)]
        
    if a==6:
        #Kapittha
        
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(6.58),math.radians(-8.7*m),math.radians(-74.1*m)]
        
        pb = ob.pose.bones.get("thumb1."+side)
        pb.rotation_euler = [math.radians(-24.4),math.radians(-25.6*m),math.radians(-10.7*m)]
        pb.location = [0.038993*m,0.021214,-0.043467]
        
        pb = ob.pose.bones.get("thumb2."+side)
        pb.rotation_euler = [math.radians(-13.6),math.radians(-32.4*m),math.radians(6.33*m)]
        
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(-1.49),math.radians(-9.17*m),math.radians(-10.4*m)]
        
        pb = ob.pose.bones.get("index2."+side)
        pb.rotation_euler = [math.radians(3.71),math.radians(6.26*m),math.radians(61.3*m)]
        
        pb = ob.pose.bones.get("index3."+side)
        pb.rotation_euler = [math.radians(5.45),math.radians(8.7*m),math.radians(64.2*m)]
        
        pb = ob.pose.bones.get("middle1."+side)
        pb.rotation_euler = [math.radians(0.724),math.radians(1.15*m),math.radians(64.2*m)]
        
        pb = ob.pose.bones.get("middle2."+side)
        pb.rotation_euler = [math.radians(2.38),math.radians(3.41*m),math.radians(70*m)]
        
        pb = ob.pose.bones.get("middle3."+side)
        pb.rotation_euler = [math.radians(2.67),math.radians(3.83*m),math.radians(69.7*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(-1.27),math.radians(-2.55*m),math.radians(53.1*m)]
        pb.location = [-0.009325*m,-0.010571,0.039031]
        
        pb = ob.pose.bones.get("ring2."+side)
        pb.rotation_euler = [math.radians(6.65),math.radians(-10.6*m),math.radians(64.2*m)]
        
        pb = ob.pose.bones.get("ring3."+side)
        pb.rotation_euler = [math.radians(18.7),math.radians(-14.3*m),math.radians(57.8*m)]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(7.02),math.radians(-3.01*m),math.radians(47.1*m)]
        pb.location = [-0.014573*m,-0.019191,0.056904]
        
        pb = ob.pose.bones.get("pinky2."+side)
        pb.rotation_euler = [math.radians(11),math.radians(-13*m),math.radians(68.2*m)]
        
        pb = ob.pose.bones.get("pinky3."+side)
        pb.rotation_euler = [math.radians(47.5),math.radians(55.9*m),math.radians(102*m)]
        
    if a==7:
        #Alapadma
        print(side)
        print(m)
        pb = ob.pose.bones.get("index1."+side)
        pb.rotation_euler = [math.radians(1.86),math.radians(-6.54*m),math.radians(-31.8*m)]
        
        pb = ob.pose.bones.get("ring1."+side)
        pb.rotation_euler = [math.radians(-0.764),math.radians(-2.07*m),math.radians(40.5*m)]
        
        pb = ob.pose.bones.get("pinky1."+side)
        pb.rotation_euler = [math.radians(-5.21),math.radians(-6.82*m),math.radians(74.7*m)]
        
def hx(a,side):
    pb = ob.pose.bones.get("upperarm."+side)

    if a==4:
        pb.rotation_euler = [math.radians(86.4),0,0]
    if a==3:
        pb.rotation_euler = [math.radians(60),0,0] 
    if a==2:
        pb.rotation_euler = [math.radians(45),0,0]
    if a==1:
        pb.rotation_euler = [math.radians(30),0,0]
    if a==0:
        pb.rotation_euler = [0,0,0]
    if a==-1:
        pb.rotation_euler = [math.radians(-30),0,0]
    if a==-2:
        pb.rotation_euler = [math.radians(-45),0,0]
    if a==-3:
        pb.rotation_euler = [math.radians(-60),0,0]
        
def hy(a,m):
    if m==1:
        pb = ob.pose.bones.get("upperarm.r")
    else:
        pb = ob.pose.bones.get("upperarm.l")
        
    if a==4:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(86.4*m)]
    if a==3:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(60*m)] 
    if a==2:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(45*m)]
    if a==1:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(30*m)]
    if a==0:
        pb.rotation_euler = [pb.rotation_euler[0],0,0]
    if a==-1:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(-30*m)]
    if a==-2:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(-45*m)]
    if a==-3:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(-60*m)]
    if a==-4:
        pb.rotation_euler = [pb.rotation_euler[0],0,math.radians(-86.4*m)]
        
def hz(a,b):
    """
    pb = ob.pose.bones.get("pelvis")
    if a==-1 and b!=-1:
        pb.rotation_euler = [0,180,0]
    if a==-1 and b==-1:
        pb.rotation_euler = [0,0,0]
        #move camera to the back
    """
        
        
def el(a,side):
    pb = ob.pose.bones.get("forearm."+side)
    if a==2:
        pb.rotation_euler = [math.radians(90),0,0]
    if a==1:
        pb.rotation_euler = [math.radians(45),0,0]
    if a==0:
        pb.rotation_euler = [0,0,0]
    if a==3:
        pb.rotation_euler = [math.radians(135),0,0]
        
def wr(a,m):
    #here, we are overriding the palm angles given by the bit number for hastas (hand sign)
    """
    if m==1:
        side = "r"
    else:
        side = "l"
    if a==-1:
        pb = ob.pose.bones.get("forearm."+side)
        pb.rotation_euler = [pb.rotation_euler[0]+math.radians(-48.2),pb.rotation_euler[1]+math.radians(83.8+m),pb.rotation_euler[2]+math.radians(-46+m)]
        pb = ob.pose.bones.get("palm."+side)
        pb.rotation_euler = [math.radians(-116),math.radians(75.2+m),math.radians(-122+m)]
    """
    
def pm(a,m):
    #here, we are overriding the palm angles given by the bit number for hastas (hand sign)
    """
    if m==1:
        side = "r"
    else:
        side = "l"
        
    pb = ob.pose.bones.get("palm."+side) 
    
    if a==1:
        pb.rotation_euler = [pb.rotation_euler[0]+math.radians(3.04),pb.rotation_euler[1]+math.radians(6.78*m),pb.rotation_euler[2]+math.radians(48.3*m)]
    if a==-1:
        pb.rotation_euler = [pb.rotation_euler[0]+math.radians(6.33),pb.rotation_euler[1]+math.radians(-8.63*m),pb.rotation_euler[2]+math.radians(-72.5*m)]
    """
    
def sj(a,m):
    if m==1:
        side = "r"
    else:
        side = "l"
        
    if a==1:
        pb = ob.pose.bones.get("upperarm."+side)
        pb.rotation_euler = [pb.rotation_euler[0]+math.radians(-0.161),pb.rotation_euler[1]+math.radians(-0.886*m),pb.rotation_euler[2]+math.radians(20.6*m)]
        pb = ob.pose.bones.get("shoulder."+side)
        pb.rotation_euler = [math.radians(-1.08),math.radians(6.08*m),math.radians(-20*m)]
        
    if a==-1:
        pb = ob.pose.bones.get("upperarm."+side)
        pb.rotation_euler = [pb.rotation_euler[0]+math.radians(-0.022),pb.rotation_euler[1]+math.radians(0.332*m),pb.rotation_euler[2]+math.radians(-7.58*m)]
        pb = ob.pose.bones.get("shoulder."+side)
        pb.rotation_euler = [math.radians(-0.127),math.radians(-2.12*m),math.radians(6.84*m)]
        
def an(a,b):
    if b==1 or b==2:
        #aramandi/ardhamandalam or mandi
        pb = ob.pose.bones.get("pelvis")
        pb.location = [0,-1.2362,0]
        pb = ob.pose.bones.get("iklegtarget.r")
        pb.rotation_euler = [math.radians(-38.6),math.radians(12.9),math.radians(46.9)]
        pb.location = [-0.41,0,0]
        pb = ob.pose.bones.get("iklegtarget.l")
        pb.rotation_euler = [math.radians(-38.6),math.radians(-12.9),math.radians(-46.9)]
        pb.location = [0.41,0,0]
        if b==2:
            pb = ob.pose.bones.get("pelvis")
            pb.location = [0,-2.2,0]
            pb = ob.pose.bones.get("iklegpole.r")
            pb.location = [1,0,0]
            pb = ob.pose.bones.get("iklegpole.l")
            pb.location = [-1,0,0]
    elif b==0:
        #sthanaka
        pb = ob.pose.bones.get("iklegtarget.r")
        pb.rotation_euler = [0,0,math.radians(-9)]
        pb.location = [-0.51,0,0]
        pb = ob.pose.bones.get("iklegtarget.l")
        pb.rotation_euler = [0,0,math.radians(9)]
        pb.location = [0.51,0,0]
        pb = ob.pose.bones.get("iklegpole.r")
        pb.location = [-0.2,0,0]
        pb = ob.pose.bones.get("iklegpole.l")
        pb.location = [0.2,0,0]

def lx(a,m):
        if m==1:
            side = "r"
        else:
            side = "l"
        pb = ob.pose.bones.get("iklegpole."+side)
        if a==3:
            pb.location = [pb.location[0]-1.8*m,pb.location[1]+0,pb.location[2]+0]
        if a==2:
            pb.location = [pb.location[0]-0.8*m,pb.location[1]+0,pb.location[2]+0]
        if a==1:
            pb.location = [pb.location[0]-0.35*m,pb.location[1]+0,pb.location[2]+0]
        if a==0:
            pb.location = [pb.location[0]+5.41*m,pb.location[1]+0,pb.location[2]+0]
        if a==-2:
            pb.location = [pb.location[0]+24.15*m,pb.location[1]+0,pb.location[2]+0]

def ly(a,m):
        if m==1:
            side = "r"
        else:
            side = "l"
        pb = ob.pose.bones.get("iklegtarget."+side)
        if a==1:
            pb.location = [pb.location[0]+0,pb.location[1]+0,pb.location[2]+0.25]
        if a==0:
            pb.location = [pb.location[0]+0,pb.location[1]+0,pb.location[2]+0]

        

n = np.genfromtxt('C:/Users/Sidd/Documents/inputanim.txt', delimiter=' ')
no_of_poses=n.size/30
frame_no = 0
print(n)
print(no_of_poses)
"""
name = "Bone"
pb = ob.pose.bones.get(name)

"""

#generating poses:
bpy.ops.object.mode_set(mode='POSE')
ob = bpy.data.objects["Armature"]

print(ob.type)
ob.rotation_mode = 'XYZ'

i = 0

for i in range(int(no_of_poses)):
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.rot_clear()
    bpy.ops.pose.loc_clear()

    ## 1 Sb_M

    a = n[i][0]
    pb = ob.pose.bones.get("head")

    if a==-1 :
        pb.rotation_euler = [math.radians(42.3),0,0]
        
    if a==1 :
        if n[i][1]==1 :
            pb.rotation_euler = [math.radians(-0.662),math.radians(1.6),math.radians(45)]
        elif n[i][1]==-1 :
            pb.rotation_euler = [math.radians(-0.662),math.radians(-1.6),math.radians(-45)]
            
    if a==2 :
        pb.rotation_euler = [math.radians(-30),math.radians(-0.21),math.radians(0.0478)]
            
    print(pb.rotation_euler[0])

    ## 2 Sb_O

    a = n[i][1]
    pb = ob.pose.bones.get("head")

    if a==1 :
        pb.rotation_euler = [+pb.rotation_euler[0],math.radians(-60)+pb.rotation_euler[1],0+pb.rotation_euler[2]] 
        
    if a==-1 :
        pb.rotation_euler = [+pb.rotation_euler[0],math.radians(60)+pb.rotation_euler[1],0+pb.rotation_euler[2]] 
        
    ## 3 R_Fg
    fingers(n[i][2],1)
    ## 4 R_HX
    hx(n[i][3],"r")
    ## 5 R_HY
    hy(n[i][4],1)
    ## 6 R_HZ
    hz(n[i][5],n[i][24])
    ## 7 R_El
    el(n[i][6],"r")
    ## 8 R_WR
    wr(n[i][7],1)
    ## 9 R_Pm
    pm(n[i][8],1)
    ## 10 R_Sj
    sj(n[i][9],1)
    ## 11 L_Fg
    fingers(n[i][10],-1)
    ## 12 L_HX
    hx(n[i][11],"l")
    ## 13 L_HY
    hy(n[i][12],-1)
    ## 14 L_HZ
    hz(n[i][13],n[i][29])
    ## 15 L_El
    el(n[i][14],"l")
    ## 16 L_WR
    wr(n[i][15],-1)
    ## 17 L_Pm
    pm(n[i][16],-1)
    ## 18 L_Sj
    sj(n[i][17],-1)
    ## 19 W_tw

    a = n[i][18]

    pb = ob.pose.bones.get("spine")
    if a==2:
        pb.rotation_euler = [0,math.radians(-85),0]
    if a==1:
        pb.rotation_euler = [0,math.radians(-45),0]
    if a==0:
        pb.rotation_euler = [0,0,0]
    if a==-1:
        pb.rotation_euler = [0,math.radians(45),0]
        
    ## 20 W_be

    #not sure what to do here

    ## 21 R_An and 22 R_Kn

    #can find anything for the ankle positions...
    an(n[i][20],n[i][21])

    ## 23 R_LX
    lx(n[i][22],1)
    ## 24 R_LY
    ly(n[i][23],1)
    ## 25 R_LZ
    ## 26 R_An
    ## 27 R_Kn
    ## 28 R_LX
    lx(n[i][22],-1)
    ## 29 R_LY
    ly(n[i][23],-1)
    ## 30 R_LZ
    
    for bone in ob.pose.bones:
        bone.keyframe_insert('rotation_euler', frame=frame_no)
        bone.keyframe_insert('location', frame=frame_no)
        
    frame_no+=3
    
    for bone in ob.pose.bones:
        bone.keyframe_insert('rotation_euler', frame=frame_no)
        bone.keyframe_insert('location', frame=frame_no)
        
    frame_no+=10