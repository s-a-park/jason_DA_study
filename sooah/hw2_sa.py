#################################################
# hw2.py
# name: sapark
# andrew id:
#################################################

#import cs112_f21_week2_linter
import math

#################################################
#구글 코랩으로 작성해서 기존 파일로는 테스트 불가 
# 테스트 시 한 문제 기준으로 돌리기
# ''' 또는 """ 로 여러줄 주석처리 가능
#################################################
n=input("n을 입력  * 정수로 입력하기 : ")
n=int(n)

def digitCount(n):
  n=abs(n)       #음수도 받을 수 있게 절댓값 처리
  len = 0        # 자릿수 받을 변수

  if n == 0 :     # 0이 들어오면 자릿수 1 리턴
    return 1
  else :
   while n > 0:
    n //= 10      #n의 자리수 카운팅 후 len에 저장
    len += 1
  return len


"""
def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed!')
"""
#테스트
#digitCount(n)

###########################################
x,y = input("양의 정수 x, y 입력 : ").split(",")
x=eval(x)     # 3**6 같은 수식도 받기 위해서 eval 사용
y=eval(y)

def gcd(x, y):
    while y > 0:
        x, y = y, x % y      # x = y / y = x % y 를 합쳐쓴 것
    return x

"""
def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed!')
"""
#테스트
#gcd(x,y)

#########################################

n=input("정수 n 입력 : ")
n=int(n)

def hasConsecutiveDigits(n):
  n= abs(n)       # 음수 때문에 절댓값 처리
  pre= -1         # 자릿수 숫자 저장하기 위해 변수 만듦
  while ( n > 0 ):
    digit = n % 10
    n //= 10        # 자릿수 숫자 뽑아냄
    if (pre == digit):     # 뽑아낸 자릿수랑 그 전 자리수랑 같은 지 확인
      return True
    pre = digit      # 같지 않다면 뽑아낸 자릿수를 전 자리수 변수에 저장함
  return False

"""
def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed!')
"""
#테스트
#hasConsecutiveDigits(n)
#########################################################

n = input("음이 아닌 정수 입력 : ")
n=int(n)

def isPrime(n):       #소수인지 판별
  if(n <= 1):        # 0 1 은 소수 아니니까 뺌
    return False
  for i in range(2, int(n**0.5)+1):    # 2~ n의 제곱근까지만 확인해봄 -> 소수의 대칭성
    if( n % i == 0 ):
      return False
  return True

def sum_digit(n):   #각 자릿수 더함
  n=abs(n)
  sum = 0
  one = 0
  while ( n > 0 ):
    one = n % 10
    n //= 10
    sum += one
  return sum

def isAdditivePrime(n):    #addictive prime인지 구별
  return (isPrime(n) and isPrime(sum_digit(n)))

def nthAdditivePrime(n):
  P = 0          # n이 되기 전까지의 additive prime 개수 세기 위해 선언
  nprime = 0     # n번째 additive priem 찾기 위해 변수 선언
  while (P <= n ):
    nprime += 1
    if(isAdditivePrime(nprime)):
      P += 1
  return nprime


"""
def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed!')
"""
#테스트
#nthAdditivePrime(n)
###########################################
import statistics
n = input("정수 n 입력 : ")
n = str(n)                # 라이브러리 쓰려면 string이어야 해서 바꿔줌

def mostFrequentDigit(n):
 fre = statistics.mode(n)    # 문자열 중에 빈도 수 높은 것 추출해주는 라이브러리
 return int(fre)

"""
def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed!')
"""
#테스트
#mostFrequentDigit(n)
############################################

x,y = input("x,y 입력 * 쉼표로 나눠서 입력 : ").split(',')
x=int(x)
y=int(y)

def digitCount(n):    # 위에서 썼던 자릿수 세는 함수
  n=abs(n)
  len = 0

  if n == 0 :
    return 1
  else :
   while n > 0:
    n //= 10
    len += 1
  return len


def isRotation(x,y):
   if digitCount(x) != digitCount(y):   # 자릿수 안맞으면 일단 rotation 아니니까 제외
        return False
   for i in range(digitCount(x)):
        Rox = (x % 10) * 10**(digitCount(x) - 1) + x // 10  # x 자리를 바꿔보면서 비교
        if (Rox == y ):
            return True
        x = Rox        # 자릿수 바꾼 숫자를 x에 넣어서 반복하게 만듦
   return False


"""
def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed!')
"""
#테스트
#isRotation(x,y)
#######################################
#f,a,b,N = input("f, a, b, N 을 입력 / f는 함수, a<=b, N은 양의 정수 * 쉼표로 구분").split(',')
#a=float(a)
#b=float(b)
#N=int(N)

