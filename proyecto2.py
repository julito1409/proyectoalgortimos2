def info_api():
      """Conecta con la apli para obtener informacion de la empresa
  returna:
  Diccionario con los datos de cada crucero"""
  
  info="https://saman-caribbean.vercel.app/api/cruise-ships"
  res= requests.get(info)
  return res.json()
def main():
  while True:           #MENU
    opcion=input('''Bienvenido a Samán Caribbean 🛳️      
    1.Ver informacion de los cruceros
    2.Habitaciones
    3.Tours
    4.Restaurants
    5.Estadisticas
    0.Salir
    >''')
    if opcion =='1':        #ejecucion del modulo 1
      data=info_api()
      for i in range(len(data)):
        print (f"Crucero: {data[i]['name']}")
        print (f"Ruta: {data[i]['route']}")
        print (f"Fecha de salida: {data[i]['departure']}")
        print (f"Costo por tipo de habitacion: {data[i]['cost']}")
        print (f"En cada piso hay: {data[i]['rooms']['simple'][0]} pasillos con {data[i]['rooms']['simple'][1]} habitaciones simples, {data[i]['rooms']['premium'][0]} pasillos con {data[i]['rooms']['premium'][1]} habitaciones premium y {data[i]['rooms']['vip'][0]} pasillos con {data[i]['rooms']['vip'][1]} habitaciones vip ")
        print (f"Capacidad por tipo de habitacion: Simple:{data[i]['capacity']['simple']} personas, premmy:{data[i]['capacity']['premium']} personas, VIP:{data[i]['capacity']['vip']} personas")
        print()

    elif opcion=='0':
      print("Adios")
      break  
    else:
      print('Seleccione una opcion Valida')
main()      