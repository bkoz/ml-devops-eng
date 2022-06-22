import pandas as pd
df = pd.read_csv('./data/iris.csv', sep=',')
print(f'{df.loc[0][0] == 5.1}')