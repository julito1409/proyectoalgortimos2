def modulo_2(self):
        c=Aplication()
        print('\nMódulo 2\n')
        print('1.Visualizar Habitaciones'
                 '\n2.Vender Habitacion'
                 '\n3.Desocupar Habitacion'
                 '\n4.Buscar Habitacion')

        mod2=numero_valido(4) #solictar numero correcto de las opciones

        if mod2==1: 
            print('Visualizar Habitaciones')
            info=''
            while info !='NO':
                opcion=c.barco(data)
                info=c.elegir_habitacion(opcion,data)
                if info=='NO':
                    main()

        elif mod2==2: #condicion para entrar en modulo-2:Vender Habitaciones
            jsonfile='datos.json' # Archivo de almacenamiento de datos
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
            dato_json=abrir_datos(jsonfile)
        
            print('\nVender Habitaciones\n')
            print('Compra de Boletos:\n'
                  '1.Por Destino\n'
                  '2.Por Barco\n'
                  '0. Menú Principal')

            boleto=numero_valido(2)
            if boleto==1:
                destino=c.destino(data)
                print('Destino elegido:', destino)
                barco=c.destino_en_barco(data,destino)
                print('Barcos Disponibles: ', barco)
                print('Seleccione un Barco')
                opcion_barco=c.barco(data)
            elif boleto==2:
                opcion_barco=c.barco(data)
            else:
                main()
                
            barco=data[opcion_barco-1]['name']
            print('Tipo de Habitacion')
            tipo_hab=c.tipo_habitacion()
            print('Numero de Personas')
            num_personas=lee_numero()

            lista_hab=data[opcion_barco-1]['rooms'] #accede a la informacion de habitaciones de un barco desde base de datos principal
            hab=c.id_habitacion(lista_hab, tipo_hab) #se obtiene la identificacion de todas las habitaciones del barco escogido
            capacidad=c.capacidad_habitacion(data, opcion_barco, tipo_hab) #se obtiene la capacidad del tipo de habitacion escogido
            asig_habitaciones=c.selec_habitacion(hab, num_personas, capacidad,dato_json,barco)#se obtiene el numero de habitaciones asignadas al cliente y los id de las habitaciones
            print('capacidad:', capacidad ,'\nnumero:',asig_habitaciones)
            personas=c.formulario(num_personas)
            costo=c.costos(data, opcion_barco, tipo_hab, asig_habitaciones, personas)

            a_bordo=c.cliente_a_bordo()
            registro=c.registro_id(opcion_barco, num_personas, asig_habitaciones)

            datos={'barco':data[opcion_barco-1]['name'],'Tipo Hab':tipo_hab,'Capacidad Hab':capacidad,
                   'Numero de Personas':num_personas,'Habitaciones':asig_habitaciones,
                   'Datos de Pasajeros':personas, 'Costos': costo,
                   'Cliente a Bordo': a_bordo, 'Boleto_id':registro}
            
            print(datos,'\n.................')

            y=agregar_datos(jsonfile, datos)
            guardar_datos(jsonfile, y)
            main()

        elif mod2==3:
            
            jsonfile='datos.json' # Archivo de almacenamiento de datos
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
            dato_json=abrir_datos(jsonfile)

            print('\nMódulo 3\n')
            print('Desocupar Habitación')
            
        
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar_id(dato_json)
                
                print(encontrado)
                registro=encontrado[0]['Boleto_id']
                
                
                print('Desea Desocupar?')
                des=lee_entrada()
                if des=='SI':
                    encontrado[0]['Cliente a Bordo']='NO'
                    dato=c.borrar_registro(registro, jsonfile)
                    dato.append(encontrado[0])
        
                    guardar_datos(jsonfile, dato)
                print(encontrado)
                print('\nDesea Buscar Otro?')
                opcion=lee_entrada()
                if opcion=='NO':
                    main()
        
        elif mod2==4:
            print('\nMódulo 4\n')
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar()
                print(encontrado)
                
                print('\nDesea Buscar Otro?')
                opcion=lee_entrada()
                if opcion=='NO':
                    main()