#ДЗ 7.4. Пошук спільних елементів
# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
# def common_elements():
# 		pass
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

def common_elements():
   import random #підключаємо бібліотеку
   numbers=[] #порожній список
   numbers1=[] #порожній список
   while len(numbers)<=100:
       elem=random.randint(0,100)
       if elem%5==0:
           numbers.append(elem) #наповнюємо список рандомними значеннями
       else:
           continue
   print("кратні 5")
   print(numbers) #кратні 5
   set1=set(numbers)
   while len(numbers1)<=100:
       elem1=random.randint(0,100)
       if elem1%3==0:
           numbers1.append(elem1) #наповнюємо список рандомними значеннями
       else:
           continue
   print("кратні 3")
   print(numbers1) #кратні 3
   set2=set(numbers1)
   intersection_set = set1.intersection(set2)
   print("множина перетину")
   print(intersection_set)
   return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ок")