def f1(x): return 42
def i1(x): return 42*x
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)


epsilon = 10**-4
def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def integral(f,a,b,N):          # 적분하는 함수 작성함
  sum = 0
  delta = b-a / N            # 구분구적법 (사다리꼴 공식 이용)
  for i in range(a+1,b-1):
    sum += 2 * f(i)              # 맨 첫항 끝항 빼고는 *2되니까 따로 빼고 합함
  sum = sum + f(a) + f(b)       # 빼둔 첫항 끝항 더함
  return delta*0.5*sum

"""                             # 어디가 틀렸는지 False 나오는 애들도 있음

def testIntegral():
    print('Testing integral()...', end='')

    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")
"""
#테스트
#almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),epsilon=epsilon)
#almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),epsilon=epsilon)
#almostEqual(integral(f2, 1, 2, 1), 4,epsilon=epsilon)
#almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),epsilon=epsilon)
#almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),epsilon=epsilon)
#almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),epsilon=epsilon)
################################################

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def f2(x): return x**2 - (x + 1)  # root at x=phi
def f1(x): return x*x - 2 # root at x=sqrt(2)
def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0

def findZeroWithBisection(f,x0,x1,epsilon):     #중간값 정리 함수 만듦
  if f(x0) * f(x1) > 0 :
    return "이 구간에는 근이 없음"       # f(x0) f(x1)가 같은 부호면 근이 없음

  while abs(x1 - x0) > epsilon:
    midx = (x0 + x1) / 2              #x0 - x1 의 거리 차가  오차범위보다 클 때
                                      # 중간 지점 구해줌
    if abs(f(midx)) < epsilon:
        return midx                   # 중간 지점 구했는데 오차범위보다 작으면 리턴

    if f(midx) * f(x0) < 0:          # 중간 지점과 f(x0) 의 부호가 반대면 그 사이에 근이 있다는 소리니까
        x1 = midx                    # 점점 중간 지점 줄여감
    else:
        x0 = midx                    # x1쪽 중간지점 말고 x0쪽 중간지점 줄여봄

  return (x0 + x1) / 2                # 계속 줄여나가다가 오차범위 안에 있는 중간값 리턴


#x = findZeroWithBisection(f1, 0, 2, 0.000000001)
#almostEqual(x, 1.41421356192)

#x = findZeroWithBisection(f2, 0, 2, 0.000000001)
#almostEqual(x, 1.61803398887)

#테스트
#x = findZeroWithBisection(f3, 1, 2, 0.000000001)
#almostEqual(x, 1.17727855081)
#############################################

x, y = input("x, y 입력 * 쉼표로 나눠서 입력  : ").split(',')
x =int(x)
y=int(y)


def carrylessAdd(x,y):
  answer = 0
  digit = 1

  while x > 0 or y > 0:
    digit_sum = (x % 10 + y % 10) % 10    # 각 자리수 별로 계산
    answer += digit_sum * digit     # 그렇게 계산한 값의 일의자리만 저장
    digit *= 10    #일 십 백 ...자릿수별로 계산하기 위해
    x //= 10
    y //= 10

  return answer




"""
def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed!')
"""
#테스트
#carrylessAdd(x,y)
########################################
n = input("n을 입력 : ")      # 리스트 안쓰고는 모르겠음
n = int(n)

def isPrime(n):     # 소수판별 위에서 가져온 함수
  if(n <= 1):
    return False
  for i in range(2, int(n**0.5)+1):
    if( n % i == 0 ):
      return False
  return True

def sum_digit(n):    #이거도 위에 있는 함수 자릿수 다 더함
  n=abs(n)
  sum = 0
  one = 0
  while ( n > 0 ):
    one = n % 10
    n //= 10
    sum += one
  return sum

def PrimeList(n):    # 소수라면 리스트에 저장해두기 위한 함수
    prime = []
    div = 2
    while n > 1:
        if n % div == 0:
            prime.append(div)
            n //= div
        else:
            div += 1
    return prime

def isSmithNumber(n):      # smith number인지 판별하는 함수
  if isPrime(n):
    return False
  prime_sum = sum(sum_digit(prime) for prime in PrimeList(n))
  return sum_digit(n) == prime_sum    # 소수 리스트에 있는 애들 각 자릿수 다 더해서 소수인지 확인

def nthSmithNumber(n):
    smith = []
    num = 4
    while len(smith) <= n:    # 찾은 스미스 수 리스트에 담음
        if isSmithNumber(num):
            smith.append(num)
        num += 1
    return smith[n]    # 그중에 n번째 리턴함




"""
def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed!')
"""
#테스트
#nthSmithNumber(n)
#############################################
import random     # 차례 넘기는거 고쳐야함 / 지금은 차례도 랜덤...

