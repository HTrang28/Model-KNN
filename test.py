import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')
x = train[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range']].values
x = x[:5]
i = 1
# for item in x:
#     print(i,' : ',item,',',item[-1])
#     i+=1
# x = {1, 4, 6, 9, 10}
# arr = set(x)
# print(arr)