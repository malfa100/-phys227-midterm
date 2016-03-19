# phys227-midterm

**Author:** Andrew Malfavon

[![Build Status](https://travis-ci.org/malfa100/-phys227-midterm.svg?branch=master)](https://travis-ci.org/malfa100/-phys227-midterm)

**Due date:** 2016/03/20

## Specification

The following discrete update map is implemented as a function **sequence(x0, r, N=100)**:
$$x_{n+1}=rx_{n}(1-x_n)$$
The code is placed in the file **midterm.py** and imported and presented in the Jupyter notebook **Midterm.ipynb**. The sequence is first plotted for specific $r$ values and then plotted again for different $x_0$ values. After these plots are analyzed, the asymptotic values of the sequence are plotted by creating a range of $r$ with a specified mesh spacing and each $r$ is used to create a sequence of $\{x_n\}$. The first part of $\{x_n\}$ is discarded and the asymptotic tail is used in the graph.


## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Andrew Malfavon