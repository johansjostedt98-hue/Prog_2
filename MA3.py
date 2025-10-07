""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc


# Ex 1 ######
import numpy as np


def approximate_pi(n): # Ex1
    nc = 0

    for _ in range(n+1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if np.sqrt(x**2 + y**2 ) <= 1:
            nc += 1
            circle_x.append(x)
            circle_y.append(y)
        else:
            box_dot_x.append(x)
            box_dot_y.append(y)

    return  4*(nc/n)

circle_x, circle_y = [], []
box_dot_x, box_dot_y = [], []



# plt.scatter(circle_x, circle_y, label ='inside circel', color = 'r', s = 1)
# plt.scatter(box_dot_x, box_dot_y, label =' Outside circle', color = 'b', s = 1)

# plt.title("Montecarlo plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()
import functools

def sphere_volume(n, d): #Ex2, approximation
    random_points  = [tuple(random.uniform(-1, 1) for i in range(d)) for _ in range(n)] # listbyggare
    
    def Vector_length(tpl):
        square = map(lambda x: x**2, tpl) # map
        return np.sqrt(functools.reduce(lambda a, b: a + b, square)) #reduce
    
    n_inside = len(list(filter(lambda point: Vector_length(point)<1, random_points))) # filter #lambda

    return float((2**d)*(n_inside/n))


def hypersphere_exact(d): #Ex2, real value
    exact_vaclue = lambda d: np.pi**(d/2)/m.gamma(d/2+1)
    return exact_vaclue(d)

print(hypersphere_exact(11))
#Ex3: parallel code - parallelize for loop

############################ Ex3 : Calculate the average of the functions’ outputs.###########################
# times = []

# n , d = 10**5, 11
# for _ in range(10):
#     start_time = pc()
#     sphere_volume(n, d)
#     end_time = pc()
#     times.append(end_time-start_time)

# avg_time = sum(times)/len(times)
# print(f'avg_time is {avg_time}, total time = {sum(times)}')
#part 2 övening Exercise 3

import concurrent.futures as future



def sphere_volume_parallel1(n,d,np=10):
    
    with future.ProcessPoolExecutor(max_workers= np) as ex:
        futures = [ex.submit(sphere_volume, n, d) for _ in range(np)]
        #r = futures.result()
        #result = ex.map(sphere_volume(n, d), [i for i in range(np)])
        result = [i.result() for i in futures] #konstigt
    
    return sum(result)/len(result)

'''[n for c in range(np)]
 

[d for cc in range(np)]
Results = list(ex.map())
mean(results)'''

def sphere_volume_parallel2(n,d,np=10):
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, int(n/np), d) for _ in range(np)]
        results = [r.result() for r in futures]
        
    return mean(results)

#print(sphere_volume_parallel2(n,d,np=10))

    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    # times = []
    # for _ in range(np):
    #     start_time = pc()

    #     sphere_volume(n, d)

    #     end_time = pc()

    #     times.append(end_time-start_time)

    # avg_time = sum(times)/len(times)

    # return avg_time, sum(times)

#Ex4: parallel code - parallelize actual computations by splitting data
# def sphere_volume_parallel2(n,d,np=10):
#     times = []
#     for _ in range(np):
#         start_time = pc()

#         p1 = mp.Process(target=sphere_volume, args = (n, d))
#         p2 = mp.Process(target=sphere_volume, args = (n, d))
    
#         p1.start()
#         p2.start()

#         p1.join()
#         p2.join()

#         end_time = pc()
#         times.append(end_time-start_time)
#     avg_time = sum(times)/len(times)
    
#     n is the number of points
#     d is the number of dimensions of the sphere
#     np is the number of processes
#     return avg_time, sum(times)


def main():
    # #Ex1
    # dots = [1000, 10000, 100000]
    # for n in dots:
    #     approximate_pi(n)
    # #Ex2
    # n = 100000
    # d = 2
    # sphere_volume(n,d)
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)} m^{d} ")

    # n = 100000
    # d = 11
    # sphere_volume(n,d)
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)} m^{d} ")

    # Ex3
    # n = 100000
    # d = 11
    # start = pc()
    # for y in range (10):
    #     sphere_volume(n,d)
    # stop = pc()
    # print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    # print("What is parallel time?")

    ## Ex4
    # n = 1000000
    # d = 11
    # start = pc()
    # sphere_volume(n,d)
    # stop = pc()
    # print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    # print("What is parallel time?")

    # start = pc()
    # sphere_volume_parallel1(10**5, 11)
    # end = pc()
    # time = (end - start)
    # print(time)

    start = pc()
    print(sphere_volume_parallel2(10**5, 11))
    end = pc()
    time = (end - start)
    print(time)

    
    

if __name__ == '__main__':
    main()

