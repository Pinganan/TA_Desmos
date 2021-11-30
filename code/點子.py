import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7, 8.5))
#手的輪廓----------------------------------------------------------------#
def ho1(x):return 0.5*x + 6.15
def ho2(x):return 0.125*x + 2.925
def ho4(x):return 2/17*x + 2379/850
def ho5(x):return 1/4*x + 3.6
def ho6(x):return 10/13*x + 396/65
def ho7(x):return 0*x + 2.82
def ho8(x):return 1/3*x + 4.22
def ho10(x):return 1/9*x + 3.82
def ho11(x):return 0*x + 3.74
def ho12(x):return -1/9*x + 3.695
def ho16(y):return 50/13*y - 10.88
def ho18(y):return 0*y + 5
def ho21(x):return 0.03*x + 1.53
def ho24(x):return -1/7*x + 1.504
def ho26(y):return 10/13*y + 5
def ho27(y):return y + 4.54
def ho28(x):return 0.4*x - 0.37
def ho30(x):return 0*x + 2.55
def ho31(y):return 0*y + 7.857
def ho32(x):return 0.3*x - 0.2
def ho33(x):return 0*x + 2.26
def ho34(x):return -0.4*x + 5.58
def ho35(y):return 0*y + 8.56
def ho36(x):return 0.8*x - 4.97
def ho37(x):return 0.5*x - 2.24
def ho38(x):return 0.1*x + 1.56
def ho40(y):return 1/2*y + 9.115
def ho41(y):return 10/13*y + 227/26
def ho42(x):return 1/3*x - 2.05
def ho44(x):return 0.6*x - 6.2
def ho47(y):return 10/23*y + 10.459
def ho49(x):return 0.5*x - 5.25
def ho50(x):return 10/29*x - 4.194
def ho52(x):return 10/12*x - 6
def ho54(x):return 10/18*x - 5.085
def ho55(x):return -0.3*x - 2.69
def ho56(x):return -0.06*x - 2.75
def ho57(x):return -0.2*x - 3.03
def ho58(x):return 0*x - 2.4
def ho59(x):return -0.16*x - 2.97
def ho61(x):return 0.3*x - 0.62
def ho62(x):return 0.6*x + 1.8
def ho64(y):return 1/3*y - 5.3083
def ho65(x):return 1/3*x + 1.9
def ho66(x):return 1/2*x + 3.14
def ho67(x):return 1/15*x + 1.47
def ho68(x):return 1/5*x + 2.34
def ho69(x):return 0.7/1*x + 5.76
def ho70(x):return -0.08*x + 2.51
def ho72(x):return -1/7*x + 1.1
def ho77(x):return -1/3.1*x + 0.3599
def ho78(x):return -1/3*x + 0.5
def ho79(x):return -1/2*x + 0.67
def ho80(y):return -1/2*y + 1/2
def ho81(x):return -x + 3.53
def ho82(x):return -1/2*x + 3.23
def ho83(y):return -1/2*y + 2.455
def ho84(y):return -y + 3.8
def ho85(y):return -y + 3.84
def ho86(y):return -1/2*y + 3.05
def ho87(y):return 0*y + 2.2
def ho89(y):return -1/3*y + 3.5
def ho91(x):return x - 1.6
def ho92(y):return -y + 5.2
def ho93(x):return 1/14*x + 0.47
def ho94(x):return 1/2*x - 4.64
def ho95(x):return 1/3*x - 3.3
def ho96(x):return 1/7*x - 1.4
def ho98(y):return 13/10*y + 6.64*13/10
def ho99(x):return 1/2*x - 4.23
def ho100(y):return 10/18*y + 9
def ho101(x):return x - 7.3
def ho102(x):return 1/4*x - 0.3
def ho104(x):return -1/6*x + 0.656
def ho105(x):return -1/19*x + 0.33
def ho107(x):return 1/2*x - 2
def ho108(x):return x - 3.88
def ho109(x):return 2*x - 6.7
def ho111(x):return 1/2.6*x - 1.58
def ho112(x):return 1.2*x - 6.53
def ho113(x):return 0.9*x - 4.55
def ho115(x):return 2*x - 14.2
def ho116(x):return 1.2*x - 8.5
def ho117(y):return 1/2*y + 7.45
def ho119(x):return x - 7.25
def ho121(y):return y + 7.13
def ho124(x):return 1/14*x - 2.15
def ho125(x):return 1/3*x - 3.36
def ho126(x):return 1/1.8*x - 4.14
def ho128(x):return -1/5*x - 2.276
#-------------------------------#設定區
xr = np.linspace(-10, -8.6, 1000)
yr = ho1(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-8.6, -7.705, 1000)
yr = ho2(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-6, -7.1, 1000)
yr = ho4(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-4.8, -6.01, 1000)
yr = ho5(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-4.3, -4.8, 1000)
yr = ho6(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-3.85, -4.2, 1000)
yr = ho7(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-4.2, -4.3, 1000)
yr = ho8(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-2.9, -0.7, 1000)
yr = ho10(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-0.75, -0.4, 1000)
yr = ho11(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-0.409, -0.18, 1000)
yr = ho12(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(3.237, 3.487, 1000)
xr = ho16(yr)
plt.plot(xr,yr,"k-")

yr = np.linspace(2.47, 3, 1000)
xr = ho18(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(2.25, 3.33, 1000)
yr = ho21(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(4.3, 4.85, 1000)
yr = ho24(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(0.877, 2, 1000)
xr = ho26(yr)
plt.plot(xr,yr,"k-")

yr = np.linspace(2, 2.4, 1000)
xr = ho27(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(6.94, 7.3, 1000)
yr = ho28(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(7.3, 7.51, 1000)
yr = ho30(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(2.16, 2.35, 1000)
xr = ho31(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(7.86, 8.2, 1000)
yr = ho32(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(8.2, 8.3, 1000)
yr = ho33(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(8.3, 8.56, 1000)
yr = ho34(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(1.77, 2.155, 1000)
xr = ho35(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(8.56, 9.1, 1000)
yr = ho36(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(9.1, 9.4, 1000)
yr = ho37(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(9.5, 9.82, 1000)
yr = ho38(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(1.43, 2.15, 1000)
xr = ho40(yr)
plt.plot(xr,yr,"k-")

yr = np.linspace(1.2, 1.43, 1000)
xr = ho41(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(9.67, 10.88, 1000)
yr = ho42(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(10.99, 11.75, 1000)
yr = ho44(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(-0.21, -0.09, 1000)
xr = ho47(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(6.8, 8.599, 1000)
yr = ho49(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(6, 6.8, 1000)
yr = ho50(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(3.3, 4.084, 1000)
yr = ho52(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(3.083, 3.3, 1000)
yr = ho54(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(0.25, 2.53, 1000)
yr = ho55(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-2, 0.25, 1000)
yr = ho56(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-3.1, -2, 1000)
yr = ho57(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-3.6, -3.1, 1000)
yr = ho58(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-4.2, -3.56, 1000)
yr = ho59(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-8.1, -5.55, 1000)
yr = ho61(xr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-9.7, -8.1, 1000)
yr = ho62(xr)
plt.plot(xr,yr,"k-")

yr = np.linspace(0.3, 1.2, 1000)
xr = ho64(yr)
plt.plot(xr,yr,"k-")

xr = np.linspace(-7.4, -5.26, 1000)
yr = ho65(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-7.99, -7.4, 1000)
yr = ho66(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-7.9, -7.4, 1000)
y7 = ho67(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-7.3, -6.5, 1000)
yr = ho68(xr)
plt.plot(xr,yr,'-k')

xr = np.linspace(-5.67, -4.8, 1000)
yr = ho69(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-3.85, -3.7, 1000)
yr = ho70(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-3, -2.16, 1000)
yr = ho72(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(1.005, 1.29, 1000)
yr = ho79(xr)
plt.plot(xr,yr,'-k')

xr = np.linspace(-2.07, -1.3, 1000)
yr = ho77(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(-0.3, 1, 1000)
yr = ho78(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(1.005, 1.29, 1000)
yr = ho79(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(0.1, 0.4, 1000)
xr = ho80(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(0.3, 0.6, 1000)
yr = ho81(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(0.5999, 1.27, 1000)
yr = ho82(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(2.68, 3.2, 1000)
xr = ho83(yr)
plt.plot(xr,yr,'k-')

yr = np.linspace(2.69, 3.1, 1000)
xr = ho84(yr)
plt.plot(xr,yr,'k-')

yr = np.linspace(1.66, 2, 1000)
xr = ho85(yr)
plt.plot(xr,yr,'k-')

yr = np.linspace(2.1, 1.555, 1000)
xr = ho86(yr)
plt.plot(xr,yr,'k-')

yr = np.linspace(1.7, 2.4, 1000)
xr = ho87(yr)
plt.plot(xr,yr,'k-')

yr = np.linspace(2.5, 2.9, 1000)
xr = ho89(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2, 2.5, 1000)
yr = ho91(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(0.5, 0.9, 1000)
xr = ho92(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(5.68, 5.99, 1000)
yr = ho93(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(5.68, 5.99, 1000)
yr = ho93(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(11.4, 11.59, 1000)
yr = ho94(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(9.8, 10, 1000)
yr = ho95(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(10, 10.1, 1000)
yr = ho96(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(-0.5, -0.08, 1000)
xr = ho98(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(10, 10.1, 1000)
yr = ho96(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(8.84, 9.2, 1000)
yr = ho99(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(0.38, 1.2, 1000)
xr = ho100(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(9.67, 9.84, 1000)
yr = ho101(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(0.8, 1.7, 1000)
yr = ho102(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(0.8, 1.7, 1000)
yr = ho102(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2.43, 2.85, 1000)
yr = ho104(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2.85, 3.3, 1000)
yr = ho105(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2.97, 3.6, 1000)
yr = ho107(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2.8, 3.7, 1000)
yr = ho108(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(2.7, 2.822, 1000)
yr = ho109(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(4.25, 6.07, 1000)
yr = ho111(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(6.07, 6.6, 1000)
yr = ho112(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(6.6, 7.139, 1000)
yr = ho113(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(8.16, 8.23, 1000)
yr = ho115(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(8, 8.56, 1000)
yr = ho116(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(0.4, 1.1, 1000)
xr = ho117(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(7.45, 7.653, 1000)
yr = ho119(xr)
plt.plot(xr,yr,'k-')

yr = np.linspace(-1.319, -0.04, 1000)
xr = ho121(yr)
plt.plot(xr,yr,'k-')

xr = np.linspace(4.6, 5.01, 1000)
yr = ho124(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(3.5, 4.6, 1000)
yr = ho125(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(3.15, 3.511, 1000)
yr = ho126(xr)
plt.plot(xr,yr,'k-')

xr = np.linspace(1.4, 2.1, 1000)
yr = ho128(xr)
plt.plot(xr,yr,'k-')


plt.plot([-6.5,-4.94],[1.039,1.125],color="black")
#-------------------------------#圓,二元二次
#ho3
x=np.linspace(-7.705,-7.1,1000)
y=np.linspace(1.95,1.962,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+7.4)**2+(4*y-8.8)**2,[1],colors=["k"])
#ho9
x=np.linspace(-4.2,-2.9,1000)
y=np.linspace(2.822,3.49,1000)
x,y=np.meshgrid(x,y)
plt.contour(x, y,(1.1*x+2.32)**2 + (y - 0.999)**2,[7],colors=["k"])
#ho13
x=np.linspace(-0.18,0.294,1000)
y=np.linspace(3.237,3.712,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(1.5*x+1)**2+(y-1.85)**2,[2**2],colors=["k"])
#ho14
x=np.linspace(0.1564,1.584,1000)
y=np.linspace(3.23,3.423,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x)**2+(4*y-11.7)**2,[2**2],colors=["k"])
#ho15
x=np.linspace(2.5209,4.99,1000)
y=np.linspace(3.05,3.5,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-3)**2+(4*y-12)**2,[2**2],colors=["k"])
#ho17
x=np.linspace(4.244,5,1000)
y=np.linspace(1.681,2.48,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-4.2)**2+(y-2.48)**2,[0.8**2],colors=["k"])
#ho19
x=np.linspace(3.759,4.244,1000)
y=np.linspace(1.682,1.707,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-4)**2+(1.5*y-1.76)**2,[0.8**2],colors=["k"])
#ho20
x=np.linspace(3.328,3.795,1000)
y=np.linspace(1.6125,1.6818,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-3.466)**2+(0.8*y-2.09)**2,[0.8**2],colors=["k"])
#ho22
x=np.linspace(2.176,2.5,1000)
y=np.linspace(1,1.6573,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-1.6)**2+(0.9*y-0.8)**2,[0.9**2],colors=["k"])
#ho23
x=np.linspace(2.5,4.29,1000)
y=np.linspace(0.891,1,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-3.4)**2+(5*y-4)**2,[1**2],colors=["k"])
#ho25
x=np.linspace(4.84,5.91,1000)
y=np.linspace(0.802,0.9,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(0.8*x-4.3)**2+(y+0.1)**2,[1**2],colors=["k"])
#ho29
x=np.linspace(7.855,7.509,1000)
y=np.linspace(2.3556,2.5511,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-7.2)**2+(y-1.6)**2,[1**2],colors=["k"])
#ho39
x=np.linspace(9.84,10.19,1000)
y=np.linspace(2.156,2.5404,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-9.3)**2+(y-1.7)**2,[1**2],colors=["k"])
#ho43
x=np.linspace(10.904,11.748,1000)
y=np.linspace(0.85,1.5922,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-10.78)**2+(y-0.6)**2,[1**2],colors=["k"])
#ho45
x=np.linspace(10.417,10.99,1000)
y=np.linspace(-0.0942,0.3954,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-12.5)**2+(y+2)**2,[8],colors=["k"])
#ho46
x=np.linspace(9.652,10.368,1000)
y=np.linspace(-0.54,-0.216,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-9.9)**2+(y+0.04)**2,[0.5**2],colors=["k"])
#ho48
x=np.linspace(8.6,9.9,1000)
y=np.linspace(-0.943,-0.542,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-10)**2+(y+3.14)**2,[2.6**2],colors=["k"])
#ho51
x=np.linspace(3.93,6.87,1000)
y=np.linspace(-2.6,-1.421,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-4.2399)**2+(y-0.9)**2,[3.5**2],colors=["k"])
#ho53
x=np.linspace(2.54,3.08,1000)
y=np.linspace(-3.5,-3.384,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-2.75)**2+(y+3)**2,[0.5**2],colors=["k"])
#ho60
x=np.linspace(-5.59,-4.208,1000)
y=np.linspace(-2.2997,-2.22,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+4.9)**2+(5*y+11.9)**2,[0.8**2],colors=["k"])
#ho63
x=np.linspace(-5.3,-5.18,1000)
y=np.linspace(-0.824,0.368,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+3.3)**2+(y+0.3)**2,[2**2],colors=["k"])
#ho71
x=np.linspace(-3.694,-3.1,1000)
y=np.linspace(2.75,2.8043,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+3.37)**2+(y-3.75)**2,[1],colors=['k'])
#ho73
x=np.linspace(-2.13,0,1000)
y=np.linspace(0.6,1.4,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+0.3)**2+(y-3.1)**2,[2.5**2],colors=['k'])
#ho74
x=np.linspace(-1.024,0.224,1000)
y=np.linspace(0.8,0.9,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+0.4)**2+(y-2.8)**2,[2**2],colors=['k'])
#ho75
x=np.linspace(0,0.88,1000)
y=np.linspace(0.619,0.779,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+0)**2+(y-3.119)**2,[2.5**2],colors=['k'])
#ho76
x=np.linspace(-3.6,-2.065,1000)
y=np.linspace(1,1.2,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x+2.8)**2+(3*y-2.4)**2,[1],colors=['k'])
#ho88
x=np.linspace(2.377,2.8,1000)
y=np.linspace(1.8819,2.8167,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-1.8)**2+(y-2)**2,[1],colors=['k'])
#ho90
x=np.linspace(2.892,2.951,1000)
y=np.linspace(2.201,2.491,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-2.26)**2+(y-2.19)**2,[0.7**2],colors=['k'])
#ho97
x=np.linspace(6.886,8.84,1000)
y=np.linspace(-1.418,0.2,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-6.2)**2+(y-1.4)**2,[2.9**2],colors=['k'])
#ho103
x=np.linspace(1.713,2.425,1000)
y=np.linspace(0.1302,0.3,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-2.17)**2+(y+0.4)**2,[0.7**2],colors=['k'])
#ho106
x=np.linspace(3.2,3.9,1000)
y=np.linspace(-0.11,0.16,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-3.2)**2+(y+0.84)**2,[1],colors=['k'])
#ho110
x=np.linspace(3.19,4.3,1000)
y=np.linspace(-0.94992,0.062,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-5)**2+(y+1.8)**2,[2**2],colors=['k'])
#ho114
x=np.linspace(7.137,7.858,1000)
y=np.linspace(1.8702,2.15,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-7.84)**2+(y-1.159)**2,[1],colors=['k'])
#ho118
x=np.linspace(7.263,7.7,1000)
y=np.linspace(0.4336,0.75,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-7.7)**2+(y-0.29)**2,[0.46**2],colors=['k'])
#ho120
x=np.linspace(7.092,7.449,1000)
y=np.linspace(-0.0389,0.1996,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-7.7)**2+(y+0.56)**2,[0.8**2],colors=['k'])
#ho122
x=np.linspace(5.011,5.817,1000)
y=np.linspace(-1.789,-1.3106,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-4.85)**2+(y+0.6)**2,[1.2**2],colors=['k'])
#ho123
x=np.linspace(4.453,5.379,1000)
y=np.linspace(-0.2999,0.05,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-5.3)**2+(y+1.15)**2,[1.2**2],colors=['k'])
#ho127
x=np.linspace(2.105,3.151,1000)
y=np.linspace(-2.74,-2.4003,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-2.4)**2+(y+1.74)**2,[1],colors=['k'])

#Lightbulb 輪廓----------------------------------------------------------------#

#sin 圖形
x = np.linspace(2.6,5.022,1000)
y = (-0.09*np.sin(7*x+3)+16.84)
plt.plot(x, y, 'k')

x = np.linspace(0.1945,7.41,1000)
y = np.linspace(14.253,20.156,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.8)**2+(y-16.55)**2,[13],colors=["k"])


x = np.linspace(1.0167,1.75,1000)
y = np.linspace(14.258,11.962,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x+2.13)**2+(y-12)**2,[15],colors=["k"])

x = np.linspace(5.85,6.583,1000)
y = np.linspace(11.876,14.258,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-9.73)**2+(y-12)**2,[15],colors=["k"])

x = np.linspace(1.67,2.096,1000)
y = np.linspace(11.958,10.95,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-2.453)**2+(y-11.65)**2,[0.6],colors=["k"])

x = np.linspace(5.54,5.895,1000)
y = np.linspace(10.98,11.86,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-5.119)**2+(y-11.63)**2,[0.6],colors=["k"])

x = np.linspace(2.06,5.533,1000)
y = np.linspace(10.978,10.567,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.8)**2+(2*y-23.37)**2,[5],colors=["k"])

x = np.linspace(2.1694,2.2509,1000)
y = np.linspace(10.7,10.879,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-2.34)**2+(y-10.73)**2,[0.03],colors=["k"])

plt.plot([2.1701,2.2799],[10.699,9.711],color="black")

plt.plot([5.243,5.241],[10.48,10.83],color="black")


x = np.linspace(5.2,5.32,1000)
y = np.linspace(10.136,10.399,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-5.144)**2+(y-10.3)**2,[0.03],colors=["k"])

plt.plot([5.203,5.269],[10.136,10.037],color="black")

plt.plot([5.269,5.269],[10.036,9.951],color="black")

plt.plot([5.27,5.339],[9.948,9.81],color="black")

plt.plot([5.338,5.201],[9.809,9.74],color="black")


x = np.linspace(2.21,2.282,1000)
y = np.linspace(9.369,9.72,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-2.5)**2+(y-9.533)**2,[0.08],colors=["k"])

x = np.linspace(5.2,5.34,1000)
y = np.linspace(9.33,9.741,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-5.11)**2+(y-9.537)**2,[0.05],colors=["k"])

plt.plot([5.204,5.228],[9.304,9.091],color="black")

plt.plot([5.13,5.229],[9.067,9.091],color="black")


x = np.linspace(2.2085,2.2689,1000)
y = np.linspace(8.94,9.371,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(2*x-5.05)**2+(y-9)**2,[0.4],colors=["k"])

plt.plot([5.117,5.13],[8.905,9.061],color="black")


x = np.linspace(5.114,4.501,1000)
y = np.linspace(8.899,8.431,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-4.4)**2+(y-9.199)**2,[0.6],colors=["k"])

x = np.linspace(2.2202,2.799,1000)
y = np.linspace(8.9,8.447,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-2.93)**2+(y-9.21)**2,[0.6],colors=["k"])

x = np.linspace(2.76,4.6,1000)
y = np.linspace(8.351,8.45,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-18.938)**2,[5],colors=["k"])

x = np.linspace(3.221,4.078,1000)
y = np.linspace(8.053,8.375,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.65)**2+(y-8.5)**2,[0.2],colors=["k"])

x = np.linspace(2.8,5.129,1000)
y = np.linspace(8.777,9.043,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-19.79)**2,[5],colors=["k"])

x = np.linspace(2.24,5.2,1000)
y = np.linspace(9.03,9.325,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-20.3)**2,[5],colors=["k"])

x = np.linspace(2.27,5.21,1000)
y = np.linspace(9.44,9.75,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-21.13)**2,[5],colors=["k"])

x = np.linspace(2.24,5.25,1000)
y = np.linspace(9.83,10.5,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-21.91)**2,[5],colors=["k"])

