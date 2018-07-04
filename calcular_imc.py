
def calcula_imc (valor):
    if valor < 17.0:
        print('{:.2f} Muito abaixo do peso'.format(valor))
    if valor > 17.0 and valor < 18.49:
        print('{:.2f} Abaixo do peso'.format(valor))
    if valor > 18.5 and valor < 24.99:
        print('{:.2f} Peso normal'.format(valor))
    if valor > 25.0 and valor < 29.99:
        print('{:.2f} Acima do peso'.format(valor))
    if valor > 30.0 and valor < 34.99:
        print('{:.2f} Obesidade I'.format(valor))
    if valor > 35.0 and valor < 39.99:
        print('{:.2f} Obesidade II'.format(valor))
    if valor > 40.0:
        print('{:.2f} Obesidade III'.format(valor))


alt = (float(input('Digite sua altura:')))
pso = (float(input('Digite seu peso:')))
z = pso/(alt*alt)
calcula_imc(z)


