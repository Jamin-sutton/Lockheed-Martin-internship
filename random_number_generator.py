import time
from random import randint

pi = "1415926535 8979323846 2643383279 5028841971 69399375105820974944 5923078164 0628620899 8628034825 34211706798214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 54930381964428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 02491412737245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 94151160943305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 83011949129833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 76694051320005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 68925892354201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 16096318595024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 76691473035982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989"


pi_list = pi.split()
pi = ''
for i in pi_list:
  pi += i

decimal = lambda n: float('0.' + str(n).split('.')[-1])

def random():
  #uses the seed to pick a random number between 0-9 from pi
  seed = str(decimal(time.time()))
  return pi[int(seed[-3:].strip('.'))]

test = []
for i in range(1000):
  test.append(random())
  #print(test[i])

#tests my random number function for occurance of numbers between 0-9
print("My Random Function")
for i in range(10):
  print('number of ' + str(i) + ': ' + str(test.count(str(i))))
  print('percent: ' + str(round((test.count(str(i))/1000)*100, 3)) + '%')

#tests randint function from teh random library
print("\n\nRandint Function from the Random library")
test = []
for i in range(1000):
  test.append(randint(0, 10))
  #print(test[i])

for i in range(10):
  print('number of ' + str(i) + ': ' + str(test.count(i)))
  print('percent: ' + str(round((test.count(i)/1000)*100, 3)) + '%')
  
# def make_num(max):
#   length = len(str(max))
#   num = ''
#   for i in range(length):
#     num += random()
#   while num[0] == '0':
#     num = num[1:]
#   return num

# def randint(min, max):
#   num = make_num(max)
#   while int(num) > max or int(num) < min:
#     num = make_num(max)

#   return int(num)

# for i in range(100):
#   print(randint(10, 1000))
