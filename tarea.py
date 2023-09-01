import pandas as pd
import matplotlib.pyplot as plt
lista = pd.read_csv('archivo_1.csv')

#promedio de edades por ciudad

promedio_edades_ciudad = lista.groupby('ciudad')['edad'].mean()
print('promedio edades por ciudad')
print(promedio_edades_ciudad)
print()

#ciudades con ingresos promedio superiores a 3000
mayores_3000 = lista[lista['ingresos'] > 3000]
promedio_mayores_3000 = mayores_3000.groupby('ciudad')['ingresos'].mean()
print('Ciudades con ingresos a 3000 promedio')
print(promedio_mayores_3000)
print()

#agregar columna de impuestos del 11%

def calcular_impuestos(ingresos):
    # Define la tasa de impuestos
    tasa_impuestos = 0.11
    
    # Calcula los impuestos como un porcentaje de los ingresos
    impuestos = ingresos * tasa_impuestos
    return impuestos

# Agrega una columna de impuestos al DataFrame
lista['impuestos'] = lista['ingresos'].apply(calcular_impuestos)

#ordenar por ingresos de forma decendente

ingresos_ordenados = lista.sort_values(by='ingresos', ascending=False)
print('forma decendente')
print(ingresos_ordenados)

#grafico pastel por numero de trabajadores por ciudad

trabajadores_por_ciudad = lista['ciudad'].value_counts()

plt.figure(figsize=(8, 6))  
plt.pie(trabajadores_por_ciudad, labels=trabajadores_por_ciudad.index, autopct='%1.0f', startangle=140)
plt.axis('equal') 

plt.title('Distribución de Trabajadores por Ciudad')
plt.show()

# Crea un histograma de las edades
plt.hist(lista['edad'], bins=10, edgecolor='black')

plt.xlabel('Edad')
plt.ylabel('Cantidad de Personas')
plt.title('Distribución de Edades')

plt.show()

