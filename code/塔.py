import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.core.function_base import linspace
def fun1(a,b,xmin,xmax):
    xr=np.linspace(xmin,xmax,2000) 
    y1r=a*xr+b
    plt.plot(xr,y1r,'k-')
#base_1
fun1(1/5,-10,250/3,150)
fun1(1/5,10,250/3,150)
fun1(1/5,70,-150,-250/3)
fun1(-1/5,-10,-150,-250/3)
fun1(-1/5,10,-150,-250/3)
fun1(-1/5,70,250/3,150)
plt.plot([150,150],[20,40],color="black")
plt.plot([-150,-150],[20,40],color="black")
#base_2
plt.plot([60,67.78],[72,76.67],color="black")
plt.plot([-60,-67.78],[72,76.67],color="black")
fun1(3/5,96,-220/3,-38)
fun1(-3/5,96,38,220/3)
fun1(3/5,108,-250/3,-50*math.pi/3-0.5)
fun1(3/5,108,-50*math.pi/3+0.5,-48)
fun1(-3/5,108,50*math.pi/3+0.5,250/3)
fun1(-3/5,108,48,50*math.pi/3-0.5)
plt.plot([-250/3,-250/3],[0,58],color="black")
plt.plot([220/3,220/3],[-6,52],color="black")
plt.plot([-220/3,-220/3],[-6,52],color="black")
plt.plot([250/3,250/3],[0,58],color="black")
plt.plot([-69.233,-69.233],[66.46,76.074],color="black")
plt.plot([69.233,69.233],[66.46,76.074],color="black")
plt.plot([52.9,66],[87.34,79.48],color="black")
plt.plot([50,51.86],[89.08,87.964],color="black")
plt.plot([-50,-51.86],[89.08,87.964],color="black")
plt.plot([-52.9,-66],[87.34,79.48],color="black")
plt.plot([37.7,50],[89.08,89.08],color="black")
plt.plot([-37.7,-50],[89.08,89.08],color="black")
#stairs_treads
plt.plot([-68,-66],[2,4],color="black")
plt.plot([-66,-64],[6,8],color="black")
plt.plot([-64,-62],[10,12],color="black")
plt.plot([-62,-60],[14,16],color="black")
plt.plot([-60,-58],[18,20],color="black")
plt.plot([-58,-56],[22,24],color="black")
plt.plot([-56,-54],[26,28],color="black")
plt.plot([-54,-52],[30,32],color="black")
plt.plot([-52,-50],[34,36],color="black")
plt.plot([-50,-48],[38,40],color="black")
plt.plot([-48,-46],[42,44],color="black")
plt.plot([-46,-44],[46,48],color="black")
plt.plot([-44,-42],[50,52],color="black")
plt.plot([-42,-40],[54,56],color="black")
plt.plot([-40,-38],[58,60],color="black")
plt.plot([68,66],[2,4],color="black")
plt.plot([66,64],[6,8],color="black")
plt.plot([64,62],[10,12],color="black")
plt.plot([62,60],[14,16],color="black")
plt.plot([60,58],[18,20],color="black")
plt.plot([58,56],[22,24],color="black")
plt.plot([56,54],[26,28],color="black")
plt.plot([54,52],[30,32],color="black")
plt.plot([52,50],[34,36],color="black")
plt.plot([50,48],[38,40],color="black")
plt.plot([48,46],[42,44],color="black")
plt.plot([46,44],[46,48],color="black")
plt.plot([44,42],[50,52],color="black")
plt.plot([42,40],[54,56],color="black")
plt.plot([40,38],[58,60],color="black")
plt.plot([-66.666,-66.001],[3.334,3.999],color="black")
plt.plot([66.666,66.001],[3.334,3.999],color="black")
#stairs_risers
plt.plot([-68,-68],[0,2],color="black")
plt.plot([-66,-66],[4,6],color="black")
plt.plot([-64,-64],[8,10],color="black")
plt.plot([-62,-62],[12,14],color="black")
plt.plot([-60,-60],[16,18],color="black")
plt.plot([-58,-58],[20,22],color="black")
plt.plot([-56,-56],[24,26],color="black")
plt.plot([-54,-54],[28,30],color="black")
plt.plot([-52,-52],[32,34],color="black")
plt.plot([-50,-50],[36,38],color="black")
plt.plot([-48,-48],[40,42],color="black")
plt.plot([-46,-46],[44,46],color="black")
plt.plot([-44,-44],[48,50],color="black")
plt.plot([-42,-42],[52,54],color="black")
plt.plot([-40,-40],[56,58],color="black")
plt.plot([-38,-38],[60,62],color="black")
plt.plot([68,68],[0,2],color="black")
plt.plot([66,66],[4,6],color="black")
plt.plot([64,64],[8,10],color="black")
plt.plot([62,62],[12,14],color="black")
plt.plot([60,60],[16,18],color="black")
plt.plot([58,58],[20,22],color="black")
plt.plot([56,56],[24,26],color="black")
plt.plot([54,54],[28,30],color="black")
plt.plot([52,52],[32,34],color="black")
plt.plot([50,50],[36,38],color="black")
plt.plot([48,48],[40,42],color="black")
plt.plot([46,46],[44,46],color="black")
plt.plot([44,44],[48,50],color="black")
plt.plot([42,42],[52,54],color="black")
plt.plot([40,40],[56,58],color="black")
plt.plot([38,38],[60,62],color="black")
#stairs_sides
plt.plot([-68,-35],[0,-6.6],color="black")
plt.plot([-66,-35],[4,-2.2],color="black")
plt.plot([-64,-35],[8,2.2],color="black")
plt.plot([-62,-35],[12,6.6],color="black")
plt.plot([-60,-35],[16,11],color="black")
plt.plot([-58,-35],[20,15.4],color="black")
plt.plot([-56,-35],[24,19.8],color="black")
plt.plot([-54,-35],[28,24.2],color="black")
plt.plot([-52,-35],[32,28.6],color="black")
plt.plot([-50,-35],[36,33],color="black")
plt.plot([-48,-35],[40,37.4],color="black")
plt.plot([-46,-35],[44,41.8],color="black")
plt.plot([-44,-35],[48,46.2],color="black")
plt.plot([-42,-35],[52,50.6],color="black")
plt.plot([-40,-35],[56,55],color="black")
plt.plot([-38,-35],[60,59.4],color="black")
plt.plot([68,35],[0,-6.6],color="black")
plt.plot([66,35],[4,-2.2],color="black")
plt.plot([64,35],[8,2.2],color="black")
plt.plot([62,35],[12,6.6],color="black")
plt.plot([60,35],[16,11],color="black")
plt.plot([58,35],[20,15.4],color="black")
plt.plot([56,35],[24,19.8],color="black")
plt.plot([54,35],[28,24.2],color="black")
plt.plot([52,35],[32,28.6],color="black")
plt.plot([50,35],[36,33],color="black")
plt.plot([48,35],[40,37.4],color="black")
plt.plot([46,35],[44,41.8],color="black")
plt.plot([44,35],[48,46.2],color="black")
plt.plot([42,35],[52,50.6],color="black")
plt.plot([40,35],[56,55],color="black")
plt.plot([38,35],[60,59.4],color="black")
plt.plot([-68,-35],[2,-4.6],color="black")
plt.plot([-66,-35],[6,-0.2],color="black")
plt.plot([-64,-35],[10,4.2],color="black")
plt.plot([-62,-35],[14,8.6],color="black")
plt.plot([-60,-35],[18,13],color="black")
plt.plot([-58,-35],[22,17.4],color="black")
plt.plot([-56,-35],[26,21.8],color="black")
plt.plot([-54,-35],[30,26.2],color="black")
plt.plot([-52,-35],[34,30.6],color="black")
plt.plot([-50,-35],[38,35],color="black")
plt.plot([-48,-35],[42,39.4],color="black")
plt.plot([-46,-35],[46,43.8],color="black")
plt.plot([-44,-35],[50,48.2],color="black")
plt.plot([-42,-35],[54,52.6],color="black")
plt.plot([-40,-35],[58,57],color="black")
plt.plot([-38,-35],[62,61.4],color="black")
plt.plot([68,35],[2,-4.6],color="black")
plt.plot([66,35],[6,-0.2],color="black")
plt.plot([64,35],[10,4.2],color="black")
plt.plot([62,35],[14,8.6],color="black")
plt.plot([60,35],[18,13],color="black")
plt.plot([58,35],[22,17.4],color="black")
plt.plot([56,35],[26,21.8],color="black")
plt.plot([54,35],[30,26.2],color="black")
plt.plot([52,35],[34,30.6],color="black")
plt.plot([50,35],[38,35],color="black")
plt.plot([48,35],[42,39.4],color="black")
plt.plot([46,35],[46,43.8],color="black")
plt.plot([44,35],[50,48.2],color="black")
plt.plot([42,35],[54,52.6],color="black")
plt.plot([40,35],[58,57],color="black")
plt.plot([38,35],[62,61.4],color="black")
#mid_stairs
plt.plot([-35,35],[-6.6,-6.6],color="black")
plt.plot([-35,35],[-2.2,-2.2],color="black")
plt.plot([-35,35],[2.2,2.2],color="black")
plt.plot([-35,35],[6.6,6.6],color="black")
plt.plot([-35,35],[11,11],color="black")
plt.plot([-35,35],[15.4,15.4],color="black")
plt.plot([-35,35],[19.8,19.8],color="black")
plt.plot([-35,35],[24.2,24.2],color="black")
plt.plot([-35,35],[28.6,28.6],color="black")
plt.plot([-35,35],[33,33],color="black")
plt.plot([-35,35],[37.4,37.4],color="black")
plt.plot([-35,35],[41.8,41.8],color="black")
plt.plot([-35,35],[46.2,46.2],color="black")
plt.plot([-35,35],[50.6,50.6],color="black")
plt.plot([-35,35],[55,55],color="black")
plt.plot([-35,35],[59.4,59.4],color="black")
plt.plot([-35,35],[-4.6,-4.6],color="black")
plt.plot([-35,35],[-0.2,-0.2],color="black")
plt.plot([-35,35],[4.2,4.2],color="black")
plt.plot([-35,35],[8.6,8.6],color="black")
plt.plot([-35,35],[13,13],color="black")
plt.plot([-35,35],[17.4,17.4],color="black")
plt.plot([-35,35],[21.8,21.8],color="black")
plt.plot([-35,35],[26.2,26.2],color="black")
plt.plot([-35,35],[30.6,30.6],color="black")
plt.plot([-35,35],[35,35],color="black")
plt.plot([-35,35],[39.4,39.4],color="black")
plt.plot([-35,35],[43.8,43.8],color="black")
plt.plot([-35,35],[48.2,48.2],color="black")
plt.plot([-35,35],[52.6,52.6],color="black")
plt.plot([-35,35],[57,57],color="black")
plt.plot([-35,35],[61.4,61.4],color="black")
#stairs_shoulders
plt.plot([-38,-38],[62,73.2],color="black")
plt.plot([38,38],[62,73.2],color="black")
plt.plot([38,48],[73.2,79.2],color="black")
plt.plot([-38,-48],[73.2,79.2],color="black")
plt.plot([73.333,83.333],[52,58],color="black")
plt.plot([-73.333,-83.333],[52,58],color="black")
plt.plot([73.333,83.333],[-6,0],color="black")
plt.plot([-73.333,-83.333],[-6,0],color="black")
plt.plot([-73.333,-68],[-6,0],color="black")
plt.plot([68,73.333],[0,-6],color="black")
#main _building_foundations
plt.plot([-25.133,-25.133],[70,103.1],color="black")
plt.plot([25.133,25.133],[70,103.1],color="black")
plt.plot([-25.1,25.1],[70,70],color="black")
plt.plot([-37.7,-37.7],[77.54,102.537],color="black")
plt.plot([37.7,37.7],[77.54,102.537],color="black")
plt.plot([-25.1,-37.7],[70,77.54],color="black")
plt.plot([25.1,37.7],[70,77.54],color="black")
plt.plot([38,25.133],[62.082,70],color="black")
plt.plot([-38,-25.133],[62.082,70],color="black")
plt.plot([-66.846,-52.86],[77.54,77.54],color="black")
plt.plot([52.86,66.846],[77.54,77.54],color="black")
plt.plot([-51.86,-50.767],[77.54,77.54],color="black")
plt.plot([50.767,51.86],[77.54,77.54],color="black")
plt.plot([-45.233,-37.7],[77.54,77.54],color="black")
plt.plot([37.7,45.233],[77.54,77.54],color="black")
plt.plot([-37.7,-50],[87.032,89.08],color="black")
plt.plot([37.7,50],[87.032,89.08],color="black")
#roof_1_ting
x = np.linspace(-31.385,31.385,1000)
y = (-100* np.cos(0.01*x)+200)
plt.plot(x,y,"k")
x = np.linspace(-32.969,32.969,1000)
y = (-100* np.cos(0.01*x)+201.083)
plt.plot(x,y,"k")
x = np.linspace(-25.13,25.13,1000)
y = (-100* np.cos(0.005*x)+209.9975)
plt.plot(x,y,"k")
x = np.linspace(-35.365,-25.1,1000)
y = (-390* np.cos(0.00548*x)+497.093)
plt.plot(x,y,"k")
x = np.linspace(35.365,25.1,1000)
y = (-390* np.cos(0.00548*x)+497.093)
plt.plot(x,y,"k")
x = np.linspace(-61.256,-32.6,1000)
y = (-4* np.cos(0.12*x)+32.8418*math.pi)
plt.plot(x,y,"k")
x = np.linspace(61.256,32.6,1000)
y = (-4* np.cos(0.12*x)+32.8418*math.pi)
plt.plot(x,y,"k")
x = np.linspace(-64.323,-31.5,1000)
y = (-4* np.cos(0.12*x)+32.4*math.pi)
plt.plot(x,y,"k")
x = np.linspace(64.323,31.5,1000)
y = (-4* np.cos(0.12*x)+32.4*math.pi)
plt.plot(x,y,"k")
plt.plot([-61.256,-43.758],[101.246,111.745],color="black")
plt.plot([61.256,43.758],[101.246,111.745],color="black")
plt.plot([-32.969,-31.4],[106.469,104.9],color="black")
plt.plot([32.969,31.4],[106.469,104.9],color="black")
def func(x):
  return 4*(x-40)**2/159 + 105.225
