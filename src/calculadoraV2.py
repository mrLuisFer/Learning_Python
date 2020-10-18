# HI! :D
print('Hi, Welcome to this Basic Calculator')

mathsOperations = input('What operations do you want to do? \n Basics? "b" \n Complex? "c": ')
maths = mathsOperations.lower()

if maths == 'basics' or maths == 'b':
  a = input('Insert one number: ')
  try:
    numberA = int(float(a))
  except: 
    print('Please insert a valid number')
    exit()

  b = input('Insert another number: ')
  try:
    numberB = int(float(b))
  except: 
    print('Please insert a valid number')
    exit()

  symbol = input('Please insert a math operation \n or -h (help) for know the commands: ')

  if symbol == 'help' or symbol == '-h':
    print('The commands you can do are: \n Addition: + \n Substraction: - \n Multiplication: * \n Division: / \n To nth power: **')
  elif symbol == '+':
    print(numberA + numberB)
  elif symbol == '-':
    print(numberA - numberB)
  elif symbol == '*' or symbol == 'x':
    if symbol == 'x':
      print('We recommend you use better asterisk: *')
    print(numberA * numberB)
  elif symbol == '/':
    print(numberA / numberB)
  elif symbol == '**':
    print(numberA ** numberB)
  else:
    print('Please insert a valid symbol :)')

elif maths == 'complex' or maths == 'c':
  command = input('Ok, the commands are a bit more specific at this point \n Put "-help" or "-h"to know what to do: ')
  commands = command.lower()

  if commands == '-help' or commands == '-h':
    print('The operations you can do are: \n Perimeter "p" \n Area "a" \n Volume "v" \n Diameter "d" \n Circumference "c" ')
    operation = input('Please insert an operation to do: ')
    lowerOperation = operation.lower()

    if lowerOperation == 'perimeter' or lowerOperation == 'p':
      print('The length and width are required')
      w = input('Please insert the width: ')
      
      l = input('Please insert the length: ')

      try: 
        width = int(float(w))
        length = int(float(l))
        perimeter = (width + width) + (length + length)
        print(perimeter)
      except:
        print('Please insert a valid number')
    
    elif lowerOperation == 'area' or lowerOperation == 'a':
      print('The Length and Width are required')

      ifKnowLength = input('Do you know the Length? \n [Y]es or [N]o: ')
      lowerKnowLength = ifKnowLength.lower()

      if (lowerKnowLength == 'no' or lowerKnowLength == 'n' or lowerKnowLength == '[n]'):
        print('You must do the perimeter and divide it by 2, and substract the width')
        p = input('Please write the perimeter: ')
        w = input('Please insert the width: ')

        try: 
          perimeter = int(float(p))
          width = int(float(w))
          print((perimeter / 2) - width)
        except:
          print('The perimeter and width must be a number')

      elif (lowerKnowLength == 'y' or lowerKnowLength == 'yes' or lowerKnowLength == '[y]'):
        w = input('Please insert the width: ')
        l = input('Please insert the length: ')

        try:
          length = int(float(l))
          width = int(float(w))

          divisionInLength = input('Length has already been subtracted by width? \n [Y]es or [N]o: ')
          lowerDivisionInLength = divisionInLength.lower()

          if (lowerDivisionInLength == 'yes' or lowerDivisionInLength == 'y' or lowerDivisionInLength == '[y]'):
            print(length * width)
          elif (lowerDivisionInLength == 'no' or lowerDivisionInLength == 'n' or lowerDivisionInLength == '[n]'):
            print((length - width) * width)
          else:
            print('Please write [Y] or [N]')
        except:
          print('The length and width must be a number')
      else : 
        print('Please insert [Y] or [N]')
    
    elif lowerOperation == 'volume' or lowerOperation == 'v' or lowerOperation == 'volumen':
      print('The width, length and height are needed')

      w = input('Please insert the width: ')
      l = input('Please insert the length: ')
      h = input('Please insert the height: ')

      try: 
        width = int(float(w))
        length = int(float(l))
        height = int(float(h))

        volume = height * length * width
        print('Volume:', volume)
      except: print('The width, length and height must be number')

    elif lowerOperation == 'diameter' or lowerOperation == 'd':
      print('The radius is required')

      r = input('Please insert the radio: ')

      try:
        radio = int(float(r))

        print('Diameter:', radio * 2)
      except:
        print('The radius must be a number')

    elif lowerOperation == 'circumference' or lowerOperation == 'c' or lowerOperation == 'circunferencia':
      print('Diameter is required')

      d = input('Please insert the diameter: ')

      try:
        diameter = int(float(d))
        pi = 3.1416
        circumference = (diameter * pi)

        print('Circumference', circumference )
      except:
        print('The diameter must be a number')

    else:
      print('Please select a valid operation')
  else: 
    print('Please insert "--help" for know the commands')
else:
  print('Please select one category :)')