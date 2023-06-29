import numpy as np
import Fun_P03 as fp
import time

clientes=[]
vistaLT=np.array([["[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]"]])
infoLT=np.array([[["Lote N° 100","Dimenciones :  500 m²","Precio : $ 1.000.000"],["Lote N° 101","Dimenciones : 1000 m²","Precio : $ 2.000.000"],["Lote N° 102","Dimenciones : 1500 m²","Precio : $ 3.000.000"],["Lote N° 103","Dimenciones : 2000 m²","Precio : $ 4.000.000"]],
                 [["Lote N° 105","Dimenciones : 1000 m²","Precio : $ 1.000.000"],["Lote N° 106","Dimenciones : 2000 m²","Precio : $ 1.500.000"],["Lote N° 107","Dimenciones : 3000 m²","Precio : $ 2.000.000"],["Lote N° 108","Dimenciones : 4000 m²","Precio : $ 2.500.000"]],
                 [["Lote N° 109","Dimenciones :  500 m²","Precio : $ 2.000.000"],["Lote N° 110","Dimenciones : 1000 m²","Precio : $ 4.000.000"],["Lote N° 111","Dimenciones : 1500 m²","Precio : $ 6.000.000"],["Lote N° 112","Dimenciones : 2000 m²","Precio : $ 8.000.000"]]])
while True:
    print("Bienvenido a LoteosDuoc\n")
    print("1.- Ver Lotes Disponibles\n2.- Seleccionar un Lote\n3.- Ver Listado de Clientes\n0.- Salir\n")
    print("Seleccione una Opcion\n")
    opcion=fp.val_op3(0,3)
    if opcion==1:
        fp.mostrar_lote(vistaLT)
        print("¿Desea Seleccionar un Lote?")
        print("1.- SI\n2.- NO")
        opcion=fp.val_op3(1,2)
        if opcion==1:
            clientes.append(fp.selec_lote(vistaLT,infoLT))
            pause=input("\nprecione cualquier tecla para continuar")
            time.sleep(1)
            fp.clear()
    elif opcion==2:
        clientes.append(fp.selec_lote(vistaLT,infoLT))
        pause=input("\nprecione cualquier tecla para continuar")
        time.sleep(1)
        fp.clear()
    elif opcion==3:
        fp.mostrar_clientes(clientes)
        pause=input("\nprecione cualquier tecla para continuar")
        time.sleep(1)
        fp.clear()
    elif opcion==0:
        print("cerrando Aplicacion")
        print("Sistema diseñado por Bastian Aguirre Muñoz")
        time.sleep(1)
        fp.clear()
        break
        
    




        



