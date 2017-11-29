"""
This code is based on code found at: https://commons.wikimedia.org/wiki/File:Beta_distribution_pdf.svg by user Horas based on the work of user Krishnavedala
"""

from matplotlib.pyplot import *
from numpy import linspace
from scipy.stats import beta

x = linspace(0,1,75)

fig = figure()
ax = fig.add_subplot(111)
ax.plot(x,beta.pdf(x,0.5,0.5),label=r"$\alpha_1=\alpha_2=0.5$")
ax.plot(x,beta.pdf(x,5,1),label=r"$\alpha_1=5, \alpha_2=1$")
ax.plot(x,beta.pdf(x,1,3),label=r"$\alpha_1=1, \alpha_2=3$")
ax.plot(x,beta.pdf(x,2,2),label=r"$\alpha_1=2, \alpha_2=2$")
ax.plot(x,beta.pdf(x,1,1),label=r"$\alpha_1=1, \alpha_2=1$")
ax.grid(True)
ax.minorticks_on()
ax.legend(loc=9)
setp(ax.get_legend().get_texts(),fontsize='small')
ax.set_ylim(0,2.6)
ax.set_xlabel("Value of $P^x(1)$")
ax.set_ylabel("Probability Density")

fig.savefig("dirichlet_distribution_pdf.pdf",bbox_inches="tight",\
	pad_inches=.15)

fig = figure()
ax = fig.add_subplot(111)
ax.plot(x,beta.pdf(x,0.5,0.5),label=r"$\alpha_1=\alpha_2=0.5$")
ax.plot(x,beta.pdf(x,0.1,0.1),label=r"$\alpha_1=\alpha_2=0.1$")
ax.plot(x,beta.pdf(x,0.01,0.01),label=r"$\alpha_1=\alpha_2=0.01$")
ax.grid(True)
ax.minorticks_on()
ax.legend(loc=9)
setp(ax.get_legend().get_texts(),fontsize='small')
ax.set_ylim(0,2.6)
ax.set_xlabel("Value of $P^x(1)$")
ax.set_ylabel("Probability Density")

fig.savefig("dirichlet_distribution_sparse_pdf.pdf",bbox_inches="tight",\
	pad_inches=.15)

fig = figure()
ax = fig.add_subplot(111)
ax.plot(x,beta.pdf(x,2,4),label=r"$\alpha_1=2,\alpha_2=4$")
ax.plot(x,beta.pdf(x,100,200),label=r"$\alpha_1=100, \alpha_2=200$")
ax.plot(x,beta.pdf(x,1000,2000),label=r"$\alpha_1=1000, \alpha_2=2000$")
ax.grid(True)
ax.minorticks_on()
ax.legend(loc=9)
setp(ax.get_legend().get_texts(),fontsize='small')
ax.set_ylim(0,2.6)
ax.set_xlabel("Value of $P^x(1)$")
ax.set_ylabel("Probability Density")

fig.savefig("dirichlet_distribution_dense_pdf.pdf",bbox_inches="tight",\
	pad_inches=.15)
