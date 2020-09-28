valorPorhora=float(input('Informe o valor da hora trabalhada:'))
QuantidadedeHoras=float(input('Informa a quantidades de horas trabalhadas no mês:'))
salarioBruto=valorPorhora*QuantidadedeHoras
if (salarioBruto>= 2500):
    AliquotaIR=15
elif(salarioBruto>=1903):
    AliquotaIR=7.5
elif (salarioBruto>=900):
    AliquotaIR=0
else:
    AliquotaIR=0
valorIR=salarioBruto*(AliquotaIR/100.0)
valorSindicato=salarioBruto*(3/100.0)
TotalDescontos=valorIR+valorSindicato

ValorFGTS=salarioBruto*(11/100.0)
salarioLiquido=salarioBruto-TotalDescontos

print('Salário Bruto:',valorPorhora*QuantidadedeHoras,':R$',salarioBruto)
print ('(-) IR (',AliquotaIR, '%): R$', valorIR)
print ('(-) Sindicato ( 3 %): R$', valorSindicato)
print ('Total de Descontos: R$', TotalDescontos)
print('Salario Liquido: R$', salarioLiquido)