x = np.linspace(3.769,2.182,1000)
y = np.linspace(10.233,10.52,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.68)**2+(2*y-22.7)**2,[5],colors=["k"])

plt.plot([3.14,3.14],[12.699,10.618],color="black")

plt.plot([4.33,4.33],[12.981,10.6],color="black")


x = np.linspace(2.97,3.132,1000)
y = np.linspace(12.699,13.125,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.2)**2+(y-12.912)**2,[0.049],colors=["k"])

plt.plot([3.14,3.14],[13.599,13.131],color="black")


x = np.linspace(3.1395,3.249,1000)
y = np.linspace(13.59,13.699,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.239)**2+(y-13.6)**2,[0.01],colors=["k"])

plt.plot([3.231,4.399],[13.7,13.7],color="black")


x = np.linspace(4.391,4.546,1000)
y = np.linspace(13.7,13.456,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(1.2*x-5.26)**2+(y-13.5)**2,[0.04],colors=["k"])

plt.plot([4.33,4.545],[12.981,13.454],color="black")


x = np.linspace(3.4,3.61,1000)
y = np.linspace(13.7,13.879,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.39)**2+(y-13.9209)**2,[0.049],colors=["k"])

x = np.linspace(3.983,4.2,1000)
y = np.linspace(13.7,13.879,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-4.2)**2+(y-13.9209)**2,[0.049],colors=["k"])

