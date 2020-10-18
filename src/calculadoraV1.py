
print("\x1b[1;33m"+'Hola bienvenido a esta calculadora basica')

numero1 = input("\033[;36m"+'Por favor ingresa un numero: ')

try:
  intNumero1 = int(float(numero1))
except:
  print("\033[4;35m"+'Por favor coloca un numero valido')
  exit()

numero2 = input("\033[;36m"+'Por favor ingresa un segundo numero: ')

try:
  intNumero2 = int(float(numero2))
except:
  print("\033[4;35m"+'Por favor coloca un numero valido')
  exit() 

symbol = input('Por favor ingresa la operacion que quieres hacer: ')

if symbol == 'help':
  print('Los comandos que puedes hacer son esos: ')
  print('Suma: + \ Resta: - \ Multiplicacion: * \ Division: /')
elif symbol == '+':
  print('Suma:', intNumero1 + intNumero2)
elif symbol == '-':
  print('Resta:', intNumero1 - intNumero2 )
elif symbol =='*':
  print('Multiplicacion:', intNumero1 * intNumero2)
elif symbol == '/':
  print('Division:', intNumero1 / intNumero2)
else:
  print("\033[4;35m"+'Por favor ingresa un numero valido')
  print('Trata de colocar help si tienes duda')
