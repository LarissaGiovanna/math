def trapezio_simples(comprimentosX, largurasY):
  h = comprimentosX[-1] - comprimentosX[0]
  Area_Trapezio = (h/2) * (largurasY[0] + largurasY[1])
  
  print(Area_Trapezio)
  

def trapezio_composto(comprimentosX, numeroDePontos, largurasY):
  h = (comprimentosX[-1] - comprimentosX[0])/(numeroDePontos-1)
  y_soma = 0
  for i in range(1,(numeroDePontos - 1)):
    y_meios = 2*largurasY[i]
    y_soma += y_meios
  Area_Trapezio = (h/2) * (largurasY[0] + y_soma + largurasY[-1])

  print(Area_Trapezio)
  