plt.plot([3.501,4.099],[14.8,14.8],color="black")
plt.plot([3.608,3.7],[13.879,14.7],color="black")
plt.plot([3.9823,3.868],[13.879,14.7],color="black")
plt.plot([2.59,3.41],[16.899,13.7],color="black")
plt.plot([4.205,5.025],[13.7,16.898],color="black")
plt.plot([4.101,4.605],[14.804,16.77],color="black")
plt.plot([2.9971,3.499],[16.761,14.804],color="black")


x = np.linspace(1.19,2.7,1000)
y = np.linspace(15.98,18.94,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.2)**2+(y-17)**2,[4],colors=["k"])

x = np.linspace(1.2,2.7,1000)
y = np.linspace(15.98,18.94,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-3.8)**2+(y-16.75)**2,[6],colors=["k"])

plt.plot([1.9301,2.4999],[12.71,11],color="black")


x = np.linspace(1.96,2.4754,1000)
y = np.linspace(12.121,11.08,1000)
x,y = np.meshgrid(x,y)
plt.contour(x,y,(x-2.6)**2+(y-11.7)**2,[0.4],colors=["k"])

plt.plot([5.243,5.29],[10.39,10.84],color="black")

x=np.linspace(1.468,2.69,1000)
y=np.linspace(15.999,18.934,1000)
x,y=np.meshgrid(x,y)
plt.contour(x,y,(x-3.2)**2+(y-17)**2,[4],colors=['k'])