xr = linspace(25.13,32.969,1000)
yr = func(xr)
plt.plot(xr,yr,'k-')
def fun0(x):
  return 4*(x+40)**2/159 + 105.225
xr = linspace(-25.13,-32.969,1000)
yr = fun0(xr)
plt.plot(xr,yr,'k-')
plt.plot([-64.4,-61.3],[101.249,101.249],color="black")
plt.plot([64.4,61.3],[101.249,101.249],color="black")
plt.plot([-52.86,-52.86],[70.584,97.788],color="black")
plt.plot([-51.86,-51.86],[70.584,97.788],color="black")
plt.plot([51.86,51.86],[70.584,97.788],color="black")
plt.plot([52.86,52.86],[70.584,97.788],color="black")
x = np.linspace(51.87,52.85,2000)
y = np.linspace(70.557,70.584,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x-50/3*np.pi)**2+2*(y-72.793)**2,[10],colors="black")
x = np.linspace(-51.87,-52.85,2000)
y = np.linspace(70.557,70.584,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x+50/3*np.pi)**2+2*(y-72.793)**2,[10],colors="black")
x = np.linspace(51.86,52.86,2000)
y = np.linspace(69.802,71.319,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x-50/3*np.pi)**2+5*(y-70.577)**2,[3],colors="black")
x = np.linspace(-51.86,-52.86,2000)
y = np.linspace(69.802,71.319,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x+50/3*np.pi)**2+5*(y-70.577)**2,[3],colors="black")
x = np.linspace(50.628,54.092,2000)
y = np.linspace(68.802,69.566,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x-50/3*np.pi)**2+5*(y-69.577)**2,[3],colors="black")
x = np.linspace(-50.628,-54.092,2000)
y = np.linspace(68.802,69.566,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x+50/3*np.pi)**2+5*(y-69.577)**2,[3],colors="black")
plt.plot([50.628,50.628],[69.566,70.588],color="black")
plt.plot([-50.628,-50.628],[69.566,70.588],color="black")
plt.plot([54.092,54.092],[69.566,70.588],color="black")
plt.plot([-54.092,-54.092],[69.566,70.588],color="black")
#door
plt.plot([-11,-11],[70,86],color="black")
plt.plot([-10,-10],[70,86],color="black")
plt.plot([-0.5,-0.5],[70,86],color="black")
plt.plot([0.5,0.5],[70,86],color="black")
plt.plot([10,10],[70,86],color="black")
plt.plot([11,11],[70,86],color="black")
plt.plot([15.7,-15.7],[86,86],color="black")
x = np.linspace(51.87,52.85,2000)
y = np.linspace(70.557,70.584,2000)
x,y = np.meshgrid(x,y) 
plt.contour(x,y,(x-50/3*np.pi)**2+2*(y-72.793)**2,[10],colors="black")
plt.plot([-5.6,-0.5],[135,135],color="k")  #[x1,x2],[y1,y2],color
plt.plot([5.6,0.5],[135,135],color="k")
plt.plot([-18.727,-15.614],[138.656,136.788],color="k")
plt.plot([18.727,15.614],[138.656,136.788],color="k")
plt.plot([18.727,15.614],[138.656,136.788],color="k")
plt.plot([12.5,12.5],[174.481,140.232],color="k")
plt.plot([12.5,12.5],[138.232,136.232],color="k")
plt.plot([-12.5,-12.5],[174.481,140.232],color="k")
plt.plot([-12.5,-12.5],[138.232,136.232],color="k")
plt.plot([18.85,18.85],[144.634,175.99],color="k")
plt.plot([18.85,18.85],[142.634,141.37],color="k")
plt.plot([-18.85,-18.85],[144.634,175.99],color="k")
plt.plot([-18.85,-18.85],[142.634,141.37],color="k")
plt.plot([-27.5,-24.5],[143.089,143.635],color="k")
plt.plot([-27.5,-24.5],[139.089,139.635],color="k")
plt.plot([27.5,24.5],[143.089,143.635],color="k")
plt.plot([27.5,24.5],[139.089,139.635],color="k")
plt.plot([15.625,23.5],[145.21,143.804],color="k")
plt.plot([15.625,22.4],[143.21,142],color="k")
plt.plot([-15.625,-23.5],[145.21,143.804],color="k")
plt.plot([-15.625,-22.4],[143.21,142],color="k")
plt.plot([-15.625,-15.625],[145.7,142.74],color="k")
plt.plot([-15.625,-15.625],[141.7,140.79],color="k")
plt.plot([15.625,15.625],[145.7,142.74],color="k")
plt.plot([15.625,15.625],[141.7,140.79],color="k")
plt.plot([16.8,15.653],[141.202,141.205],color="k")
plt.plot([22.4,23.5],[140,139.804],color="k")
plt.plot([16.8,22.4],[139,138],color="k")
plt.plot([-16.8,-15.653],[141.202,141.205],color="k")
plt.plot([-22.4,-23.5],[140,139.804],color="k")
plt.plot([-16.8,-22.4],[139,138],color="k")
plt.plot([17.35,17.35],[173.41,150.41],color="k")
plt.plot([14,14],[171.4,148.4],color="k")
plt.plot([14,17.35],[171.4,173.41],color="k")
plt.plot([14,17.35],[148.4,150.41],color="k")
plt.plot([-17.35,-17.35],[173.41,150.41],color="k")
plt.plot([-14,-14],[171.4,148.4],color="k")
plt.plot([-14,-17.35],[171.4,173.41],color="k")
plt.plot([-14,-17.35],[148.4,150.41],color="k")
plt.plot([7.65,7.65],[173.41,150.41],color="k")
plt.plot([11,11],[171.4,148.4],color="k")
plt.plot([11,7.65],[171.4,173.41],color="k")
plt.plot([11,7.65],[148.4,150.41],color="k")
plt.plot([-7.65,-7.65],[173.41,150.41],color="k")
plt.plot([-11,-11],[171.4,148.4],color="k")
plt.plot([-11,-7.65],[171.4,173.41],color="k")
plt.plot([-11,-7.65],[148.4,150.41],color="k")
plt.plot([6.15,6.15],[173.4,163.4],color="k")
plt.plot([-6.15,-6.15],[173.4,163.4],color="k")
plt.plot([6.15,-6.15],[163.4,163.4],color="k")
plt.plot([6.15,-6.15],[173.4,173.4],color="k")
plt.plot([6.15,6.15],[160.4,150.4],color="k")
plt.plot([-6.15,-6.15],[160.4,150.4],color="k")
plt.plot([6.15,-6.15],[160.4,160.4],color="k")
plt.plot([6.15,-6.15],[150.4,150.4],color="k")
plt.plot([5.75,5.75],[137.027,135.027],color="k")
plt.plot([5,5],[135,136.893],color="k")
plt.plot([4.8,4.8],[136.857,135.2],color="k")
plt.plot([4.8,5],[135.2,135],color="k")
plt.plot([5.75,5.75],[146.5,145],color="k")
plt.plot([5,5],[146.5,145],color="k")
plt.plot([4.8,4.8],[144,138.86],color="k")
plt.plot([5.75,5.75],[144,139.03],color="k")
plt.plot([5,5],[144,138.9],color="k")
plt.plot([4.8,4.8],[145.2,146.5],color="k")
plt.plot([4.8,5],[145.2,145],color="k")
plt.plot([-5.75,-5.75],[137.027,135.027],color="k")
plt.plot([-5,-5],[135,136.893],color="k")
plt.plot([-4.8,-4.8],[136.857,135.2],color="k")
plt.plot([-4.8,-5],[135.2,135],color="k")
plt.plot([-5.75,-5.75],[146.5,145],color="k")
plt.plot([-5,-5],[146.5,145],color="k")
plt.plot([-4.8,-4.8],[144,138.86],color="k")
plt.plot([-5.75,-5.75],[144,139.03],color="k")
plt.plot([-5,-5],[144,138.9],color="k")
plt.plot([-4.8,-4.8],[145.2,146.5],color="k")
plt.plot([-4.8,-5],[145.2,145],color="k")
plt.plot([8,8],[144,145],color="k")
plt.plot([8,7.8],[145,145.2],color="k")
plt.plot([5.8,7.8],[145.2,145.2],color="k")
plt.plot([6.6,6.6],[147.436,146.7],color="k")
plt.plot([6.4,6.4],[147.41,146.5],color="k")
plt.plot([6.6,6.4],[146.7,146.5],color="k")
plt.plot([8.729,7.559],[148.762,147.572],color="k")
plt.plot([8.334,8.717],[149,148.77],color="k")
plt.plot([-8,-8],[144,145],color="k")
plt.plot([-8,-7.8],[145,145.2],color="k")
plt.plot([-5.8,-7.8],[145.2,145.2],color="k")
plt.plot([-6.6,-6.6],[147.436,146.7],color="k")
plt.plot([-6.4,-6.4],[147.41,146.5],color="k")
plt.plot([-6.6,-6.4],[146.7,146.5],color="k")
plt.plot([-8.729,-7.559],[148.762,147.572],color="k")
plt.plot([-8.334,-8.717],[149,148.77],color="k")
plt.plot([8,-8],[144,144],color="k")
plt.plot([8,-8],[145,145],color="k")
plt.plot([4.8,-4.8],[145.2,145.2],color="k")
plt.plot([6.4,-6.4],[146.5,146.5],color="k")
plt.plot([0,0.2],[248.2,248],color="k")
plt.plot([0,-0.2],[248.2,248],color="k")
plt.plot([0.2,-0.2],[248,248],color="k")
def circle(xc,yc,z,x1=0,x2=30,y1=0,y2=50): #paint the circle (xc,yc圓心座標,z=r^2 x1,x2=X軸始末值 y1,y2=Y軸始末值 如果沒有特別設定會是預設值)
   x = np.linspace(x1, x2, 1000) #limit the x range
   y = np.linspace(y1, y2, 1000) #limit the y range
   x,y=np.meshgrid(x,y)
   plt.contour(x,y,(x-xc)**2+(y-yc)**2,[z],colors='k')
