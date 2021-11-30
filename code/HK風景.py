import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
import math

figure, ax = plt.subplots()
#739
x739=plt.Rectangle((16.1,6.36), 3, 0.44,color='k',alpha=0.5)
ax.add_patch(x739)
#770

#771

#810~811(塗色)
x811=plt.Rectangle((15.1,11.257), 0.587,0.143 ,color='k',alpha=0.8)
ax.add_patch(x811)
#812(塗色)
x812=plt.Rectangle((15.375,8.59), 0.633,0.19 ,color='k',alpha=0.5)
ax.add_patch(x812)
#820~821(塗色)
x820=plt.Rectangle((16,6.9), 0.295,3.6 ,color='k',alpha=0.8)
ax.add_patch(x820)
#822(塗色)
x822=plt.Rectangle((16.4,10.23), 0.768,0.22 ,color='k',alpha=0.5)
ax.add_patch(x822)
#54
x54=plt.Rectangle((17.4,5.3), 0.6,0.1,color='k',alpha=0.5)
ax.add_patch(x54)
#58
x58=plt.Rectangle((17.4,4.95), 0.6,0.15 ,color='k',alpha=0.5)
ax.add_patch(x58)
#206
x206=plt.Rectangle((17.96,10), 0.74,0.35 ,color='k',alpha=0.7)
ax.add_patch(x206)
x525= plt.Rectangle((29.2,8.72), 0.35,2.316,color='k', alpha=0.7)     #525~526
ax.add_patch(x525)
x534= plt.Rectangle((31.6,9.7), 0.8,0.3,color='k', alpha=0.5)       #534
ax.add_patch(x534)
x547= plt.Rectangle((31.6,10.24), 0.57,0.95,color='k', alpha=0.7)       #547
ax.add_patch(x547)
x616= plt.Rectangle((26.27,10.39), 0.23,0.5,color='k', alpha=0.7)       #616~617
ax.add_patch(x616)
x619= plt.Rectangle((27.8,7), 0.2,4.476,color='k', alpha=0.5)       #619
ax.add_patch(x619)
x681= plt.Rectangle((23.577,6.63), 0.173,3.05,edgecolor = 'None',facecolor = 'k', alpha=0.5)       #681
ax.add_patch(x681)
x682= plt.Rectangle((23.75,6.63), 0.15,3.05,edgecolor = 'None',facecolor = 'k', alpha=0.68)       #682
ax.add_patch(x682)
x683= plt.Rectangle((22.905,6.63), 0.672,2.18,edgecolor = 'None',facecolor = 'k', alpha=0.5)       #683
ax.add_patch(x683)
x684= plt.Rectangle((22.65,6.63), 0.255,1.88,edgecolor = 'None',facecolor = 'k', alpha=0.5)       #684
ax.add_patch(x684)
x295= plt.Rectangle((9.9,12.6), 0.4,0.25,edgecolor = 'None',facecolor = 'k', alpha=1)       #295~297
ax.add_patch(x295)
x98= plt.Circle((16, 4.37), 0.3,fill=False)                           #98
ax.set_aspect(1)
ax.add_artist(x98)
x100= plt.Circle((15.75, 4.37), 0.3,fill=False)                           #100
ax.set_aspect(1)
ax.add_artist(x100)
x101= plt.Circle((15.5, 4.37), 0.3,fill=False)                           #101
ax.set_aspect(1)
ax.add_artist(x101)
x102= plt.Circle((16.25, 4.37), 0.3,fill=False)                           #102
ax.set_aspect(1)
ax.add_artist(x102)
x103= plt.Circle((16.5, 4.37), 0.3,fill=False)                           #103
ax.set_aspect(1)
ax.add_artist(x103)
x105= plt.Circle((18, 4.37), 0.3,fill=False)                           #105
ax.set_aspect(1)
ax.add_artist(x105)
x106= plt.Circle((18.25, 4.37), 0.3,fill=False)                           #106
ax.set_aspect(1)
ax.add_artist(x106)
x107= plt.Circle((18.5, 4.37), 0.3,fill=False)                          
ax.set_aspect(1)
ax.add_artist(x107)
x108= plt.Circle((18.75, 4.37), 0.3,fill=False)                          
ax.set_aspect(1)
ax.add_artist(x108)
x109= plt.Circle((19, 4.37), 0.3,fill=False)                          
ax.set_aspect(1)
ax.add_artist(x109)
x111= plt.Circle((18.5, 3.5), (0.02)**(0.5),fill=False)                          
ax.set_aspect(1)
ax.add_artist(x111)
x112= plt.Circle((18, 3.5), (0.02)**(0.5),fill=False)                          
ax.set_aspect(1)
ax.add_artist(x112)
x113= plt.Circle((16, 3.6), (0.02)**(0.5),fill=False)                          
ax.set_aspect(1)
ax.add_artist(x113)
x114= plt.Circle((16.5, 3.55), (0.02)**(0.5),fill=False)                 #114         
ax.set_aspect(1)
ax.add_artist(x114)

#5
x1=np.arange(12.99,23.5,0.00001)   
y1=0.1*(np.sin(x1))+3.2
plt.plot(x1,y1,'k-')
#6
x2=np.arange(13.14,13.5,0.00001)   
y2=0.02*((x2-18)**2)+3.3
plt.plot(x2,y2,'k-')
#7
x3=np.arange(13.33,13.5,0.00001)
y3=0.02*((x3-18)**2)+2.95
plt.plot(x3,y3,'k-')
#8
x4=np.arange(13.14,13.326,0.00001)
y4=(-2.0698*x4)+30.97
plt.plot(x4,y4,'k-')
#9
x5=np.arange(23.13,23.3,0.00001)
y5=0.01*((x5-18.2)**2)+3.3
plt.plot(x5,y5,'k-')
#10
x6=np.arange(22.95,23.03,0.00001)
y6=0.01*((x6-18.2)**2)+3.05
plt.plot(x6,y6,'k-')
#11
x7=np.arange(23.03,23.3,0.000001)
y7=(1.0259*x7)-20.34
plt.plot(x7,y7,'k-')
#13
x8=np.arange(13.86,14.9,0.00001)
y8=(-0.10576*x8)+5.465
plt.plot(x8,y8,'k-')
#14
plt.vlines(13.86,3.843,4.213,colors='black')
#15
plt.vlines(14.9,3.692,4.125,colors='black')
#16
x9=np.arange(13.275,18,0.000001)
y9=0.01*((x9-18.2)**2)+3.5
plt.plot(x9,y9,'k-')
#17
x10=np.arange(15.5,16.6,0.000001)
y10=0.02*((x10-18)**2)+3.7
plt.plot(x10,y10,'k-')
x11=np.arange(17.7,18,0.000001)
y11=0.02*((x11-18)**2)+3.7
plt.plot(x11,y11,'k-')
#18
x12=np.arange(18,23.13,0.00001)
y12=0.01*((x12-18.2)**2)+3.5
plt.plot(x12,y12,'k-')
#19
x13=np.arange(18,19.06,0.00001)
y13=0.01*((x13-18.2)**2)+3.7
plt.plot(x13,y13,'k-')
x14=np.arange(20.3,21.6,0.00001)
y14=0.01*((x14-18.2)**2)+3.7
plt.plot(x14,y14,'k-')
#20
plt.vlines(13.275,3.747,3.947,colors='black')
#21
plt.vlines(15.5,3.625,4.09)
#22
plt.vlines(19.06,3.507,4.065,colors='black')
#23
plt.vlines(23.13,3.543,3.743,colors='black')
#25
plt.vlines(16.6,3.739,4.054,colors='black')
#26
plt.vlines(17.7,3.702,4.051,colors='black')
#27
plt.vlines(20,3.532,4.084,colors='black')
#28
plt.vlines(21.6,3.616,4.131,colors='black')
#30
x15=np.arange(13.3,23.03,0.00001)
y15=-0.003*((x15-17.2)**2)+4.95
plt.plot(x15,y15,'k-')
#31
x16=np.arange(13.3,17.1,0.00001)
y16=0.0155*((x16-17.1)**2)+4.2
plt.plot(x16,y16,'k-')
#32
x17=np.arange(17.1,23.03,0.00001)
y17=0.004*((x17-17.1)**2)+4.2
plt.plot(x17,y17,'k-')
#34
plt.vlines(14.42,4.927,5.8,colors='black')
#35
plt.vlines(21.5,4.9,5.8,colors='black')
#36
x18=np.arange(13.3,17.1,0.00001)
y18=0.0155*((x18-17.1)**2)+4.05
plt.plot(x18,y18,'k-')
#37
x19=np.arange(17.1,23.03,0.00001)
y19=0.004*((x19-17.1)**2)+4.05
plt.plot(x19,y19,'k-')
#38
plt.vlines(13.3,4.904,4.274,colors='black')
#39
plt.vlines(23.03,4.848,4.191,colors='black')
#40
plt.vlines(13.43,3.918,4.259,colors='black')
#41
plt.vlines(22.9,3.721,4.185,colors='black')
#42
plt.vlines(22.5,3.685,4.167,colors='black')
#44
plt.hlines(3.95,16.8,17.5,colors='black')
#45
plt.hlines(4.8,16.8,17.5,colors='black')
#46
plt.vlines(16.8,3.529,3.95,colors='black')
plt.vlines(16.8,4.201,4.8,colors='black')
#47
plt.vlines(17,3.529,3.8,colors='black')
plt.vlines(17,4.201,4.7,colors='black')
#48
plt.vlines(17.3,3.51,3.8,colors='black')
plt.vlines(17.3,4.201,4.7,colors='black')
#49
plt.vlines(17.5,3.505,3.95,colors='black')
plt.vlines(17.5,4.201,4.8,colors='black')
#51
plt.vlines(17.4,4.95,5.4,colors='black')
#52
plt.vlines(18,4.948,5.4,colors='black')
#53
plt.hlines(5.4,18,17.4,colors='black')



