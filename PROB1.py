import pandas as pd

data1 = {'Student':['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}

data2 = {'Student':['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}

data3 = {'Student':['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,94]}

data4 = {'Student':['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}

A = pd.DataFrame(data1, columns = ['Student','Math'])

B = pd.DataFrame(data2, columns = ['Student','Electronics'])

C = pd.DataFrame(data3, columns = ['Student','GEAS'])

D = pd.DataFrame(data4, columns = ['Student','ESAT'])

merge1 = pd.merge(A,B,on = 'Student')

merge2 = pd.merge(merge1,C,on = 'Student')

merge3 = pd.merge(merge2,D,on = 'Student')

long = pd.melt(merge3, id_vars = ['Student'], var_name = 'Subject', value_name = 'Grades')

print(long)