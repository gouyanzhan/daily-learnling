#输出一个由*组成的直角三角形
#*
#**
#***
#****
#*****

for i in range(1,6):
    print("*" * i)

#写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和
j_sum = 0
o_sum = 0
for i in range(0,101):

    if i%2 == 0:
        o_sum += i
    else:
        j_sum += i
print("偶数和",o_sum)
print("奇数和",j_sum)