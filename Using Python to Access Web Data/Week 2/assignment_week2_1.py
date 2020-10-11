import re

#handler = open('regex_sum_42.txt')
handler = open('regex_sum_967384.txt')
txt = handler.read()

numbersInt = list()
for number in re.findall('[0-9]+' , txt): numbersInt.append(int(number))

print(sum(numbersInt))
