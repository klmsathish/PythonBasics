import numpy as np
import matplotlib.pyplot as pyp
import random
import seaborn as sb
import pandas as pd
x = np.random.random((10,1))
print(x)
#pyp.plot(x,".")
#pyp.show()
x = np.linspace(0,10,10)
y = np.power(x,0.5)
a = np.linspace(0,50,10)
b = np.power(x,2)
#pyp.plot(x,y,"+-")
#pyp.show()
#print(x.shape)
sb.set()
#sb.lineplot(x,y)
#pyp.show()
#sb.barplot(a,b)
#pyp.show()
import pandas as pd
df = pd.read_csv('MobileData.csv')
print(df.head())
#pyp.show()
#ax=sb.scatterplot(x='Stand_by_time',y='Battery_life',data=df)
#pyp.show()
uniform_data=np.random.random((10,12))
print(uniform_data)
ax=sb.heatmap(uniform_data)
pyp.show()
import matplotlib.image as mpimg
img = mpimg.imread('hello.png')
print(img)
print()
imgplot = pyp.imshow(img)
pyp.show()