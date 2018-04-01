inputFileName = input('Enter sales: ')
totalFileName = input('Enter name for sales file')

inputFile = open(inputFileName, 'r')
outputFile = open(totalFileName, 'w')
for sales in inputFile:
    sumTotal = 0.0
    sales = sales.strip()
    sales = sales.split(' ')
    
    for sale in sales:
        sale = sale.replace('$', '')
        salesFloat = float(sale)
        print('$', '{:8.2f}'.format(saleFloat), end= ' ', file=outputFile)
        sumTotal = sumTotal + saleFloat
        
    print('$', '{:8.2f}'.format(sumTotal), sep='', file=outputFile)
    
print('Done writing totals to', totalFileName)

