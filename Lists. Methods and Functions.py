# Metods of lists
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print (letters.index('r'), end='')
print (letters.index('p'), end='')
print (letters.index('p'))
letters.reverse()
print (letters)

l = [1,2,3,4,1,2,3,4]
L = [4,5,6,7,8]
print (l)
print (l.reverse ())  # Arranges the list items in reverse order. No output
l.reverse ()  # реверсирует только что реверсированный список. т.е. приводит его к первоначальному виду
print (l)
l.append(0)  # Adds a element to the end of the list
print (l)
print (l.index(4), '- Index of the first element with a value of - 4')
l.extend(L)  # Расширяет список «l», добавляя в конец все элементы списка «L»
print ('    Expands the «l» list by adding to the end all the elements of the list «L»', '\n', l)
l.insert(2, 100)
print ('Вставка в список "l" элемента "100" с индексом "2"\n', l)

# Functions of lists
print (max(l), '- Maximum value')
print (min(l), '- Minimum value')
