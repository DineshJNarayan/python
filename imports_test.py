## please use 'conda activate test_env' before running script 'python3 imports_test.py'

#import importlib
#toolbox_specs = importlib.util.find_spec("pandas")
#print(toolbox_specs)
#toolbox = importlib.util.module_from_spec(toolbox_specs)
#toolbox_specs.loader.exec_module(toolbox)

import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pylab as plt
import scipy as scpy
import sklearn as skl

print('numpy: {}'.format(np.__version__))
print('pandas: {}'.format(pd.__version__))
print('matplotlib: {}'.format(plt.__version__))
print('scipy: {}'.format(scpy.__version__))
print('mysql.connector: {}'.format(mysql.connector.__version__))
print('sklearn: {}'.format(skl.__version__))

t = np.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()

# Load dataset
mydb = mysql.connector.connect  (   host="127.0.0.1", user="root", password="Vmcp2020Gain", database="MachineLearning"  )
mycursor = mydb.cursor()
query = "SELECT sepal_length, sepal_width, petal_length, petal_width, class FROM iris_ml"
mycursor.execute(query)
records = mycursor.fetchall()

#print(records)
print("mysql success")
print(np.__file__)
print(pd.__file__)
print(mysql.__file__)
print(plt.__file__)
print(scpy.__file__)
print(skl.__file__)