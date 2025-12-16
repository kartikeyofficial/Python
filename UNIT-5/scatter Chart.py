import matplotlib.pyplot as plt
yrs=[2010,2011,2012,2013,2014,2015]
sales=[10,25,30,40,50,60]
plt.scatter(yrs,sales,color='g',marker='*',s=100)
plt.plot(yrs,sales,color='r')
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()