#55
plt.hlines(5.3,18,17.4,colors='black')
#56
plt.hlines(5.1,18,17.4,colors='black')
#57
plt.hlines(5.1,18,17.4,colors='black')
#60
x20=np.arange(14.42,14.585,0.00001)
y20=-2.12727*x20+35.9552
plt.plot(x20,y20,'k-')
#61
x21=np.arange(14.202,14.42,0.00001)
y21=1.6376*x21-18.3343
plt.plot(x21,y21,'k-')
#62
x22=np.arange(21.29,21.5,0.00001)
y22=1.1428*x22-19.4302
plt.plot(x22,y22,'k-')
#63
x23=np.arange(21.5,21.69,0.00001)
y23=-1.3157*x23+33.4275
plt.plot(x23,y23,'k-')
#64
x24=np.arange(14.42,17.4,0.00001)
y24=0.02*((x24-17.6)**2)+5.3
plt.plot(x24,y24,'k-',linestyle="--")
x25=np.arange(18,21.25,0.00001)
y25=0.02*((x25-17.6)**2)+5.3
plt.plot(x25,y25,'k-',linestyle="--")
#65
x26=np.arange(13.563,14.42,0.00001)
y26=0.69078*x26-4.45904
plt.plot(x26,y26,'k-',linestyle="--")
#66
x27=np.arange(21.5,22.435,0.00001)
y27=-0.78716*x27+22.5279
plt.plot(x27,y27,'k-',linestyle="--")
#68
x28=np.arange(13.4,14.8,0.00001)
y28=0.0155*((x28-17.1)**2)+4.35
plt.plot(x28,y28,'k-')
x29=np.arange(15,16.8,0.00001)
y29=0.0155*((x29-17.1)**2)+4.35
plt.plot(x29,y29,'k-')
#69
x30=np.arange(17.5,20,0.00001)
y30=0.004*((x30-17.1)**2)+4.35
plt.plot(x30,y30,'k-')
x31=np.arange(20.2,22.93,0.00001)
y31=0.004*((x31-17.1)**2)+4.35
plt.plot(x31,y31,'k-')
#71
x31=np.arange(13.4,14.8,0.00001)
y31=0.005*((x31-17.1)**2)+4.7
plt.plot(x31,y31,'k-')
#72
plt.vlines(13.4,4.562,4.768,colors='black')
#73
plt.vlines(13.6,4.54,4.761,colors='black')
#74
plt.vlines(13.8,4.519,4.754,colors='black')
#75
plt.vlines(14,4.499,4.748,colors='black')
#76
plt.vlines(14.2,4.48,4.742,colors='black')
#77
plt.vlines(14.4,4.463,4.736,colors='black')
#78
plt.vlines(14.6,4.443,4.731,colors='black')
#79
plt.vlines(14.8,4.432,4.726,colors='black')
#80
plt.hlines(4.75,15,16.8,colors='black')
#81
plt.vlines(15,4.418,4.75,colors='black')
#82
plt.vlines(15.5,4.39,4.75,colors='black')
#83
plt.vlines(16.25,4.361,4.75,colors='black')
#84
plt.hlines(4.75,17.5,20,colors='black')
#85
plt.vlines(18.4,4.357,4.75,colors='black')
#86
plt.vlines(19.2,4.369,4.75,colors='black')
#87
plt.vlines(20,4.384,4.75,colors='black')
#88
x32=np.arange(20.2,22.93,0.00001)
y32=0.002*((x32-17.1)**2)+4.65
plt.plot(x32,y32,'k-')
#89
plt.vlines(20.2,4.388,4.669,colors='black')
#90
plt.vlines(20.6,4.399,4.674,colors='black')
#91
plt.vlines(21,4.411,4.68,colors='black')
#92
plt.vlines(21.4,4.424,4.687,colors='black')
#93
plt.vlines(21.8,4.438,4.694,colors='black')
#94
plt.vlines(22.2,4.454,4.702,colors='black')
#95
plt.vlines(22.6,4.471,4.711,colors='black')
#96
plt.vlines(22.93,4.486,4.718,colors='black')
#98

#124

#126
x126=np.arange(9.5,12,0.00001)
y126=0.1*(np.sin(x126/0.3+2.5))+3.7
plt.plot(x126,y126,'k-')
#127
x127=np.arange(32,37,0.00001)
y127=0.1*(np.sin(x127/0.4+2))+5.5
plt.plot(x127,y127,'k-')
#128
x128=np.arange(30.3,35.3,0.00001)
y128=0.1*(np.sin(x128/0.5+2))+4.75
plt.plot(x128,y128,'k-')
#130
x130=np.arange(19.412,19.523,0.00001)
y130=(0.6*x130)-0.71
plt.plot(x130,y130,'k-')
#131
x131=np.arange(19.46,19.519,0.00001)
y131=(0.6*x131)-0.78
plt.plot(x131,y131,'k-')
#132
x132=np.arange(19.519,19.523,0.00001)
y132=18*x132-340.41
plt.plot(x132,y132,'k-')
#133
x133=np.arange(19.505,19.591,0.00001)
y133=0.6*x133-0.82
plt.plot(x133,y133,'k-')
#134
x134=np.arange(19.449,19.488,0.00001)
y134=0.6*x134-0.9
plt.plot(x134,y134,'k-')
x134_1=np.arange(19.578,19.608,0.00001)
y134_1=0.6*x134_1-0.9
plt.plot(x134_1,y134_1,'k-')
#135
x135=np.arange(19.591,19.609,0.00001)
y135=-3.83333*x135+86.0337
plt.plot(x135,y135,'k-')
#136
x136=np.arange(19.372,19.417,0.00001)
y136=0.6*x136-0.95
plt.plot(x136,y136,'k-')
x136_1=np.arange(19.51,19.535,0.00001)
y136_1=0.6*x136_1-0.95
plt.plot(x136_1,y136_1,'k-')
#137
x137=np.arange(19.425,19.493,0.00001)
y137=0.6*x137-1.03
plt.plot(x137,y137,'k-')
#138
x138=np.arange(19.418,19.493,0.00001)
y138=-0.4666*x138+19.7614
plt.plot(x138,y138,'k-')
#139
x139=np.arange(19.51,19.58,0.00001)
y139=-0.4857*x139+20.232
plt.plot(x139,y139,'k-')
#140
plt.vlines(19.535,10.771,10.789)
#141
x141=np.arange(19.505,19.578,0.00001)
y141=-0.4931*x141+20.5009
plt.plot(x141,y141,'k-')
#142
x142=np.arange(19.605,19.614,0.00001)
y142=-6.444*x142+137.144
plt.plot(x142,y142,'k-')
#143
x143=np.arange(19.394,19.609,0.00001)
y143=-0.47*x143+19.845
plt.plot(x143,y143,'k-')
#144
x144=np.arange(19.412,19.611,0.00001)
y144=-0.47*x144+19.91
plt.plot(x144,y144,'k-')
#145
x145=np.arange(19.412,19.605,0.00001)
y145=-0.47*x145+20.03
plt.plot(x145,y145,'k-')
#146
x146=np.arange(19.401,19.588,0.00001)
y146=-0.47*x146+19.97
plt.plot(x146,y146,'k-')
#147
x147=np.arange(19.58,19.613,0.00001)
y147=0.909*x147-7.0762
plt.plot(x147,y147,'k-')
#148
plt.vlines(19.4,10.85,10.93,colors='black')
#149
plt.vlines(19.412,10.906,10.937,colors='black')


