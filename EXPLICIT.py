num_int=123
num_str="456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before type casting:", type(num_str))
 
num_str=int(num_str)
print("Data type of num_str after type casting:", type(num_str))

num_sum =num_int + num_str


print("Sum of num_int and num_str:", num_sum)
print("data type of the sum:",type(num_sum))