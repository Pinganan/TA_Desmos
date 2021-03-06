import matplotlib.pyplot as plt
import numpy as np

def f1(x1):
    return -100+x1*0
x1=np.linspace(-100,100,1000)
y1=f1(x1)
plt.plot(x1,y1,'k-')

def f2(x2):
    return 10*x2+900
x2=np.linspace(-100,-92,1000)
y2=f2(x2)
plt.plot(x2,y2,'k-')

def f3(x3):
    return -10*x3+900
x3=np.linspace(92,100,1000)
y3=f3(x3)
plt.plot(x3,y3,'k-')

def f4(x4):
    return -20+x1*0
x4=np.linspace(-92,92,1000)
y4=f4(x4)
plt.plot(x4,y4,'k-')

def f5(x5):
    return 0.01*x5**2-200
x5=np.linspace(-100,100,1000)
a1=[]
a2=[]
for i in x5:
    if f5(i)>-102:
        a1.append(f5(i))
        a2.append(i)

plt.plot(a2,a1,'k-')

def f6(x6):
    return -102+x6*0
x6=np.linspace(-98.995,98.995,1000)
y6=f6(x6)
plt.plot(x6,y6,'k-')

import matplotlib.pyplot as plt
import numpy as np
def fy(a,b,t,r):
    def f1(y):
        return a*y+b
    y=np.linspace(t,r,1000)
    x=f1(y)
    plt.plot(x,y,'k-')


def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')


def yp1(a,b,c,w,t,r):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    p=[]
    for i in x:
        if f1(i)<=r:
            l.append(i)
            p.append(f1(i))
    plt.plot(l,p,'k-')




def yp2(a,b,c,w,t,r):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    p=[]
    for i in x:
        if f1(i)>=r:
            l.append(i)
            p.append(f1(i))
    plt.plot(l,p,'k-')


def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')




def cri(a,b,r):
    t=np.arange(0,2*np.pi,0.001)
    x=a+r*np.cos(t)
    y=b+r*np.sin(t)
    plt.plot(x,y,'k-')


def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')

fy(0,-92,-17,80)
fy(0,92,-17,80)
fy(0,-90,-15,78)
fy(0,90,-15,78)
fy(0,80,0,70)
fy(0,-80,0,70)
fx(0,80,-92,92)
fx(0,-17,-92,-78)
fx(0,-17,78,92)
fx(0,-17,-69.5,69.5)
fx(0,-10,-90,90)
fx(0,78,-90,90)
fx(0,0,-80,80)
fx(0,70,-80,80)
yp1(1.5,90.5,-20,-100,-90.6,-17)
yp1(1.5,-90.5,-20,90.6,100,-17)
yp2(-3,78.6,-16,-78.023,0,-20)
yp2(-3,-78.6,-16,0,78.023,-20)
yp3(-4,70,-16,-70,100,-20,-17)
yp3(-4,-70,-16,0,70,-20,-17)
yp0(10,89.4,-19,-90.029,-89.847)
yp0(10,-89.4,-19,89.847,90.029)
cri(-85,-14,1)
cri(85,-14,1)
cri(0,75,2)
cri(0,75,1/2)
cri(10,75,(1/3)**(1/2))
cri(-6,75,1)

def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')

def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')

fx(0,-97,-30,30)
fx(10,209.6,-30.59,-28.58)
fx(-10,209.6,28.58,30.59)
fx(0,-76.2,-28.58,28.58)
yp0(2,30,-97,-30.6,-29.99)
yp0(2,-30,-97,29.99,30.6)

def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')

def fxl(a,b,t,r,q,p):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,10000)
    l=[]
    k=[]
    for i in x:
        if q<=fun(i)<=p:
            l.append(i)
            k.append(fun(i))
    plt.plot(l,k,'k-')


fxl(10,855,-90,-80,-25,-22.65)

fx(0,-22.65,-87.765,-79)
fx(0,-22.65,-77,-68)
fx(0,-22.65,-66,-57)
fx(0,-22.65,-55,-46)
fx(0,-22.65,-44,-35)
fx(0,-22.65,-33,-24)
fx(0,-22.65,-22,-14)
fx(0,-22.65,-12,-3)
fx(0,-22.65,-1,8)
fx(0,-22.65,10,19)
fx(0,-22.65,21,30)
fx(0,-22.65,32,41)
fx(0,-22.65,43,52)
fx(0,-22.65,54,63)
fx(0,-22.65,65,74)
fx(0,-22.65,76,87.765)

fxl(10,767,-100,0,-25,-22.65)
fxl(10,657,-100,0,-25,-22.65)
fxl(10,638,-100,0,-25,-22.65)
fxl(10,748,-100,0,-25,-22.65)
fxl(10,547,-100,0,-25,-22.65)
fxl(10,527,-100,0,-25,-22.65)
fxl(10,437,-100,0,-25,-22.65)
fxl(10,417,-100,0,-25,-22.65)
fxl(10,327,-100,0,-25,-22.65)
fxl(10,307,-100,0,-25,-22.65)
fxl(10,217,-100,0,-25,-22.65)
fxl(10,197,-100,0,-25,-22.65)
fxl(10,97,-100,0,-25,-22.65)
fxl(10,117,-100,0,-25,-22.65)
fxl(10,7,-100,0,-25,-22.65)

