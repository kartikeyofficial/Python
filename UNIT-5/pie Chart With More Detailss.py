import matplotlib.pyplot as plt
import numpy as np
mylabels=['Delhi','Lucknow','Kanpur','Greater Noida']
y= np.array([68,24,30,55,60])
explodedata=[0.2,0,0,0,0]
plt.pie(y,labels=mylabels,explode=explodedata)
plt.show()