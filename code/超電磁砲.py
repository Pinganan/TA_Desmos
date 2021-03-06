import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
import math

y6 = np.arange(3.51, 3.96, 0.000001)
x6=-1/20*y6-0.6/20
plt.plot(x6,y6,'k-')

y7 = np.arange(3.58, 3.745, 0.000001)
x7=-1/2*y7+3.31/2
plt.plot(x7,y7,'k-')

x9 = np.arange(-0.164, -0.052, 0.000001)
y9=-1.5*x9+3.48
plt.plot(x9,y9,'k-')

x10 = np.arange(-0.167, -0.14, 0.000001)
y10=-3*x10+3.4
plt.plot(x10,y10,'k-')

y11 = np.arange(3.82, 4.1, 0.000001)
x11=1/7*y11-4.8/7
plt.plot(x11,y11,'k-')

y16 = np.arange(3.654, 3.893, 0.000001)
x16=-1/3*y16+3.9/3
plt.plot(x16,y16,'k-')

y18 = np.arange(3.992, 4.096, 0.000001)
x18=1/10*y18-2.5/10
plt.plot(x18,y18,'k-')

# x21 = np.arange(0.2773)
# y21=20*x21+1.6
# y21=np.arange(4.269)
# plt.plot(x21,y21,'k-')

x24 = np.arange(0.1071, -0.0845, 0.000001)
y24=-8*x24+2.68
plt.plot(x24,y24,'k-')

# x30 = np.linspace(0.79,5, 100)
# y30 = np.linspace(-0.5, 3.79, 100)
# a30, b30 = np.meshgrid(x30, y30)
# C30=(a30-0.82)**2+(b30-3.7)**2-0.01
# figure, axes = plt.subplots()
# axes.contour(a30,b30,C30,[0])
# axes.set_aspect(1)



x34 = np.arange(1.402, 1.597, 0.000001)
y34=-3.5*x34+9
plt.plot(x34,y34,'k-')

x35 = np.arange(1.57, 2.024, 0.000001)
y35=-5*(x35-1.75)**3-0.6*(x35-1.75)+3.3
plt.plot(x35,y35,'k-')

x36 = np.arange(1.388, 1.829, 0.000001)
y36=-5*x36**3+22.5*x36**2-33.75*x36+16.875-1.2*x36+1.8+3.4
plt.plot(x36,y36,'k-')

x37 = np.arange(1.335, 1.829, 0.000001)
y37=-4*x37**3+18*x37**2-27.7*x37+14.55+3.2
plt.plot(x37,y37,'k-')

x38 = np.arange(1.17, 1.67, 0.000001)
y38=-5*x38**3+24.75*x38**2-42.0375*x38+27.240625
plt.plot(x38,y38,'k-')

x39 = np.arange(1.063, 1.3224, 0.000001)
y39=-5*x39**3+22.5*x39**2-34.55*x39+20.975
plt.plot(x39,y39,'k-')

x40 = np.arange(0.9711, 1.3224, 0.000001)
y40=-3*x40**3+13.5*x40**2-20.55*x40+13.575
plt.plot(x40,y40,'k-')

x41 = np.arange(1.5, 2.024, 0.000001)
y41=-0.7*x41+4.45
plt.plot(x41,y41,'k-')

x42 = np.arange(1.5, 1.67, 0.000001)
y42=-2.5*x42+6.95
plt.plot(x42,y42,'k-')

x43 = np.arange(0.02, 0.1, 0.000001)
y43=-5*x43**2+x43+3.28
plt.plot(x43,y43,'k-')

x54 = np.arange(0.575, 0.843, 0.000001)
y54=-x54**2+0.8*x54-0.16+4.23
plt.plot(x54,y54,'k-')

y56 = np.arange(2.84, 3.04, 0.000001)
x56=y56*0+0.93
plt.plot(x56,y56,'k-')

x57 = np.arange(0.3, 0.7, 0.000001)
y57=-0.2*x57+3.02
plt.plot(x57,y57,'k-')

x572 = np.arange(0.817, 0.93, 0.000001)
y572=-0.2*x572+3.02
plt.plot(x572,y572,'k-')

x59 = np.arange(0.186,0.407, 0.000001)
y59=-1.5*x59+3.1
plt.plot(x59,y59,'k-')

y60 = np.arange(2.3636,2.825, 0.000001)
x60=-1/1.6*y60+4.08/1.6
plt.plot(x60,y60,'k-')

x62 = np.arange(0.407,0.714, 0.000001)
y62=1.2*x62+2
plt.plot(x62,y62,'k-')

y63 = np.arange(2.3636,2.5, 0.000001)
x63=1/5*y63+3/5
plt.plot(x63,y63,'k-')

