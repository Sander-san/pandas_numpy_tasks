import numpy as np
from scipy.spatial.distance import cdist


"""
Numpy library 
"""
# Task 1
arr1 = np.random.randint(1, 11, size=(10, ))
arr1[(arr1 > 3) & (arr1 < 8)] *= -1


# Task 2
max_i = np.argmax(arr1)
arr1[max_i] = 0


# Task 3
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# var 1
comb = np.array([(i, j) for i in arr2[0] for j in arr2[1]])
# var 2
mesh = np.meshgrid(*arr2)
combinations = np.vstack([m.flatten() for m in mesh]).T


# Task 4
arr3 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [2, 1, 3],
                 [4, 6, 5],
                 [3, 1, 2],
                 [9, 8, 7],
                 [6, 4, 5]])

arr4 = np.array([[1, 2],
                 [3, 4]])
res = arr3[np.isin(arr3, arr4).sum(axis=1) == arr4.size]


# Task 5
arr5 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [2, 2, 3],
                 [7, 7, 7],
                 [4, 4, 4],
                 [3, 2, 1],
                 [1, 1, 1],
                 [2, 2, 2],
                 [3, 3, 3],
                 [8, 8, 8]])
# Task 6
arr6 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [1, 2, 3],
                 [7, 8, 9],
                 [4, 5, 6]])

unique_arr = np.unique(arr6, axis=0)


'''
Python and nupy
'''
# Task 1
X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])

counter = 0
for i in X:
    for j in i:
        if j == 0:
            counter += 1

zero_in_diagonal = np.diagonal(X)
zero_in_diagonal = np.prod(zero_in_diagonal[zero_in_diagonal != 0])


# Task 2
x = np.array([1, 2, 2, 4])
y = np.array([4, 2, 1, 2])


# Task 3
e = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])


# Task 4
f = np.array([2, 2, 2, 3, 3, 3, 5])


# Task 5
X = np.random.rand(1000, 10)
Y = np.random.rand(500, 10)
distances = np.linalg.norm(X[:, np.newaxis] - Y, axis=2)

distances_cdist = cdist(X, Y)
np.max(np.abs(distances - distances_cdist))


'''
CrunchieMunchies
'''
# Task 1
calorie_stats = np.loadtxt("./data/cereal.csv", delimiter=",")

# Task 2
average_calories = calorie_stats.mean()
diff_calories = round(average_calories - 60)

# Task 3
calorie_stats_sorted = np.sort(calorie_stats)

# Task 4
median_calories = np.median(calorie_stats)

# Task 5
nth_percentile = 0
for i in range(101):
    percentile = np.percentile(calorie_stats_sorted, i)
    if percentile > 60:
        nth_percentile = percentile
        break

# Task 6
more_calories = [x for x in calorie_stats_sorted if x > 60]
gap_percent = round(len(more_calories) / len(calorie_stats_sorted) * 100)
# print(f'Better than {gap_percent}% other products')

# Task 7
calorie_std = np.std(calorie_stats_sorted)

# Task 8
''''
We can use this data to show that this product is less caloric than the other  
Almost 2 times lower than average 
Big gap between other products in general
'''



















