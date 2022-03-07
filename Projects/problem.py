import numpy as np
import pandas as pd


x=10000
y=5
K=[round((p/x)*y,4) for p in range(0, int(x))]
data = {'number': K}
df = pd.DataFrame(data, columns = ['number'])
df.to_excel('example.xlsx', sheet_name='example')