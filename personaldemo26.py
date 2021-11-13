file=open("26.txt")
a=file.readline()
data=[] #массив с данными
people=0 #счетчик людей
max1=0 #последнее значение которое запишется в памяти, до проверки
Finalmax=0 # максимальное значение(ответ)
peopleG=int(a.split()[1]) # общее кол.во людей
memory=int(a.split()[0]) # всего памяти
for i in range(peopleG):
    data.append(int(file.readline())) #заполняем массив
    data.sort()
i=0
while memory-data[i]>=0:
    memory-=data[i]
    i+=1                 #считаем сколько человек помещаветя в памяти+сколько свободной памяти останется
    people+=1
    max1=data[i]
for i in range(people,peopleG):
    if memory+max1>=data[i]:
        Finalmax=data[i]
        #если оставшаяся память + последний элемент больше или равны следующего
        #   элемента, значит он умещается и поэтому меняем последний элемент на следующий
print(Finalmax,people)
