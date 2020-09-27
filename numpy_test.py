import numpy as np
import pandas as pd

#
# print(np.arange(1,10,2))
#
# print(np.eye(3))
#
# print(np.random.rand(3))
#
# a = np.array([[2,3],[2,4]])
# print(np.square(a)[0,:])

# b = np.array([0,1,2,3,4,5,6,7])
# print(b[-3:-1])

# a=np.array([[1,2],[3,4]])
# print(a[1:])

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
#
# print(s)

df = pd.read_csv('resources/u.rating', sep='\t', header=0)
# print(df.head())
print(df.columns)
# print(df['user_id'])