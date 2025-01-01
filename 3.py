import random

# Paso 1: Generación de la matriz de tiempos aleatorios
num_empleados = 3
num_tareas = 3
tiempos = [[random.randint(1, 10) for _ in range(num_tareas)] for _ in range(num_empleados)]

# Imprimir la matriz de tiempos
print("Matriz de tiempos:")
for i in range(num_empleados):
    print(f"Empleado {i+1}: {tiempos[i]}")

# Paso 2: Generación de la lista de tareas
tipos_tareas = ["Tarea 1", "Tarea 2", "Tarea 3"]
num_tareas_totales = 20
tareas = [random.choice(tipos_tareas) for _ in range(num_tareas_totales)]

# Imprimir la lista de tareas
print("\nLista de tareas generadas:")
print(tareas)

# Paso 3: Asignación de tareas a los empleados con balance de carga
# Creamos una lista para contar las tareas asignadas a cada empleado
tareas_asignadas = {f"Empleado {i+1}": {tipo: 0 for tipo in tipos_tareas} for i in range(num_empleados)}
carga_total = {f"Empleado {i+1}": 0 for i in range(num_empleados)}

# Asignar tareas a los empleados considerando su carga total
for tarea in tareas:

    tarea_index = tipos_tareas.index(tarea)
    
    empleado_id = min(range(num_empleados), key=lambda i: carga_total[f"Empleado {i+1}"])
    
    tareas_asignadas[f"Empleado {empleado_id+1}"][tarea] += 1
    carga_total[f"Empleado {empleado_id+1}"] += tiempos[empleado_id][tarea_index]

# Imprimir la asignación de tareas
print("\nAsignación de tareas:")
for empleado, tareas in tareas_asignadas.items():
    print(f"{empleado}: {tareas}")