#150
plt.vlines(19.46,10.884,10.896,colors='black')
#151
plt.vlines(19.588,10.728,10.764,colors='black')
#152
plt.vlines(19.609,10.629,10.693,colors='black')
#153
plt.vlines(19.393,10.731,10.798,colors='black')
#154
x154=np.arange(19.387,19.418,0.00001)
y154=0.7258*x154-3.2705
plt.plot(x154,y154,'k-')
#155
x155=np.arange(19.418,19.488,0.00001)
y155=-0.4285*x155+19.1436
plt.plot(x155,y155,'k-')
#156
plt.vlines(19.412,10.786,10.82,colors='black')
#157
x157=np.arange(19.425,19.371,0.00001)
y157=-0.4666*x157+19.7614
plt.plot(x157,y157,'k-')
#160
plt.vlines(11.25,10.51,14,colors='black')
#161
plt.vlines(13,8.8,9.95,colors='black')
#162
plt.vlines(12.15,8.766,14.7,colors='black')
#163
plt.vlines(12.55,10.28,13.9,colors='black')
#164
plt.vlines(11.7,10.51,11.36,colors='black')
#165
x165=np.arange(11.27,12.15,0.00001)
y165=0.7772*x165+5.2571
plt.plot(x165,y165,'k-')
#166
x166=np.arange(12.15,12.55,0.00001)
y166=-2*x166+39
plt.plot(x166,y166,'k-')
#167
x165=np.arange(12.15,13.9,0.00001)
y165=-0.356*x165+14.578
plt.plot(x165,y165,'k-')
#168
plt.vlines(11.86,14.474,16,colors='black')
#169
plt.vlines(12.29,14.42,16,colors='black')
#170
plt.hlines(14.84,11.86,12.29)
#171
x171=np.arange(11.25,12.15,0.00001)
y171=-0.7177*x171+22.074
plt.plot(x171,y171,'k-')
#172
x172=np.arange(12.15,12.55,0.00001)
y172=1.365*x172-3.2307
plt.plot(x172,y172,'k-')
#173
x173=np.arange(12.15,12.55,0.00001)
y173=-2.0099*x173+37.7755
plt.plot(x173,y173,'k-')
#174
x174=np.arange(12.15,12.55,0.00001)
y174=1.45*x174-5.647
plt.plot(x174,y174,'k-')
#175
x175=np.arange(12.15,12.55,0.00001)
y175=-1.849*x175+34.447
plt.plot(x175,y175,'k-')
#176
x176=np.arange(12.15,12.55,0.00001)
y176=1.642*x175-9.383
plt.plot(x176,y176,'k-')
#177
x177=np.arange(11.25,12.15,0.00001)
y177=0.804*x177+3.580
plt.plot(x177,y177,'k-')
#178
x178=np.arange(11.25,12.15,0.00001)
y178=-0.733*x178+20.88
plt.plot(x178,y178,'k-')
#179
x179=np.arange(11.7,12.15,0.00001)
y179=1.355*x179-4.499
plt.plot(x179,y179,'k-')
#180
x180=np.arange(11.25,12.15,0.00001)
y180=0.7511*x180+2.844
plt.plot(x180,y180,'k-')
#181
x181=np.arange(11.25,11.7,0.00001)
y181=0.1466*x181+9.644
plt.plot(x181,y181,'k-')
#182
x182=np.arange(11.7,12.15,0.00001)
y182=-1.748*x182+31.821
plt.plot(x182,y182,'k-')
#183
x183=np.arange(11.85,12.15,0.00001)
y183=1.170*x183-3.64
plt.plot(x183,y183,'k-')
#184
x184=np.arange(11.405,11.7,0.00001)
y184=2.881*x184-22.35
plt.plot(x184,y184,'k-')
#185
x185=np.arange(11.25,11.537,0.00001)
y185=-2.731*x185+42.025
plt.plot(x185,y185,'k-')
#186
x186=np.arange(11.85,12.15,0.00001)
y186=-1.526*x186+27.80
plt.plot(x186,y186,'k-')
#187
x187=np.arange(12.15,13,0.00001)
y187=0.811*x187-0.6029
plt.plot(x187,y187,'k-')
#188
x188=np.arange(11.85,12.15,0.00001)
y188=1.383*x188-7.54
plt.plot(x188,y188,'k-')
#189
x189=np.arange(12.15,12.76,0.00001)
y189=-0.754*x189+18.422
plt.plot(x189,y189,'k-')
#190
x190=np.arange(11.85,12.035,0.00001)
y190=-1.302*x190+23.882
plt.plot(x190,y190,'k-')
#193
plt.vlines(17.7,8.85,10,colors='black')
#194
plt.vlines(19.23,7.9,10,colors='black')
#195
plt.hlines(10,17.7,19.23,colors='black')
#196
plt.vlines(17.5,8.85,10.8,colors='black')
#197
plt.vlines(17.57,8.85,9.936,colors='black')
#198
x198=np.arange(17.57,17.7,0.00001)
y198=0.492*x198+1.286
plt.plot(x198,y198,'k-')
#199
plt.hlines(10.8,17.5,17.96,colors='black')
plt.hlines(10.8,18.47,18.85,colors='black')
#200
plt.vlines(17.96,10,10.8,colors='black')
#201
plt.vlines(17.8,10,10.8,colors='black')
#202
plt.vlines(18.85,10,10.8,colors='black')
#203
plt.vlines(18.47,10.45,10.8,colors='black')
#204
plt.vlines(18.7,10,10.8,colors='black')
#205
plt.hlines(10.45,17.8,18.85,colors='black')
#207
plt.vlines(18.01,8.85,10,colors='black')
#208
plt.vlines(18.18,8.85,10,colors='black')
#209
plt.vlines(18.89,7,10,colors='black')
#210
plt.vlines(19.058,7.9,10,colors='black')
#211
plt.hlines(9.84,17.7,19.23,colors='black')
#212
plt.hlines(9.16,17.7,19.23,colors='black')
#213
plt.hlines(8.33,18.25,19.23,colors='black')
#214
plt.hlines(7.445,18.25,19,colors='black')
#215
plt.vlines(18.85,6.9,9.84,colors='black')
#216
x216=np.arange(17.7,18.087,0.00001)
y216=0.413*x216+2.522
plt.plot(x216,y216,'k-')
#217
x217=np.arange(18.087,18.55,0.00001)
y217=-0.345*x217+16.250
plt.plot(x217,y217,'k-')
#218
x218=np.arange(18.55,18.96,0.00001)
y218=0.39*x218+2.6
plt.plot(x218,y218,'k-')
#219
x219=np.arange(18.96,19.23,0.00001)
y219=-0.592*x219+21.235
plt.plot(x219,y219,'k-')
#220
x220=np.arange(17.7,18.103,0.00001)
y220=0.558*x220-0.72
plt.plot(x220,y220,'k-')
#221
x221=np.arange(18.103,18.513,0.00001)
y221=-0.548*x221+19.319
plt.plot(x221,y221,'k-')
#222
x222=np.arange(18.103,18.513,0.00001)
y222=-0.5487*x222+19.3195
plt.plot(x222,y222,'k-')
#223
x223=np.arange(18.513,18.97,0.00001)
y223=0.371*x223+2.2733
plt.plot(x223,y223,'k-')
#224
x224=np.arange(18.97,19.23,0.00001)
y224=-0.6538*x224+21.7334
plt.plot(x224,y224,'k-')
#225
x225=np.arange(18.25,18.55,0.00001)
y225=-0.459*x225+16.862
plt.plot(x225,y225,'k-')
#226
x226=np.arange(18.55,18.97,0.00001)
y226=0.5238*x226-1.386
plt.plot(x226,y226,'k-')
#227
x227=np.arange(18.97,19.23,0.00001)
y227=-0.846*x227+24.601
plt.plot(x227,y227,'k-')
#228
x228=np.arange(18.25,18.55,0.00001)
y228=-0.509*x228+16.905
plt.plot(x228,y228,'k-')
#229
x229=np.arange(18.55,18.89,0.00001)
y229=0.5058*x229-1.939
plt.plot(x229,y229,'k-')
#232
plt.vlines(34.66,8.93,13.25,colors='black')
#233
plt.vlines(35.116,10.06,13.4,colors='black')
#234
plt.vlines(36.095,12.205,13.4,colors='black')
#235
plt.hlines(13.4,35.116,36.095,colors='black')
#236
x236=np.arange(34.66,35.116,0.00001)
y236=0.328*x236+1.848
plt.plot(x236,y236,'k-')
#237
plt.vlines(35.39,10.06,13.09,colors='black')
#238
plt.vlines(35.72,10.06,13.09,colors='black')
#239
plt.vlines(35.75,10.06,13.05,colors='black')
#240
plt.hlines(13.09,35.39,35.72,colors='black')
#241
plt.vlines(35.01,10.06,12.915,colors='black')
#242
x242=np.arange(34.66,35.01,0.00001)
y242=0.1857*x242+6.4131
plt.plot(x242,y242,'k-')
#243
x243=np.arange(35.72,35.75,0.00001)
y243=-1.333*x243+60.71
plt.plot(x243,y243,'k-')
#244
plt.hlines(13.52,35.19,35.806,colors='black')
#245
x245=np.arange(35.806,36.095,0.00001)
y245=-0.415*x245+28.3875
plt.plot(x245,y245,'k-')
#246
x246=np.arange(34.88,35.19,0.00001)
y246=0.306*x246+2.7359
plt.plot(x246,y246,'k-')
#247
x247=np.arange(34.66,34.88,0.00001)
y247=0.7954*x247-14.32
plt.plot(x247,y247,'k-')
#248
x248=np.arange(35.116,35.19,0.00001)
y248=1.6216*x248-43.544
plt.plot(x248,y248,'k-')
#249
plt.vlines(35.806,13.52,13.678,colors='black')
#250
plt.hlines(13.678,35.19,35.806,colors='black')
#251
plt.vlines(35.19,13.52,13.678,colors='black')
#252
plt.vlines(34.88,13.426,13.568,colors='black')
#253
plt.hlines(13.78,35.131,35.615,colors='black')
#254
x254=np.arange(34.88,35.19,0.00001)
y254=0.3548*x254+1.1912
plt.plot(x254,y254,'k-')
#255
x255=np.arange(34.88,35.131,0.00001)
y255=0.844*x255-15.89
plt.plot(x255,y255,'k-')
#256
x256=np.arange(35.131,35.19,0.00001)
y256=-1.728*x256+74.514
plt.plot(x256,y256,'k-')
#257
x257=np.arange(35.516,35.806,0.00001)
y257=-0.534*x257+32.79
plt.plot(x257,y257,'k-')
#258
plt.vlines(35.34,13.78,15.111,colors='black')
#259
x259=np.arange(35.257,35.34,0.00001)
y259=1.795*x259-49.512
plt.plot(x259,y259,'k-')
#260
x260=np.arange(35.34,35.447,0.00001)
y260=-1.39*x260+63.14
plt.plot(x260,y260,'k-')
#261
plt.hlines(14.144,35.25,35.415,colors='black')
#262
plt.hlines(14.44,35.28,35.4,colors='black')
#265
x265=np.arange(28.47,29.6,0.00001)
y265=-0.08*((x265-28.7)**2)+14.5
plt.plot(x265,y265,'k-')
x265_1=np.arange(31.6,34.107,0.00001)
y265_1=-0.08*((x265_1-28.7)**2)+14.5
plt.plot(x265_1,y265_1,'k-')
x265_2=np.arange(34.267,34.66,0.00001)
y265_2=-0.08*((x265_2-28.7)**2)+14.5
plt.plot(x265_2,y265_2,'k-')
#266
x266=np.arange(24,25.13,0.00001)
y266=0.4049*x266+3.280
plt.plot(x266,y266,'k-')
#267
x267=np.arange(25,26.5,0.00001)
y267=0.196*x267+8.48
plt.plot(x267,y267,'k-')
#268
x268=np.arange(22,24,0.00001)
y268=0.099*x268+10.6
plt.plot(x268,y268,'k-')
#269
x269=np.arange(21,22,0.00001)
y269=-0.199*x269+17.199
plt.plot(x269,y269,'k-')
#270
x270=np.arange(20.2,21.13,0.00001)
y270=0.624*x270-0.124
plt.plot(x270,y270,'k-')
#271
x271=np.arange(26.5,28.47,0.00001)
y271=0.404*x271+2.992
plt.plot(x271,y271,'k-')
#273
plt.vlines(9.2,13.6,14,colors='black')
#274
plt.hlines(14,9,9.2,colors='black')
#276
x276=np.arange(9,10.52,0.00001)
y276=-0.3*((x276-9.8)**2)+13.7
plt.plot(x276,y276,'k-')
#277
x277=np.arange(10.52,11.25,0.00001)
y277=-0.101*x277+14.610
plt.plot(x277,y277,'k-')
#278
x278=np.arange(12.55,13.4,0.00001)
y278=-0.02*x278+13.46
plt.plot(x278,y278,'k-')
#279
x279=np.arange(13.4,14.1,0.00001)
y279=-0.085*x279+14.348
plt.plot(x279,y279,'k-')
#280
x280=np.arange(16.08,17.4,0.00001)
y280=0.2*((x280-16.8)**2)+12.7
plt.plot(x280,y280,'k-')
#281
x281=np.arange(15.5,16.08,0.00001)
y281=-0.1482*x281+15.188
plt.plot(x281,y281,'k-')
#282
plt.hlines(12.772,17.4,18,colors='black')
#283
plt.vlines(18,12.52,12.772,colors='black')
#284
x284=np.arange(18.12,18.5,0.00001)
y284=-0.539*x284+22.239
plt.plot(x284,y284,'k-')
#286
x286=np.arange(9.4,10.9,0.00001)
y286=-0.25*((x286-10)**2)+12.5
plt.plot(x286,y286,'k-')
#287
plt.vlines(9.5,12.438,13,colors='black')
#288
plt.vlines(10.7,12.377,13,colors='black')
#289
plt.hlines(13,9.5,10.7,colors='black')
#290
plt.vlines(9.7,12.477,12.85,colors='black')
#291
plt.vlines(9.8,12.49,12.85,colors='black')
#292
plt.vlines(10.55,12.424,12.85,colors='black')
#293
plt.vlines(10.45,12.451,12.85,colors='black')
#294
plt.hlines(12.85,9.7,9.8,colors='black')
plt.vlines(12.85,10.45,10.55,colors='black')
'''
#295
x295=np.arange(,,0.00001)
y295=*x295
plt.plot(x295,y295,'k-')
#296
x296=np.arange(,,0.00001)
y296=*x296
plt.plot(x296,y296,'k-')
#297
x297=np.arange(,,0.00001)
y297=*x297
plt.plot(x297,y297,'k-')
'''
#298
x298=np.arange(19.4,19.6,0.00001)
y298=0.165*x298+9.065
plt.plot(x298,y298,'k-')
#300
x300=np.arange(18.65,19.45,0.00001)
y300=-0.2*((x300-18.6)**2)+12.02
plt.plot(x300,y300,'k-')
#301
plt.vlines(18.65,12.019,12.34,colors='black')
#302
plt.vlines(19.4,11.892,12.34,colors='black')
#303
plt.hlines(12.34,18.5,18.823,colors='black')
plt.hlines(12.34,19.16,19.4,colors='black')
#304
plt.vlines(18.5,12.128,12.34,colors='black')
#305
x305=np.arange(18.4,18.65,0.00001)
y305=-0.72*x305+25.521
plt.plot(x305,y305,'k-')
#306
x306=np.arange(18.544,18.823,0.00001)
y306=((x306-19.05)**2)+12.45
plt.plot(x306,y306,'k-')
x306_1=np.arange(19.16,19.47,0.00001)
y306_1=((x306_1-19.05)**2)+12.45
plt.plot(x306_1,y306_1,'k-')
#307

