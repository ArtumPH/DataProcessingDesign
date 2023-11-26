import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import SelfDefFormatter

"""
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

#plt.style.use('seaborn-v0_8-colorblind')
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)

ax.set_title('Exponent graph',fontsize=14)
ax.set_xlabel('number',fontsize=14)
ax.set_ylabel('exponent',fontsize=14)

ax.tick_params(axis='both',labelsize=14)

plt.show()
"""

x_values=range(1,1001)
y_values=[x**2 for x in x_values]
z_values=[y/1000 for y in y_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=10)
 
ax.set_title("Square number",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of values",fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)

ax.axis([0,1100,0,1100000])
plt.ticklabel_format(axis='both',style='plain',scilimits=(0,0))
#plt.xticks([1,200,300,450])
#plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d k'))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(SelfDefFormatter.y_update_scale_value))

plt.show()
print(dir(SelfDefFormatter))