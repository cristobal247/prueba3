import csv

plansito = []

def menu():
    print(".-.-.-.-.-.-.-.-.-.")
    print(".-.-. M E N U .-.-.")
    print(".-.-.-.-.-.-.-.-.-.")
    print("1.- Agregar Plan")
    print("2.- Listar Planes")
    print("3.- Eliminar Plan por ID")
    print("4.- Generar csv")
    print("5.- Cargar csv")
    print("6.- Estadisticas")
    print("0.- Salir")

def Agregar_Plan():
    Id_numero_plan = int(input("Ingrese el ID de su plan: "))
    nombre = input("Ingrese el nombre de su plan: ")
    porsentaje_efectividad = int(input("Ingrese el porsentaje de efectividad de su plan: "))
    plan = {'ID': Id_numero_plan, 'nombre': nombre, 'porsentaje_efectividad': porsentaje_efectividad}
    print("Su plan fue agregado con exito")
    if porsentaje_efectividad>=0 and porsentaje_efectividad<25:
        porsentaje_efectividad="chiste"
    elif porsentaje_efectividad>=26 and porsentaje_efectividad<50:
        porsentaje_efectividad="anecdota"
    elif porsentaje_efectividad>=51 and porsentaje_efectividad<75:
        porsentaje_efectividad="peligro"
    elif porsentaje_efectividad>=76 and porsentaje_efectividad<99:
        porsentaje_efectividad="atencion"
    elif porsentaje_efectividad>=100:
        porsentaje_efectividad="esclavitud"
    plan=[Id_numero_plan,nombre,porsentaje_efectividad]
    plansito.append(plan)
    
def Listar_Planes():
    for plan in plansito:
        print(f"Id_numero_plan: ",plan[0], "nombre: ",plan[1],"porsentaje_efectividad: ",plan[2])
        
def Eliminar_Plan_por_ID():
    Id_numero_plan = input("Ingrese el ID de su plan a eliminar: ")
    for plan in plansito:
        if plan['ID'] == Id_numero_plan:
            plansito.remove(plan)
            print(f"plan '{plan['nombre']}' el plan fue eliminado con exito.")
    print("Plan no encontrado")
    
def Generar_csv():
    with open("plan.csv","w", newline="")as archivo:
        escribircsv=csv.writer(archivo)
        escribircsv.writerow(["Id_numero_plan","nombre","porsentaje_efectividad"])
        escribircsv.writerows(plansito)
        print("Archivo guardado correctamente.")
        
def Cargar_csv():
    plansito.clear()
    with open("plan.csv","r",newline="")as archivo:
        leercsv=csv.reader(archivo)
        for plan in leercsv:
            plansito.append(plan)
    plansito.pop(0)
    for plan in plansito:
        print("ID: ",plan[0],"nombre: ",plan[1],"porsentaje_efectividad: ",plan[2])

def Estadisticas():
    total=0
    mayor_efectividad=0
    for x in plansito:
        porsentaje_efectividad=int(x[2])
        total=total+porsentaje_efectividad
        if porsentaje_efectividad>mayor_efectividad:
            promedio=total/mayor_efectividad
            print("promedio de su plan: ",promedio)
            print("mayor de porsentaje del plan: ",mayor_efectividad)

while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        print("Agregar Plan")
        Agregar_Plan()
    elif opcion == 2:
        print("Listar Planes")
        Listar_Planes()
    elif opcion == 3:
        print("Eliminar plan por ID")
        Eliminar_Plan_por_ID()
    elif opcion == 4:
        print("Generar csv")
        Generar_csv()
    elif opcion == 5:
        print("Cargar csv")
        Cargar_csv()
    elif opcion == 6:
        print("Estadisticas")
        Estadisticas()
    elif opcion == 0:
        print("ADIOSSSSSSSS")
        break
    else:
        print("Ingrese una opcion valida")
        print("Redirigiendo al menu")