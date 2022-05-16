preço = float(input('Qual é o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava {:.2f}R$ com o desconto de 5% fica {:.2f}R$'.format(preço,novo))