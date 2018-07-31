import numpy as np
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt

# define pts from the question

pts = np.array([
[12.35823 , 76.59615],
[12.35809 , 76.59594],
[12.35821 , 76.5961],
[12.35826 , 76.59612],
[12.3583 , 76.59617],
[12.35831 , 76.59619],
[12.35829 , 76.59612],
[12.35832 , 76.59616],
[12.35839 , 76.59623],
[12.35834 , 76.59619],
[12.35831 , 76.59614],
[12.35834 , 76.59616],
[12.35835 , 76.5962],
[12.35832 , 76.59619],
[12.35834 , 76.5962],
[12.35832 , 76.59618],
[12.35831 , 76.59617],
[12.35833 , 76.5962],
[12.35831 , 76.59618],
[12.3583 , 76.59618],
[12.35829 , 76.59617],
[12.35832 , 76.5962],
[12.35831 , 76.5962],
[12.35829 , 76.59615],
[12.35829 , 76.59614],
[12.3583 , 76.59615],
[12.35826 , 76.59616],
[12.35826 , 76.59617],
[12.35825 , 76.59615],
[12.35826 , 76.59615],
[12.35826 , 76.59614],
[12.35827 , 76.59614],
[12.35825 , 76.59614],
[12.35827 , 76.59615],
[12.35827 , 76.59616],
[12.35828 , 76.59616],
[12.35828 , 76.59617],
[12.35827 , 76.59617],
[12.35825 , 76.59617],
[12.35824 , 76.59617],
[12.35823 , 76.59617],
[12.35824 , 76.59616],
[12.35825 , 76.59616],
[12.35828 , 76.59615],
[12.35829 , 76.59616],
[12.35828 , 76.59618],
[12.35828 , 76.59619],
[12.35827 , 76.59619],
[12.35827 , 76.5962],
[12.35827 , 76.59621],
[12.35826 , 76.59622],
[12.35826 , 76.59623],
[12.35825 , 76.59623],
[12.35825 , 76.59624],
[12.35825 , 76.59625],
[12.35824 , 76.59625],
[12.35824 , 76.59626],
[12.35824 , 76.59627],
[12.35823 , 76.59627],
[12.35823 , 76.59628],
[12.35822 , 76.59628],
[12.35821 , 76.59629],
[12.3582 , 76.59629],
[12.35819 , 76.59629],
[12.35818 , 76.59629],
[12.35818 , 76.59628],
[12.35817 , 76.59628],
[12.35817 , 76.59627],
[12.35817 , 76.59626],
[12.35817 , 76.59625],
[12.35817 , 76.59624],
[12.35817 , 76.59623],
[12.35817 , 76.59622],
[12.35818 , 76.59621],
[12.35819 , 76.5962],
[12.35819 , 76.59619],
[12.35818 , 76.59618],
[12.35818 , 76.59617],
[12.35818 , 76.59616],
[12.35818 , 76.59615],
[12.35818 , 76.59614],
[12.35818 , 76.59613],
[12.35818 , 76.59612],
[12.35818 , 76.59611],
[12.35818 , 76.5961],
[12.35818 , 76.59609],
[12.35819 , 76.59609],
[12.35819 , 76.59608],
[12.3582 , 76.59608],
[12.3582 , 76.59607],
[12.35821 , 76.59607],
[12.35822 , 76.59607],
[12.35822 , 76.59606],
[12.35823 , 76.59607],
[12.35824 , 76.59607],
[12.35825 , 76.59607],
[12.35826 , 76.59607],
[12.35827 , 76.59607],
[12.35828 , 76.59607],
[12.35828 , 76.59608],
[12.35829 , 76.59608],
[12.3583 , 76.59608],
[12.3583 , 76.59609],
[12.35831 , 76.59609],
[12.35831 , 76.5961],
[12.35831 , 76.59611],
[12.35831 , 76.59612],
[12.35831 , 76.59613],
[12.3583 , 76.59614],
[12.35831 , 76.59615],
[12.35831 , 76.59616],
[12.3583 , 76.59616],
[12.35828 , 76.59614],
[12.35828 , 76.59613],
[12.35829 , 76.59613],
[12.35832 , 76.59614],
[12.3583 , 76.59613],
[12.35827 , 76.59613],
[12.35825 , 76.59613],
[12.35824 , 76.59613],
[12.35823 , 76.59613],
[12.35822 , 76.59613],
[12.35821 , 76.59613],
[12.35821 , 76.59612],
[12.35821 , 76.59611],
[12.35823 , 76.59614],
[12.35824 , 76.59614],
[12.35829 , 76.59618],
[12.35829 , 76.59619],
[12.35829 , 76.5962],
[12.35828 , 76.5962],
[12.35828 , 76.59621],
[12.35828 , 76.59622],
[12.35828 , 76.59623],
[12.35827 , 76.59623],
[12.35829 , 76.59621],
[12.3583 , 76.59619],
[12.35826 , 76.59613],
[12.35833 , 76.59614],
[12.35833 , 76.59616],
[12.35828 , 76.59612],
[12.35827 , 76.59612],
[12.35828 , 76.59611],
[12.35827 , 76.59611],
[12.35835 , 76.59615],
[12.35834 , 76.59615],
[12.3583 , 76.59612],
[12.35832 , 76.59613],
[12.35833 , 76.59615],
[12.35835 , 76.59616],
[12.35836 , 76.59616],
[12.35834 , 76.59617],
[12.35833 , 76.59617],
[12.35834 , 76.59618],
[12.35835 , 76.59618],
[12.35832 , 76.59615],
[12.35832 , 76.59621],
[12.35832 , 76.59622],
[12.35833 , 76.59623],
[12.35833 , 76.59625],
[12.35834 , 76.59626],
[12.35834 , 76.59628],
[12.35835 , 76.59629],
[12.35835 , 76.59631],
[12.35836 , 76.59633],
[12.35854 , 76.59767],
[12.35857 , 76.59812],
[12.35859 , 76.59839],
[12.35862 , 76.59866],
[12.35734 , 76.59759],
[12.35724 , 76.59764],
[12.358 , 76.5967],
[12.35799 , 76.59671],
[12.35801 , 76.59669],
[12.35801 , 76.59668],
[12.35805 , 76.59663],
[12.35823 , 76.59643],
[12.35828 , 76.59638],
[12.35828 , 76.59637],
[12.35827 , 76.59638],
[12.35827 , 76.59639],
[12.35826 , 76.59639],
[12.35825 , 76.5964],
[12.35825 , 76.59641],
[12.35824 , 76.59641],
[12.35824 , 76.5964],
[12.35825 , 76.59639],
[12.35825 , 76.59638],
[12.35842 , 76.59621]
])

tck, u = splprep(pts.T, u=None, s=0.0, per=1) 
u_new = np.linspace(u.min(), u.max(), 1000)
x_new, y_new = splev(u_new, tck, der=0)

plt.plot(pts[:,0], pts[:,1], 'ro')
plt.plot(x_new, y_new, 'b--')
plt.show()