y64 = np.arange(2.794,2.88, 0.000001)
x64=-1/1.6*y64+4/1.6
plt.plot(x64,y64,'k-')

y65 = np.arange(2.794,2.86, 0.000001)
x65=y65-2.04
plt.plot(x65,y65,'k-')

x76 = np.arange(0.11,0.17, 0.000001)
y76=-2.5*x76**2+1.615*x76+3.7323
plt.plot(x76,y76,'k-')

x77 = np.arange(0.05,0.27, 0.000001)
y77=-1.2*x77**2+1.35*x77+3.7955
plt.plot(x77,y77,'k-')

x78 = np.arange(0.05,0.3, 0.000001)
y78=-1.2*x78**2+1.56*x78+3.785
plt.plot(x78,y78,'k-')

x82 = np.arange(-0.078,-0.03, 0.000001)
y82=-1.2*x82**2-1.5*x82+3.75
plt.plot(x82,y82,'k-')

y87 = np.arange(2.069,2.458, 0.000001)
x87=-1/4.7*y87+6.5/4.7
plt.plot(x87,y87,'k-')

x88 = np.arange(0.51,0.955, 0.000001)
y88=0.1*x88**2-1.4*x88+4.9-1.6
plt.plot(x88,y88,'k-')

x89 = np.arange(0.455,0.9735, 0.000001)
y89=-0.4*x89**2-0.56*x89-0.196+3.08
plt.plot(x89,y89,'k-')

x97 = np.arange(0.1422,0.1917, 0.000001)
y97=-0.4*x97+2.9
plt.plot(x97,y97,'k-')

x99 = np.arange(-0.6,-0.2, 0.000001)
y99=-0.52*x99+1.83
plt.plot(x99,y99,'k-')

x100 = np.arange(-0.59,0.008, 0.000001)
y100=0.45*x100**2-0.738*x100+2.30258    
plt.plot(x100,y100,'k-')

x101 = np.arange(-0.43,0, 0.000001)
y101=2.63-0.52*x101
plt.plot(x101,y101,'k-')

x104 = np.arange(-0.4885,-0.2, 0.000001)
y104=-1.2*(x104+0.3)**2+3.01
plt.plot(x104,y104,'k-')

x105 = np.arange(-0.6236,-0.444, 0.000001)
y105=-6*(x105+0.55)**2+2.99
plt.plot(x105,y105,'k-')

x106 = np.arange(-0.983,-0.581, 0.000001)
y106=-2*(x106+0.85)**2+3.06
plt.plot(x106,y106,'k-')

x107 = np.arange(-1.113,-0.42, 0.000001)
y107=2.1+0.12*x107
plt.plot(x107,y107,'k-')

x109 = np.arange(0.111,0.1655, 0.000001)
y109=3.33-3*x109
plt.plot(x109,y109,'k-')

x110 = np.arange(0.111,0.236, 0.000001)
y110=3.13-1.2*x110
plt.plot(x110,y110,'k-')

x111 = np.arange(-0.8812,-0.6438, 0.000001)
y111=-5.5*x111**2-9.9*x111-1.395
plt.plot(x111,y111,'k-')

y112 = np.arange(2.09,2.699, 0.000001)
a112=np.arctan(5*(y112-2.4))
x112=1/5*a112-4.2/5
plt.plot(x112,y112,'k-')

x115 = np.arange(-1.489,-0.82, 0.000001)
y115=2.05-0.45*x115
plt.plot(x115,y115,'k-')

x116 = np.arange(-1.25,-0.76, 0.000001)
y116=2.71-0.32*x116
plt.plot(x116,y116,'k-')

x117 = np.arange(-2.686,-1.25, 0.000001)
y117=-0.1*(x117+2.25)**3+0.1*(x117+2.25)+2.71-0.32*x117
plt.plot(x117,y117,'k-')

x118 = np.arange(-3.719,-2.686, 0.000001)
y118=-1/10*0.9*(x118+3.09)**2-1/10*np.arctan(5*(x118+3.09))+3.66
plt.plot(x118,y118,'k-')

x119 = np.arange(-3.858,-3.719, 0.000001)
y119=2*(x119+3.7)**2+3.75
plt.plot(x119,y119,'k-')

x121 = np.arange(-3.075,-1.489, 0.000001)
y121=0.5/20*(x121+2.2)**2-1/20*np.arctan(5*(x121+2.2))-5/20*x121+2.4
plt.plot(x121,y121,'k-')

x123 = np.arange(-3.689,-3.25, 0.000001)
y123=1.15*(x123+3.25)**2+3.39
plt.plot(x123,y123,'k-')

x124 = np.arange(-3.38,-3.075, 0.000001)
y124=0.9*(x124+3.4)**2+3.16
plt.plot(x124,y124,'k-')

