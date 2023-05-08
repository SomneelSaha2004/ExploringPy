def fibonacci(n:int)->int:
    nums=[0,1]
    if(n==1):
        return 0
    elif(n==2):
        return 1

    for i in range(2,n+2):
        nums.append(nums[i-1]+nums[i-2])
    return nums[-1]
print(list(map(fibonacci,[1,2,3,4,5,6])))