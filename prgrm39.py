import pandas as pd
df = pd.read_csv('filename.txt', delimiter=' ')
mean=df['column_name'].mean()
print(mean)
