import numpy as np
import matplotlib.pyplot as plt

def prim(x, alpha, n):
        return -(1/(n+1-alpha))*((x**alpha)*((1-x)**(n+1-alpha)))

def integrate(alpha, n, i, j):
    if(alpha == 0):
        print(prim(j, alpha, n)-prim(i, alpha, n))
        return prim(j, alpha, n)-prim(i, alpha, n)
    else:
        return prim(j,alpha, n)-prim(i, alpha, n)+(alpha/(n+1-alpha))*integrate(alpha-1,n,i,j)

def posterior_density_and_mass(alpha, n):
        N = integrate(alpha, n, 0, 1)
        print("N: %f"%N)
        def density(x):
                return ((x**(alpha))*((1-x)**(n-alpha)))/N

        def mass(i, j):
                return integrate(alpha, n, i, j)/N

        return (density, mass)

def table_posterior_density(alpha, n, x_step):
        (d, _) = posterior_density_and_mass(alpha, n)
        
        points = np.arange(0, 1+x_step, x_step)
        values = [d(x) for x in points]
        return (points, values)

plt.subplot(221)
plt.margins(0)
(p,v) = table_posterior_density(4, 9, 0.01)
plt.plot(p,v)
plt.title("alpha = 4, n = 9")
plt.ylabel("posterior density")
plt.xlabel("matching score")
#plt.show()

plt.subplot(222)
plt.margins(0)
(p,v) = table_posterior_density(7, 9, 0.01)
plt.plot(p,v)
plt.title("alpha = 7, n = 9")
plt.ylabel("posterior density")
plt.xlabel("matching score")
#plt.show()


plt.subplot(223)
plt.margins(0)
(p,v) = table_posterior_density(40, 90, 0.01)
plt.plot(p,v)
plt.title("alpha = 40, n = 90")
plt.ylabel("posterior density")
plt.xlabel("matching score")
#plt.show()

plt.subplot(224)
plt.margins(0)
(p,v) = table_posterior_density(70, 90, 0.01)
plt.plot(p,v)
plt.title("alpha = 70, n = 90")
plt.ylabel("posterior density")
plt.xlabel("matching score")

#plt.gca().yaxis.get_major_formatter().set_scientific(False)
plt.show()

p = np.arange(0, 1.1, 0.1)
bins = [(p[i], p[i+1]) for i in range(len(p)-1)]

(d, m) = posterior_density_and_mass(4,9)

t = [m(i, j) for (i,j) in bins ]
print("4,9:")
print(t)


(d, m) = posterior_density_and_mass(40,90)
print("40,90:")
t = [m(i, j) for (i,j) in bins ]
print(t)

x = 0
for v in t:
        x = x+v
print(x)