#308
x308=np.arange(18.544,19.47,0.00001)
y308=-0.0863*x308+14.3080
plt.plot(x308,y308,'k-')
plt.hlines(y=6, xmin=29.2, xmax=29.55,color='black')     #524
plt.hlines(y=8.64, xmin=29.2, xmax=29.55,color='black')    #527
plt.hlines(y=8.39, xmin=29.2, xmax=29.55,color='black')
plt.hlines(y=8.14, xmin=29.2, xmax=29.55,color='black')
plt.hlines(y=7.89, xmin=29.2, xmax=29.55,color='black')
plt.hlines(y=7.64, xmin=29.2, xmax=29.55,color='black')
plt.hlines(y=7.39, xmin=29.2, xmax=29.55,color='black')
plt.hlines(y=7.14, xmin=29.2, xmax=29.55,color='black')    #529
plt.vlines(32.4,7.5,10.24)        #531
plt.hlines(10.24,31.6,32.4)        
plt.hlines(10,31.6,32.4)         #533  
plt.hlines(9.7,31.6,32.4)         #535
plt.hlines(9.5,31.6,32.2)
plt.hlines(9.3,31.6,32.15)
plt.hlines(9.1,31.6,32.1)
plt.hlines(8.7,31.6,32.05)
plt.hlines(8.5,31.6,32)
plt.hlines(8.3,31.6,32)
plt.hlines(8.3,31.6,32)
plt.hlines(8.1,31.6,32)         #534
plt.vlines(32.17,10.24,11.19)       #545
plt.hlines(11.19,31.6,32.17)       #546
plt.hlines(7.16,24.03,26.63)      #550
plt.vlines(24.292,6.35,7.16)
plt.vlines(24.03,6.35,7.16)
plt.vlines(26.63,6.638,7.16)
plt.hlines(6.8,24.36,26.528)
plt.hlines(6.9,24.36,26.528)
plt.hlines(7,24.36,26.528)
plt.vlines(23.9,6.63,11.056)
plt.vlines(24.2,7.16,11.15)
plt.vlines(25.6,7.672,11.15)
plt.hlines(11.15,24.2,25.6)     #560
plt.plot([23.9,24.2 ], [11.056, 11.15],color="k")     #561
plt.plot([25.255,25.6 ], [11.4, 11.15],color="k")
plt.hlines(11.4,24.282,25.255)
plt.plot([23.9, 24.28], [11.056, 11.398],color="k")
plt.plot([24.2, 24.388], [11.15, 11.4],color="k")
plt.vlines(24, 7.26, 11.006, linestyle="dashed")
plt.vlines(24.1, 7.237, 11.05, linestyle="dashed")
plt.vlines(24.3, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.4, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.5, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.6, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.7, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.8, 7.254, 11.05, linestyle="dashed")
plt.vlines(24.9, 7.254, 11.05, linestyle="dashed")
plt.vlines(25, 7.254, 11.05, linestyle="dashed")
plt.vlines(25.1, 7.254, 11.05, linestyle="dashed")
plt.vlines(25.2, 7.254, 11.05, linestyle="dashed")
plt.vlines(25.3, 7.254, 11.05, linestyle="dashed")
plt.vlines(25.4, 7.254, 11.05, linestyle="dashed")
plt.vlines(25.5, 7.254, 11.05, linestyle="dashed")     #580
plt.vlines(25.85,7.16,9.19)        #582
plt.hlines(9.19,25.85,26.5)     
plt.hlines(9,25.9,26.4) 
plt.hlines(8.9,25.9,26.4)
plt.hlines(8.8,25.9,26.4)
plt.hlines(8.7,25.9,26.4)
plt.hlines(8.6,25.9,26.4)
plt.hlines(8.5,25.9,26.4)
plt.hlines(8.4,25.9,26.4)         #590 
plt.hlines(10.135,25.6,26.3)       #592
plt.vlines(26.3,9.19,10.135) 
plt.vlines(25.93,9.17,10.135) 
plt.vlines(25.71, 8.665, 9.92, linestyle="dashed")
plt.vlines(25.66, 8.665, 9.9, linestyle="dashed")
plt.vlines(25.76, 8.668, 9.93, linestyle="dashed")
plt.vlines(25.81, 8.67, 9.95, linestyle="dashed")
plt.vlines(26.2, 9.19, 9.95, linestyle="dashed")
plt.vlines(26.05, 9.19, 9.95, linestyle="dashed")
plt.vlines(26.1, 9.19, 9.95, linestyle="dashed")
plt.vlines(26.1, 9.19, 9.95, linestyle="dashed")
plt.vlines(26, 9.19, 9.95, linestyle="dashed")
plt.vlines(26.25, 9.19, 9.95, linestyle="dashed")
plt.plot([25.602, 25.935], [10.138, 10.484],color="k")
plt.plot([25.935, 26.3], [10.484, 10.135],color="k")
plt.plot([25.935, 25.92], [10.483, 10.135],color="k")
plt.hlines(10.39,26.003,26.5)                 #608
plt.vlines(29.2,7,11.476)     #610
plt.vlines(28,7,11.476)
plt.vlines(27.8,7,11.476)
plt.vlines(26.5,7.16,11.25)
plt.vlines(26.27,10.39,10.89)
plt.hlines(10.839,26.27,26.5)   #615
plt.hlines(11.476,26.8,28)     #618
plt.vlines(27.18,6.9,11.1)     #620
plt.vlines(27.4,6.9,11.1)
plt.vlines(27.5,6.9,11.1)
plt.plot([27.18, 27.32], [11.1, 11.35],color="k")
plt.plot([27.32, 27.4], [11.35, 11.1],color="k")
plt.plot([27.32, 27.5], [11.35, 11.1],color="k")
plt.vlines(26.8,6.9,11.476)
plt.vlines(28.31,7,11.6)
plt.vlines(28.87,7,11.6)
plt.hlines(7.2,28,29.2)
plt.hlines(11.6,28.31,28.87)
plt.hlines(11.4,28.31,28.87)
plt.plot([26.5, 26.8], [11.25, 11.476],color="k")
plt.plot([28, 28.31], [11.476, 11.6],color="k")
plt.plot([28.87, 29.2], [11.6, 11.476],color="k")
plt.hlines(6.9,26.63,27.526)
plt.plot([28, 28.31], [11.3, 11.4],color="k")
plt.plot([28.87, 29.2], [11.4, 11.3],color="k")     #637
plt.hlines(10.7,25.6,26.27)         #639
plt.hlines(9.68,23.577,23.9)
plt.hlines(8.81,22.905,23.577)
plt.hlines(8.51,22.65,22.905)
plt.hlines(9.584,21.875,23.03)
plt.hlines(10.2,22.3,23.32)
plt.hlines(10.1,22.4,23.25)
plt.hlines(10,22.4,23.25)
plt.hlines(9.9,22.4,23.25)
plt.hlines(9.8,22.4,23.25)
plt.hlines(9.7,22.4,23.25)
plt.hlines(10.3,23.32,23.9)
plt.vlines(23.577,8.81,9.68)
plt.vlines(22.905,8.51,8.81)
plt.vlines(23.03,8.81,9.584)
plt.vlines(21.875,8.54,9.584)
plt.vlines(22.04,8.54,9.584)
plt.vlines(22.3,8.54,9.584)
plt.vlines(22.33,8.54,9.584)
plt.vlines(22.6,8.54,9.584)
plt.vlines(22.86,8.51,9.584)
plt.vlines(22.3,9.584,10.2)
plt.vlines(23.32,8.81,10.3)
plt.hlines(10.2,23.36,23.85, linestyles='dashed')
plt.hlines(10.1,23.36,23.85, linestyles='dashed')
plt.hlines(10,23.36,23.85, linestyles='dashed')
plt.hlines(9.9,23.36,23.85, linestyles='dashed')
plt.hlines(9.8,23.36,23.85, linestyles='dashed')
plt.hlines(9.72,23.36,23.85, linestyles='dashed')     #669
plt.hlines(9.5,22.1,22.5)  #671
plt.hlines(9.4,22.1,22.5)  #672
plt.hlines(9.3,22.1,22.5)  #673
plt.hlines(9.2,22.1,22.5)  #674
plt.hlines(9.1,22.1,22.5)  #675
plt.hlines(9,22.1,22.5)   #676
plt.hlines(8.9,22.1,22.5)  #677
plt.hlines(8.8,22.1,22.5)  #678
plt.hlines(8.7,22.1,22.5)  #679
plt.hlines(9.5,22.375,22.535)
plt.hlines(8.9,22.375,22.535)
plt.hlines(8.7,22.375,22.535)
plt.hlines(8.8,22.375,22.535)
plt.hlines(9,22.375,22.535)
plt.hlines(9.1,22.375,22.535)
plt.hlines(9.2,22.375,22.535)
plt.hlines(9.3,22.375,22.535)
plt.hlines(9.4,22.375,22.535)
plt.hlines(9.5,22.65,22.8)
plt.hlines(9.4,22.65,22.8)
plt.hlines(9.3,22.65,22.8)
plt.hlines(9.2,22.65,22.8)
plt.hlines(9.1,22.65,22.8)
plt.hlines(9,22.65,22.8)
plt.hlines(8.9,22.65,22.8)
plt.hlines(8.8,22.65,22.8)
plt.hlines(8.7,22.65,22.8)    #679
plt.vlines(14.99,7,11.85)     #803
plt.vlines(14.88,7,11.8)
plt.vlines(14.79,7,11.75)
plt.vlines(14.673,7,11.7)     #806
#825
plt.hlines(9.5,32.4,33)
#826
plt.vlines(32.317,10.24,11.327)
#827
plt.vlines(32.896,9.5,11.327)
#828
plt.hlines(11.327,32.317,32.896)
#829
x829 = plt.Rectangle((32.4,7.5),0.6,2,color='k', alpha=0.7)     
ax.add_patch(x829)
#830
x830 = plt.Rectangle((32.4,7.5),0.1,2,color='k', alpha=0.7)     
ax.add_patch(x829)
#831
x831 = plt.Rectangle((32.9,7.5),0.1,2,color='k', alpha=0.7)     
ax.add_patch(x829)
#832
x832 = plt.Rectangle((32.896,9.5),33-32.896,10.8-9.5,color='k', alpha=0.7)     
ax.add_patch(x832)
#833
x833 = plt.Rectangle((32.896,9.5),33-32.896,10.8-9.5,color='k', alpha=0.7)     
ax.add_patch(x833)
#834
x834 = plt.Rectangle((32.896,9.5),33-32.896,10.8-9.5,color='k', alpha=0.7)     
ax.add_patch(x834)
#836
plt.plot([36.7,36.3], [11,10.91],color="k")
#837
plt.plot([36.7,36.3], [10.7,10.6],color="k")
#839
plt.hlines(7.69,36.25,39)
#840
plt.hlines(7.6,36.31,37.44)
plt.hlines(7.6,37.53,38.24)
plt.hlines(7.6,38.32,39)
#841
x841 = plt.Rectangle((36.9,6.8),37.44-36.9,0.8,color='k', alpha=0.7)     
ax.add_patch(x829)
x841_2 = plt.Rectangle((37.53,6.8),38.24-37.53,0.8,color='k', alpha=0.7)     
ax.add_patch(x829)
x841_3 = plt.Rectangle((38.32,6.8),39-38.32,0.8,color='k', alpha=0.7)  
#842
x842 = plt.Rectangle((36.9,6.8),37.44-36.9,0.8,color='k', alpha=0.7)     
ax.add_patch(x829)
x842_2 = plt.Rectangle((37.53,6.8),38.24-37.53,0.8,color='k', alpha=0.7)     
ax.add_patch(x829)
x842_3 = plt.Rectangle((38.32,6.8),39-38.32,0.8,color='k', alpha=0.7)  
#843
x843 = plt.Rectangle((36.31,7.5),36.9-36.31,0.1,color='k', alpha=0.7)     
ax.add_patch(x843)
#844
x844 = plt.Rectangle((36.31,7.5),36.9-36.31,0.1,color='k', alpha=0.7)     
ax.add_patch(x844)
#845
plt.vlines(36.31,7.5,7.6)
#846
plt.vlines(37.44,6.8,7.6)
#847
plt.vlines(38.24,6.8,7.6)
#848
plt.vlines(38.32,6.8,7.6)
#849
plt.vlines(37.53,6.8,7.6)
#850
plt.vlines(36.25,7.5,7.69)
#851
plt.vlines(38.2,7.69,11.26)
#852
plt.vlines(38.4,7.69,11.26)
#853
plt.vlines(38.6,7.69,11.26)
#854
plt.vlines(38.8,7.69,11.26)
#855
plt.hlines(11.26,38.2,39)
#856
x856 = np.arange(38.1,38.2,0.00001)
y856 = (x856-38.1)*(0.06/0.1)+11.2
plt.plot (x856,y856,'k-')
#858
plt.vlines(36,7.5,12.17)
#859
plt.vlines(36.7,7.69,12.414)
#860
plt.vlines(37.17,7.69,12.414)
#861
plt.vlines(37.33,7.69,12.414)
#862
plt.vlines(38.1,7.69,12.414)
#863
plt.hlines(12.414,36.7,38.1)
#864
x864 = np.arange(36,36.7,0.00001)
y864 = (x864-36)*((12.414-12.17)/(36.7-36))+12.17
plt.plot (x864,y864,'k-')
#865
x865 = plt.Rectangle((37.17,7.69),0.16,12.414-7.69,color='k', alpha=0.7)     
ax.add_patch(x865)
#866
plt.plot([36.3,36.25], [7.69,7.69],color="k")
plt.plot([36.25,36.25], [7.69,7.5],color="k")
plt.plot([36.25,36], [7.5,7.5],color="k")
plt.plot([36,36.12], [7.5,12.17],color="k")
plt.plot([36.12,36.3], [12.17,12.275],color="k")
plt.plot([36.3,36.3], [12.275,7.69],color="k")
#867
plt.plot([37.73,38.1], [12.414,12.414],color="k")
plt.plot([38.1,38.1], [12.414,7.69],color="k")
plt.plot([38.1,37.73], [7.69,7.69],color="k")
plt.plot([37.73,37.73], [7.69,12.414],color="k")
#868
plt.vlines(36.3,7.69,10.368)
plt.vlines(36.3,10.565,12.275)
#869
plt.vlines(37.73,7.69,10.43)
plt.vlines(37.73,10.62,12.414)
#870
plt.hlines(12,36.7,37.17)
plt.hlines(12,37.33,37.73)
#871
plt.hlines(11,36.7,37.17)
plt.hlines(11,37.33,37.73)
#872
plt.hlines(10.7,36.7,37.17)
plt.hlines(10.7,37.33,37.73)
#873
plt.plot([36.7,36.3], [12,11.87],color="k")
#874
plt.hlines(8,36.7,37.17)
plt.hlines(8,37.33,37.73)
#875
plt.plot([36.7,36.3], [8,7.93],color="k")
#877
plt.vlines(34.78,7.5,9.64)
#878
plt.vlines(35.9,7.5,9.64)
#879
plt.vlines(34.9,9.64,10.06)
#880
plt.vlines(35.8,9.64,10.06)
#881
plt.hlines(10.06,34.9,35.8)
#882
plt.hlines(9.64,34.78,34.9)
plt.hlines(9.64,35.8,35.9)
#883
plt.hlines(8.93,34.56,34.78)
#884
x884 = plt.Rectangle((34.56,7.5),0.22,1.43,color='k', alpha=0.7)     
ax.add_patch(x884)
#885
x885 = plt.Rectangle((34.56,7.5),0.22,1.43,color='k', alpha=0.7)     
ax.add_patch(x885)
#886
plt.vlines(35.05,7.6,9.7)
plt.vlines(35.05,9.8,10)
#887
plt.vlines(35.2,7.6,9.7)
#888
plt.vlines(35.37,7.6,9.7)
#889
plt.vlines(35.53,7.6,9.7)
#890
plt.vlines(35.68,7.6,9.7)
plt.vlines(35.68,9.8,10)
#891
plt.vlines(34.9,7.6,9.5)
#892
plt.vlines(35.8,7.6,9.5)
#893
plt.hlines(9.8,35.05,35.68)
#894
x894 = plt.Rectangle((35.05,9.8),35.68-35.05,0.2,color='k', alpha=0.7)     
ax.add_patch(x894)
#898
x898 = plt.Rectangle((34.56,8.93),0.1,10.77-8.93,color='k', alpha=0.7)     
ax.add_patch(x898)
#900
plt.hlines(7.174,9,11.2)
#901
plt.vlines(11.2,6.74,7.174)
#902
plt.vlines(9.68,6.649,7.174)
#903
plt.hlines(7.5,9.36,11)
#904
plt.vlines(11,7.5,10)
#905
plt.vlines(9.75,7.5,10)
#906
plt.vlines(9.36,7.5,9.9)
#907
plt.hlines(10,9.75,11)
#908
y908 = np.arange(7.174,7.5,0.00001)
x908 = (y908-7.5)*((9.85-9.36)/(7.174-7.5))+9.36
plt.plot (x908,y908,'k-')
#909
y909 = np.arange(7.174,7.5,0.00001)
x909 = (y909-7.5)*((9.99-9.75)/(7.174-7.5))+9.75
plt.plot (x909,y909,'k-')
#910
y910 = np.arange(9.9,10,0.00001)
x910 = (y910-10)*((9.36-9.75)/(9.9-10))+9.75
plt.plot (x910,y910,'k-')
#911
y911 = np.arange(7.174,7.5,0.00001)
x911 = (y911-7.174)*((11-10.6)/(7.5-7.174))+10.6
plt.plot (x911,y911,'k-')
#912
plt.vlines(9.5,7.6,9.7)
#913
plt.vlines(9.6,7.6,9.8)
#914
plt.vlines(9.9,7.6,9.8)
#915
plt.vlines(10,7.6,9.8)
#916
plt.vlines(10.1,7.6,9.8)
#917
plt.vlines(10.2,7.6,9.8)
#918
plt.vlines(10.3,7.6,9.8)
#919
plt.vlines(10.4,7.6,9.8)
#920
plt.vlines(10.5,7.6,9.8)
#921
plt.vlines(10.6,7.6,9.8)
#922
plt.vlines(10.7,7.6,9.8)
#923
plt.vlines(10.8,7.6,9.8)
#924
plt.vlines(10.9,7.6,9.8)
#926
plt.vlines(10.36,10,10.36)
#927
plt.vlines(10.62,10,10.51)
#928
plt.vlines(11.85,6.976,10.51)
#929
plt.hlines(10.51,10.62,11.85)
#930
plt.plot([10.36,10.62], [10.36,10.51],color="k")
#931
plt.vlines(10.7,10,10.32)
#932
plt.vlines(10.9,10,10.32)
#933
plt.vlines(11.1,10,10.32)
#934
plt.vlines(11.3,10,10.32)
#935
plt.vlines(11.5,10,10.32)
#936
plt.vlines(11.7,10,10.32)
#939
plt.hlines(9.7,9,9.36)
#940
plt.vlines(10.25,10,11.5)
#941
plt.hlines(11.5,9,10.25)
#942
plt.vlines(9.52,9.941,11.5)
#943
plt.hlines(11.35,9.1,9.4)
plt.hlines(11.35,9.6,10.2)
#944
plt.hlines(11.2,9.1,9.4)
plt.hlines(11.2,9.6,10.2)
#945
plt.hlines(11.05,9.1,9.4)
plt.hlines(11.05,9.6,10.2)
#946
plt.hlines(10.9,9.1,9.4)
plt.hlines(10.9,9.6,10.2)
#947
plt.hlines(10.75,9.1,9.4)
plt.hlines(10.75,9.6,10.2)
#948
plt.hlines(10.6,9.1,9.4)
plt.hlines(10.6,9.6,10.2)
#949
plt.hlines(10.45,9.1,9.4)
plt.hlines(10.45,9.6,10.2)
#950
plt.hlines(10.3,9.1,9.4)
plt.hlines(10.3,9.6,10.2)
#952
plt.plot([12.55,13.5], [11.4,11.4],color="k")
plt.plot([13.5,13.5], [11.4,8.8],color="k")
plt.plot([13.5,13], [8.8,8.8],color="k")
plt.plot([13,13], [8.8,9.95],color="k")
plt.plot([13,12.55], [9.95,10.28],color="k")
plt.plot([12.55,12.55], [10.28,11.4],color="k")
#953
plt.plot([12.55,12.7], [11.4,11.4],color="k")
plt.plot([12.7,12.7], [11.4,10.3],color="k")
plt.plot([12.7,13.15], [10.3,9.95],color="k")
plt.plot([13.15,13.15], [9.95,8.8],color="k")
plt.plot([13.15,13.1], [8.8,8.8],color="k")
plt.plot([13.1,13.8], [8.8,8.8],color="k")
plt.plot([13.8,13.9], [8.8,9.95],color="k")
plt.plot([13.9,12.55], [9.95,10.28],color="k")
plt.plot([12.55,12.55], [10.28,11.4],color="k")
#954
plt.hlines(11.7,12.55,13.5)
#955
plt.hlines(11.4,12.55,13.5)
#956
plt.vlines(13.5,8.8,11.7)
#957

