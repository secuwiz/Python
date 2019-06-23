#!/usr/bin/python3

# References inside functions are local...
snoggle = 17
def wongle(n):
    snoggle = n

print('A:', snoggle,end=' ')
wongle(235)
print(snoggle)

# ...unless declared global.
def wangle(n):
    global snoggle
    snoggle = n

print('B:', snoggle,end=' ')
wangle(235)
print(snoggle)

# Arguments are pass-by-value...
def snapple(n):
    n = 55

print('C:', snoggle,end=' ')
wangle(snoggle)
print(snoggle)

# ...except for the contents objects, such as lists...
def snarffle(z):
    z.append(22)

toggle = [ 'a', 'b', 'c' ];
print('D:', toggle,end=' ')
snarffle(toggle)
print(toggle)

# ...which means the contents of the object, not the parameter.
def snarggle(z):
    z = [ 4, 5 ]

print('F:', toggle,end=' ')
snarggle(toggle)
print(toggle)