def play(a):    # 게임 기본 룰 함수
 total_score = 0
 print("player %d의 차례입니다 \n" % a)
 while True:
  roll = random.randint(1, 6)
  print("%d 이 나왔습니다 \n" % roll)

  if roll == 1:
   print("1이 나왔습니다. 득점 없이 턴을 종료합니다 \n")
   return 0

  else:
   total_score += roll
   print("이번 턴의 플레이어 %d의 점수는 %d 입니다 \n" % (a,total_score))
   choice = input("계속 진행 또는 멈춤을 고르세요 * 진행 / 멈춤 입력:  ")

   if choice == '멈춤':
    print("턴을 종료합니다 \n")
    return total_score

def pig_game():       # 점수 저장하면서 턴 넘기기 / 점수 100넘으면 게임 종료하는 함수
    player1 = 0
    player2 = 0
    a = random.randint(1,2)
    while (player1 and player2) <= 100:
     print("현재 점수는 player1 : %d / player2 : %d 입니다 \n" % (player1,player2))
     pre_score = play(a)
     if pre_score == 0:
      if a == 1 :
        a = 2
      else :
        a = 1
     else:
      if a == 1 :
       player1 += pre_score
      else :
       player2 += pre_score

     if player1 >= 100:
      print("player1이 이겼습니다 \n")
     elif player2 >=100:
      print("player2가 이겼습니다 \n")
      break

"""
def testPlayPig():
    print('** Note: You need to manually test playPig()')
"""
#테스트
#pig_game()












'''
def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Part A
#################################################

def digitCount(n):
 n=abs(n)
 len = 0
 if n == 0 :
  return 1
 else :
   while n > 0:
    n //= 10
    len += 1
 return len

def gcd(a,b):
    return 42

def hasConsecutiveDigits(n):
    return 42

def nthAdditivePrime(n):
    return 42

def mostFrequentDigit(n):
    return 42

def isRotation(x, y):
    return 42

def integral(f, a, b, N):
    return 42

#################################################
# Part B
#################################################

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def carrylessAdd(x1, x2):
    return 42

def nthSmithNumber(n):
    return 42

#################################################
# Bonus/Optional
#################################################

def bonusPlay112(game):
    return 42

def bonusCarrylessMultiply(x1, x2):
    return 42

############################
# spicy bonus: integerDataStructures
############################

def intCat(n, m): pass
def lengthEncode(value): pass
def lengthDecode(encoding): pass
def lengthDecodeLeftmostValue(encoding): pass
def newIntList(): pass
def intListLen(intList): pass
def intListGet(intList, i): pass
def intListSet(intList, i, value): pass
def intListAppend(intList, value): pass
def intListPop(intList): pass
def newIntSet(): pass
def intSetAdd(intSet, value): pass
def intSetContains(intSet, value): pass
def newIntMap(): pass
def intMapGet(intMap, key): pass
def intMapContains(intMap,key): pass
def intMapSet(intMap, key, value): pass
def newIntFSM(): pass
def isAcceptingState(fsm, state): pass
def addAcceptingState(fsm, state): pass
def setTransition(fsm, fromState, digit, toState): pass
def getTransition(fsm, fromState, digit): pass
def accepts(fsm, inputValue): pass
def states(fsm, inputValue): pass
def encodeString(s): pass
def decodeString(intList): pass

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed!')

def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed!')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed!')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed!')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed!')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed!')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed!')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed!')

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length-encoded 0
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # [1, 42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # [1, 567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # [1, 9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # [1, 9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # [ 0 ]
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # [ 0 ]
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # [ 2, 42, 73 ]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # [ 2, 42, 98765 ]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # [ 4, 42, 98765, 99, 0 ]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # 6* -> 1
    fsm = setTransition(fsm, 1, 7, 2) # 7 -> 2
    fsm = setTransition(fsm, 2, 7, 2) # 7* -> 2
    fsm = setTransition(fsm, 2, 8, 3) # 7* -> 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # [1, 65]
    assert(encodeString('f') == 1111113102) # [1, 102]
    assert(encodeString('3') == 111111251) # [1, 51]
    assert(encodeString('!') == 111111233) # [1, 33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # [4,65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDigitCount()
    testGcd()   
    testHasConsecutiveDigits()   
    testNthAdditivePrime()   
    testMostFrequentDigit()
    testIsRotation()
    testIntegral()

    # Part B:
    testFindZeroWithBisection()
    testCarrylessAdd()
    testNthSmithNumber()
    testPlayPig()

    # Bonus:
    # testBonusPlay112()
    # testBonusCarrylessMultiply()
    # testIntegerDataStructures()

def main():
    cs112_f21_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
'''