#958
plt.vlines(13,11.47,11.6)
plt.vlines(13,11.625,11.63)
#959
plt.vlines(13.1,11.45,11.65)
#960
plt.vlines(13.2,11.47,11.6)
plt.vlines(13.2,11.625,11.63)
#961
plt.hlines(11.59,13.045,13.15)
#963
plt.vlines(13.76,8.8,10.2)
#964
plt.hlines(10.2,13.76,14.1)
#966
plt.vlines(14.1,7,13.7)
#967
plt.hlines(13.7,14.1,15.32)
#968
x968 = plt.Rectangle((14.1,13.5),15.32-14.1,0.2,color='k', alpha=0.7)     
ax.add_patch(x968)
#969
plt.vlines(15.32,11.583,13.7)
#970
plt.vlines(15.5,11.583,13.53)
#971
plt.plot([15.32,15.5], [13.7,13.53],color="k")
#972
x972 = plt.Rectangle((14.1,13.3),0.553,0.16,color='k', alpha=0.7)     
ax.add_patch(x972)
x972_2 = plt.Rectangle((14.1,9.2),0.5,0.17,color='k', alpha=0.7)     
ax.add_patch(x972_2)
#973
x973 = plt.Rectangle((14.1,13.3),0.553,0.16,color='k', alpha=0.7)     
ax.add_patch(x973)
x973_2 = plt.Rectangle((14.1,9.2),0.5,0.17,color='k', alpha=0.7)     
ax.add_patch(x973_2)
#974
plt.plot([15.32,15.32], [13.7,13.5],color="k")
plt.plot([15.32,15.5], [13.5,13.377],color="k")
plt.plot([15.5,15.5], [13.377,13.53],color="k")
plt.plot([15.5,15.32], [13.53,13.7],color="k")
#975
plt.vlines(14.3,7,9.2)
plt.vlines(14.3,9.37,11.3)
plt.vlines(14.3,11.46,13.3)
#976
plt.vlines(14.5,7,9.2)
plt.vlines(14.5,9.37,11.3)
plt.vlines(14.5,11.46,13.3)
#977
plt.vlines(14.7,11.711,13.3)
#978
plt.vlines(14.9,11.795,13.3)
#979
plt.vlines(15.1,11.655,13.3)
#982
plt.vlines(21,8.444,10.6)
#983
plt.hlines(10.6,21,22)
#984
plt.vlines(22,9.584,10.6)
#985
plt.vlines(21.5,8.523,10.6)
#986
plt.hlines(10.5,21.1,21.4)
plt.hlines(10.5,21.6,21.9)
#987
plt.hlines(10.25,21.1,21.4)
plt.hlines(10.25,21.6,21.9)
#988
plt.hlines(10,21.1,21.4)
plt.hlines(10,21.6,21.9)
#989
plt.hlines(9.75,21.1,21.4)
plt.hlines(9.75,21.6,21.9)
#990
plt.hlines(9.5,21.1,21.4)
plt.hlines(9.5,21.6,21.875)
#991
plt.hlines(9.25,21.1,21.4)
plt.hlines(9.25,21.6,21.875)
#992
plt.hlines(9,21.1,21.4)
plt.hlines(9,21.6,21.875)
#994
plt.hlines(10,20.2,20.9)
#995
plt.vlines(20.2,8.399,10)
#996
plt.vlines(20.49,8.416,10)
#997
plt.vlines(20.9,8.439,10)
#998
plt.plot([20.51,20.2], [10.558,10],color="k")
#999
plt.plot([20.51,20.49], [10.558,10],color="k")
#1000
plt.plot([20.51,20.9], [10.558,10],color="k")
#1002
plt.vlines(20.59,10.45,11.7)
#1003
plt.vlines(21.7,10.6,11.7)
#1004
plt.hlines(11.7,20.59,21.7)
#1005
plt.vlines(22.7,10.2,12)
#1006
plt.vlines(21.95,10.6,12)
#1007
plt.hlines(12,21.95,22.7)
#1008
plt.plot([21.7,21.95], [11.7,12],color="k")
#1009
x1009 = plt.Rectangle((20.75,11.3),21.1-20.75,0.2,color='k', alpha=0.7)     
ax.add_patch(x1009)
x1009_2 = plt.Rectangle((21.2,11.3),21.55-21.2,0.2,color='k', alpha=0.7)     
ax.add_patch(x1009_2)
#1010
x1010 = plt.Rectangle((20.75,10.9),21.1-20.75,11.1-10.9,color='k', alpha=0.7)     
ax.add_patch(x1010)
x1010_2 = plt.Rectangle((21.2,10.9),21.55-21.2,11.1-10.9,color='k', alpha=0.7)     
ax.add_patch(x1010_2)
#1011
x1011 = plt.Rectangle((20.75,10.9),21.1-20.75,11.1-10.9,color='k', alpha=0.7)     
ax.add_patch(x1011)
x1011_2 = plt.Rectangle((21.2,10.9),21.55-21.2,11.1-10.9,color='k', alpha=0.7)     
ax.add_patch(x1011_2)
#1012
plt.vlines(22.2,9.684,12)
#1013
plt.vlines(22.45,10.2,12)
#1015
plt.vlines(17,10.5,10.9)
#1016
plt.vlines(16.4,10.5,11.2)
#1017
plt.vlines(16.2,10.5,11.2)
#1018
plt.hlines(11.2,16.2,16.75)
#1019
plt.vlines(16.75,10.9,11.2)
#1020
plt.hlines(10.9,16.75,17)
#1021
plt.vlines(16.3,11.2,11.4)
#1024
plt.vlines(19.18,10,11.1)
#1025
plt.vlines(19.75,9.8,11.1)
#1026
plt.hlines(11.1,19.18,19.75)
#1027
plt.hlines(10.5,19.28,19.83)
#1028
plt.hlines(9.8,19.28,19.83)
#1029
plt.vlines(19.28,7.9,11.1)
#1030
plt.vlines(19.83,8.855,9.8)
#1031
plt.hlines(8.855,19.23,19.886)
#1032
plt.vlines(19.886,7.9,8.855)
#1033
plt.vlines(19.37,8,8.75)
plt.vlines(19.37,8.95,9.7)
plt.vlines(19.37,9.9,10.4)
#1034
plt.vlines(19.47,8,8.75)
plt.vlines(19.47,8.95,9.7)
plt.vlines(19.47,9.9,10.4)
#1035
plt.vlines(19.57,8,8.75)
plt.vlines(19.57,8.95,9.7)
plt.vlines(19.57,9.9,10.4)
#1036
plt.vlines(19.67,8,8.75)
plt.vlines(19.67,8.95,9.7)
plt.vlines(19.67,9.9,10.4)
#1037
plt.vlines(19.77,8,8.75)
plt.vlines(19.77,8.95,9.7)
#1039
plt.hlines(9.7,19.83,20.2)
#1041
plt.vlines(19.6,11.1,12.7)
#1042
plt.hlines(12.7,19.6,20)
#1043
plt.vlines(20.2,12,12.5)
#1044
plt.plot([20.2,20], [12.5,12.7],color="k")
#1046
plt.vlines(19.69,11.1,11.8)
#1047
plt.hlines(11.8,19.69,19.88)
#1049
plt.vlines(20.77,11.7,11.8)
#1050
plt.hlines(12,19.88,20.43)
#1051
plt.vlines(20.43,11.8,12)
#1052
plt.hlines(11.8,20.43,20.77)
#1053
plt.vlines(19.88,9.7,12)
#1054
x1054 = plt.Rectangle((20,9.7),0.1,12-9.7,color='k', alpha=0.7)     
ax.add_patch(x1054)
#1055
x1055 = plt.Rectangle((20,9.7),0.1,12-9.7,color='k', alpha=0.7)     
ax.add_patch(x1055)
#1056
plt.vlines(20.35,10.285,11.64)
#1057
plt.hlines(11.64,20.1,20.35)
#1059
plt.hlines(10.6,17,17.5)
#1060
plt.vlines(17.3,10.6,11.4)
#1061
plt.vlines(18.1,10.45,12)
#1062
plt.vlines(17.65,10.8,12)
#1063
x1063 = plt.Rectangle((17.65,11.4),18.1-17.65,12-11.4,color='k', alpha=0.7)     
ax.add_patch(x1063)
#1064
plt.plot([17.65,17.3], [12,11.4],color="k")
#1066
plt.vlines(18.3,10.45,11.5)
#1067
plt.vlines(19.3,11.1,11.5)
#1068
plt.hlines(11.5,18.3,19.3)
#1070
plt.hlines(12,20.815,21.52)
#1071
plt.plot([20.815,20.68], [12,11.8],color="k")
#1072
plt.plot([21.52,21.626], [12,11.7],color="k")
#1073
plt.vlines(20.983,12,12.3)
#1074
plt.vlines(21.368,12,12.3)
#1076
plt.hlines(6.638,25.313,28)
#1077
plt.vlines(25.313,6.36,6.638)
#1078
plt.hlines(6.63,22.379,23.95)
#1079
plt.hlines(6.58,22.508,24)
#1080
plt.plot([23.95,24.6], [6.63,6.58],color="k")
#1081
y1081 = np.arange(6.58,6.63,0.00001)
x1081= (y1081-6.58)*((22.379-22.508)/(6.663-6.58))+22.508
plt.plot (x1081,y1081,'k-')
#1082
plt.vlines(23.9,6.36,6.58)
#1083
plt.vlines(22.55,6.36,6.58)
#1084
plt.vlines(22.42,6.36,6.614)
#1085
y1085 = np.arange(6.82,7,0.00001)
x1085= (y1085-6.638)*((27.306-26.806)/(6.82-6.638))+26.806
plt.plot (x1085,y1085,'k-')
#1086
plt.hlines(7,27.8,30.276)
plt.hlines(7,30.529,33.45)
#1087
plt.hlines(6.82,27.306,34)
#1088
plt.vlines(27.58,6.638,6.82)
#1089
x1089 = plt.Rectangle((30.85,6.36),32-30.85,6.82-6.36,color='k', alpha=0.7)     
ax.add_patch(x1089)
#1090
x1090 = np.arange(28,28.5,0.00001)
y1090 = (x1090-28.5)*((6.638-6.82)/(28-28.5))+6.82
plt.plot (x1090,y1090,'k-')
#1091
plt.vlines(28.5,6.36,6.82)
#1092
plt.vlines(28.65,6.36,6.82)
#1093
plt.vlines(28.8,6.36,6.82)
#1094
plt.vlines(28.95,6.36,6.82)
#1095
plt.vlines(29.1,6.36,6.82)
#1096
plt.vlines(29.25,6.36,6.82)
#1097
plt.vlines(29.4,6.36,6.82)
#1098
plt.vlines(29.55,6.36,6.82)
#1099
plt.vlines(29.7,6.36,6.82)
#1100
plt.vlines(29.85,6.36,6.82)
#1101
plt.vlines(30,6.36,6.82)
#1102
plt.vlines(30.2,6.36,6.82)
#1103
plt.vlines(30.4,6.36,6.82)
#1104
plt.vlines(30.6,6.36,6.82)
#1105
plt.vlines(30.85,6.2,6.82)
#1106
plt.hlines(6.48,28.5,30.85)
#1107
plt.hlines(6.624,28.5,30.85)
plt.hlines(6.624,32,34)
#1108
plt.vlines(28,6.36,6.638)
#1109
x1109 = np.arange(30,30.393,0.00001)
y1109= (x1109-30)*((7.076-6.82)/(30.393-30))+6.82
plt.plot (x1109,y1109,'k-')
#1110
y1110 = np.arange(6.82,7.076,0.00001)
x1110= (y1110-6.82)*((30.393-30.85)/(7.076-6.82))+30.85
plt.plot (x1110,y1110,'k-')
#1111

