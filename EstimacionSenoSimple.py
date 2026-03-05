#estimacion de la funcion seno recursivamente

#insertamos un valor x al cual calcularle el seno
x = float(input("x = "))

term = x #definimos el primer término de la sumatoria

sum = x #definimos sumatoria

i = 2 #contador de iternaciones, comenzamos en 2 ya que el primer término ya está

eps = 10**(-8) #Definimos el error máximo que queremos

while (term/sum) >= eps or (term/sum) <= -eps:

  term = -term * x * x/((2 * i - 1) * (2 * i - 2)) #definimos el termino siguiente con base en el anterior
  sum += term #agregamos el término a la sumatoria
  i += 1 #pasamos al siguiente término

print("sin(x) = ", sum)
print("i = ", i)
print("error = ", term/sum)