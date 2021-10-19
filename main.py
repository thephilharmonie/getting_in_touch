#!/usr/bin/python

dist= 12

led = 0

for i in range(dist):
    led  = led + (pow(10, i))
    print(i)

zeros = pow(10, (16-dist))

end_value = led*zeros

print(end_value)



ledd = str(led)

print(ledd)
print(type(ledd))

