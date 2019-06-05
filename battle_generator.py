import numpy as np

def get_municipio():
   return np.random.randint(68)

def battle():
  id_x = get_municipio();
#TODO: Extraer en la BBDD propietario del municipio con este id
  prop_x = 1
  if id_x == prop_x :
    create_conquest(prop_x)
  else:
    create_revellion()


def create_conquest(prop_x,id_x):
  prop_y=get_frontera(prop_x,id_x)
  #TODO: buscar en la bbdd la probabilidad de éxito de municipio x
  prob_x = 0.1
  #TODO: buscar en la bbdd la probabilidad de éxito de municipio Y
  prob_y = 0.2


  return 0

def create_revellion():
  return 0

def get_frontera(prop_x,id_x):
  #TODO: buscar en la base de datos las fronteras de id_x
  fronteras = "3,4,5"
  array_fronteras = fronteras.split(',')
  n_random = np.random.randint(len(array_fronteras))
  res = 404
  #bucle hasta encontrar una frontera válida
  i=0
  while i<len(array_fronteras):
    frontera_y = array_fronteras[n_random+i]
    #TODO: buscar en la BD el propietario de Y
    prop_y =4
    if prop_y != prop_x:
      res = prop_y
      break
    i+=1
  return res