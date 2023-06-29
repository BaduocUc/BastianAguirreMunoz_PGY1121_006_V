import os
def clear():
    if os.name=="posix":
        os.system("clear")   
    elif os.name in ["ce","nt","dos"]:
        os.system ("cls")    
     
def val_op(min,max):
    mensaje="Opcion Invalida... Intentelo nuevamente"
    try:
        op=int(input())
        if op<min or op>max:
            print(mensaje)
            return val_op(min,max)
        else:
            return op
    except:
        print(mensaje)
        return val_op(min,max)
    
def val_op2(min,max):
    mensaje="Opcion Invalida... Intentelo nuevamente"
    try:
        op=int(input())
        if op not in range(min,max+1):
            print(mensaje)
            return val_op2(min,max)
        else:
            return op
    except:
        print(mensaje)
        return val_op2(min,max)
    
def val_op3(min,max):
    mensaje="Opcion Invalida... Intentelo nuevamente"
    try:
        op=int(input())
        if op in range(min,max+1):
            return op
        else:
            print(mensaje)
            return val_op3(min,max)           
    except:
        print(mensaje)
        return val_op3(min,max)
    
def mostrar_lote(matriz):
    print("C  0   1   2   3")
    linea="  ━━━╋━━━╋━━━╋━━━"
    for i in range(3):
        if i == 2:
            linea=" "
        print(i,end=" ")
        for j in range(4):
            if j==3:
                print(matriz[i][j])
            else:
                print(matriz[i][j],end="┃")
        print(linea)
        
def val_rut():
    mensaje="RUT invalido... verifique la informacion e intentelo nuevamente..."
    rut=input("RUT:     ejemplo 12345678-k: \n").upper()
    if len(rut) not in [9,10]:
        print(mensaje)
        return val_rut()
    elif rut[-1] not in ["0","1","2","3","4","5","6","7","8","9","K"]:
        print(mensaje)
        return val_rut()
    elif rut[-2]!="-":
        print(mensaje)
        return val_rut()
    for i in range(len(rut)-2):
        try:
            if int(rut[i]) in range(0,10):
                continue
        except:
            print(mensaje)
            return val_rut()
    return rut

def val_correo():
        mensaje="correo invalido... verifique la informacion e intentelo nuevamente..."
        correo=input("Correo:     ejemplo@correo.com  \n")
        if correo[-4:].upper()==".COM" or correo[-3:].upper()==".CL":
            pass
        else:
            print(mensaje)
            return val_correo()
        for i in correo:
            if i =="@":
                return correo
        print(mensaje)
        return val_correo 
        
def selec_lote(disponibilidad,info):
    cliente=[]
    print("por favor ingrese las coordenadas del lote")
    print("ingrese la fila")
    fila=val_op3(0,2)
    print("ingrese la columna")
    columna=val_op3(0,3)
    if disponibilidad[fila][columna]=="[ ]":
        for i in range(3):
            print(info[fila][columna][i])
        print("\nEl lote se encuentra disponible")
        print("¿Desea Adquirirlo?\n")
        print("1.- SI \n2.- NO\n")
        selec=val_op3(1,2)
        if selec==1:
            print("ingrese sus datos")
            aux=val_rut()
            cliente.append(aux)
            aux=input("nombre completo: \n")
            cliente.append(aux)
            print("N° de Telefono/Celular   Ejemplo 912345678")
            aux=val_op3(911111111,999999999)
            cliente.append(aux)
            aux=val_correo()
            cliente.append(aux)
            cliente.append(info[fila][columna])
            disponibilidad[fila][columna]="[X]"
            print("\nSolicitud de Adquisicion ingresada \nnuestros Ejecutivos se pondran en contacto con ud. para finalizar la transaccion")
            return cliente
        else:
            return
    else:
        print("\nLo sentimos este Lote no se encuentra disponible...")
        print("¿desea seleccinar otro?")
        print("1.- SI \n2.-NO\n")
        selec=val_op3(1,2)
        if selec==1:
            return selec_lote()
        return
    
def mostrar_clientes(clientes):
    for i in range(len(clientes)):
        print(f"\nCliente   {i+1}")
        print(f"Rut              : {clientes[i][0]}")
        print(f"Nombre Completo  : {clientes[i][1]}")
        print(f"Telefono/Celular : {clientes[i][2]}")
        print(f"Correo           : {clientes[i][3]}")
        print("Lote Comprado    :")
        for j in range(3):
            print(f"    {clientes[i][4][j]}")
            
        