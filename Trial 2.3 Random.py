from numpy import random
x = random.randint(100, size = (5))
print("5 Random integers 0 to 100 ",x)
print("type of this list is ",type(x))
x = random.randint(50,100, size=(3,5))
print("an array of 3 rows each containg 5 elements with random numbers between 50 to 100 ", x)
print("type of this list is ",type(x))
x = random.randint(1,6,size=(3))
print(x)
# generate an array with 100 random integer of choice 2,5,7,12 with probability of 0.2, 0.3, 0.4, 0.1
x = random.choice([2,5,7,12], p=[0.2,0.3,0.4,0.1], size=(100))
print(x)
# generate an array of size 10,5 random integer of choice 2,5,7,12 with probability of 0.2, 0.3, 0.4, 0.1
x = random.choice([2,5,7,12], p=[0.2,0.3,0.4,0.1], size=(10,5))
print(x)