#手的陰影
plt.plot([-5.175,-5.8],[1.125,0.5],color="black")
plt.plot([-4.963,-5.5],[1.037,0.5],color="black")
plt.plot([-6.3,-6.5],[-0.2,-0.4],color="black")
plt.plot([-5.85,-6.2],[-0.05,-0.4],color="black")
plt.plot([-5.4,-5.97],[0.1,-0.47],color="black")
plt.plot([-5.289,-5.6],[-0.089,-0.4],color="black")
plt.plot([-5.29,-5.4],[-0.49,-0.6],color="black")
plt.plot([-4.367,-5.1],[2.733,2],color="black")
plt.plot([-4.06,-4.7],[2.82,2.18],color="black")
plt.plot([-3.787,-4.3],[2.813,2.3],color="black")
plt.plot([-3.536,-4],[2.764,2.3],color="black")
plt.plot([-3.242,-3.6],[2.758,2.4],color="black")
plt.plot([-2.888,-3.314],[1.512,1.086],color="black")
plt.plot([-2.713,-3.08],[1.487,1.12],color="black")
plt.plot([-2.45,-2.767],[1.45,1.133],color="black")
plt.plot([-2.188,-2.484],[1.412,1.116],color="black")
plt.plot([-2.017,-2.227],[1.283,1.073],color="black")
plt.plot([-1.856,-2],[1.144,1],color="black")
plt.plot([0.122,0],[0.622,0.5],color="black")
plt.plot([0.343,0.15],[0.643,0.45],color="black")
plt.plot([0.589,0.3],[0.689,0.4],color="black")
plt.plot([0.525,0.9],[0.325,0.7],color="black")
plt.plot([0.75,1.3],[0.25,0.8],color="black")
plt.plot([0.975,1.6],[0.175,0.8],color="black")
plt.plot([1.18,1.5],[0.08,0.4],color="black")
plt.plot([-1.55,-1.68],[3.65,3.52],color="black")
plt.plot([-1.325,-1.54],[3.675,3.46],color="black")
plt.plot([-0.987,-1.4],[3.713,3.3],color="black")
plt.plot([-0.64,-1.2],[3.74,3.18],color="black")
plt.plot([-0.364,-1],[3.736,3.1],color="black")
plt.plot([-0.123,-0.7],[3.677,3.1],color="black")
plt.plot([0.043,-0.4],[3.543,3.1],color="black")
plt.plot([0.187,-0.1],[3.387,3.1],color="black")
plt.plot([0.527,-0.1],[3.407,2.78],color="black")
plt.plot([0.785,0.2],[3.385,2.8],color="black")
plt.plot([1.221,0.5],[3.321,2.6],color="black")
plt.plot([1.543,0.8],[3.243,2.5],color="black")
plt.plot([2.068,1],[3.368,2.3],color="black")
plt.plot([2.486,1],[3.476,1.99],color="black")
plt.plot([2.899,1.3],[3.499,1.9],color="black")
plt.plot([3.295,1.4],[3.495,1.6],color="black")
plt.plot([3.671,1.6],[3.471,1.4],color="black")
plt.plot([4.029,1.8],[3.429,1.2],color="black")
plt.plot([4.365,2.608],[3.365,1.608],color="black")
plt.plot([4.674,3.021],[3.274,1.621],color="black")
plt.plot([4.931,3.415],[3.131,1.615],color="black")
plt.plot([5,3.903],[2.8,1.703],color="black")
plt.plot([4.999,4.233],[2.449,1.683],color="black")
plt.plot([2.383,2.2],[1.383,1.2],color="black")
plt.plot([2.483,2],[1.083,0.6],color="black")
plt.plot([2.847,2.18],[0.967,0.3],color="black")
plt.plot([3.196,2.448],[0.996,0.248],color="black")
plt.plot([3.499,2.705],[0.999,0.205],color="black")
plt.plot([3.785,2.974],[0.985,0.174],color="black")
plt.plot([4.052,3.259],[0.952,0.159],color="black")
plt.plot([4.291,3.511],[0.891,0.111],color="black")
plt.plot([4.554,3.716],[0.854,0.016],color="black")
plt.plot([3.887,4.816],[-0.113,0.816],color="black")
plt.plot([5.189,4.42],[0.889,0.12],color="black")
plt.plot([5.495,4.907],[0.895,0.307],color="black")
plt.plot([5.395,7.45],[0.495,2.55],color="black")
plt.plot([6,7.217],[1.3,2.517],color="black")
plt.plot([5.72,7.611],[0.62,2.511],color="black")
plt.plot([7.302,7.741],[2.002,2.441],color="black")
plt.plot([7.69,7.857],[2.14,2.307],color="black")
plt.plot([3.81,4.3],[-2.09,-1.6],color="black")
plt.plot([4.26,4.8],[-1.94,-1.4],color="black")
plt.plot([4.62,5.6],[-1.82,-0.84],color="black")
plt.plot([5.011,7],[-1.789,0.2],color="black")
plt.plot([5.477,7.8],[-1.623,0.7],color="black")
plt.plot([8.1,7],[1.22,0.12],color='black')
plt.plot([8.56,7.5],[1.96,0.9],color='black')
plt.plot([8.557,8],[2.157,1.6],color='black')


