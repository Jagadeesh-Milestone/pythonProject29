#DataFrame:
import pandas as pd

data={'fruits':['banana','apple','mango'],
      'cost/kg':['40','100','70']}
x=pd.DataFrame(data)
print(x)
print(x.loc[0])
print(x.loc[1])