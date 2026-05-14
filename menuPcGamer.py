print ("----------------------SIMULADOR DE PC GAMER-------------------------")
print ("                                                                    ")
print ("Su presupuesto es: $1.200.000")

opmenu = None
puntos = 0
tiene_pc = False
costo = 0
# Tiene PC NO = 0 , SI = 1
while opmenu != 4:
    try:
        opmenu = int(input("""Elija una de las siguientes opciones:                              
1. Armar y comprar un PC  
2. Test de rendimiento (FPS)
3. Vender/Resetear PC
4. Salir
-> """))
    except ValueError:
        print ("ERROR: Debe ingresar un número")


    #ARMADO DE PC
    if opmenu == 1:
        if tiene_pc == True:
            print ("Ya tiene PC")
        else:
            try:
                cpu = int(input("""Elija uno de los siguientes procesadores:
1: Ryzen 3 3200G (Precio 80.000)
2: Ryzen 5 5600X (Precio: 150.000)
3: Ryzen 7 5700G (Precio 220.000)
4: Ryzen 7 5800X3D (Precio 350000)
5: Ryzen 9 7950X (Precio: 550000)
-> """)) 
#ELECCIÓN CPU
                if cpu != 1 and cpu != 2 and cpu != 3 and cpu != 4 and cpu != 5:
                    print ("No eligió una opción válida y se escogió automaticamente la opción 1")
                    cpu = 1

                if cpu == 1:
                    puntos += 20 ; costo += 80000
                elif cpu == 2:
                    puntos += 45 ; costo += 150000
                elif cpu ==3:
                    puntos += 65 ; costo += 220000
                elif cpu ==4:
                    puntos += 90 ; costo += 350000
                elif cpu ==5:
                    puntos += 130 ; costo += 550000

                gpu = int(input("""Elija una de las siguientes gráficas:
1: GTX 1650 (Precio: 150.000)
2: RTX 3060 (Precio: 280.000)
3: RTX 3070 (Precio: 400.000)                      
4: RTX 4070 (Precio: 600.000)                      
5: RTX 4090 (Precio: 950.000)                                              
-> """))
                
                if gpu != 1 and gpu != 2 and gpu!= 3 and gpu != 4 and gpu != 5:
                    print ("No eligió una opción válida y se escogió automaticamente la opción 1")
                    gpu = 1

                if gpu == 1:
                  puntos += 30 ; costo += 150000
                elif gpu == 2:
                    puntos += 70 ; costo += 280000
                elif gpu ==3:
                    puntos += 100; costo += 400000
                elif gpu ==4:
                    puntos += 130; costo += 600000
                elif gpu ==5:
                    puntos += 200; costo += 950000

                ram = int(input(""" Elija una de las siguientes memorias RAM:
1: 8GB  (Precio: 35.000)                      
2: 16GB (Precio: 65.000)
3: 32GB (Precio: 110.000)                                              
-> """))
                if ram != 1 and ram != 2 and ram != 3 :
                    print ("No eligió una opción válida y se escogió automaticamente la opción 1")
                    ram = 1    
                if ram == 1:
                    multiplicador = 0.7 ; costo += 35000
                elif ram == 2:
                    multiplicador = 1 ; costo += 65000
                elif ram == 3:
                    multiplicador = 1.3 ; costo += 110000
        
                psu = int(input("""Elija una de las siguientes fuentes de poder:
1: 500W Genérica (Precio: 30.000)                      
2: 650W Certificada Bronce (Precio: 65.000)                      
3: 850W Certificada Gold (Precio: 120.000)
-> """))
                if psu != 1 and psu != 2 and psu != 3:
                    print ("No eligió una opción válida y se escogió automaticamente la opción 1")
                    psu = 1

                if psu == 1:
                    costo += 30000
                elif psu == 2:
                    costo += 65000                
                elif psu == 3:
                    costo += 120000 


#Validación de Presupuesto:
                if costo > 1200000:
                    print ("Error: Te pasaste del presupuesto, acumulaste: $", costo)
                    break
#Validación de Fuente de Poder:
                if (gpu == 3 or gpu == 4 or gpu == 5) and psu == 1:
                    print ("ADVERTENCIA !!! EL PC EXPLOTÓ!")
                    break
                elif gpu == 5 and psu == 2 :
                    print ("ADVERTENCIA !!! EL PC EXPLOTÓ!")
                    break
                else:
                    vuelto = 1200000 - costo 
                    tiene_pc = True
                    print ("Compra exitosa, este es su vuelto: $", vuelto)

            except ValueError:
                print ("ERROR: Entrada no válida. Proceso cancelado.")
    
    
    
    if opmenu == 2:
        if tiene_pc == False:
            print ("No tienes un PC que testear !!!")
        elif tiene_pc == True:

            rendimientobase = puntos * multiplicador

            print ("""------Test de Rendimiento (FPS)------
Qué juego desea probar?
1. League of Legends
2. Left 4 Dead 2
3. Minecraft
4. Valorant
5. The Forest
6. Sekiro: Shados Die Twice
7. Resident Evil 4 Remake
8. Cyberpunk 2077
9. ClairObscure: Expedition 33""")

            try :
                opfps = int(input("->"))
            
                if opfps != 1 and opfps != 2 and opfps != 3 and opfps != 4 and opfps != 5 and opfps != 6 and opfps != 7 and opfps != 8 and opfps != 9:
                    print ("No escogió una opción válida y se eligió automaticamente la opción 1")
                    opfps = 1

                
                if opfps == 1:
                    fps = int(rendimientobase * 2.8)
                    print (f"League of Legends te correrá a: {fps} FPS")
                elif opfps == 2:
                    fps = int(rendimientobase * 2.5)
                    print (f"Left 4 Dead2 te correrá a: {fps} FPS")
                elif opfps == 3:
                    fps = int(rendimientobase * 2.0)
                    print (f"Minecraft te correrá a: {fps} FPS")
                elif opfps == 4:
                    fps = int(rendimientobase * 1.8)
                    print (f"Valorant te correrá a: {fps} FPS")
                elif opfps == 5:
                    fps = int(rendimientobase * 1.4)
                    print (f"The Forest te correrá a: {fps} FPS")
                elif opfps == 6:
                    fps = int(rendimientobase * 1)
                    print (f"Sekiro: Shados Die Twice te correrá a: {fps} FPS")
                elif opfps == 7:
                    fps = int(rendimientobase * 0.8)
                    print (f"Resident Evil 4 Remake te correrá a: {fps} FPS")
                elif opfps == 8:
                    fps = int(rendimientobase * 0.6)
                    print (f"Cyberpunk 2077 te correrá a: {fps} FPS")
                elif opfps == 9:
                    fps = int(rendimientobase * 0.3)
                    print (f"ClairObscure: Expedition 33 te correrá a: {fps} FPS")
            except ValueError:
                print ("ERROR: Debe ingresar un número.")
            

    if opmenu == 3:
       costo = 0 ; puntos = 0 ; vuelto = 0 ; tiene_pc = False
       print ("PC Vendido con éxito")
    