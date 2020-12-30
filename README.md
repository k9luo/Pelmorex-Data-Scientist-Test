# Pelmorex-Data-Scientist-Test
====================================================================

![](https://img.shields.io/badge/linux-ubuntu-red.svg)

![](https://img.shields.io/badge/python-3.7.6-green.svg)

![](https://img.shields.io/badge/scipy-1.5.2-blue.svg)
![](https://img.shields.io/badge/numpy-1.19.1-blue.svg)
![](https://img.shields.io/badge/sklearn-0.23.2-blue.svg)
![](https://img.shields.io/badge/jupyter-1.0.0-blue.svg)
![](https://img.shields.io/badge/ipython-7.18.1-blue.svg)
![](https://img.shields.io/badge/pandas-1.1.3-blue.svg)

## Objective

The goal is to build a model that can predict if a user will click or not based on the available data points.

## Solution

Solutions:

- First, we perform exploratory data analysis to inspect the dataset.
- Then, we perform feature engineering.
- Finally, because of the nature of logistic activation function, the output from logistic regression is probability calibrated. We can simply apply a threshold on prediction results to determine if the system should recommend ads to users. I choose logistic regression as the learning algorithm for this task.

The detailed analysis can be found in this [notebook](https://github.com/k9luo/Pelmorex-Data-Scientist-Test/blob/main/main.ipynb).
