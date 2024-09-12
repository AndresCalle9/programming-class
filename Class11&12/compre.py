# LISTAS
#  Primeros mil numeros naturales

opt_1 = range(1,1001)
print(opt_1)
for i in opt_1:
    print(i)

opt_2 = []
for i in opt_1:
    if i % 2 == 0 and i % 3 == 0:
        opt_2.append(i)

print(opt_2)

#Comprenhension

opt_3 = [i for i in range(1,1001) if i%2 == 0 and i%3 == 0]
print(opt_2 == opt_3)

# Challenge
# Create with a list comprehension, a list of all the multiples of 4 that at the same time are multiples of 6 and 9 up to 5 digits. That is, from 1 to 99,999
res = [i for i in range(1,100000)if i % 4 == 0 and i% 6 == 0 and i%9 == 0 and i >= 10000]
print(res)

# DICT

opt_4 = {i:i**0.5 for i in range(1,1001)}
print(opt_4)


opt_5 = {i:i**0.5 for i in range(1,1001) if i%25 == 0}
print(opt_5)

print(len(opt_4.keys()), len(opt_5.keys()))