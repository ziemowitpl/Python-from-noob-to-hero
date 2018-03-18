moja_lista = [1,2,3]
print(moja_lista)

my_list = ["String", 2, 3]
print(my_list)

mylist = ['one','two','three']
print(mylist[0])
print(mylist[1])

another_list = ['four', 'five']

print(mylist + another_list)

new_list = mylist + another_list
print(new_list)

print(new_list[:2])
print(new_list[::])
print(new_list[::-1])
print(new_list[::2])

new_list[0] = 'zastepczy element'
print(new_list)

new_list.append('six')
print(new_list)

new_list.pop(0)
print(new_list)

new_list.pop()
print(new_list)

popped_item = new_list.pop(2)
print(popped_item)

lista_liter = ['c', 'a', 'd', 'b']
lista_liter.sort()
print(lista_liter)

# tak nie dziala
nowa_lista = ['c', 'a', 'd', 'b', 'y', 'f', 'z', 'g', 'x']
mySortedList = nowa_lista.sort()
print(mySortedList)
# dziala za to TAK:
najnowsza = ['c', 'a', 'd', 'b', 'y', 'f', 'z', 'g', 'x']
najnowsza.sort()
posortowana = najnowsza
print(posortowana)

lista_numerow = [5, 3, 1, 2, 4]
lista_numerow.sort()
print(lista_numerow)

lista_num = [1, 2, 3, 4, 5]
lista_num.reverse()
print(lista_num)