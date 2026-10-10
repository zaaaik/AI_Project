# Sistema de recomendación de productos usando KNN
# Importar las librerías necesarias
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Crear un dataset de ejemplo de productos con pandas (sin archivo CSV)
data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'price': [1000, 800, 600, 200, 300],
    'rating': [4.5, 4.7, 4.3, 4.0, 4.2]
}
df = pd.DataFrame(data)

# Dividir los datos en entrenamiento y prueba
train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

# Crear y entrenar un modelo KNeighborsClassifier
model = NearestNeighbors(n_neighbors=2, algorithm='auto')

# Crear y entrenar un modelo KNeighborsClassifier
model.fit(train_data[['price', 'rating']])


# Evaluar el modelo y mostrar la precisión
test_features = test_data[['price', 'rating']]
distances, indices = model.kneighbors(test_features)
print("Distancias:", distances)
print("Índices:", indices)

# Función para recomendar un producto
def recommend_product(product_id):
    # Encontrar el índice del producto en el dataset
    product_index = df[df['product_id'] == product_id].index[0]
    # Obtener las características del producto
    product_features = df.loc[product_index, ['price', 'rating']].values.reshape(1, -1)
    # Encontrar los vecinos más cercanos
    distances, indices = model.kneighbors(product_features)
    # Devolver los IDs de los productos recomendados
    return df.loc[indices[0], 'product_id'].tolist()

