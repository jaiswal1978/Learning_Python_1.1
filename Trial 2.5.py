import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0,5,10,15])
ypoints = np.array([0,20,45,0])
#plt.plot(xpoints,ypoints,'x')
plt.plot(ypoints)
#plt.plot(xpoints,ypoints,marker = "v")
'''
#plot with lines
plt.plot(xpoints, ls = 'dashed')
plt.plot(xpoints,ypoints, ls = ':', lw = '5.0', c = 'r' )
plt.show()
'''
x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,3,4])
plt.plot(x1,y1, x2, y2, c = 'r', ls = ':', lw = '3')
plt.show()

#Sub plots
#plot with 1 row and two coloum
#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()

#plot with 2 row and 1 coloum
#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.plot(x,y)

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()

#plot with 4 rows and 3 coloums
#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,1)
plt.plot(x,y)
plt.title("ABC 1")

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,2)
plt.plot(x,y)
plt.title("ABC - 2")

#Plot 3
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,3)
plt.plot(x,y)
plt.title("ABC - 3")

#plot 4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,4)
plt.plot(x,y)
plt.title("ABC - 4")

#Plot 5
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,5)
plt.plot(x,y)
plt.title("ABC - 5")

#plot 6
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,6)
plt.plot(x,y)
plt.title("ABC - 6")

#Plot 7
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,7)
plt.plot(x,y)
plt.title("ABC - 7")

#plot 8
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,8)
plt.plot(x,y)
plt.title("ABC - 8")

#Plot 9
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,9)
plt.plot(x,y)
plt.title("ABC - 9")

#plot 10
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,10)
plt.plot(x,y)
plt.title("ABC - 10")

#Plot 11
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(4,3,11)
plt.plot(x,y)
plt.title("ABC - 11")

#plot 12
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(4,3,12)
plt.plot(x,y)
plt.title("ABC - 12")

plt.suptitle("Chart with 4 rows and 3 coloums")
plt.show()

