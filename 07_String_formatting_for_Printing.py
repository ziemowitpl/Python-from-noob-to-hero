print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# musza byc wszystkie numerowane lub wszystkie wolne
#print('The {2} {} {0}'.format('fox','brown','quick'))

print('The {2} {2} {2}'.format('fox', 'brown', 'quick'))

result = 100/777
print(result)

print("The result was {}".format(result))

print("The result was {rz}".format(rz=result))

print("The result was {r:30.2f}".format(r=result))

name = 'Ziemo'
print(f'Hello, his name is {name}')
age = 39
print(f'Hello, his name is {name} and is {age} years old')
# KLAMRY a nie nawiasy okragle !!!
