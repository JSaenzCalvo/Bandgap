import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter

#variable inicializing
x_points = []
y_points = []
x_pointsr = []
y_pointsr = []
fd = []
fdr = []
deriv = []
derivr = []

#read x from file
with open("number.txt") as textFile:
    x = [line.split()[0] for line in textFile]

#read y from file
with open("number.txt") as textFile:
    y = [line.split()[1] for line in textFile]

#read xr from file
with open("numberinrange.txt") as textFile:
    xr = [line.split()[0] for line in textFile]

#read yr from file
with open("numberinrange.txt") as textFile:
    yr = [line.split()[1] for line in textFile]

#convert list of strings to list of floats
for item in x:
    x_points.append(float(item))
for item in y:
    y_points.append(float(item))
for item in xr:
    x_pointsr.append(float(item))
for item in yr:
    y_pointsr.append(float(item))

#intervas of 0.001 betwen range of data
xx = np.arange((x_points[len(x_points)-1]), (x_points[0]), 0.01)
xxx = np.arange((x_points[len(x_points)-1])-0.5, (x_points[0]-1), 0.01)
xxr = np.arange((x_pointsr[len(x_pointsr)-1]), (x_pointsr[0]), 0.01)

#spline of x and y points 
s = inter.UnivariateSpline(x_points[::-1], y_points[::-1], s=0.01) 
s1 = inter.UnivariateSpline(x_points[::-1], y_points[::-1], s=0.001) 
s2 = inter.UnivariateSpline(x_points[::-1], y_points[::-1], s=0.01) 
sr = inter.UnivariateSpline(x_pointsr[::-1], y_pointsr[::-1], s=0.01) 
sd = s1.derivative(1)
sd2 = s2.derivative(1)

#evaluate derivates of spline with each point in x_points 
#it gets the 0th to 3rd derivate of the spline
#and stores it in deriv as a list of lists
for var in x_pointsr:
    derivr.append(sr.derivatives(var)) 
for var in x_points:
    deriv.append(s.derivatives(var)) 

#gets average of first derivates stored in fd and prints the average
for i in derivr:
   fdr.append(i[1])
for i in deriv:
   fd.append(i[1])

m = float(sum(fdr)/len(fdr))

#lineal aprox
b = float(y_pointsr[len(y_pointsr)-1]-m*x_pointsr[len(x_pointsr)-1])
yy = m*xxx + b

pd = []
for i in deriv:
    pd.append(i[1])

#plotting the spline
plt.plot(xx, s(xx), 'b-', label = 'Spline fit')
#plotting real data
plt.scatter(x_points, y_points, label='Data')
#plotting lineal aprox
plt.plot(xxx, yy, 'r-', label = 'Aprox')
plt.plot(xx, sd(xx), 'g-', label = 'deriv')
plt.plot(xx, sd2(xx), 'y-', label = 'deriv spline')
#plot 
plt.legend()
plt.title("x = "+ str(-b/m))
plt.axhline(color ='k')
plt.xlabel('eV')
plt.ylabel('F')
plt.show()
#buscar como mostrar varios plot
#print derivates in a textfile
file1 = open('results.txt','w')
for x in range(len(deriv)): 
    file1.writelines(str(deriv[x])+'\n')

file1 = open('first derivate.txt','w')
for i in deriv:
    file1.writelines(str(i[1])+'\n')