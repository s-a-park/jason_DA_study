#################################################
# hw1.py
# name: 김창현
# andrew id:
#################################################

import cs112_f21_week1_linter
import math

#################################################
# Helper functions
#################################################

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

def distance(x1, y1, x2, y2): ## 두 점 사이에 거리 공식 이용 
    x = pow(x2 -x1,2) ## ( x2 - x1 )^2
    y = pow(y2 - y1,2) ## ( y2 - y1 )^2
    
    return math.sqrt(x + y) ## 루트

# def circlesIntersect(x1, y1, r1, x2, y2, r2):
        ## 각 원의 중심 사이의 거리를 구한 후 
        ## 두 원의 반지름보다 길면 교차가 되지 않고, 같거나 작으면 교차됨
    # x = pow(x2 -x1,2) 
    # y = pow(y2 - y1,2) 
    # r = pow(r1 + r2,2)
    # return (x+y <= r)
    
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return distance(x1, y1, x2, y2) <= (r1+r2)
    

# def getInRange(x, bound1, bound2):
#     ## 두 수 사이에 x값이 존재 하는 경우
#     if ((x>=bound1) and (x <= bound2)) or ((x >=bound2) and (x <= bound1)):
#         return x
#     ## bound1이 bound2보다 클 경우
#     elif bound1 > bound2:
#         return (x > bound1)*bound1 + (x < bound2)*bound2

#     ## bound2가 bound1보다 클 경우     
#     else:
#         return (x > bound2)*bound2 + (x < bound1)*bound1

def getInRange(x, bound1, bound2):
    a = min(bound1, bound2)
    b = max(bound1, bound2)
    if a > x :
        return a
    elif b < x :
        return b
    else:
        return x

def eggCartons(eggs):
    ## egg 가 12의 배수이면 + 0, 12의 배수가 아니면 +1
    return  eggs // 12 + (eggs%12 > 0)

def pascalsTriangleValue(row, col): 
    ## 파스칼 삼각형 공식 이용 
    if (row < col) or (row < 0) or (col < 0):
        return None
    else:
        n = math.factorial(row)
        r = math.factorial(col)
        return n //(r * math.factorial(row-col)) 

def getKthDigit(n, k):
    return abs(n) // (10**k) % 10



def setKthDigit(n, k, d):
    source = abs(n) // (10**k) % 10 * pow(10,k) ## n의 k번째 자릿수
    kd = d * pow(10,k) ## 변경할 값을 k번째 자리수로 만듦
        
    if n < 0: ## n이 음수일 경우
        return n + source - kd
         
    else:    ## n이 양수일 경우
        return n-source + kd

#################################################
# Part B
#################################################





def nearestOdd(n):
    num = roundHalfUp(n)
    
    
    ## n이 짝수인 경우
    if num % 2 ==0:
        ## n이 내림이 된 경우
        if num >= n: 
            return int(num -1)
        ## n이 올림이 된 경우
        else:
            return int(num + 1)
    
    ## n이 홀수인 경우
    else:
        return int(num)

def numberOfPoolBalls(rows): ## 1 ~ n 사이의 수 합계공식 이용
    return (rows*(rows+1) // 2)

def numberOfPoolBallRows(balls):
    n = int(math.sqrt(2*balls))
    if (n*(n+1) // 2) >= balls:
        return n
    else:
        return n+1


def colorBlender(rgb1, rgb2, midpoints, n):
    if n > midpoints+1 or n < 0:
        return None
    x1 = rgb1 // 1000000
    y1 = (rgb1 - (x1*1000000)) // 1000
    z1 = rgb1 % 1000
    x2 = rgb2 // 1000000
    y2 = (rgb2 - (x2*1000000)) // 1000
    z2 = rgb2 % 1000
    
    
    mid = midpoints + 1
    x= roundHalfUp(x1 + (x2-x1)*(n/mid))*1000000
    y= roundHalfUp(y1 + (y2-y1)*(n/mid))*1000
    z= roundHalfUp(z1 + (z2-z1)*(n/mid))
    return x + y + z 

#################################################
# Bonus/Optional
#################################################

def bonusPlayThreeDiceYahtzee(dice):
    return 42

def handToDice(num):
    x = num // 100
    y = num // 10 - x * 10
    z = num % 10 
    return ( x, y, z )

def diceToOrderedHand(a, b, c):
    if max(a,b,c)==a:
        if min(b,c) == b:
            return int(str(a)+str(c)+str(b))    
        else:
            return int(str(a)+str(b)+str(c))

    elif max(a,b,c)==b:
        if min(a,c) == a:
            return int(str(b)+str(c)+str(a))    
        else:
            return int(str(b)+str(a)+str(c))
    else:
        if min(a,b) == a:
            return int(str(c)+str(b)+str(a))
        else:
            return int(str(c)+str(a)+str(b))

def playStep2(hand, dice):
    return 0

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # # comment out the tests you do not wish to run!
    # # Part A:
    # testDistance()
    # testCirclesIntersect()
    # testGetInRange()
    # testEggCartons()
    # testPascalsTriangleValue()
    # testGetKthDigit()
    # testSetKthDigit()
    # # Part B:
    print("#################################################")
    print("# Part B")
    print("#################################################")
    # testNearestOdd()
    # testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    # testColorBlender()
    # Bonus:
    #testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_f21_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