circle(2,133.3,0.25,x1=0,x2=1000,y1=0,y2=1000)
circle(2,137.3,0.25,x1=0,x2=1000,y1=0,y2=1000)
circle(-2,133.3,0.25,x1=-1000,x2=0,y1=0,y2=1000)
circle(-2,137.3,0.25,x1=-1000,x2=0,y1=0,y2=1000)
circle(-26,137.6,0.25,x1=-1000,x2=0,y1=0,y2=1000)
circle(26,137.6,0.25,x1=0,x2=1000,y1=0,y2=1000)
circle(-26,141.6,0.25,x1=-1000,x2=0,y1=0,y2=1000)
circle(26,141.6,0.25,x1=0,x2=1000,y1=0,y2=1000)
# i dont know what this is
plt.plot([-23.133,-23.133],[72,84],color="k") #[x1,x2],[y1,y2],color
plt.plot([-12,-12],[72,84],color="k")
plt.plot([12,12],[72,84],color="k")
plt.plot([23.133,23.133],[72,84],color="k")
plt.plot([-12,-23.133],[72,72],color="k")
plt.plot([-12,-23.133],[84,84],color="k")
plt.plot([12,23.133],[72,72],color="k")
plt.plot([12,23.133],[84,84],color="k")
# panels
plt.plot([27.133,35.7],[73.3,78.4],color="k")
plt.plot([27.133,35.7],[87.3,92.4],color="k")
plt.plot([27.133,35.7],[85.3,90.4],color="k")
plt.plot([27.133,35.7],[99.3,103.4],color="k")
plt.plot([-27.133,-35.7],[73.3,78.4],color="k")
plt.plot([-27.133,-35.7],[87.3,92.4],color="k")
plt.plot([-27.133,-35.7],[85.3,90.4],color="k")
plt.plot([-27.133,-35.7],[99.3,103.4],color="k")
plt.plot([35.7,35.7],[92.4,103.4],color="k")
plt.plot([35.7,35.7],[90.4,78.4],color="k")
plt.plot([-35.7,-35.7],[92.4,103.4],color="k")
plt.plot([-35.7,-35.7],[90.4,78.4],color="k")
plt.plot([27.133,27.133],[87.3,99.3],color="k")
plt.plot([27.133,27.133],[85.3,73.3],color="k")
plt.plot([-27.133,-27.133],[87.3,99.3],color="k")
plt.plot([-27.133,-27.133],[85.3,73.3],color="k")
plt.plot([-23.133,-16.35],[86,86],color="k")
plt.plot([23.133,16.35],[86,86],color="k")
x1 = np.arange(-16.35,0,0.01)
y1 = 0.01*(x1+9)**3+90
plt.plot(x1,y1,color="k")
x2 = np.arange(0,16.35,0.01)
y2 = -0.01*(x2-9)**3+90
plt.plot(x2,y2,color="k")
plt.plot([-23.133,-23.133],[86,98],color="k")
plt.plot([23.133,23.133],[86,98],color="k")
plt.plot([-23.133,23.133],[98,98],color="k")
# base two base
x3 = np.arange(-29.83,29.83,0.01)
y3 = 1/400*(x3**2)+113
plt.plot(x3,y3,color="k")
x4 = np.arange(-32.281,32.281,0.01)
y4 = 1/400*(x4**2)+114
plt.plot(x4,y4,color="k")
#177 x5 = np.arange(-43.834,-29.83)
#y5 = 0.326*x5+105.5
#plt.plot(x5,y5,color="k")
# 178 x6
x7 = np.arange(-29.836,-25.095,0.001)
y7 = -0.937*x7+87.27
plt.plot(x7,y7,color="k")
x8 = np.arange(25.095,29.836,0.001)
y8 = 0.937*x8+87.27
plt.plot(x8,y8,color="k")
# capcap
#182 x9
#183 x10
#184 x11
#185 x12
#186 x13
x14 = np.arange(-10.392,-4.8,0.001)
y14 = -0.01*(x14**2)+197.16
plt.plot(x14,y14,color="k")
x15 = np.arange(4.8,10.392,0.001)
y15 = -0.01*(x15**2)+197.16
plt.plot(x15,y15,color="k")
x16 = np.arange(-22.321,22.321,0.001)
y16 = np.cos(1/3*x16)+175
plt.plot(x16,y16,color="k")
x17 = np.arange(-20.853,20.853,0.001)
y17 = np.cos(1/3*x17)+176
plt.plot(x17,y17,color="k")
#190 x18
#191 x19
#192 x20
#193 x21
# spire
plt.plot([0,0],[196,200],color="k")
y18 = np.arange(196.998,200.791,0.001)
x18 = (15+(y18-200)**2)**0.5
plt.plot(x18,y18,color="k")
plt.plot(-x18,y18,color="k")
plt.plot([-4.9,0],[196.98,196],color="k")
plt.plot([0,4.9],[196,196.98],color="k")
plt.plot([-3.953,0],[200.791,200],color="k")
plt.plot([0,3.953],[200,200.791],color="k")
x19 = np.arange(-5/3,-0.2,0.001)
y19 = (-6/5)*x19+206
plt.plot(x19,y19,color="k")
plt.plot(x19,y19+3,color="k")
plt.plot(x19,y19+6,color="k")
plt.plot(x19,y19+9,color="k")
plt.plot(x19,y19+12,color="k")
plt.plot(x19,y19+15,color="k")
plt.plot(x19,y19+18,color="k")
plt.plot(x19,y19+21,color="k")
plt.plot(x19,y19+24,color="k")
x20 = np.arange(0.2,5/3,0.001)
y20 = (6/5)*x20+206
plt.plot(x20,y20,color="k")
plt.plot(x20,y20+3,color="k")
plt.plot(x20,y20+6,color="k")
plt.plot(x20,y20+9,color="k")
plt.plot(x20,y20+12,color="k")
plt.plot(x20,y20+15,color="k")
plt.plot(x20,y20+18,color="k")
plt.plot(x20,y20+21,color="k")
plt.plot(x20,y20+24,color="k")
x21 = np.arange(-5/3,-0.2,0.001)
y21 = (-3/5)*x21+207
plt.plot(x21,y21,color="k")
plt.plot(x21,y21+3,color="k")
plt.plot(x21,y21+6,color="k")
plt.plot(x21,y21+9,color="k")
plt.plot(x21,y21+12,color="k")
plt.plot(x21,y21+15,color="k")
plt.plot(x21,y21+18,color="k")
plt.plot(x21,y21+21,color="k")
plt.plot(x21,y21+24,color="k")
x22 = np.arange(0.2,5/3,0.001)
y22 = (3/5)*x22+207
plt.plot(x22,y22,color="k")
plt.plot(x22,y22+3,color="k")
plt.plot(x22,y22+6,color="k")
plt.plot(x22,y22+9,color="k")
plt.plot(x22,y22+12,color="k")
plt.plot(x22,y22+15,color="k")
plt.plot(x22,y22+18,color="k")
plt.plot(x22,y22+21,color="k")
plt.plot(x22,y22+24,color="k")
plt.plot([0.2,0.2],[204.12,206.24],color="k")
plt.plot([0.2,0.2],[207.12,209.24],color="k")
plt.plot([0.2,0.2],[210.12,212.24],color="k")
plt.plot([0.2,0.2],[213.12,215.24],color="k")
plt.plot([0.2,0.2],[216.12,218.24],color="k")
plt.plot([0.2,0.2],[219.12,221.24],color="k")
plt.plot([0.2,0.2],[222.12,224.24],color="k")
plt.plot([0.2,0.2],[225.12,227.24],color="k")
plt.plot([0.2,0.2],[228.12,230.24],color="k")
plt.plot([0.2,0.2],[202.331,204.12],color="k")
plt.plot([-0.2,-0.2],[204.12,206.24],color="k")
plt.plot([-0.2,-0.2],[207.12,209.24],color="k")
plt.plot([-0.2,-0.2],[210.12,212.24],color="k")
plt.plot([-0.2,-0.2],[213.12,215.24],color="k")
plt.plot([-0.2,-0.2],[216.12,218.24],color="k")
plt.plot([-0.2,-0.2],[219.12,221.24],color="k")
plt.plot([-0.2,-0.2],[222.12,224.24],color="k")
plt.plot([-0.2,-0.2],[225.12,227.24],color="k")
plt.plot([-0.2,-0.2],[228.12,230.24],color="k")
plt.plot([-0.2,-0.2],[202.331,204.12],color="k")
#208 x23
#209 x24
plt.plot([-0.201,0.201],[242,242],color="k")
plt.plot([0,0],[242,248],color="k")
plt.plot([-0.3,0.3],[244,244],color="k")
plt.plot([-0.3,0.3],[245,245],color="k")
plt.plot([-0.3,0.3],[246,246],color="k")
plt.plot([-0.3,0.3],[247,247],color="k")
x25 = np.arange(0.2,3.952,0.001)
y25 = -(x25**0.5)+202.7785
plt.plot(x25,y25,color="k")
x26 = np.arange(-3.952,-0.2,0.001)
y26 = -((-x26)**0.5)+202.7785
plt.plot(x26,y26,color="k")
# something else
x27 = np.arange(-25.5,25.5,0.1)
y27 = 1/400*(x27**2)+120
plt.plot(x27,y27,color="k")
x28 = np.arange(-31.5,31.5,0.1)
y28 = 1/400*(x28**2)+121
plt.plot(x28,y28,color="k")
plt.plot([24.2,31.5],[131.136,123.523],color="k")
plt.plot([-31.5,-24.2],[123.523,131.136],color="k")
y29 = np.arange(127.639,131.183,0.001)
x29 = (2000-4*((y29-150)**2))**0.5
plt.plot(x29,y29,color="k")
plt.plot(-x29,y29,color="k")
y30 = np.arange(128.639,135.183,0.001)
x30 = (2000-4*((y30-151)**2))**0.5
plt.plot(x30,y30,color="k")
plt.plot(-x30,y30,color="k")
plt.plot([28.5,31.612],[136.598,135.183],color="k")
plt.plot([-31.612,-28.5],[135.183,136.598],color="k")
plt.plot([-31.6,-25.546],[123.48,121.664],color="k") 
plt.plot([25.546,31.6],[121.664,123.48],color="k")
#266 x31
#267 x32
#268 x33
#269 x34
plt.plot([45.362,48.398],[111.992,114.602],color="k")
plt.plot([-48.398,-45.362],[114.602,111.992],color="k")
#232 x35
#233 x36
plt.plot([-30.866,-24.347],[134.756,131.217],color="k")
plt.plot([24.347,30.866],[131.217,134.756],color="k")
# more stuff
#237 x37
#238 x38
#239 x39
#240 x40
plt.plot([41.2,42.995],[124.92,127.728],color="k")
plt.plot([-42.995,-41.2],[127.728,124.92],color="k")
x41 = np.arange(-42.878,-30.9,0.001)
y41 = 10*np.cos(0.068*(x41+7))+135.242
plt.plot(x41,y41,color="k")
x42 = np.arange(30.9,42.878,0.001)
y42 = 10*np.cos(0.068*(x42-7))+135.242
plt.plot(x42,y42,color="k")
# poles
plt.plot([-24.5,-24.5],[142.375,178.4],color="k")
plt.plot([-24.5,-24.5],[138.375,140.375],color="k")
plt.plot([-24.5,-24.5],[135,136.375],color="k")
plt.plot([24.5,24.5],[142.375,178.4],color="k")
plt.plot([24.5,24.5],[138.375,140.375],color="k")
plt.plot([24.5,24.5],[135,136.375],color="k")
plt.plot([-23.5,-23.5],[142.196,178],color="k")
plt.plot([-23.5,-23.5],[138.196,140.196],color="k")
plt.plot([-23.5,-23.5],[135,136.196],color="k")
plt.plot([23.5,23.5],[142.196,178],color="k")
plt.plot([23.5,23.5],[138.196,140.196],color="k")
plt.plot([23.5,23.5],[135,136.196],color="k")
#258
#259
# tree pillars
plt.plot([-0.5,-0.5],[130,140],color="k")
plt.plot([0.5,0.5],[130,140],color="k")
plt.plot([28.5,28.5],[135,145],color="k")
plt.plot([-28.5,-28.5],[135,145],color="k")
plt.plot([27.5,27.5],[135,145],color="k")
plt.plot([-27.5,-27.5],[135,145],color="k")
y43 = np.arange(129.711,130,0.001)
x43 = (0.25-3*((y43-130)**2))**0.5
plt.plot(x43,y43,color="k")
plt.plot(-x43,y43,color="k")
y44 = np.arange(134.711,135,0.001)
x44 = (0.25-3*((y44-135)**2))**0.5-28
plt.plot(x44,y44,color="k")
plt.plot(-x44,y44,color="k")
y45 = np.arange(134.711,135,0.001)
x45 = (0.25-3*((y45-135)**2))**0.5+28
plt.plot(x45,y45,color="k")
plt.plot(-x45,y45,color="k")
x46 = np.arange(-0.5,0.5,0.001)
y46 = 91/10*(x46**5)+140.284
plt.plot(x46,y46,color="k")
x47 = np.arange(27.5,28.5,0.001)
y47 = 91/10*((x47-28)**5)+145.284
plt.plot(x47,y47,color="k")
x48 = np.arange(-28.5,-27.5,0.001)
y48 = 91/10*((x48+28)**5)+145.284
plt.plot(x48,y48,color="k")
x49 = np.arange(-0.5,0.5,0.001)
y49 = -91/10*(x49**5)+140.284
plt.plot(x49,y49,color="k")
x50 = np.arange(27.5,28.5,0.001)
y50 = -91/10*((x50-28)**5)+145.284
plt.plot(x50,y50,color="k")
x51 = np.arange(-28.5,-27.5,0.001)
y51 = -91/10*((x51+28)**5)+145.284
plt.plot(x51,y51,color="k")
#276 52x
#277 53x
#278 54x

