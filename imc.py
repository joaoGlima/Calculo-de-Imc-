nome = input ("qual o seu nome ? ")
altura = input ("qual a sua altura: ")
idade = input ("qual a sua idade: ")
peso = input ( " qual o seu peso: ")

print ( "seu nome é", nome)
print ("sua altura é", altura)
print ("sua idade é", idade)
print ( " seu peso é", peso)

peso1_calculo = float(peso)
calculoimc = float(altura)
imc = peso1_calculo / calculoimc **2

print (f'seu imc é {imc:.2f}')