x125 = np.arange(-3.96,-3.654, 0.000001)
y125=0.5*(x125+4.5)**2+3.22
plt.plot(x125,y125,'k-')

x126 = np.arange(-4.32,-3.96, 0.000001)
y126=0.9*x126+6.93
plt.plot(x126,y126,'k-')

x128 = np.arange(-4.23,-3.936, 0.000001)
y128=0.78*x128+6.28
plt.plot(x128,y128,'k-')

x129 = np.arange(-3.936,-3.83, 0.000001)
y129=0.5*x129+5.178
plt.plot(x129,y129,'k-')

x133 = np.arange(-3.712,-3.472, 0.000001)
y133=-4.8*(x133+3.52)**2+3.425
plt.plot(x133,y133,'k-')

x134 = np.arange(-3.71,-3.595, 0.000001)
y134=0.5*(x134+3.32)**2+3.36
plt.plot(x134,y134,'k-')

x141 = np.arange(-3.465,-3.356, 0.000001)
y141=1.15*(x141+3.0)**2+3.29
plt.plot(x141,y141,'k-')

x142 = np.arange(1.093,1.27, 0.000001)
y142=3.23-0.7*x142
plt.plot(x142,y142,'k-')

y143 = np.arange(2.098,2.377, 0.000001)
x143=1/20*y143+1.1
plt.plot(x143,y143,'k-')

y144 = np.arange(2.0124,2.344, 0.000001)
x144=1/20*y144+1.153
plt.plot(x144,y144,'k-')

y146 = np.arange(2.035,2.2262, 0.000001)
x146=1/4*y146+0.76
plt.plot(x146,y146,'k-')

x150 = np.arange(1.3062,1.5926, 0.000001)
y150=-4.5*(x150-1.443)**2+1.635
plt.plot(x150,y150,'k-')

x153 = np.arange(1.3018,1.3648, 0.000001)
y153=-7*(x153-1.51)
plt.plot(x153,y153,'k-')

x1532 = np.arange(1.4578,1.4677, 0.000001)
y1532=-7*(x1532-1.51)
plt.plot(x1532,y1532,'k-')

y154 = np.arange(-0.0776,1.6152, 0.000001)
x154=-1/20*np.arctan(10*(y154-0.92))-1/20*2.5*y154+1/20*1.3*(abs(y154-0.9)-(y154-0.9))+1.65
plt.plot(x154,y154,'k-')

x155 = np.arange(1,1.44, 0.000001)
y155=-1.6*x155+3.2
plt.plot(x155,y155,'k-')

x156 = np.arange(1.44,1.5556, 0.000001)
y156=-1.6*x156+3.05
plt.plot(x156,y156,'k-')

y157 = np.arange(0.745,0.9, 0.000001)
x157=y157*0+1.44
plt.plot(x157,y157,'k-')

x158 = np.arange(1.4578,1.5556, 0.000001)
y158=2*x158-2.55
plt.plot(x158,y158,'k-')

x159 = np.arange(-0.2105,1.536, 0.000001)
y159=-0.29*(x159-0.69)**2+0.73
plt.plot(x159,y159,'k-')

x160 = np.arange(-0.2296,-0.2105, 0.000001)
y160=10*(x160+0.26)
plt.plot(x160,y160,'k-')

x161 = np.arange(-0.2296,1.468, 0.000001)
y161=-0.25*(x161-0.61)**2+0.48
plt.plot(x161,y161,'k-')

y163 = np.arange(0.395,0.5139, 0.000001)
x163=6*(y163-0.53)**2-0.33
plt.plot(x163,y163,'k-')

y164 = np.arange(0.5139,1.0334, 0.000001)
x164=1/13*np.arctan(12*(y164-0.7))-0.24
plt.plot(x164,y164,'k-')

y165 = np.arange(1.0334,1.265, 0.000001)
x165=1/0.7*y165-1.13/0.7
plt.plot(x165,y165,'k-')

y166 = np.arange(1.107,1.7, 0.000001)
x166=-1/20*np.arctan(10*(y166-1.28))-1/20*y166-0.03
plt.plot(x166,y166,'k-')

y167 = np.arange(1.595,1.8018, 0.000001)
x167=1/3*y167-1/3*1.88
plt.plot(x167,y167,'k-')

x170 = np.arange(-0.702,-0.269, 0.000001)
y170=x170-0.38
plt.plot(x170,y170,'k-')

y171 = np.arange(-0.6486,0.28, 0.000001)
x171=1/8*y171-1/8*1.5
plt.plot(x171,y171,'k-')

x172 = np.arange(-0.695,-0.5198, 0.000001)
y172=-1.77-x172
plt.plot(x172,y172,'k-')

y173 = np.arange(-0.9552,-0.78, 0.000001)
x173=y173*0-0.4
plt.plot(x173,y173,'k-')

