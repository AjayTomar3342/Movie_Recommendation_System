import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

import pandas as pd

cars = {'Brand': [2,3,4,7],
        'Price': [21,22,23,24],
        'val':["A","B","C","D"],
        'userId':[1,2,3,7],
        'rating':[2,3,4,4]
        }
#B,C
df = pd.DataFrame(cars, columns = ['Brand', 'Price','val','userId','rating'])

listy=[2,3,4,7]
result=[3.6,2.5,1.8,4.1]
zipped=dict(zip(listy,result))
sorted_new=dict(sorted(zipped.items(),key=lambda x:x[1], reverse=True))
user_ids=list(sorted_new.keys())
print(user_ids)

for i in user_ids[:3]:
        k=df.loc[df['userId'] == i]
        for individual_rating in k['rating'].values:
                if int(individual_rating)>2:
                        print(k['val'].values)


#result=[3.6,2.5,1.8,4.1]



#Zipping
# k=dict(zip(listy, result))
#
# sort_orders = dict(sorted(k.items(), key=lambda x: x[1], reverse=True))
#
# for key in sort_orders.keys():
#         k2 = df.loc[df['Brand'] == key]
#         print(k2['val'].values)
#



