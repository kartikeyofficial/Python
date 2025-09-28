import matplotlib.pyplot as plt
yrs=[2010,2011,2012,2013,2014,2015]
sales=[10,20,30,40,50,60]
plt.bar(yrs,sales,marker='*',color='red')
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()