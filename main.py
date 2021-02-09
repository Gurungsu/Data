



if __name__ == '__main__':
    print_hi('-------------------Data Science-------------------------------------------')

import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)
p=pd.set_option('display.max_columns', None)
df = pd.read_csv("Crime.csv")
subset = df.loc[:, ['Year', 'Population', 'Year', 'Population', 'ViolentCrime', 'Murder', 'Robbery']]
print(subset)

print('\n---------------------------PERCENTILES-----------------------------------')
percentile = df.loc[:, [ 'ViolentCrime', 'Murder', 'Robbery']]
print(percentile.describe())

# Murder
Q1=df.Murder.quantile(0.25)
Q3 = df.Murder.quantile(0.75)

# Robbery
R1=df.Robbery.quantile(0.25)
R3 = df.Robbery.quantile(0.75)
# ViolentCrime
S1 = df.ViolentCrime.quantile(0.25)
S3 = df.ViolentCrime.quantile(0.75)

print('\n---------------------------IQR PERCENTILES Values Murder-----------------------------------')
print("Percentile vale of Murder 25% : " , Q1)
print("Percentile vale of Murder 75% : " , Q3)
IQR = Q3 -Q1
print("Value of IQR", IQR)

print('\n---------------------------IQR PERCENTILES Values Robbery-----------------------------------')
print("Percentile vale of Murder 25% : " , R1)
print("Percentile vale of Murder 75% : " , R3)
IQR = R3 -R1
print("Value of IQR", IQR)

print('\n---------------------------IQR PERCENTILES Values ViolentCrime-----------------------------------')

print("Percentile vale of Murder 25% : " , S1)
print("Percentile vale of Murder 75% : " , S3)
IQR = S3 - S1
print("Value of IQR", IQR)

lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
print("lower limit: ",lower_limit, "upper limits: ", upper_limit)
lm=df[(df.Murder<lower_limit)|(df.Murder>upper_limit)]
print('\n-------------------Outliers-------------------------')
print(lm)

print('\n-------------------Mean, Median, Mode Robbery Attributes Robbery--------------------------')

print('mean for the attribute Robbery : ', df['Robbery'].mean())
print('median for the attribute Robbery : ', df['Robbery'].median())
print('mode for the attribute Property Robbery : ', df['Robbery'].mode())

print('\n-------------------Mean, Median, Mode Robbery Attributes Murder--------------------------')

print('mean for the attribute Murder : ', df['Murder'].mean())
print('median for the attribute Murder : ', df['Murder'].median())
print('mode for the attribute Property Murder : ', df['Murder'].mode())

print('\n-------------------Mean, Median, Mode Robbery Attributes Rape--------------------------')

print('mean for the attribute Robbery : ', df['Rape'].mean())
print('median for the attribute Robbery : ', df['Rape'].median())
print('mode for the attribute Property Robbery : ', df['Rape'].mode())
print('\n---------------------------------------------------------------------------------------')

x=df['Murder']
y=df['City']
plt.xlabel('Murder')
plt.ylabel('City')
plt.scatter(x,y)
plt.show()
print("---------------------------------------------------------------------------------------------")