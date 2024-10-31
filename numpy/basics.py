import numpy as np

# ------ create operations  --------
data = np.random.rand(2, 3, 4)
zeroes = np.zeros((2, 2, 2))
ones = np.ones((2, 2, 2))
full = np.full((2, 2, 2), 7)  # elements will be 7

arr = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])

type(arr)
print(full)


# ------ read operations  --------
shape = data.shape
size = data.size
types = data.dtype

arr = data[0]
slicer = data[0:2]
slicer2 = data[0][0:2]
reverse = data[-1]
singleval = data[0][0][0]

# ------ update operations  --------
list1 = np.random.rand(10)
list2 = np.random.rand(10)

# basic maths
add = np.add(list1, list2)
sub = np.subtract(list1, list2)
div = np.div(list1, list2)
mult = np.multiply(list1, list2)
dot = np.dot(list1, list2)

# statistic functions (saplemf)
sqrt = np.sqrt(25)
ab = np.abs(-2)
power = np.power(2, 7)
log = np.log(25)
exp = np.exp([2, 3])
min = np.min(list1)
max = np.max(list1)

data[0][0] = 700
data.sort()
data.reshape((2, 2, -1)) # last dimension will be auto calculated

zeroes = np.zeros(8)
zeroes = np.append(zeroes, [3, 4]) # end e insert
zeroes = np.insert(zeroes, 2, 1) # position 2 te 1 insert

# ------ delete operations  --------
np.delete(data, 0, axis = 1) # axis = 1 means row
np.save("new array", data)
test = np.load("new array.npy")