import numpy as np
from math import sqrt
from collections import Counter
dataset = {'a' : [[1, 2], [3, 4], [1, 3]], 'b' : [[7, 8], [10, 11], [7, 9]]}
predict = [5, 7]
def knn(data, pre, k) : 
	if(len(data) >= k):
		return "The dataset size is lesser than k"
	dist = []
	for grp in data : 
		for i in data[grp] : 
			temp = np.linalg.norm(np.array(i) - np.array(pre))
			dist.append([temp, grp])
	sorted(dist)
	votes = [i[1] for i in dist[:k]]
	result = Counter(votes).most_common(1)
	return result[0][0]

res = knn(dataset, predict, 3)
print(res)
