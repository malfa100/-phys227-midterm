"""
File: midterm.py
Copyright (c) 2016 Andrew Malfavon
PHYS227 Midterm
License: MIT
Analysis of a discete update map.
"""

import numpy as np
import matplotlib.pyplot as plt

#while loop used to creat an array of x-values depending on a specified initial value and r.
def sequence(x0, r, N = 100):
    n = 1
    x = np.zeros(N + 1)
    x[0] = x0
    while n <= N:
        x[n] = (r * x[n - 1]) * (1 - x[n - 1])
        n += 1
    return x

#testing to make sure the sequence gives correct values.
#the values were calculated by hand and will be tested here.
def test_sequence():
    assert sequence(0.5, 2.5)[100] == 0.6
    assert sequence(0.5, 2.5)[1] == 0.625
    assert sequence(0.5, 3.2)[1] == 0.8
    assert sequence(0.5, 3.5)[1] == 0.875

#graphs three different r-values on the same graph with the same initial conditions.
def graph(r1, r2, r3, xmin, xmax, ymin, ymax, x0, n = 101):
    x_values_r1 = sequence(x0, r1)
    x_values_r2 = sequence(x0, r2)
    x_values_r3 = sequence(x0, r3)
    n_values = np.linspace(0, 100, n)
    plt.plot(n_values, x_values_r1)
    plt.plot(n_values, x_values_r2)
    plt.plot(n_values, x_values_r3)
    plt.title('Discrete Update Map')
    plt.xlabel('$n$', **{'fontsize' :20})#for font size of the axes labels
    plt.ylabel('$x_n$', **{'fontsize' :20})
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

#similar graph but allows 9 different x-values to be graphed with the same r-value.
def graph2(x1, x2, x3, x4, x5, x6, x7, x8, x9, xmin, xmax, ymin, ymax, r, n = 101):
    x_values_x1 = sequence(x1, r)#each specified x-value is put the the sequence
    x_values_x2 = sequence(x2, r)#x-values can be called "0" if we want to graph less than 9 values
    x_values_x3 = sequence(x3, r)
    x_values_x4 = sequence(x4, r)
    x_values_x5 = sequence(x5, r)
    x_values_x6 = sequence(x6, r)
    x_values_x7 = sequence(x7, r)
    x_values_x8 = sequence(x8, r)
    x_values_x9 = sequence(x9, r)
    n_values = np.linspace(0, 100, n)
    plt.plot(n_values, x_values_x1)
    plt.plot(n_values, x_values_x2)
    plt.plot(n_values, x_values_x3)
    plt.plot(n_values, x_values_x4)
    plt.plot(n_values, x_values_x5)
    plt.plot(n_values, x_values_x6)
    plt.plot(n_values, x_values_x7)
    plt.plot(n_values, x_values_x8)
    plt.plot(n_values, x_values_x9)
    plt.title('Discrete Update Map')
    plt.xlabel('$n$', **{'fontsize' :20})
    plt.ylabel('$x_n$', **{'fontsize' :20})
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

#same as the first sequence function except N can be implemented manually.
def sequence_new(x0, r, N):
    n = 1
    x = np.zeros(N + 1)
    x[0] = x0
    while n <= N:
        x[n] = (r * x[n - 1]) * (1 - x[n - 1])
        n += 1
    return x

#the parameters for an r-array can be implemented as well as the size of the mesh between each value.
#n and N represent the beginning and end of the x-array.
def graph3(ra, rb, mesh, x0, n, N, xmin, xmax, ymin, ymax):
    r = np.linspace(ra, rb, ((rb - ra) / mesh) + 1)#creates the r-array
    xn = []#this will be the full x-array
    xn_tail = []#this will be the shortened array used as the asymptotic tail
    for i in range(int((rb - ra) / mesh) + 1 ):#puts each r-value into the sequence equation for each x-value
        x = sequence_new(mesh, r[i], N)
        xn.append(x)
    for j in range(int((rb - ra) / mesh) + 1):#shortens the x-array based on the n and N values
        x_tail = xn[j][n:N + 1]
        xn_tail.append(x_tail)
    plt.figure(figsize=(50, 50))#makes the graph larger
    plt.plot(r, xn_tail, 'ro')
    plt.title('Asymptotic Values of the Sequence', **{'fontsize' :50})
    plt.xlabel('$r$', **{'fontsize' :50})
    plt.ylabel('$x_n$', **{'fontsize' :50})
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)