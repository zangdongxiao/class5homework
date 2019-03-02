#!/usr/bin/env python

import argparse
import os
import os.path as op
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("my_file",
                       type=str, help="Path to the input csv file.")
args = parser.parse_args()

my_file = args.my_file



header_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
data = pd.read_csv(my_file, sep='\s+|,', header=None, names=header_names)
print(data.head())

print(data.shape)
print(data.iloc[3:5,:])



print(np.mean(data))
print(np.std(data))
print(np.average(data))


#1 feature(column)
plt.figure(figsize=(8,8))
plt.hist(data.iloc[:, -1], bins=30, rwidth=0.9)
plt.savefig("MEDV.png")

plt.show()

#2 fetures(column)
plt.figure(figsize=(8,8))
plt.scatter(data.iloc[:, -1], data.iloc[:, 6])
plt.savefig("AGE vs MEDV.png")

plt.show()