#1113
plt.vlines(34,6.2,6.82)
#1114
plt.vlines(33.25,6.2,6.82)
#1115
plt.vlines(33.4,6.36,6.82)
#1116
plt.vlines(33.85,6.36,6.82)
#1117
plt.vlines(33,6.36,6.82)
#1118
plt.vlines(32.75,6.36,6.82)
#1119
plt.vlines(32.5,6.36,6.82)
#1120
plt.vlines(32.25,6.36,6.82)
#1121
plt.vlines(32,6.36,6.82)
#1122
x1122 = np.arange(33.25,33.6,0.00001)
y1122= (x1122-33.25)*((7-6.82)/(33.45-33.25))+6.82
plt.plot (x856,y856,'k-')
#1123
x1123 = np.arange(33.6,34,0.00001)
y1123 = (x1123-34)*((7.135-6.82)/(33.6-34))+6.82
plt.plot (x1123,y1123,'k-')
#1125
plt.hlines(6.8,34.27,39)
#1126
plt.vlines(34.27,6.36,6.8)
#1127
plt.vlines(35,6.36,6.8)
#1128
plt.vlines(35.4,6.36,6.8)
#1129
plt.vlines(35.8,6.36,6.8)
#1130
plt.vlines(36.2,6.36,6.8)
#1131
plt.vlines(37,6.36,6.8)
#1132
plt.hlines(6.6,34.27,36.2)
plt.hlines(6.6,37,39)
#1133
x1133 = plt.Rectangle((36.2,6.36),0.8,0.44,color='k', alpha=0.7)     
ax.add_patch(x1133)
#1135

#1136

#1137
plt.hlines(7.57,25.55,24.7)
#1138
plt.hlines(7.57,26.7,25.85)
#1139
plt.vlines(25.7,8.56,7.71)
#1140
plt.vlines(25.7,7.41,6.638)
#1141
x1141 = np.arange(25.599,24.998,0.00001)
y1141 = x1141 - 18.15
plt.plot (x1141,y1141,'k-')
#1142
x1142 = np.arange(26.412,25.811,0.00001)
y1142 = x1142 - 18.15
plt.plot (x1142,y1142,'k-')
#1143
x1143 = np.arange(25.594,24.962,0.00001)
y1143 = -0.9*x1143 +30.7
plt.plot (x1143,y1143,'k-')
#1144
x1144 = np.arange(25.599,24.998,0.00001)
y1144 = -0.9*x1144 +30.7
plt.plot (x1144,y1144,'k-')
#1145
x1145 = np.arange(24.775,25.564,0.00001)
y1145 = 0.4*x1145-2.73 
plt.plot (x1145,y1145,'k-')
#1146
x1146 = np.arange(25.842,26.632,0.00001)
y1146 = 0.4*x1146-2.73
plt.plot (x1146,y1146,'k-')
#1147
x1147 = np.arange(24.775,25.564,0.00001)
y1147 = -0.4*x1147 +17.85
plt.plot (x1141,y1141,'k-')
#1148
x1148 = np.arange(25.842,26.632,0.00001)
y1148 = -0.4*x1148 +17.85
plt.plot (x1148,y1148,'k-')
#1149
x1149 = np.arange(25.258,25.624,0.00001)
y1149 = -2.1*x1149 +61.5
plt.plot (x1149,y1149,'k-')
#1150
x1150 = np.arange(25.752,26.118,0.00001)
y1150 = -2.1*x1150+61.5 
plt.plot (x1150,y1150,'k-')
#1151
x1151 = np.arange(25.266,25.629,0.00001)
y1151 = 2.1*x1151 -46.4 
plt.plot (x1151,y1151,'k-')
#1152
x1152 = np.arange(25.761,26.126,0.00001)
y1152 = 2.1*x1152 -46.4 
plt.plot (x1152,y1152,'k-')
#1153
x1153 = np.arange(24.717,25.614,0.00001)
y1153 = 1.2*x1153-23.3
plt.plot (x1153,y1153,'k-')
#1154
x1154 = np.arange(25.796,26.468,0.00001)
y1154 = -1.2*x1154 +38.4
plt.plot (x1141,y1141,'k-')
#1156
x1156 = np.arange(19.279,20.26,0.00001)
y1156 = -0.19*(x1156-21.1)**2+6.99
plt.plot (x1156,y1156,'k-')
#1157
x1157 = np.arange(20.26,21.05,0.00001)
y1157 = -0.8*(x1157-20.26)**2+6.859
plt.plot (x1157,y1157,'k-')
#1158
x1158 = np.arange(20.987,22.42,0.00001)
y1158 = -0.5*(x1158-21.754)**2+6.73
plt.plot (x1158,y1158,'k-')
#1159
x1159 = np.arange(9,9.68,0.00001)
y1159 = -1.9*(x1159-9.25)**2+7
plt.plot (x1159,y1159,'k-')
#1160
x1160 = np.arange(9.679,9.97,0.00001)
y1160 = -1*(x1160-9.9)**2+6.7
plt.plot (x1160,y1160,'k-')
#1161
x1161 = np.arange(11.2,13.35,0.00001)
y1161 = -0.2*(x1161-12.2)**2+7
plt.plot (x1161,y1161,'k-')
#1162
x1162 = np.arange(9,9.36,0.00001)
y1162 = -0.9*(x1162-9.2)**2+8.6
plt.plot (x1162,y1162,'k-')
#1163