fx(0,-25,-88,-79.2)
fx(0,-25,-77.3,-68.2)
fx(0,-25,-66.3,-57.2)
fx(0,-25,-55.2,-46.2)
fx(0,-25,-44.2,-35.2)
fx(0,-25,-33.2,-24.2)
fx(0,-25,-22.2,-14.2)
fx(0,-25,-12.2,-3.2)
fxl(-10,-905,-100,0,-25.5,-25)
fxl(-10,-817,-100,0,-25.5,-25)
fxl(-10,-798,-100,0,-25.5,-25)
fxl(-10,-707,-100,0,-25.5,-25)
fxl(-10,-688,-100,0,-25.5,-25)
fxl(-10,-597,-100,0,-25.5,-25)
fxl(-10,-577,-100,0,-25.5,-25)
fxl(-10,-487,-100,0,-25.5,-25)
fxl(-10,-467,-100,0,-25.5,-25)
fxl(-10,-377,-100,0,-25.5,-25)
fxl(-10,-357,-100,0,-25.5,-25)
fxl(-10,-267,-100,0,-25.5,-25)
fxl(-10,-247,-100,0,-25.5,-25)
fxl(-10,-167,-100,0,-25.5,-25)
fxl(-10,-147,-100,0,-25.5,-25)
fxl(-10,-57,-100,0,-25.5,-25)
fx(0,-25.5,-87.95,-79.25)
fx(0,-25.5,-77.15,-68.15)
fx(0,-25.5,-66.25,-57.15)
fx(0,-25.5,-55.15,-46.15)
fx(0,-25.5,-44.15,-35.15)
fx(0,-25.5,-33.15,-24.15)
fx(0,-25.5,-22.15,-14.15)
fx(0,-25.5,-12.15,-3.15)
fxl(-10,-812.5,-100,0,-23.25,-22.75)
fxl(-10,-702.5,-100,0,-23.25,-22.75)
fxl(-10,-592.5,-100,0,-23.25,-22.75)
fxl(-10,-482.5,-100,0,-23.25,-22.75)
fxl(-10,372.5,-100,0,-23.25,-22.75)
fxl(-10,-262.5,-100,0,-23.25,-22.75)
fxl(-10,-162.5,-100,0,-23.25,-22.75)
fxl(-10,-52.5,-100,0,-23.25,-22.75)

fxl(10,766,-100,0,-25.5,-23.2)
fxl(10,656,-100,0,-25.5,-23.2)
fxl(10,546,-100,0,-25.5,-23.2)
fxl(10,436,-100,0,-25.5,-23.2)
fxl(10,326,-100,0,-25.5,-23.2)
fxl(10,216,-100,0,-25.5,-23.2)
fxl(10,116,-100,0,-25.5,-23.2)
fxl(10,6,-100,0,-25.5,-23.2)

