import matplotlib.pyplot as plt 
import torch
from crimes import *

# move M or F to the integers like this: M-0, F-1
def move():
    updated_list = []
    for update in train_data['sex']:
        if update == 'M':
            updated_list.append(0)
        else:
            updated_list.append(1)

move()



# for slice in zip(train_data['sex'], train_data['age']):
#     print(slice)

def plotting():
    plt.style.use('ggplot')
    plt.scatter(train_data['age'][:1000], train_data['sex'][:1000])
    plt.show()

plotting()