x174 = np.arange(-0.4,0.6688, 0.000001)
y174=1/5*np.arctan(4*(x174-0.2))-0.72
plt.plot(x174,y174,'k-')

x175 = np.arange(0.2664,0.6688, 0.000001)
y175=2*(x175-0.47)*(-0.4*x175-1)
plt.plot(x175,y175,'k-')

x176 = np.arange(0.4738,0.6625, 0.000001)
y176=-1.3+1.2*x176
plt.plot(x176,y176,'k-')

y177 = np.arange(-0.7448,-0.575, 0.000001)
x177=-1/3*y177+1/3*0.69
plt.plot(x177,y177,'k-')

x178 = np.arange(0.478,1.5237, 0.000001)
y178=1/8*np.arctan(4*(x178-1.05))-0.6
plt.plot(x178,y178,'k-')

x180 = np.arange(1.41,1.5164, 0.000001)
y180=-2.3+1.21*x180
plt.plot(x180,y180,'k-')

y181 = np.arange(-0.5939,-0.4795, 0.000001)
x181=y181*0+1.41
plt.plot(x181,y181,'k-')

x183=np.arange(-0.496,-0.4915,0.000001)
y183=-270.583333333333333*x183-135.193966667
plt.plot(x183,y183,'k-')

y184 = np.arange(-3.8,-2.176, 0.000001)
x184=1/6*np.arctan(1.7*(y184+3))-0.65
plt.plot(x184,y184,'k-')

y185 = np.arange(-2.75,-0.7406, 0.000001)
x185=1/6*np.arctan(1.7*(y185+1.5))+0.375
plt.plot(x185,y185,'k-')

y186 = np.arange(-3.8,-2.75, 0.000001)
x186=1/18*np.arctan(8*(y186+3))+0.125
plt.plot(x186,y186,'k-')

y187 = np.arange(-2.957,-0.694, 0.000001)
x187=-1/3.5*y187+2.16/3.5
plt.plot(x187,y187,'k-')

x188=np.arange(1.7844,2.0909,0.000001)
y188=-8.67830342577*x188+14.951464633
plt.plot(x188,y188,'k-')

x190=np.arange(2.0909,2.378,0.000001)
y190=-2.7969348659*x190+2.6541111111
plt.plot(x190,y190,'k-')

y191=np.arange(-3.12,-2.9,0.000001)
x191=-1/2.8*y191-3.95/2.8
plt.plot(x191,y191,'k-')

x192=np.arange(1.64,1.8,0.000001)
y192=-0.25-1.7*x192
plt.plot(x192,y192,'k-')

x193=np.arange(0.4458,0.9353,0.000001)
y193=1/20*np.arctan(12*(x193-0.6))-1.18
plt.plot(x193,y193,'k-')

x194=np.arange(1.7911,2.107,0.000001)
y194=1.49-1.15*x194
plt.plot(x194,y194,'k-')

x195=np.arange(2.107,2.2535,0.000001)
y195=-3.04+x195
plt.plot(x195,y195,'k-')

x196=np.arange(2.107,2.2255,0.000001)
y196=-0.6*(x196-2.107)-0.933
plt.plot(x196,y196,'k-')

x197=np.arange(1.9056,2.2255,0.000001)
y197=-2.74+0.78*x197
plt.plot(x197,y197,'k-')

y198=np.arange(-1.004,-0.8318,0.000001)
x198=-1/10*y198+2.125
plt.plot(x198,y198,'k-')

y217=np.arange(1.6,5.6,0.000001)
x217=-1*(y217-3.6)**2+-4.25
plt.plot(x217,y217,'r-')

y218=np.arange(1.6,5.6,0.000001)
x218=-1/0.48*(y218-3.6)**2+-2.1024/0.48
plt.plot(x218,y218,'r-')

y219=np.arange(1.6,5.6,0.000001)
x219=-1/0.24*(y219-3.6)**2+-1.0656/0.24
plt.plot(x219,y219,'r-')

y220=np.arange(1.6,5.6,0.000001)
x220=-1/0.12*(y220-3.6)**2+-0.5364/0.12
plt.plot(x220,y220,'-',color='orange')

y221=np.arange(1.6,5.6,0.000001)
x221=-1/0.08*(y221-3.6)**2+-0.3584/0.08
plt.plot(x221,y221,'-',color='orange')

y222=np.arange(1.6,5.6,0.000001)
x222=-1/0.06*(y222-3.6)**2+-0.2691/0.06
plt.plot(x222,y222,'-',color='orange')

y223=np.arange(1.6,5.6,0.000001)
x223=-1/0.04*(y223-3.6)**2+-0.1796/0.04
plt.plot(x223,y223,'-',color='orange',linewidth='4')






plt.xlim(-10,15)
plt.ylim(-5,10)
plt.show()