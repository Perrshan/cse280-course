#Prove 1
'''def xor(p, q):
    if p == True and q == True:
        return False
    elif p == True or q == True:
        return True
    else:
        return False

def truth_table_2_vars(function):
    print(f"{function.__name__}")
    print(f"{'p':<8}{'q':<8}{'ANS':<8}")
    print("----------------------------------------")
    rows = [(p,q) for p in (True, False) 
                  for q in (True, False)]    
    for p, q in rows:
        ans = function(p,q)
        print(f"{p!s:<8}{q!s:<8}{ans!s:<8}")
    print()

truth_table_2_vars(xor)
'''

#prove 2
'''
def is_even(x):
    return x % 2 == 0

def is_natural(x):
    return x > 0

def is_palindrome(x):
    return x == x[::-1]

def in_unit_circle(point):
    return (point[0]**2 + point[1]**2) <= 1

def forall(predicate, domain):
    print(f"\u2200x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False
    if(predicate.__name__ == "is_even"):
        for x in domain:
            if(is_even(x) == False):
                return False
    elif(predicate.__name__ == "is_natural"):
        for x in domain:
            if(is_natural(x) == False):
                return False
    elif(predicate.__name__ == "is_palindrome"):
        for x in domain:
            if(is_palindrome(x) == False):
                return False
    elif(predicate.__name__ == "in_unit_circle"):
        for x in domain:
            if(in_unit_circle(x) == False):
                return False
    
    
    return True

def exists(predicate, domain):
    print(f"\u2203x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False
    if(predicate.__name__ == "is_even"):
        for x in domain:
            if(is_even(x) == True):
                return True
    elif(predicate.__name__ == "is_natural"):
        for x in domain:
            if(is_natural(x) == True):
                return True
    elif(predicate.__name__ == "is_palindrome"):
        for x in domain:
            if(is_palindrome(x) == True):
                return True
    elif(predicate.__name__ == "in_unit_circle"):
        for x in domain:
            if(in_unit_circle(x) == True):
                return True
            
    return False

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_even,numbers1)) # False
print(exists(is_even,numbers1)) # True
print("================================")
print(forall(is_natural,numbers1)) # True
print(exists(is_natural,numbers1)) # True
print("================================")

numbers2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_natural,numbers2)) # False
print(exists(is_natural,numbers2)) # True

print("================================")
words1 = ['civic', 'rotor', 'apple']
print(forall(is_palindrome,words1)) # False
print(exists(is_palindrome,words1)) # True
print("================================")

words2 = ['racecar', 'madam', '123454321']
print(forall(is_palindrome,words2)) # True
print(exists(is_palindrome,words2)) # True
print("================================")

words3 = ['no', 'palindromes', 'here']
print(forall(is_palindrome,words3)) # False
print(exists(is_palindrome,words3)) # False
print("================================")

points1 = [(0.5,0.5), (-1,0), (-0.75,-0.3)]
print(forall(in_unit_circle,points1)) # True
print(exists(in_unit_circle,points1)) # True
print("================================")

points2 = [(0.25,-1), (0.9,1.1), (0.1,-0.1)]
print(forall(in_unit_circle,points2)) # False
print(exists(in_unit_circle,points2)) # True
'''

#Prove 3
'''
Set1 = {1/(2**n) for n in range(1,5)} 
Set2 = {n**2 for n in range(-2,3)} 
Set3 = {n for n in range(1,13) if 24 % n == 0} 
Set4 = {n for n in range (-10,11) if n % 2 != 0} 

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)
'''

#Prove 4
'''
f1 = lambda x: x**3 + x**2 + x + 1
f2 = lambda x: 3*x + 5
f3 = lambda x: (x*(x+1))/2

domain = range(-5,6)
f1_points = {(x,f1(x)) for x in domain}
f2_points = {(x,f2(x)) for x in domain}
f3_points = {(x,f3(x)) for x in domain}

# Expected results below may be sorted differently
print(f1_points)
# {(3, 40), (-1, 0), (4, 85), (2, 15), (5, 156), (-2, -5), (-5, -104), (1, 4), (-4, -51), (-3, -20), (0, 1)}
print(f2_points)
# {(-5, -10), (-1, 2), (5, 20), (3, 14), (1, 8), (2, 11), (-3, -4), (0, 5), (4, 17), (-2, -1), (-4, -7)}
print(f3_points)
# {(0, 0.0), (-1, 0.0), (-3, 3.0), (1, 1.0), (3, 6.0), (4, 10.0), (2, 3.0), (-4, 6.0), (5, 15.0), (-2, 1.0), (-5, 10.0)}
'''
'''
#Prove 6

adjacency_table = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E']
}

def find_neighbors(vertex, adjacency_table):
    
    return adjacency_table[vertex]

def is_neighbor(vertex1, vertex2, adjacency_table):
    
    return vertex2 in adjacency_table[vertex1]

print(find_neighbors('A', adjacency_table)) # should print ['B', 'C']
print(find_neighbors('D', adjacency_table)) # should print ['C', 'E', 'F']

print(is_neighbor('A','B',adjacency_table)) # True
print(is_neighbor('D','F',adjacency_table)) # True
print(is_neighbor('C','F',adjacency_table)) # False
'''

