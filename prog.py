import os
import sys
from pyspark import SparkContext
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Python3 program to add two numbers
num1 = 15
num2 = 12
 
# Adding two nos
sum = num1 + num2
 
# printing values
print("Sum of", num1, "and", num2 , "is", sum)
