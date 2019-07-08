#1. 최고값을 구하는 함수 작성 : my_max()
#2. 최저값을 구하는 함수 작성 : my_min()
#3. 합계를 구하는 함수 작성 : my_sum()
#4. 평균을 구하는 함수 작성 : my_avg()




##1. 
def my_max(x):
  maxium = x[0]
  for i in range(len(x)):
    if maxium < x[i]: 
       maxium = x[i]
  return( maxium )



print(my_max([20,2,3,4,9,15]))


##2. 
def my_min(x):
  minium = x[0]
  for i in range(len(x)):
    if minium > x[i]:
       minium = x[i]
  return( minium )

print(my_min([-3,-4,-5,11,1,0]))


##3.
## 내가 입력값을 주었을 때의 값

def my_sum(x):
  sum = 0
  for i in range(len(x)): #다섯개를 입력했으니까 길이는 5 (그럼 각각 0,1,2,3,4)
    sum += x[i]           #x[0]은 1 / x[1]
  return(sum)

print(my_sum([1,3,5,7,9]))


##4. 

def my_avg( x ):
  sum = 0
  for i in range(len(x)):
    sum += x[i]
  avg = (sum/len(x))
  return(avg)

print(my_avg([1,2,3]))
