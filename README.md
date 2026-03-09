# Numerical Methods for ODEs: Three-Body Problem and Accuracy Testing

This repository contains Python implementations of numerical methods for solving Ordinary Differential Equations (ODEs). The project is divided into two main parts: simulating an orbit in the restricted three-body problem and testing the accuracy of various mathematical algorithms.

## Project Description

### Project 1: Three-Body Problem (`project1.py`)
This script solves the restricted three-body problem, specifically modeling the Earth-Moon system. To calculate the trajectory, it uses three different numerical methods:
* **Euler Method**
* **Runge-Kutta 4th Order (RK4)**
* **Dormand-Prince Method**

The output is a plotted visualization of the orbit, allowing for a direct visual comparison of how each algorithm performs.

### Project 2: Dormand-Prince Accuracy Test (`project2.py`)
This script evaluates the accuracy of the Dormand-Prince algorithm using a set of test differential equations with known exact solutions. It calculates and outputs the absolute error of the method for a given number of iterations. It also explores step-size modification to assess the reliability of the algorithm.

## Prerequisites

To run this code on your local machine, you need Python 3.6 or higher installed, along with a few external libraries.

Install the required libraries using the following command in your terminal:

```bash
pip install numpy matplotlib
```
## How To Use