plt.plot([-1.9,-2.444], [-2.0,-2.544],color="black")
plt.plot([-1.8,-2.2], [-2.2,-2.6 ],color="black")
plt.plot([-1.3,-1.94], [-2.0,-2.64 ],color="black")
plt.plot([-1.3,-1.66], [-2.29,-2.56],color="black")
plt.plot([-0.7,-1.29], [-2.09,-2.68],color="black")
plt.plot([-0.6,-0.99], [-2.3,-2.69],color="black")
plt.plot([-0.17,-0.7], [-2.17,-2.7],color="black")
plt.plot([-0.1,-0.42], [-2.4,-2.72],color="black")
plt.plot([-0.04,0.44], [-2.74,-2.26],color="black")
plt.plot([0.26,0.55], [-2.74,-2.45],color="black")
plt.plot([0.99,0.47], [-2.31,-2.83],color="black")
plt.plot([1.1,0.78], [-2.6,-2.92],color="black")
plt.plot([1.5,1.065], [-2.57,-3.005],color="black")
plt.plot([1.25,1.46], [-3.05,-2.84],color="black")
plt.plot([1.515,1.99], [-3.145,-2.67],color="black")
plt.plot([1.777,2.269], [-3.223,-2.731],color="black")
plt.plot([2.008,2.577], [-3.292,-2.723],color="black")
plt.plot([2.238,3.28], [-3.362,-2.32],color="black")
plt.plot([2.39,3.66], [-3.41,-2.14],color="black")
plt.plot([2.618,4.11], [-3.482,-1.99],color="black")
plt.plot([2.936,4.56], [-3.464,-1.84],color="black")
plt.plot([4.103,4.9], [-2.597,-1.8],color="black")
plt.plot([4.404,5.1], [-2.596,-1.9],color="black")
plt.plot([4.735,5.3], [-2.565,-2],color="black")
plt.plot([5.07,5.77], [-2.5,-1.8],color="black")
plt.plot([5.397,6.4], [-2.403,-1.4],color="black")
plt.plot([5.736,6.99], [-2.264,-1.01],color="black")
plt.plot([6.266,7.5], [-1.954,-0.72],color="black")
plt.plot([7.018,8.5], [-1.382,0.1],color="black")
plt.plot([7.329,9.5], [-1.271,0.9],color="black")
plt.plot([7.747,8.653], [-1.053,0.153],color="black")
plt.plot([8.94,9.375], [0.24,0.675],color="black")
plt.plot([9.83,8.99], [1.43,0.59],color="black")
plt.plot([10.03,9.2], [1.83,1],color="black")
plt.plot([10.178,9.4], [2.178,1.4],color="black")
plt.plot([10.1,9.7], [2.3,1.9],color="black")
plt.plot([7.165,6.572], [-1.335,-1.928],color="black")
plt.plot([7.516,6.9], [-1.184,-1.8],color="black")
plt.plot([7.48,8.2], [-1.51,-0.79],color="black")
plt.plot([7.9,8.8], [-1.3,-0.4],color="black")
plt.plot([8.5,9.1], [-1,-0.4],color="black")
plt.plot([8.929,9.5], [-0.771,-0.2],color="black")
plt.plot([9.249,9.77], [-0.651,-0.13],color="black")
plt.plot([9.514,10.5], [-0.586,0.4],color="black")
plt.plot([9.737,11], [-0.553,0.71],color="black")
plt.plot([9.964,10.5], [-0.536,0],color="black")
plt.plot([10.84,11.647], [0.29,1.097],color="black")
plt.plot([11.425,11.718], [0.655,0.948],color="black")
plt.plot([-2.775,-2.16], [-2.475,-1.86],color="black")
plt.plot([-3.1,-2.6], [-2.4,-1.9],color="black")
plt.plot([-3.5,-2.7], [-2.4,-1.6],color="black")
plt.plot([-3.853,-2.9], [-2.353,-1.4],color="black")
plt.plot([-4.198,-3.4], [-2.298,-1.5],color="black")
plt.plot([-4.537,-3.8], [-2.237,-1.5],color="black")
plt.plot([-5.105,-4.4], [-2.225,-1.52],color="black")
plt.plot([-5.6,-4.7], [-2.3,-1.4],color="black")
plt.plot([-4.821,-4.3], [-2.221,-1.7],color="black")
plt.plot([-6.029,-5.2], [-2.429,-1.6],color="black")
plt.plot([-6.457,-5.7], [-2.557,-1.8],color="black")
plt.plot([-6.743,-5.8], [-2.643,-1.7],color="black")
plt.plot([-7.171,-6.3], [-2.771,-1.9],color="black")
plt.plot([-8.029,-7.3], [-3.029,-2.3],color="black")
plt.plot([-8.625,-7.8], [-3.375,-2.55],color="black")
plt.plot([-9.2,-8.3], [-3.72,-2.82],color="black")
plt.plot([-9.65,-8.6], [-3.99,-2.94],color="black")
plt.plot([-6.825,-7.3], [0.975,0.5],color="black")
plt.plot([-6.032,-6.7], [1.068,0.4],color="black")
plt.plot([-5.604,-6.3], [1.096,0.4],color="black")
plt.plot([-4.963,-5.5], [1.037,0.5],color="black")