#1165
plt.hlines(6.2,39,9)
#1166
plt.hlines(6.36,39,9)
#1168
plt.vlines(9,20.5,2)
#1169
plt.vlines(39,20.5,2)
#1170
plt.hlines(2,39,9)
#1171
plt.hlines(20.5,39,9)
plt.vlines(18.648,12.34,12.471,color='k')
plt.plot([18.544,18.338],[12.706,12.64],color='k')
plt.vlines(18.823,12.01,12.502,color='k')
plt.vlines(19.16,11.957,12.462,color='k')
plt.vlines(13.6,13.185,13.845,color='k')
plt.vlines(23.5,12.955,13.33,color='k')
plt.hlines(13.33,23.5,24.81,color='k')
plt.vlines(13.2,13.21,13.5,color='k')
plt.hlines(13.5,12.55,13.2,color='k')
plt.hlines(12.8,25.15,26,color='k')
plt.vlines(25.3,12.8,13,color='k')
plt.vlines(25.8,12.8,13,color='k')
plt.hlines(13,25.3,25.8,color='k')
plt.plot([25.3,25.8],[12.8,13],color='k')
plt.hlines(13.419,28.756,29.144,color='k')
plt.vlines(13.2,11.968,12.24,color='k')
plt.hlines(12.24,13.2,14.1,color='k')
plt.vlines(29,14.493,14.7,color='k')
plt.vlines(29,14.48,14.8,color='k')
plt.vlines(29.3,14.471,14.8,color='k')
plt.vlines(30.5,17.4,7.02,color='k')
plt.vlines(31.37,17.4,7.02,color='k')
plt.vlines(29.55,14,7,color='k')
plt.vlines(31.6,14.1,7,color='k')
plt.vlines(30,14.1,7,color='k')
plt.hlines(14.1,31.37,31.6,color='k')
plt.hlines(14.1,30,30.5,color='k')
plt.hlines(14,29.55,30,color='k')
plt.vlines(29.6,17.2,14.011,color='k')
plt.vlines(29.98,17.4,14.096,color='k')
plt.plot([29.6,29.98],[17.2,17.4],'k')
plt.vlines(31.5,17.4,14.1,color='k')
plt.hlines(17.4,31.5,31.37,color='k')
plt.hlines(17.4,30.5,29.98,color='k')
plt.plot([29.98,30.17],[17.4,18.87],'k')
plt.plot([30.384,30.45],[18.87,17.4],'k')
plt.plot([31.207,31.41],[18.87,17.4],'k')
plt.hlines(18.87,30.384,31.207,color='k')
plt.plot([29.635,29.847],[17.218,18.7],'k')
plt.plot([31.15,29.846],[19.34,18.697],'k')
plt.plot([30.258,30.16],[19.34,18.794],'k')
plt.plot([30.258,30.13],[19.34,19.298],'k')
plt.plot([30.334,30.384],[19.34,18.87],'k')
y366=np.arange(18.87,19.34,0.0000001)
x366=(y366-354)/-11
plt.plot(x366,y366,'k-')
y367=np.arange(18.87,19.34,0.0000001)
x367=(y367-355)/-11
plt.plot(x367,y367,'k-')
y368=np.arange(18.87,19.34,0.0000001)
x368=(y368-356)/-11
plt.plot(x368,y368,'k-')
y369=np.arange(18.87,19.34,0.0000001)
x369=(y369-357)/-11
plt.plot(x369,y369,'k-')
y370=np.arange(18.87,19.34,0.0000001)
x370=(y370-358)/-11
plt.plot(x370,y370,'k-')
y371=np.arange(18.87,19.34,0.0000001)
x371=(y371-359)/-11
plt.plot(x371,y371,'k-')
y372=np.arange(18.87,19.34,0.0000001)
x372=(y372-360)/-11
plt.plot(x372,y372,'k-')
y373=np.arange(18.87,19.34,0.0000001)
x373=(y373-361)/-11
plt.plot(x373,y373,'k-')
y374=np.arange(18.87,19.34,0.0000001)
x374=(y374-362)/-11
plt.plot(x374,y374,'k-')
plt.vlines(30.6,7.02,7.72,color='k')
plt.vlines(30.7,7.02,7.72,color='k')
plt.vlines(30.8,7.02,7.72,color='k')
plt.vlines(30.9,7.02,7.72,color='k')
plt.vlines(31,7.02,7.72,color='k')
plt.vlines(31.1,7.02,7.72,color='k')
plt.vlines(31.2,7.02,7.72,color='k')
plt.vlines(31.3,7.02,7.72,color='k')
plt.vlines(30.6,10.862,11.17,color='k')
plt.vlines(30.62,10.862,11.17,color='k')
plt.vlines(30.64,10.862,11.17,color='k')
plt.vlines(30.66,10.862,11.17,color='k')
plt.vlines(30.68,10.862,11.17,color='k')
plt.vlines(30.7,10.862,11.17,color='k')
plt.vlines(30.72,10.862,11.17,color='k')
plt.vlines(30.74,10.862,11.17,color='k')
plt.vlines(30.76,10.862,11.17,color='k')
plt.vlines(30.78,10.862,11.17,color='k')
plt.vlines(30.80,10.862,11.17,color='k')
plt.vlines(30.82,10.862,11.17,color='k')
plt.vlines(30.84,10.862,11.17,color='k')
plt.vlines(30.86,10.862,11.17,color='k')
plt.vlines(30.88,10.862,11.17,color='k')
plt.vlines(30.90,10.862,11.17,color='k')
plt.vlines(30.92,10.862,11.17,color='k')
plt.vlines(30.94,10.862,11.17,color='k')
plt.vlines(30.96,10.862,11.17,color='k')
plt.vlines(30.98,10.862,11.17,color='k')
plt.vlines(31,10.862,11.17,color='k')
plt.vlines(31.02,10.862,11.17,color='k')
plt.vlines(31.04,10.862,11.17,color='k')
plt.vlines(31.06,10.862,11.17,color='k')
plt.vlines(31.08,10.862,11.17,color='k')
plt.vlines(31.10,10.862,11.17,color='k')
plt.vlines(31.12,10.862,11.17,color='k')
plt.vlines(31.14,10.862,11.17,color='k')
plt.vlines(31.16,10.862,11.17,color='k')
plt.vlines(31.18,10.862,11.17,color='k')
plt.vlines(31.20,10.862,11.17,color='k')
plt.vlines(31.22,10.862,11.17,color='k')
plt.vlines(31.24,10.862,11.17,color='k')
plt.vlines(31.26,10.862,11.17,color='k')
plt.vlines(31.28,10.862,11.17,color='k')
plt.vlines(30.60,14.068,13.774,color='k')
plt.vlines(30.62,14.068,13.774,color='k')
plt.vlines(30.64,14.068,13.774,color='k')
plt.vlines(30.66,14.068,13.774,color='k')
plt.vlines(30.68,14.068,13.774,color='k')
plt.vlines(30.70,14.068,13.774,color='k')
plt.vlines(30.72,14.068,13.774,color='k')
plt.vlines(30.74,14.068,13.774,color='k')
plt.vlines(30.76,14.068,13.774,color='k')
plt.vlines(30.78,14.068,13.774,color='k')
plt.vlines(30.80,14.068,13.774,color='k')
plt.vlines(30.82,14.068,13.774,color='k')
plt.vlines(30.84,14.068,13.774,color='k')
plt.vlines(30.86,14.068,13.774,color='k')
plt.vlines(30.88,14.068,13.774,color='k')
plt.vlines(30.90,14.068,13.774,color='k')
plt.vlines(30.92,14.068,13.774,color='k')
plt.vlines(30.94,14.068,13.774,color='k')
plt.vlines(30.96,14.068,13.774,color='k')
plt.vlines(30.98,14.068,13.774,color='k')
plt.vlines(31,14.068,13.774,color='k')
plt.vlines(31.02,14.068,13.774,color='k')
plt.vlines(31.04,14.068,13.774,color='k')
plt.vlines(31.06,14.068,13.774,color='k')
plt.vlines(31.08,14.068,13.774,color='k')
plt.vlines(31.10,14.068,13.774,color='k')
plt.vlines(31.12,14.068,13.774,color='k')
plt.vlines(31.14,14.068,13.774,color='k')
plt.vlines(31.16,14.068,13.774,color='k')
plt.vlines(31.18,14.068,13.774,color='k')
plt.vlines(31.20,14.068,13.774,color='k')
plt.vlines(31.22,14.068,13.774,color='k')
plt.vlines(31.24,14.068,13.774,color='k')
plt.vlines(31.26,14.068,13.774,color='k')
plt.vlines(31.28,14.068,13.774,color='k')
plt.vlines(31.3,14.068,13.774,color='k')
plt.vlines(30.58,15.628,15.926,color='k')
plt.vlines(30.60,15.628,15.926,color='k')
plt.vlines(30.62,15.628,15.926,color='k')
plt.vlines(30.64,15.628,15.926,color='k')
plt.vlines(30.66,15.628,15.926,color='k')
plt.vlines(30.68,15.628,15.926,color='k')
plt.vlines(30.70,15.628,15.926,color='k')
plt.vlines(30.72,15.628,15.926,color='k')
plt.vlines(30.74,15.628,15.926,color='k')
plt.vlines(30.76,15.628,15.926,color='k')
plt.vlines(30.78,15.628,15.926,color='k')
plt.vlines(30.80,15.628,15.926,color='k')
plt.vlines(30.82,15.628,15.926,color='k')
plt.vlines(30.84,15.628,15.926,color='k')
plt.vlines(30.86,15.628,15.926,color='k')
plt.vlines(30.88,15.628,15.926,color='k')
plt.vlines(30.90,15.628,15.926,color='k')
plt.vlines(30.92,15.628,15.926,color='k')
plt.vlines(30.94,15.628,15.926,color='k')
plt.vlines(30.96,15.628,15.926,color='k')
plt.vlines(30.98,15.628,15.926,color='k')
plt.vlines(31,15.628,15.926,color='k')
plt.vlines(31.02,15.628,15.926,color='k')
plt.vlines(31.04,15.628,15.926,color='k')
plt.vlines(31.06,15.628,15.926,color='k')
plt.vlines(31.08,15.628,15.926,color='k')
plt.vlines(31.10,15.628,15.926,color='k')
plt.vlines(31.12,15.628,15.926,color='k')
plt.vlines(31.14,15.628,15.926,color='k')
plt.vlines(31.16,15.628,15.926,color='k')
plt.vlines(31.18,15.628,15.926,color='k')
plt.vlines(31.20,15.628,15.926,color='k')
plt.vlines(31.22,15.628,15.926,color='k')
plt.vlines(31.24,15.628,15.926,color='k')
plt.vlines(31.26,15.628,15.926,color='k')
plt.hlines(7.5,31.6,36.9,color='k')
plt.vlines(36.9,6.8,7.5,color='k')
plt.vlines(35.1,6.8,7.5,color='k')
plt.vlines(33.52,12.161,7.5,color='k')
plt.vlines(34.153,12.161,7.5,color='k')
plt.vlines(33,11,7.5,color='k')
plt.vlines(34.56,11,7.5,color='k')
plt.plot([33.425,33],[12.323,11],'k')
plt.plot([34.2,34.56],[12.323,11],'k')
plt.plot([33.425,33.52],[12.323,12.161],'k')
plt.plot([34.2,34.16],[12.323,12.161],'k')
plt.hlines(12.161,33.52,34.16,color='k')
plt.vlines(33.33,11.76,7.5,color='k')
plt.vlines(34.33,11.76,7.5,color='k')
plt.plot([33.52,34.153],[11.89,11.795],color='k')
plt.plot([33.52,34.153],[11.746,11.694],color='k')
plt.plot([33.52,34.153],[9.976,9.81],color='k')
plt.plot([31.98,32.81],[7,7.4],color='k')
plt.vlines(36.35,7,7.3,color='k')
plt.vlines(36.5,7,7.4,color='k')
plt.hlines(7.3,33,35,color='k')
plt.hlines(7.2,33,35,color='k')
plt.hlines(7.1,33,33.56,color='k')
plt.hlines(7.1,33.6441,35,color='k')
#686
plt.vlines(22.65,6.63,8.54,colors='black')
#687
plt.vlines(21.7,6.79,8.54,colors='black')
#688
plt.vlines(21.1,6.79,8.49,colors='black')
#689
plt.hlines(6.79,21.1,22.65,colors='black')
#690
plt.hlines(8.54,21.7,22.65,colors='black')
#691
x691=np.arange(21.1,21.7,0.00001)
y691=0.0833*x691+6.7316
plt.plot(x691,y691,'k-')
#692
x692=np.arange(20.83,21.1,0.00001)
y692=0.7074*x692-8.136
plt.plot(x692,y692,'k-')
#693
x693=np.arange(21.1,21.587,0.00001)
y693=0.05*x693+7
plt.plot(x693,y693,'k-')
#694
x694=np.arange(21.1,21.587,0.00001)
y694=0.05*x694+6.9
plt.plot(x694,y694,'k-')
#695
x695=np.arange(21.1,21.587,0.00001)
y695=0.05*x695+6.8
plt.plot(x695,y695,'k-')
#696
x696=np.arange(21.1,21.587,0.00001)
y696=0.05*x696+6.7
plt.plot(x696,y696,'k-')
#697
x697=np.arange(21.1,21.587,0.00001)
y697=0.05*x697+6.6
plt.plot(x697,y697,'k-')
#698
x698=np.arange(21.1,21.587,0.00001)
y698=0.05*x698+6.5
plt.plot(x698,y698,'k-')
#699
x699=np.arange(21.1,21.587,0.00001)
y699=0.05*x699+6.4
plt.plot(x699,y699,'k-')
#700
x700=np.arange(21.1,21.587,0.00001)
y700=0.05*x700+6.3
plt.plot(x700,y700,'k-')
#701
x701=np.arange(21.1,21.587,0.00001)
y701=0.05*x701+6.2
plt.plot(x701,y701,'k-')
#702
x702=np.arange(21.1,21.587,0.00001)
y702=0.05*x702+6.1
plt.plot(x702,y702,'k-')
#703
x703=np.arange(21.1,21.587,0.00001)
y703=0.05*x703+6
plt.plot(x703,y703,'k-')
#704
x704=np.arange(21.1,21.587,0.00001)
y704=0.05*x704+5.9
plt.plot(x704,y704,'k-')
#705
x705=np.arange(21.1,21.587,0.00001)
y705=0.05*x705+5.8
plt.plot(x705,y705,'k-')
#706
plt.hlines(8.11,21.794,22.65,colors='black')
#707
plt.hlines(8.01,21.794,22.65,colors='black')
#708
plt.hlines(7.91,21.794,22.65,colors='black')
#709
plt.hlines(7.81,21.794,22.65,colors='black')
#710
plt.hlines(7.71,21.794,22.65,colors='black')
#711
plt.hlines(7.61,21.794,22.65,colors='black')
#712
plt.hlines(7.51,21.794,22.65,colors='black')
#713
plt.hlines(7.41,21.794,22.65,colors='black')
#714
plt.hlines(7.31,21.794,22.65,colors='black')
#715
plt.hlines(7.21,21.794,22.65,colors='black')
#716
plt.hlines(7.11,21.794,22.65,colors='black')
#717
plt.hlines(7.01,21.794,22.65,colors='black')
#718
plt.hlines(6.91,21.794,22.65,colors='black')
#720
plt.hlines(7.9,19,20.1,colors='black')
#721
plt.vlines(19,6.9,7.9,colors='black')
#722
plt.vlines(20.1,6.8,7.9,colors='black')
#723
plt.vlines(19.25,6.36,7.825,colors='black')
#724
plt.hlines(7.825,19.25,20.1,colors='black')
#725
plt.vlines(19.322,6.389,7.825,colors='black')
#726
plt.vlines(19.422,6.455,7.825,colors='black')
#727
plt.vlines(19.522,6.517,7.825,colors='black')
#728
plt.vlines(19.622,6.575,7.825,colors='black')
#729
plt.vlines(19.722,6.629,7.825,colors='black')
#730
plt.vlines(19.822,6.68,7.825,colors='black')
#731
plt.vlines(19.922,6.726,7.825,colors='black')
#732
plt.vlines(20.022,6.769,7.825,colors='black')
#733
plt.hlines(6.9,16,19.2,colors='black')
#734
plt.vlines(16,6.36,6.9,colors='black')
#735
plt.vlines(19.2,6.36,6.9,colors='black')
#736
plt.vlines(19.1,6.36,6.8,colors='black')
#737
plt.vlines(6.8,16.1,19.1,colors='black')
#738
plt.vlines(16.1,6.36,6.8,colors='black')
#741
plt.hlines(8.85,17.175,18.25,colors='black')
#742
plt.vlines(17.175,6.9,8.85,colors='black')
#743
plt.vlines(18.25,6.9,8.85,colors='black')
#744
plt.vlines(17.67,6.9,8.85,colors='black')
#745
plt.hlines(8.65,17.304,17.404,colors='black')
plt.hlines(8.65,17.773,18.16,colors='black')
#746
plt.hlines(8.55,17.304,17.404,colors='black')
plt.hlines(8.55,17.773,18.16,colors='black')
#747
plt.hlines(8.45,17.304,17.404,colors='black')
plt.hlines(8.45,17.773,18.16,colors='black')
#748
plt.hlines(8.35,17.304,17.404,colors='black')
plt.hlines(8.35,17.773,18.16,colors='black')
#749
plt.hlines(8.25,17.304,17.404,colors='black')
plt.hlines(8.25,17.773,18.16,colors='black')
#750
plt.hlines(8.15,17.304,17.404,colors='black')
plt.hlines(8.15,17.773,18.16,colors='black')
#751
plt.hlines(7.95,17.304,17.404,colors='black')
plt.hlines(7.95,17.773,18.16,colors='black')
#752
plt.hlines(7.85,17.304,17.404,colors='black')
plt.hlines(7.85,17.773,18.16,colors='black')
#753
plt.hlines(7.75,17.304,17.404,colors='black')
plt.hlines(7.75,17.773,18.16,colors='black')
#754
plt.hlines(7.65,17.304,17.404,colors='black')
plt.hlines(7.65,17.773,18.16,colors='black')
#755
plt.hlines(7.55,17.304,17.404,colors='black')
plt.hlines(7.55,17.773,18.16,colors='black')
#756
plt.hlines(7.45,17.304,17.404,colors='black')
plt.hlines(7.45,17.773,18.16,colors='black')
#757
plt.hlines(7.35,17.304,17.404,colors='black')
plt.hlines(7.35,17.773,18.16,colors='black')
#758
plt.hlines(7.25,17.304,17.404,colors='black')
plt.hlines(7.25,17.773,18.16,colors='black')
#759
plt.hlines(7.15,17.304,17.404,colors='black')
plt.hlines(7.15,17.773,18.16,colors='black')
#760
plt.hlines(7.05,17.304,17.404,colors='black')
plt.hlines(7.05,17.773,18.16,colors='black')
#762
plt.vlines(13.5,6.625,7,colors='black')
#763
plt.vlines(15.13,6.543,7,colors='black')
#764
plt.vlines(13.35,6.632,7,colors='black')
#765
plt.hlines(7,13.5,15.13,colors='black')
#766
x766=np.arange(9.97,16,0.00001)
y766=-0.05*x766+7.3
plt.plot(x766,y766,'k-')
#767
x767=np.arange(10.3,16,0.00001)
y767=-0.05*x767+7.2
plt.plot(x767,y767,'k-')
#768
plt.vlines(9.97,6.36,6.801,colors='black')
#769
plt.vlines(10.3,6.36,6.685,colors='black')
#773
plt.vlines(13.9,7,8.8,colors='black')
#774
plt.vlines(12.387,6.994,8.8,colors='black')
#775
plt.vlines(12.035,6.995,8.75,colors='black')
#776
plt.vlines(13.9,7,8.8,colors='black')
#777
plt.hlines(8.8,12.387,13.9,colors='black')
#778
plt.hlines(8.539,12.387,13.9,colors='black')
#779
plt.hlines(8.239,12.387,13.9,colors='black')
#780
plt.hlines(7.939,12.387,13.9,colors='black')
#781
plt.hlines(7.639,12.387,13.9,colors='black')
#782
plt.hlines(7.339,12.387,13.9,colors='black')
#783
x783=np.arange(12.035,12.387,0.00001)
y783=0.1408*x783+7.054
plt.plot(x783,y783,'k-')
#784
x784=np.arange(12.04,12.39,0.00001)
y784=0.1*x784+7.3
plt.plot(x784,y784,'k-')
#785
x785=np.arange(12.04,12.39,0.00001)
y785=0.1*x785+7
plt.plot(x785,y785,'k-')
#786
x786=np.arange(12.04,12.39,0.00001)
y786=0.1*x786+6.7
plt.plot(x786,y786,'k-')
#787
x787=np.arange(12.04,12.39,0.00001)
y787=0.1*x787+6.4
plt.plot(x787,y787,'k-')
#788
x788=np.arange(12.04,12.39,0.00001)
y788=0.1*x788+6.1
plt.plot(x788,y788,'k-')





