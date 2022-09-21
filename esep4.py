lost = 0
n = int(input('До какого номера карточки в игре: '))
 
# Сумма всех карточек
for i in range(1, n + 1):
  lost += i
 
for i in range(n - 1):
  lost -= int(input('Введите номер {0} оставшейся карточки: '.format(i + 1)))
 
print('Потеряна карточка с номером:', lost)