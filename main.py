from prettytable import PrettyTable

table = PrettyTable(['Месяц','Ежемесячный платеж',' Основной долг','Долг по процентам','Остаток основного долга'])
sumCredit  =int(input('Сумма кредита: '))
percentCredit=int(input('Процентная ставка: '))
countMount=int(input('Количество месяцев: '))
percStavka=percentCredit/(100*12)
print(percStavka)
i=0
pe =sumCredit* (percStavka+ percStavka/(((1+percStavka)**countMount)-1))
while(sumCredit>=0):
    Ipe=sumCredit*percStavka
    mainPe=pe-Ipe
    sumCredit-=mainPe
    i+=1
    table.add_row([i,round(pe,2),round(mainPe,2),round(Ipe,2),round(sumCredit,2)])
print(table)
input()