#790
plt.vlines(19.6,7.9,8.386,colors='black')
#791
x791=np.arange(19.96,21.1,0.00001)
y791=0.0561*x791+7.2654
plt.plot(x791,y791,'k-')
#792
plt.vlines(20.716,6.693,8.428,colors='black')
#793
plt.vlines(20.895,6.645,8.35,colors='black')
#794
plt.vlines(20.995,6.63,8.35,colors='black')
#795
plt.vlines(20.795,6.63,8.35,colors='black')
#796
plt.vlines(20.05,7.9,8.3,colors='black')
#797
plt.vlines(20.15,6.819,8.31,colors='black')
#798
plt.vlines(20.25,6.853,8.32,colors='black')
#799
plt.vlines(20.35,6.853,8.33,colors='black')
#800
plt.vlines(20.45,6.83,8.34,colors='black')
#801
plt.vlines(20.55,6.792,8.35,colors='black')
#803

#804

#805

#806

#807
x807=np.arange(14.673,15.031,0.00001)
y807=0.4201*x807+5.5348
plt.plot(x807,y807,'k-')
#814
plt.vlines(16.5,6.9,10,colors='black')
#815
plt.vlines(17.1,6.9,10,colors='black')
#816
plt.vlines(16.8,6.9,10,colors='black')
#817
plt.hlines(10.5,16.01,17.25,colors='black')
#818
plt.vlines(17.25,8.85,10.5,colors='black')
#819
plt.vlines(16.295,6.9,10.5,colors='black')

plt.xlim(7,40)
plt.ylim(0,23) 
plt.show()