import datetime
import os

#import pandas as pd
#
#df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]}, index=['falcon', 'dog'])
#print(df)
#
#print(datetime.datetime.now())
try:
    print(os.environ["VAR_1"], "ми прочитали змінну")
except KeyError as e:
    print("Сталась помилка")
    print(e)

print("Програма виконалась")