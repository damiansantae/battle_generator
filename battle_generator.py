import numpy as np
import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='dat14',
                             db='cwb_bd')
cursor = db.cursor()


def get_municipio():
  return np.random.randint(1, high=89)  ##Municipios +1

def battle():
  id_x = get_municipio();
  sql = "SELECT id_propietario from municipios where id_municipio = {0}".format(id_x)
  cursor.execute(sql)

  prop_x=cursor.fetchall()
  if id_x == prop_x :
    create_conquest(prop_x,id_x)
  else:
    create_revellion(prop_x,id_x)


def create_conquest(prop_x,id_x):
  id_y=get_fronteras(prop_x,id_x)
  #TODO: buscar en la bbdd la probabilidad de éxito de municipio x
  prob_x = 0.3+0.3
  #TODO: algoritmo de éxito
  success = 0
  if success:
    sql = "UPDATE municipios SET id_propietario = {0} WHERE id_municipio={1}".format(prop_x, id_y)
    try:
      cursor.execute(sql)
      db.commit()
    except:
      db.rollback()


def create_revellion(prop_x,id_x):
  #TODO: Extraer bd probabilidad de rebelion de X
  prob_x = 0.05
  #TODO: algoritmo de éxito
  succes =0
  if succes:
    pass
  #TODO: cambiar en la bd propietario prop_x = id_x
  else:
    create_conquest(prop_x,id_x)

def get_fronteras(prop_x,id_x):
  sql = "SELECT fronteras from municipios where id_municipio = {0}".format(id_x)
  cursor.execute(sql)
  fronteras = cursor.fetchall()
  array_fronteras = fronteras[0][0].split(',')
  n_random = np.random.randint(len(array_fronteras))
  res = 404
  #bucle hasta encontrar una frontera válida
  i=0
  while i<len(array_fronteras):
    frontera_y = array_fronteras[n_random+i]
    sql = "SELECT id_propietario from municipios where id_municipio = {0}".format(frontera_y)
    cursor.execute(sql)
    prop_y = cursor.fetchall()

    if prop_y != prop_x:
      res = frontera_y
      break
    i+=1
  return res


if __name__ == "__main__":
    battle()