'''
m = '100'
i = '11'
s = '0'
p = '101'
word = 'mississippi'
result = ''

for letter in word:
    if letter == 'm':
        result += m
    elif letter == 'i':
        result += i
    elif letter == 's':
        result += s
    elif letter == 'p':
        result += p

print(result)
print(len(result))
'''
'''
def fun1(n):
    if n == 0:
        return 5
    return fun1(n-1) + 3*n

def fun2(n):
    if n == 0:
        return 1
    return n**3 + fun2(n-1)

def fun3(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    return fun3(n-1)*fun3(n-2)

def fun4(n):
    if n == 0:
        return 1
    elif n == 1:
        return 5
    return fun4(n-1) + fun4(n-2)**2

print([fun1(n) for n in range(10)]) # [5, 8, 14, 23, 35, 50, 68, 89, 113, 140]
print([fun2(n) for n in range(10)]) # [1, 2, 10, 37, 101, 226, 442, 785, 1297, 2026]
print([fun3(n) for n in range(10)]) # [1, 3, 3, 9, 27, 243, 6561, 1594323, 10460353203, 16677181699666569]
print([fun4(n) for n in range(10)]) # [1, 5, 6, 31, 67, 1028, 5517, 1062301, 31499590, 1128514914191]
'''

'''
seq1 = [k**3 for k in range(54)]

seq2 = [(2**k -2) for k in range(28)]

seq3 = [(k**5 + 1) for k in range(-3, 19)]

seq4 = [2**k for k in range(-2, 8)]


print(sum(seq1)) # 2047761
print(sum(seq2)) # 268435392
print(sum(seq3)) # 6656947
print(sum(seq4)) # 255.75
'''
'''
def gcd(x,y):
    for n in range(min(x,y),1,-1):
        if x % n == 0 and y % n == 0:
            return n
    return 1

def lcm(x, y):
    return (x*y)//gcd(x,y)


print(gcd(12,15)) # 3
print(gcd(12,24)) # 12
print(gcd(12,18)) # 6 
print(gcd(7,13))  # 1
print(gcd(1,2))   # 1
print(gcd(5,5))   # 5
print("===================")
print(lcm(12,15)) # 60
print(lcm(12,24)) # 24
print(lcm(12,18)) # 36 
print(lcm(7,13))  # 91
print(lcm(1,2))   # 2
print(lcm(5,5))   # 5
'''

'''
# def gcd_ext(x,y):

#     (old_r, r) = (x, y)
#     (old_s, s) = (1, 0)
#     (old_t, t) = (0, 1)
#     while r != 0:
#         q = old_r // r
#         (old_r, r) = (r, old_r - q * r)
#         (old_s, s) = (s, old_s - q * s)
#         (old_t, t) = (t, old_t - q * t)
#     return (old_r, old_s, old_t)

# def gcd(x,y):
#     for n in range(min(x,y),1,-1):
#         if x % n == 0 and y % n == 0:
#             return n
#     return 1

# phi = (137-1)*(211-1)
# e = 11
# d = 0
# ans = 0

# while ans != 1:
#     e += 1
#     ans = gcd(e, phi)
#     if ans == 1:
#         print(ans)
#         print(e)

# print(gcd_ext(e, phi))

# print(2197*e % phi)
# print(gcd_ext())

# print(-7789*11 + 3*phi)

# print(137*211)

# Put your values from Part 1
p = 137
q = 211
e = 13
N = 28907
phi = 28560
d = 2197

m = 5645
# Write code to encrypt 'm' and display it
encoded_m = (m**e) % N
print(encoded_m)

# Write code to decrypt it back again and display it.   It should be 5645 again.
decoded_m = (encoded_m**d) % N
print(decoded_m)
'''

from math import factorial
# factorial(6) = 6! = 720

def P(n,r):
    return factorial(n) // factorial(n-r)

def C(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(C(8,5))
