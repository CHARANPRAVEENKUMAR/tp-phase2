a=8
b=7
statement1=f"sum of {a} and {b} is {a+b}" # use formatting without any parameters using existed
statement2="sum of {} and {} is {}".format(8,7,8+7) # pass values
statement3="sum of {2} and {1} is {0}".format(8+7,7,8) # pass values in an order
print(statement1)
print(statement2)
print(statement3)
print(type(statement1))