# AAAAAAAAAAA
plt.plot([-27.5,-0.5],[142.911,138.089],color="k")
plt.plot([0.5,27.5],[138.089,142.911],color="k")
plt.plot([-27.5,-0.5],[140.911,136.089],color="k")
plt.plot([0.5,27.5],[136.089,140.911],color="k")
plt.plot([-27.5,-0.5],[138.911,134.089],color="k")
plt.plot([0.5,27.5],[134.089,138.911],color="k")
plt.plot([-27.5,-0.5],[136.911,132.089],color="k")
plt.plot([0.5,27.5],[132.089,136.911],color="k")
plt.plot([-20.5,-20.5],[133.661,135.661],color="k")
plt.plot([-13.5,-13.5],[132.411,134.411],color="k")
plt.plot([-6.5,-6.5],[131.161,133.161],color="k")
plt.plot([7.5,7.5],[131.339,133.339],color="k")
plt.plot([14.5,14.5],[132.589,134.589],color="k")
plt.plot([21.5,21.5],[133.839,135.839],color="k")
plt.plot([20.5,20.5],[133.661,135.661],color="k")
plt.plot([13.5,13.5],[132.411,134.411],color="k")
plt.plot([6.5,6.5],[131.161,133.161],color="k")
plt.plot([-7.5,-7.5],[131.339,133.339],color="k")
plt.plot([-14.5,-14.5],[132.589,134.589],color="k")
plt.plot([-21.5,-21.5],[133.839,135.839],color="k")
# 291
plt.xlim(-150,150) 
plt.ylim(-7,250)
plt.show()