#Lightbulb的陰影----------------------------------------------------------------#
plt.plot([3.275,4.033],[8.275,9.044],color="black")
plt.plot([2.21,2.43],[9,9.22],color="black")
plt.plot([2.283,2.65],[8.783,9.15],color="black")
plt.plot([2.43,2.902],[8.63,9.102],color="black")
plt.plot([2.606,3.16],[8.506,9.06],color="black")
plt.plot([2.834,3.439],[8.434,9.039],color="black")
plt.plot([3.12,3.73],[8.4,9.01],color="black")

plt.plot([3.42,4.387],[8.12,9.09],color="black")
plt.plot([3.655,4.767],[8.062,9.164],color="black")
plt.plot([4.3,5.2],[8.4,9.304],color="black")
plt.plot([4.68,5.11],[8.48,8.91],color="black")
plt.plot([3.14,3.3],[12.543,12.697],color="black")
plt.plot([3.14,3.6],[12.25,12.696],color="black")
plt.plot([3.14,3.6],[11.95,12.395],color="black")
plt.plot([3.14,3.6],[11.653,12.096],color="black")
plt.plot([3.14,3.6],[11.35,11.79],color="black")
plt.plot([3.14,3.6],[11.045,11.496],color="black")
plt.plot([3.14,3.6],[10.74,11.19],color="black")
plt.plot([3.305,3.6],[10.605,10.897],color="black")
plt.plot([3.58,3.696],[10.58,10.696],color="black")
plt.plot([3.6,3.7],[10.6,10.69],color="black")
plt.plot([4.201,4.526],[10.301,10.626],color="black")
plt.plot([4.4,4.914],[10.201,10.713],color="black")
plt.plot([4.701,5.25],[10.201,10.75],color="black")
plt.plot([4.782,5.25],[9.982,10.45],color="black")
plt.plot([5.404,5.893],[11.11,11.593],color="black")
plt.plot([5.405,5.853],[11.405,11.853],color="black")
plt.plot([5.41,5.85],[11.71,12.15],color="black")
plt.plot([5.555,5.888],[12.155,12.488],color="black")
plt.plot([1.116,1.197],[14.116,14.197],color="black")
plt.plot([0.99,1.108],[14.29,14.408],color="black")
plt.plot([0.861,1.047],[14.461,14.647],color="black")
plt.plot([0.741,0.996],[14.641,14.896],color="black")
plt.plot([0.635,0.878],[14.834,15.078],color="black")
plt.plot([0.53,0.786],[15.03,15.286],color="black")
plt.plot([0.443,0.728],[15.243,15.528],color="black")
plt.plot([0.362,0.598],[15.701,15.998],color="black")
plt.plot([0.3,0.59],[15.701,15.99],color="black")
plt.plot([0.245,0.496],[15.945,16.196],color="black")
plt.plot([0.21,0.396],[16.21,16.396],color="black")
plt.plot([0.2,0.298],[16.5,16.598],color="black")
plt.plot([0.203,0.278],[16.803,16.878],color="black")
plt.plot([1.003,1.594],[18.203,18.794],color="black")
plt.plot([1.104,1.696],[18.604,19.196],color="black")
plt.plot([1.71,1.997],[18.71,18.997],color="black")
plt.plot([3.15,3.26],[13.32,13.43],color="black")
plt.plot([3.22,3.46],[13.12,13.36],color="black")
plt.plot([3.45,3.69],[13.11,13.35],color="black")
plt.plot([3.7,3.89],[13.1,13.29],color="black")
plt.plot([3.91,3.99],[13.11,13.19],color="black")
plt.plot([-1.7,-0.73],[10.53,11.52],color="black")
plt.plot([8.23,9.22],[11.52,10.53],color="black")
plt.plot([3.75, 3.75], [22.0, 24.4],color="black")
plt.plot([-3.575,-2.575],[16,16],color="black")
plt.plot([10.075,11.075],[16,16],color="black")
plt.plot([8.222,9.222],[20.472,21.472],color="black")
plt.plot([-1.722,-0.722],[21.47,20.5],color="black")
plt.plot([0.362,0.59],[15.462,15.69],color="black")
plt.plot([6.666,6.739],[18.566,18.639],color="black")
plt.plot([6.67,6.859],[18.27,18.451],color="black")
plt.plot([6.606,6.96],[17.945,18.26],color="black")
plt.plot([6.605,7.065],[17.605,18.065],color="black")
plt.plot([6.61,7.15],[17.31,17.85],color="black")
plt.plot([6.707,7.238],[17.107,17.638],color="black")
plt.plot([6.71,7.3],[16.8,17.4],color="black")
plt.plot([6.81,7.35],[16.61,17.15],color="black")
plt.plot([6.805,7.38],[16.305,16.88],color="black")
plt.plot([6.904,7.4],[16.104,16.6],color="black")
plt.plot([6.91,7.397],[15.81,16.297],color="black")
plt.plot([7.01,7.35],[15.61,15.95],color="black")
plt.plot([7.16,7.27],[15.46,15.57],color="black")
# plt.xlim(-15,15,5)
# plt.ylim(-10,40,5)
plt.show()