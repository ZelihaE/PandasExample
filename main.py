import pandas as pd
import numpy as np

numpy_array = np.array([10,20,30,40])

#pandas(data= , index= ) data ve index kısmında index verisi olmazsa kendisi ekler.
pandas_series = pd.Series(numpy_array)
print(pandas_series)

name_list = ["James", "Lars", "Kirk", "Rob"]

my_series = pd.Series(data=numpy_array, index=name_list)
print(my_series)

my_series["Kirk"] = 100
print(my_series )