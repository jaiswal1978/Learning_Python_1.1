import pandas as pd
import numpy as np
print("Pandas version is ", pd.__version__)
mydataset = {
    'cars': ['BMW', 'Volve', 'Tata', 'Audi'],
    'ratings': [4.5, 4.0, 4.6, 4.9]
}
myvar = pd.DataFrame(mydataset)
print("this is the first data set created")
print(myvar)
a = {'values': np.array(np.arange(1,10))}
b = np.array(np.random.randint(10,100,10))
index = []
for i in np.array(np.arange(97,106,1)):
    index.append(chr(i))
#Series in Pandas
myvar = pd.Series(a, index=index)
print("This is an example of series")
print(myvar)
myvar = pd.DataFrame(a, index=index)
print(myvar)
print(myvar.loc['e'])
print(myvar.loc[['a','e']])

#importing data file - csv
myvar1 = pd.read_csv('data.csv')
print(myvar1.to_string())
print(type(myvar1))
print(myvar1)

print(myvar1.head())
print(myvar1.tail())
print(myvar1.info())

#Remove rows which have even one empty cell in any column and save it to a new Dataframe
myvar2 = myvar1.dropna()
print(myvar2.to_string())
print(myvar2.info())

#Remove rows which have even one empty cell in any column and save it to Same Dataframe
myvar3 = pd.read_csv('data.csv')
print(myvar3.info())
myvar3.dropna(inplace = True)
print(myvar3.to_string())
print(myvar3.info())

#Replace NULL values with new value of equal to the mean of the coloumn
myvar4 = pd.read_csv('data.csv')
x = myvar4['Calories'].mean()
print(x)
myvar4.fillna(x, inplace=True)
print(myvar4.to_string())

