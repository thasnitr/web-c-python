def find_factors(num):
    factors=[]
    for i in range(1,num+1):
        if num % i==0:
            factors.append(i)
    return factors
num=int(input("Enter the number of rows:"))
result=find_factors(num)
print(f"The factors of {num} are:{result}")
