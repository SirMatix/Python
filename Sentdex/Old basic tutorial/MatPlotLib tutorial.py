from matplotlib import pyplot as plt
from matplotlib import style

#style.use('ggplot')

x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

##print(len(x))
##print(len(y))
plt.grid(True, color='k')
plt.scatter(x,y, linewidth=5, label='Line One')
plt.scatter(x2,y2, linewidth=10, label='Line Two')

plt.title('epic chart')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()



plt.show()
 
