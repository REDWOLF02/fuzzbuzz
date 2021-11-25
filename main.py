number = 0

for number in range(1,101):
  if number % 3==0 and number % 5==0:
    print("fuzzbuzz")
  elif number % 5==0:
    print("buzz")
  elif number% 3==0:
    print("fuzz")
  else:
    print(number)
    