from operator import length_hint
from time import time

lst = [1,2,3,4,5,6]
# method 1
start_time1 = time()
count = 0
for i in lst:
    count +=1
print("length using for loop ",count)
total_time = time()- start_time1
print('total time: ',total_time)

# method2
start_time2 = time()
count = len(lst)
print('total_time :',time()-start_time2)

# method3
start_time3 = time()
count = length_hint(lst)
print('total_time :',time()-start_time3)