def fa1(a,b,m,n,q,p):
    def fa(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fa(i)<=p:
            x1.append(i)
            y1.append(fa(i))
    plt.plot(x1,y1,'k-')
    
def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    y=fb(x)
    plt.plot(x,y,'k-')


fa1(-10,855,-100,200,-25,-22.65)
fa1(20,-2,-50,50,-25,-22.65)
fa1(-10,57,0,50,-25,-22.65)
fa1(-10,77.5,-200,200,-25,-22.65)
fa1(-10,167,-200,200,-25,-22.65)
fa1(-10,187.5,-200,200,-25,-22.65)
fa1(-10,277,-200,200,-25,-22.65)
fa1(-10,297.5,-200,200,-25,-22.65)
fa1(-10,387,-200,200,-25,-22.65)
fa1(-10,407.5,-200,200,-25,-22.65)
fa1(-10,497,-200,200,-25,-22.65)
fa1(-10,517.5,-200,200,-25,-22.65)
fa1(-10,607,-200,200,-25,-22.65)
fa1(-10,627.5,-200,200,-25,-22.65)
fa1(-10,717,-200,200,-25,-22.65)
fa1(-10,737.5,-200,200,-25,-22.65)

fb1(0,-25,-1.15,8.2)
fb1(0,-25,10.25,19.2)
fb1(0,-25,21.25,30.2)
fb1(0,-25,32.25,41.2)
fb1(0,-25,43.25,52.2)
fb1(0,-25,54.25,63.2)
fb1(0,-25,65.25,74.2)
fb1(0,-25,76.25,88)

fa1(10,-905,-500,500,-25.5,-25)
fa1(10,-787,-500,500,-25.5,-25)
fa1(10,-767,-500,500,-25.5,-25)
fa1(10,-677,-500,500,-25.5,-25)
fa1(10,-657,-500,500,-25.5,-25)
fa1(10,-567,-500,500,-25.5,-25)
fa1(10,-547,-500,500,-25.5,-25)
fa1(10,-457,-500,500,-25.5,-25)
fa1(10,-437,-500,500,-25.5,-25)
fa1(10,-347,-500,500,-25.5,-25)
fa1(10,-327,-500,500,-25.5,-25)
fa1(10,-237,-500,500,-25.5,-25)
fa1(10,-217,-500,500,-25.5,-25)
fa1(10,-127,-500,500,-25.5,-25)
fa1(10,-107,-500,500,-25.5,-25)
fa1(-10,-36,-500,500,-25.5,-25)

fb1(0,-25.5,-1.05,8.15)
fb1(0,-25.5,10.15,19.15)
fb1(0,-25.5,21.15,30.15)
fb1(0,-25.5,32.15,41.15)
fb1(0,-25.5,43.15,52.15)
fb1(0,-25.5,54.15,63.15)
fb1(0,-25.5,65.15,74.15)
fb1(0,-25.5,76.15,87.15)

fa1(10,-782.75,-500,500,-23.15,-22.65)
fa1(10,-672.75,-500,500,-23.15,-22.65)
fa1(10,-562.75,-500,500,-23.15,-22.65)
fa1(10,-452.75,-500,500,-23.15,-22.65)
fa1(10,-342.75,-500,500,-23.15,-22.65)
fa1(10,-232.75,-500,500,-23.15,-22.65)
fa1(10,-122.75,-500,500,-23.15,-22.65)

fa1(-10,736,-500,500,-25.5,-23.15)
fa1(-10,626,-500,500,-25.5,-23.15)
fa1(-10,516,-500,500,-25.5,-23.15)
fa1(-10,406,-500,500,-25.5,-23.15)
fa1(-10,296,-500,500,-25.5,-23.15)
fa1(-10,186,-500,500,-25.5,-23.15)
fa1(-10,76,-500,500,-25.5,-23.15)

def fa1(a,b,m,n,q,p):
    def fa(x):
        return a*x+b
    x=np.linspace(m,n,1000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fa(i)<=p:
            x1.append(i)
            y1.append(fa(i))
    plt.plot(x1,y1,'k-')

def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,1000)
    y=fb(x)
    plt.plot(x,y,'k-')

def fc1(a,b,c,m,n):
    def fc(x):
        return a*(x+b)**2+c
    x=np.linspace(m,n,1000)
    y=fc(x)
    plt.plot(x,y,'k-')

fa1(10,200,-40,0,-70,-64)
fa1(-10,200,40,0,-70,-64)

fb1(0,-70,-27,27)
fb1(0,-64,-26.4,26.4)
fb1(0,-71,-26.482,26.5)

fc1(1,25.775,-71.5,-27,-26.48)
fc1(1,-25.775,-71.5,26.48,27)

def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    y=fb(x)
    plt.plot(x,y,'k-')

def fa1(a,b,m,n,q,p):
    def fa(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fa(i)<=p:
            x1.append(i)
            y1.append(fa(i))
    plt.plot(x1,y1,'k-')

fb1(0,-64,69,80)
fb1(0,-64,82,92)

fa1(-10,236,-200,200,-70,-64)
fa1(-10,346,-200,200,-70,-64)
fa1(-10,366,-200,200,-70,-64)
fa1(-10,476,-200,200,-70,-64)
fa1(-10,496,-200,200,-70,-64)
fa1(-10,606,-200,200,-70,-64)

fb1(0,-70,30.6,41.6)
fb1(0,-70,43.6,54.6)
fb1(0,-70,56.6,67.6)
fb1(0,-70,69.6,80.6)
fb1(0,-70,82.6,92.6)

fa1(-10,234,-200,200,-71,-65)
fa1(10,-364,-200,200,-65,-64)

fa1(10,-376,-200,200,-71,-70)
fa1(10,-486,-200,200,-71,-70)
fa1(10,-506,-200,200,-71,-70)
fa1(10,-616,-200,200,-71,-70)
fa1(10,-636,-200,200,-71,-70)
fa1(10,-746,-200,200,-71,-70)
fa1(10,-766,-200,200,-71,-70)
fa1(10,-876,-200,200,-71,-70)
fa1(10,-896,-200,200,-71,-70)
fa1(10,-996,-200,200,-71,-70)

fa1(10,-494,-200,200,-65,-64)
fa1(10,-624,-200,200,-65,-64)
fa1(10,-754,-200,200,-65,-64)
fa1(10,-884,-200,200,-65,-64)

fa1(-10,234,-200,200,-71,-65)
fa1(-10,364,-200,200,-71,-65)
fa1(-10,494,-200,200,-71,-65)
fa1(-10,624,-200,200,-71,-65)
fa1(-10,754,-200,200,-71,-65)

fb1(0,-71,30.5,41.5)
fb1(0,-71,43.5,54.5)
fb1(0,-71,56.5,67.5)
fb1(0,-71,69.5,80.5)
fb1(0,-71,82.5,92.5)

fb1(0,-64,30,41)
fb1(0,-64,43,54)
fb1(0,-64,56,67)

fa1(-10,626,-200,200,-70,-64)
fa1(-10,856,-200,200,-70,-64)
fa1(-10,756,-200,200,-70,-64)
fa1(-10,736,-200,200,-70,-64)

fb1(0,-66.95,56.275,67.275)
fb1(0,-66.95,69.275,80.275)
fb1(0,-66.95,82.275,92.275)
fb1(0,-67.15,56.315,67.315)
fb1(0,-67.15,69.315,80.315)
fb1(0,-67.15,82.315,92.315)

def cri(a,b,r):
    t=np.arange(0,2*np.pi,0.001)
    x=a+r*np.cos(t)
    y=b+r*np.sin(t)
    plt.plot(x,y,'k-')


def circle(xc,yc,z,x1,x2,y1,y2): 
  x = np.linspace(x1, x2, 1000) 
  y = np.linspace(y1, y2, 1000) 
  x,y=np.meshgrid(x,y)
  plt.contour(x,y,(x-xc)**2+(y-yc)**2,[z],colors='black')

def circle1(xc,yc,z,x1,x2,y1,y2,a,b): 
  x = np.linspace(x1, x2, 1000) 
  y = np.linspace(y1, y2, 1000) 
  x,y=np.meshgrid(x,y)
  plt.contour(x,y,a*((x-xc))**2+b*((y-yc))**2,[z],colors='black')


def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')


def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')

def fy(a,b,t,r):
    def f1(y):
        return a*y+b
    y=np.linspace(t,r,1000)
    x=f1(y)
    plt.plot(x,y,'k-')

def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')
def ys(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**3+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')

circle(0,40,220,-50,-2.04,38.618,100)
circle(0,40,220,2.04,50,38.618,100)
yp0(1/20,0,20,-9.33,12.432)
yp3(1/5,0,-5,-14.8,-14.2,28.333,38.618)
yp3(-50,-8,23.5,-50,8,16,50)
yp3(-50,8,23.5,-8,50,16,50)
yp0(1/200,-10,14,-8.75,0)
yp3(-2,0,14.5,0,50,11.5,50)
yp0(-1/5,8,16.8,-8.98,-8)
cri(-1,12,1/5**(1/2))
cri(2,12.5,1/7**(1/2))
cri(-1,-12,1/10**(1/2))
cri(2,12.5,1/12**(1/2))
yp3(-1,25,10,-50,-24.5,0,50)
yp3(-1,-25,10,24,50,0,50)
yp0(-1/95,0,16.7,-18.758,-12.738)
yp0(-1/95,0,16.7,8,11.5)
yp0(-1/7,-8,17,8,11)
yp0(1/250,10,13,1,10)
yp0(-1/5,-22,12,21.5,25.191)
yp3(-1,-25,10,20,24,2,7)
fx(-2/5,21,12.586,18.75)
yp0(-1/10,-12,16,10.823,12.586)
yp0(-1,-21.5,12.5,21.326,22.214)
yp0(1/2,-20.955,12.4,19.783,21.327)
yp0(-1/2.5,-18.75,13.5,18.75,19.828)
ys(1/112,18,13.5,-25,-16)
yp3(-1,25,10,-23,50,0.5,50)
circle1(1,12,100,-15.478,-12.85,10,100,1/3,2)
circle1(1,12,100,7.685,17.658,12,100,1/3,2)
yp3(100,1,4,-50,50,0,11.649)
yp3(100,-2,6,0,50,0,12.216)
fy(0,-1,3,4)
fy(0,2,5,6)

def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,10000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,10000)
    y=f1(x)
    plt.plot(x,y,'k-')


def yp4(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**3+c
    x=np.linspace(w,t,10000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def yp5(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**3+c
    x=np.linspace(w,t,10000)
    y=f1(x)
    plt.plot(x,y,'k-')

yp0(1/2,-22,12,14.971,21.095)
yp3(1/8,0,55,-200,200,0,58)
yp3(1/6,0,54,-200,200,54.692,58)
yp3(1/2,19.62,30,-20,0,32.142,42.493)
yp0(1/2,17.5,32.242,-17.5,-15)
yp0(3,19,13,-19,-16.43)
yp0(2,10,0,-14.204,-10)
yp3(-1,0,41,-200,200,40,58)

yp5(1/7,4,36,-3,-0.929)

yp4(1/2,4,36,-200,200,36.1,40)

yp0(5,7,-3,-9.8,-7.775)
yp0(4,-18,0,14.832,16.031)
yp0(1,-16,15,10.98,14.895)
yp0(1/40,-10,38,0.984,11.2)
yp0(1/20,10,35,-9.757,-2.454)
def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,10000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,10000)
    y=f1(x)
    plt.plot(x,y,'k-')

def yp4(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**3+c
    x=np.linspace(w,t,10000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def yp5(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**3+c
    x=np.linspace(w,t,10000)
    y=f1(x)
    plt.plot(x,y,'k-')

def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,1000)
    y=fb(x)
    plt.plot(x,y,'k-')

def fd1(a,b,m,n):
    def fd(y):
        return a*y+b
    y=np.linspace(m,n,1000)
    x=fd(y)
    plt.plot(x,y,'k-')

yp3(-1,0,31,-500,500,30.5,100)

fd1(0,10,25,31)

yp0(-1/200,-10,31,0.66,10)
yp0(-1/200,10,31,-9.608,-0.66)
yp0(-1/12,-14,32,10,11.921)
yp0(1/40,0,22,-4,4)
yp0(1/50,0,23,-6,6)
yp0(1/65,0,24,-4,4)
yp0(1/100,0,25.5,-8,8)
yp0(-1/200,0,27,-5,5)
yp0(-1/300,0,28,-4,4)
yp0(-1/200,-10,29.5,0,6)
yp0(-1/200,10,29.5,-6,0)

def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')

def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def yp3f(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')
    plt.fill(l,k,"k",alpha=0.5)

def crif(a,b,r):
    t=np.arange(0,2*np.pi,0.001)
    x=a+r*np.cos(t)
    y=b+r*np.sin(t)
    plt.plot(x,y,'k-')
    plt.fill(x,y,"k")

yp0(-1/20,-5,34,1.697,8.8)
yp0(-1/20,-5,36,1.697,8.8)
yp0(-1/20,5,36,-5,-1.697)
yp0(-1/20,5,34,-8.8,-1.697)
yp3(1/2,5,28,-20,20,30.697,33.455)
yp3(1/2,-5,28,-20,20,30.967,33.455)
yp3f(1.5,-5,28,-20,20,30.946,33.714)
yp3f(1.5,5,28,-20,20,30.946,33.714)
crif(5,33,1/2**(1/2))
crif(-5,33,1/2**(1/2))

def fy(a,b,t,r):
    def f1(y):
        return a*y+b
    y=np.linspace(t,r,1000)
    x=f1(y)
    plt.plot(x,y,'k-')


def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')


def yp0(a,b,c,w,t):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    y=f1(x)
    plt.plot(x,y,'k-')

def yp3(a,b,c,w,t,r,p):
    def f1(x):
        return a*(x+b)**2+c
    x=np.linspace(w,t,1000)
    l=[]
    k=[]
    for i in x:
        if r<=f1(i)<=p:
            l.append(i)
            k.append(f1(i))
    plt.plot(l,k,'k-')

def circle(xc,yc,z,x1,x2,y1,y2): 
  x = np.linspace(x1, x2, 1000) 
  y = np.linspace(y1, y2, 1000) 
  x,y=np.meshgrid(x,y)
  plt.contour(x,y,(x-xc)**2+(y-yc)**2,[z],colors='black')

fx(0,50,10.954,28)
fx(0,50,-28,-10.954)
fy(0,30,0,48)
fy(0,-30,0,48)

circle(-28,48,4,-100,-28,48,100)
circle(28,48,4,28,100,48,100)

yp0(1/2,-60,-4,47.834,57.172)
yp3(1,-72,-10,-100,72,12,52)
yp3(1,-72,-10,-100,72,58,64)
yp0(1/2,75,-5,-71.838,-62.753)
fy(0,1,55.5,70)
fy(0,-1,55.5,70)
yp3(3,78,-2,-78,100,0,15)
yp3(3,78,-2,-78,100,60,70)
fx(0,25,-67.254,-30)
fx(0,25,30,52.384)
fx(0,27,30,52.126)
fx(0,24.5,30,52.126)
fx(0,20,30,52.126)
fx(0,20,-67.254,-30)

circle(-60,70,200,-63.917,-45.858,0,70)

def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    y=fb(x)
    plt.plot(x,y,'k-')

def fa1(a,b,m,n,q,p):
    def fa(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fa(i)<=p:
            x1.append(i)
            y1.append(fa(i))
    plt.plot(x1,y1,'k-')

fa1(10,855,-200,200,-62,-54)

fb1(0,-54,-90.9,-58)
fb1(0,-54,-5,5)
fb1(0,-54,-17,-7)
fb1(0,-54,-29,-19)
fb1(0,-54,-41,-31)
fb1(0,-54,-54,-43)

fa1(10,526,-200,200,-62,-54)
fa1(10,485,-200,200,-62,-54)
fa1(10,376,-200,200,-62,-54)
fa1(10,355,-200,200,-62,-54)
fa1(10,256,-200,200,-62,-54)
fa1(10,235,-200,200,-62,-54)
fa1(10,136,-200,200,-62,-54)
fa1(10,115,-200,200,-62,-54)
fa1(10,16,-200,200,-62,-54)
fa1(10,-5,-200,200,-62,-54)
fa1(-10,-5,-200,200,-62,-54)

fb1(0,-62,-91.7,-58.8)
fb1(0,-62,-54.7,-43.8)
fb1(0,-62,-41.7,-31.8)
fb1(0,-62,-29.7,-19.8)
fb1(0,-62,-17.7,-7.8)
fb1(0,-62,-5.7,5.7)

fa1(-10,-979,-200,200,-63,-62)
fa1(-10,-650,-200,200,-63,-62)
fa1(-10,-609,-200,200,-63,-62)
fa1(-10,-500,-200,200,-63,-62)
fa1(-10,-479,-200,200,-63,-62)
fa1(-10,-380,-200,200,-63,-62)
fa1(-10,-359,-200,200,-63,-62)
fa1(-10,-260,-200,200,-63,-62)
fa1(-10,-239,-200,200,-63,-62)
fa1(-10,-140,-200,200,-63,-62)
fa1(-10,-119,-200,200,-63,-62)
fa1(10,-119,-200,200,-63,-62)

fb1(0,-63,-91.6,-58.7)
fb1(0,-63,-54.6,-43.7)
fb1(0,-63,-41.6,-31.7)
fb1(0,-63,-29.6,-19.7)
fb1(0,-63,-17.6,-7.7)
fb1(0,-63,-5.6,5.6)

fa1(-10,-634,-200,200,-55,-54)
fa1(-10,-484,-200,200,-55,-54)
fa1(-10,-364,-200,200,-55,-54)
fa1(-10,-244,-200,200,-55,-54)
fa1(-10,-124,-200,200,-55,-54)

fa1(10,524,-200,200,-63,-55)
fa1(10,374,-200,200,-63,-55)
fa1(10,254,-200,200,-63,-55)
fa1(10,134,-200,200,-63,-55)
fa1(10,14,-200,200,-63,-55)
def fb1(a,b,m,n):
    def fb(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    y=fb(x)
    plt.plot(x,y,'k-')

def fa1(a,b,m,n,q,p):
    def fa(x):
        return a*x+b
    x=np.linspace(m,n,100000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fa(i)<=p:
            x1.append(i)
            y1.append(fa(i))
    plt.plot(x1,y1,'k-')

fb1(0,-64,-41,-30)
fb1(0,-70,-41.6,-30.6)
fb1(0,-64,-55,-44)
fb1(0,-70,-55.7,-44.7)
fb1(0,-64,-70,-59)
fb1(0,-70,-70.6,-59.8)
fb1(0,-64,-92,-74)
fb1(0,-70,-92.6,-74.8)

fa1(10,855,-200,200,-70,-64)
fa1(10,676,-200,200,-70,-64)
fa1(10,635,-200,200,-70,-64)
fa1(10,527,-200,200,-70,-64)
fa1(10,487,-200,200,-70,-64)
fa1(10,377,-200,200,-70,-64)
fa1(10,346,-200,200,-70,-64)
fa1(10,236,-200,200,-70,-64)

fa1(-10,-995,-200,200,-71,-70)
fa1(-10,-816,-200,200,-71,-70)
fa1(-10,-775,-200,200,-71,-70)
fa1(-10,-667,-200,200,-71,-70)
fa1(-10,-627,-200,200,-71,-70)
fa1(-10,-517,-200,200,-71,-70)
fa1(-10,-486,-200,200,-71,-70)
fa1(-10,-376,-200,200,-71,-70)

fb1(0,-71,-92.4,-74.5)
fb1(0,-71,-70.4,-59.6)
fb1(0,-71,-55.4,-44.6)
fb1(0,-71,-41.4,-30.6)

fa1(-10,-804,-200,200,-65,-64)
fa1(-10,-654,-200,200,-65,-64)
fa1(-10,-504,-200,200,-65,-64)
fa1(-10,-364,-200,200,-65,-64)

fa1(10,674,-200,200,-71,-65)
fa1(10,524,-200,200,-71,-65)
fa1(10,374,-200,200,-71,-65)
fa1(10,234,-200,200,-71,-65)
def fxl(a,b,t,r,q,p):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,10000)
    l=[]
    k=[]
    for i in x:
        if q<=fun(i)<=p:
            l.append(i)
            k.append(fun(i))
    plt.plot(l,k,'k-')

def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')

fxl(-10,855,0,100,-62,-54)
fx(0,-54,68,90.9)
fx(0,-54,56,66)
fx(0,-54,44,54)
fx(0,-54,32,42)
fx(0,-54,20,30)
fx(0,-54,8,18)
fxl(-10,26,0,100,-62,-54)
fxl(-10,125,0,100,-62,-54)
fxl(-10,146,0,100,-62,-54)
fxl(-10,245,0,100,-62,-54)
fxl(-10,266,0,100,-62,-54)
fxl(-10,365,0,100,-62,-54)
fxl(-10,386,0,100,-62,-54)
fxl(-10,485,0,100,-62,-54)
fxl(-10,506,0,100,-62,-54)
fxl(-10,605,0,100,-62,-54)
fxl(-10,626,0,100,-62,-54)
fx(0,-62,8.8,18.7)
fx(0,-62,20.8,30.7)
fx(0,-62,32.8,42.7)
fx(0,-62,44.8,54.7)
fx(0,-62,56.8,66.7)
fx(0,-62,68.8,91.7)
fxl(10,-979,0,100,-63,-62)
fxl(-10,624,0,100,-63,-55)
fxl(10,-750,0,100,-63,-62)
fxl(10,-729,0,100,-63,-62)
fxl(10,-630,0,100,-63,-62)
fxl(10,-609,0,100,-63,-62)
fxl(10,-510,0,100,-63,-62)
fxl(10,-489,0,100,-63,-62)
fxl(10,-390,0,100,-63,-62)
fxl(10,-369,0,100,-63,-62)
fxl(10,-270,0,100,-63,-62)
fxl(10,-249,0,100,-63,-62)
fxl(10,-150,0,100,-63,-62)
fxl(10,-734,0,100,-55,-54)
fxl(10,-614,0,100,-55,-54)
fxl(10,-494,0,100,-55,-54)
fxl(10,-374,0,100,-55,-54)
fxl(10,-254,0,100,-55,-54)
fxl(10,-134,0,100,-55,-54)
fxl(-10,504,0,100,-63,-55)
fxl(-10,384,0,100,-63,-55)
fxl(-10,264,0,100,-63,-55)
fxl(-10,144,0,100,-63,-55)
fxl(-10,24,0,100,-63,-55)
fx(0,-63,68.7,91.6)
fx(0,-63,56.7,66.6)
fx(0,-63,44.7,54.6)
fx(0,-63,32.7,42.6)
fx(0,-63,20.7,30.6)
fx(0,-63,8.7,18.6)
def fxl(a,b,t,r,q,p):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,10000)
    l=[]
    k=[]
    for i in x:
        if q<=fun(i)<=p:
            l.append(i)
            k.append(fun(i))
    plt.plot(l,k,'k-')

def fx(a,b,t,r):
    def fun(x):
        return a*x+b
    x=np.linspace(t,r,1000)
    y=fun(x)
    plt.plot(x,y,'k-')

fxl(10,855,-100,0,-52,-44)
fx(0,-44,-89.9,-62)
fx(0,-44,-11,-1)
fx(0,-44,-23,-13)
fx(0,-44,-35,-25)
fx(0,-44,-47,-37)
fx(0,-44,-59,-49)
fxl(10,576,-100,0,-52,-44)
fxl(10,545,-100,0,-52,-44)
fxl(10,446,-100,0,-52,-44)
fxl(10,425,-100,0,-52,-44)
fxl(10,326,-100,0,-52,-44)
fxl(10,305,-100,0,-52,-44)
fxl(10,206,-100,0,-52,-44)
fxl(10,185,-100,0,-52,-44)
fxl(10,86,-100,0,-52,-44)
fxl(10,65,-100,0,-52,-44)
fxl(40,-4,-100,0,-52,-44)
fx(0,-52,-90.7,-62.8)
fx(0,-52,-59.7,-49.8)
fx(0,-52,-47.7,-37.8)
fx(0,-52,-35.7,-25.8)
fx(0,-52,-23.7,-13.8)
fx(0,-52,-11.7,-1.2)
fxl(-10,-959,-100,0,-53,-52)
fxl(-10,-680,-100,0,-53,-52)
fxl(-10,-649,-100,0,-53,-52)
fxl(-10,-550,-100,0,-53,-52)
fxl(-10,-529,-100,0,-53,-52)
fxl(-10,-430,-100,0,-53,-52)
fxl(-10,-409,-100,0,-53,-52)
fxl(-10,-310,-100,0,-53,-52)
fxl(-10,-289,-100,0,-53,-52)
fxl(-10,-190,-100,0,-53,-52)
fxl(-10,-169,-100,0,-53,-52)
fxl(-10,-64,-100,0,-53,-52)
fx(0,-53,-90.6,-62.7)
fx(0,-53,-59.6,-49.7)
fx(0,-53,-47.6,-37.7)
fx(0,-53,-35.6,-25.7)
fx(0,-53,-23.6,-13.7)
fx(0,-53,-11.6,-1.1)
fxl(-10,-664,-100,0,-45,-44)
fxl(-10,-534,-100,0,-45,-44)
fxl(-10,-414,-100,0,-45,-44)
fxl(-10,-294,-100,0,-45,-44)
fxl(-10,-174,-100,0,-45,-44)
fxl(-10,-54,-100,0,-45,-44)
fxl(10,574,-100,0,-53,-45)
fxl(10,444,-100,0,-53,-45)
fxl(10,324,-100,0,-53,-45)
fxl(10,204,-100,0,-53,-45)
fxl(10,84,-100,0,-53,-45)
fxl(40,-8,-100,0,-53,-45)



fxl(-10,855,0,100,-52,-44)
fx(0,-44,73,89.9)
fx(0,-44,61,71)
fx(0,-44,49,59)
fx(0,-44,37,47)
fx(0,-44,25,35)
fx(0,-44,13,23)
fx(0,-44,1,11)
fxl(-40,-4,0,100,-52,-44)
fxl(-10,65,0,100,-52,-44)
fxl(-10,86,0,100,-52,-44)
fxl(-10,185,0,100,-52,-44)
fxl(-10,206,0,100,-52,-44)
fxl(-10,305,0,100,-52,-44)
fxl(-10,326,0,100,-52,-44)
fxl(-10,425,0,100,-52,-44)
fxl(-10,446,0,100,-52,-44)
fxl(-10,545,0,100,-52,-44)
fxl(-10,566,0,100,-52,-44)
fxl(-10,665,0,100,-52,-44)
fxl(-10,686,0,100,-52,-44)
fx(0,-52,1.2,11.7)
fx(0,-52,13.8,23.7)
fx(0,-52,25.8,35.7)
fx(0,-52,37.8,47.7)
fx(0,-52,49.8,59.7)
fx(0,-52,61.8,71.7)
fx(0,-52,73.8,90.7)
fxl(10,-959,0,100,-53,-52)
fxl(10,-790,0,100,-53,-52)
fxl(10,-774,0,100,-45,-44)
fxl(10,-769,0,100,-53,-52)
fxl(10,-669,0,100,-53,-52)
fxl(10,-649,0,100,-53,-52)
fxl(10,-549,0,100,-53,-52)
fxl(10,-529,0,100,-53,-52)
fxl(10,-429,0,100,-53,-52)
fxl(10,-409,0,100,-53,-52)
fxl(10,-309,0,100,-53,-52)
fxl(10,-289,0,100,-53,-52)
fxl(10,-189,0,100,-53,-52)
fxl(10,-169,0,100,-53,-52)
fxl(10,-64,0,100,-53,-52)
fxl(10,-654,0,100,-45,-44)
fxl(10,-534,0,100,-45,-44)
fxl(10,-414,0,100,-45,-44)
fxl(10,294,0,100,-45,-44)
fxl(10,-174,0,100,-45,-44)
fxl(10,-54,0,100,-45,-44)
fxl(-10,564,0,100,-53,-45)
fxl(-10,444,0,100,-53,-45)
fxl(-10,324,0,100,-53,-45)
fxl(-10,204,0,100,-53,-45)
fxl(-10,84,0,100,-53,-45)
fxl(-40,-12,0,100,-53,-45)
fx(0,-53,73.7,90.6)
fx(0,-53,61.7,71.6)
fx(0,-53,49.7,59.6)
fx(0,-53,37.7,47.6)
fx(0,-53,25.7,35.6)
fx(0,-53,13.7,23.6)
fx(0,-53,1.1,11.6)

def f1(a,b,m,n):
    def fun1(x):
        return a*x+b
    x=np.linspace(m,n,1000000)
    y=fun1(x)
    plt.plot(x,y,'k-')
def f2(a,b,m,n,q,p):
    def fun2(x):
        return a*x+b
    x=np.linspace(m,n,1000000)
    x1=[]
    y1=[]
    for i in x:
        if q<=fun2(i)<=p:
            x1.append(i)
            y1.append(fun2(i))
    plt.plot(x1,y1,'k-')
f2(10,855,-200,200,-42,-34)
f2(0,-34,-200,200,-18,8)
f2(0,-34,-200,200,-30,-20)
f1(0,-34,-18,-8)
f1(0,-34,-30,-20)
f1(0,-34,-42,-32)
f1(0,-34,-54,-44)
f1(0,-34,-66,-56)
f1(0,-34,-88.9,-68)
f2(10,646,-200,200,-42,-34)
f2(10,625,-200,200,-42,-34)
f2(10,526,-200,200,-42,-34)
f2(10,505,-200,200,-42,-34)
f2(10,406,-200,200,-42,-34)
f2(10,385,-200,200,-42,-34)
f2(10,286,-200,200,-42,-34)
f2(10,265,-200,200,-42,-34)
f2(10,166,-200,200,-42,-34)
f2(10,145,-200,200,-42,-34)
f2(10,46,-200,200,-42,-34)
f2(10,25,-200,200,-42,-34)
f2(-10,5,-200,200,-42,-34)
f1(0,-42,-89.7,-68.8)
f1(0,-42,-66.7,-56.8)
f1(0,-42,-54.7,-44.8)
f1(0,-42,-42.7,-32.8)
f1(0,-42,-30.7,-20.8)
f1(0,-42,-18.7,-8.8)
f1(0,-42,-6.7,4.7)
f2(-10,-939,-200,200,-43,-41)
f2(-10,-730,-200,200,-43,-42)
f2(-10,-709,-200,200,-43,-42)
f2(-10,-610,-200,200,-43,-42)
f2(-10,-589,-200,200,-43,-42)
f2(-10,-490,-200,200,-43,-42)
f2(-10,-469,-200,200,-43,-42)
f2(-10,-370,-200,200,-43,-42)
f2(-10,-349,-200,200,-43,-42)
f2(-10,-250,-200,200,-43,-42)
f2(-10,-229,-200,200,-43,-42)
f2(-10,-130,-200,200,-43,-42)
f1(0,-43,-89.6,-68.7)
f1(0,-43,-66.6,-56.7)
f1(0,-43,-54.6,-44.7)
f1(0,-43,-42.6,-32.7)
f1(0,-43,-30.6,-20.7)
f1(0,-43,-18.6,-8.7)
f2(-10,-714,-200,200,-35,-34)
f2(-10,-594,-200,200,-35,-34)
f2(-10,-474,-200,200,-35,-34)
f2(-10,-354,-200,200,-35,-34)
f2(-10,-234,-200,200,-35,-34)
f2(-10,-114,-200,200,-35,-34)
f2(10,644,-200,200,-43,-35)
f2(10,524,-200,200,-43,-35)
f2(10,404,-200,200,-43,-35)
f2(10,284,-200,200,-43,-35)
f2(10,164,-200,200,-43,-35)
f2(10,44,-200,200,-43,-35)
f2(-10,-109,-200,200,-43,-42)
f2(10,-89,-200,200,-43,-42)
f1(0,-43,-6.6,4.6)
f2(10,855,-200,200,-32,-26)
f1(0,-26,-88.1,-78)
f1(0,-26,-76,-66)
f1(0,-26,-64,-54)
f1(0,-26,-52,-42)
f1(0,-26,-40,-30)
f1(0,-26,-28,-18)
f1(0,-26,-16,-6)
f2(10,754,-200,200,-32,-26)
f2(10,733,-200,200,-32,-26)
f2(10,634,-200,200,-32,-26)
f2(10,613,-200,200,-32,-26)
f2(10,514,-200,200,-32,-26)
f2(10,493,-200,200,-32,-26)
f2(10,394,-200,200,-32,-26)
f2(10,373,-200,200,-32,-26)
f2(10,274,-200,200,-32,-26)
f2(10,253,-200,200,-32,-26)
f2(10,154,-200,200,-32,-26)
f2(10,133,-200,200,-32,-26)
f2(10,34,-200,200,-32,-26)
f1(0,-32,-88.7,-78.6)
f1(0,-32,-76.5,-66.6)
f1(0,-32,-64.5,-54.6)
f1(0,-32,-52.5,-42.6)
f1(0,-32,-40.5,-30.6)
f1(0,-32,-28.5,-18.6)
f1(0,-32,-16.5,-6.6)
f2(-10,-919,-200,200,-33,-32)
f2(-10,-818,-200,200,-33,-32)
f2(-10,-797,-200,200,-33,-32)
f2(-10,-698,-200,200,-33,-32)
f2(-10,-677,-200,200,-33,-32)
f2(-10,-578,-200,200,-33,-32)
f2(-10,-557,-200,200,-33,-32)
f2(-10,-458,-200,200,-33,-32)
f2(-10,-437,-200,200,-33,-32)
f2(-10,-338,-200,200,-33,-32)
f2(-10,-317,-200,200,-33,-32)
f2(-10,-218,-200,200,-33,-32)
f2(-10,-197,-200,200,-33,-32)
f2(-10,-98,-200,200,-33,-32)
f2(-10,-806,-200,200,-27,-26)
f2(-10,-686,-200,200,-27,-26)
f2(-10,-566,-200,200,-27,-26)
f2(-10,-446,-200,200,-27,-26)
f2(-10,-326,-200,200,-27,-26)
f2(-10,-206,-200,200,-27,-26)
f2(-10,-86,-200,200,-27,-26)
f1(0,-33,-88.6,-78.5)
f1(0,-33,-76.4,-66.5)
f1(0,-33,-64.4,-54.5)
f1(0,-33,-52.4,-42.5)
f1(0,-33,-40.4,-30.5)
f1(0,-33,-28.4,-18.5)
f1(0,-33,-16.4,-6.5)
f2(10,752,-200,200,-33,-27)
f2(10,632,-200,200,-33,-27)
f2(10,512,-200,200,-33,-27)
f2(10,392,-200,200,-33,-27)
f2(10,272,-200,200,-33,-27)
f2(10,152,-200,200,-33,-27)
f2(10,32,-200,200,-33,-27)
f2(-10,855,-200,200,-32,-26)
f1(0,-26,-4,6)
f1(0,-26,8,18)
f1(0,-26,8,18)
f1(0,-26,20,30)
f1(0,-26,32,42)
f1(0,-26,44,54)
f1(0,-26,56,66)
f1(0,-26,68,88.1)
f2(10,13,-200,200,-32,-26)
f2(-10,33,-200,200,-32,-26)
f2(-10,54,-200,200,-32,-26)
f2(-10,153,-200,200,-32,-26)
f2(-10,174,-200,200,-32,-26)
f2(-10,273,-200,200,-32,-26)
f2(-10,294,-200,200,-32,-26)
f2(-10,393,-200,200,-32,-26)
f2(-10,414,-200,200,-32,-26)
f2(-10,513,-200,200,-32,-26)
f2(-10,534,-200,200,-32,-26)
f2(-10,633,-200,200,-32,-26)
f2(-10,654,-200,200,-32,-26)
f1(0,-32,-4.5,6.5)
f1(0,-32,8.5,18.5)
f1(0,-32,20.5,30.5)
f1(0,-32,32.5,42.5)
f1(0,-32,44.5,54.5)
f1(0,-32,56.5,66.5)
f1(0,-32,68.5,88.7)
f2(10,-919,-200,200,-33,-32)
f2(10,-718,-200,200,-33,-32)
f2(10,-697,-200,200,-33,-32)
f2(10,-598,-200,200,-33,-32)
f2(10,-577,-200,200,-33,-32)
f2(10,-478,-200,200,-33,-32)
f2(10,-457,-200,200,-33,-32)
f2(10,-358,-200,200,-33,-32)
f2(10,-337,-200,200,-33,-32)
f2(10,-238,-200,200,-33,-32)
f2(10,-217,-200,200,-33,-32)
f2(10,-118,-200,200,-33,-32)
f2(10,-97,-200,200,-33,-32)
f2(-10,-77,-200,200,-33,-32)
f1(0,-33,-4.4,6.4)
f1(0,-33,8.4,18.4)
f1(0,-33,20.4,30.4)
f1(0,-33,32.4,42.4)
f1(0,-33,44.4,54.4)
f1(0,-33,56.4,66.4)
f1(0,-33,68.4,88.4)
f2(10,-706,-200,200,-26,-27)
f2(10,-586,-200,200,-26,-27)
f2(10,-466,-200,200,-26,-27)
f2(10,-346,-200,200,-26,-27)
f2(10,-226,-200,200,-26,-27)
f2(10,-106,-200,200,-26,-27)
f2(-10,652,-200,200,-33,-27)
f2(-10,532,-200,200,-33,-27)
f2(-10,412,-200,200,-33,-27)
f2(-10,292,-200,200,-33,-27)
f2(-10,172,-200,200,-33,-27)
f2(-10,52,-200,200,-33,-27)
f2(-10,855,-200,200,-42,-34)
f1(0,-34,-6,4)
f1(0,-34,6,16)
f1(0,-34,18,28)
f1(0,-34,30,40)
f1(0,-34,42,52)
f1(0,-34,54,64)
f1(0,-34,66,76)
f1(0,-34,78,89)
f2(-10,26,-200,200,-42,-34)
f2(-10,125,-200,200,-42,-34)
f2(-10,146,-200,200,-42,-34)
f2(-10,245,-200,200,-42,-34)
f2(-10,266,-200,200,-42,-34)
f2(-10,365,-200,200,-42,-34)
f2(-10,386,-200,200,-42,-34)
f2(-10,485,-200,200,-42,-34)
f2(-10,506,-200,200,-42,-34)
f2(-10,605,-200,200,-42,-34)
f2(-10,626,-200,200,-42,-34)
f2(-10,725,-200,200,-42,-34)
f2(-10,746,-200,200,-42,-34)
f1(0,-42,6.8,16.7)
f1(0,-42,18.8,28.7)
f1(0,-42,30.8,40.7)
f1(0,-42,42.8,52.7)
f1(0,-42,54.8,64.7)
f1(0,-42,66.8,76.7)
f1(0,-42,78.8,89.7)
f2(10,-939,-200,200,-43,-42)
f2(10,-829,-200,200,-43,-42)
f2(10,-809,-200,200,-43,-42)
f2(10,-709,-200,200,-43,-42)
f2(10,-689,-200,200,-43,-42)
f2(10,-589,-200,200,-43,-42)
f2(10,-569,-200,200,-43,-42)
f2(10,-469,-200,200,-43,-42)
f2(10,-449,-200,200,-43,-42)
f2(10,-349,-200,200,-43,-42)
f2(10,-329,-200,200,-43,-42)
f2(10,-229,-200,200,-43,-42)
f2(10,-209,-200,200,-43,-42)
f2(10,-109,-200,200,-43,-42)
f1(0,-43,78.6,89.6)
f1(0,-43,66.6,76.6)
f1(0,-43,54.6,64.6)
f1(0,-43,42.6,52.6)
f1(0,-43,30.6,40.6)
f1(0,-43,18.6,28.6)
f1(0,-43,6.6,16.6)
f2(10,-814,-200,200,-35,-34)
f2(10,-694,-200,200,-35,-34)
f2(10,-574,-200,200,-35,-34)
f2(10,-454,-200,200,-35,-34)
f2(10,-334,-200,200,-35,-34)
f2(10,-214,-200,200,-35,-34)
f2(10,-94,-200,200,-35,-34)
f2(-10,744,-200,200,-43,-35)
f2(-10,624,-200,200,-43,-35)
f2(-10,504,-200,200,-43,-35)
f2(-10,384,-200,200,-43,-35)
f2(-10,264,-200,200,-43,-35)
f2(-10,144,-200,200,-43,-35)
f2(-10,24,-200,200,-43,-35)

axes=plt.subplot()
axes.set_aspect(1)
plt.show()