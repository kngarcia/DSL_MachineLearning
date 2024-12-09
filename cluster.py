import matplotlib.pyplot as plt
import random
import math

class KMeans:
    def __init__(self, k, max_iterations=100, tolerance=1e-4):
        self.k = k
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.centroids = []

    def fit(self, data):
        # Inicializar los centroides utilizando K-means++
        self.centroids = self.initialize_centroids(data)
        
        for _ in range(self.max_iterations):
            # Asignar cada punto al centroide más cercano
            clusters = self.create_clusters(data)
            
            # Guardar los centroides actuales para verificar la convergencia
            old_centroids = self.centroids
            
            # Calcular nuevos centroides
            self.centroids = self.calculate_centroids(clusters)
            
            # Verificar convergencia (si los centroides no cambian)
            if self.has_converged(old_centroids, self.centroids):
                break

    def initialize_centroids(self, data):
        """Inicializa los centroides utilizando el método K-means++."""
        centroids = [random.choice(data)]
        while len(centroids) < self.k:
            distances = [min(self.euclidean_distance(point, centroid) for centroid in centroids) for point in data]
            probabilities = [d / sum(distances) for d in distances]
            cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
            r = random.random()
            for i, cumulative_probability in enumerate(cumulative_probabilities):
                if r < cumulative_probability:
                    centroids.append(data[i])
                    break
        return centroids

    def create_clusters(self, data):
        clusters = [[] for _ in range(self.k)]
        for point in data:
            closest_centroid_index = self.closest_centroid(point)
            clusters[closest_centroid_index].append(point)
        return clusters

    def closest_centroid(self, point):
        distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
        return distances.index(min(distances))

    def calculate_centroids(self, clusters):
        centroids = []
        for cluster in clusters:
            if cluster:  # Asegurarse de que el cluster no esté vacío
                centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
            else:
                centroid = random.choice(self.centroids)  # Reasignar un centroide aleatorio si el cluster está vacío
            centroids.append(centroid)
        return centroids

    def has_converged(self, old_centroids, new_centroids):
        total_movement = sum(self.euclidean_distance(old, new) for old, new in zip(old_centroids, new_centroids))
        return total_movement < self.tolerance

    def euclidean_distance(self, point1, point2):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

    def predict(self, data):
        predictions = []
        for point in data:
            closest_centroid_index = self.closest_centroid(point)
            predictions.append(closest_centroid_index)
        return predictions

    def plot_clusters(self, data):
        """Genera un gráfico de los clústeres y sus centroides."""
        clusters = self.create_clusters(data)

        plt.figure(figsize=(8, 6))
        colors = plt.cm.tab10.colors  # Paleta de colores

        # Graficar los puntos de cada clúster
        for cluster_idx, cluster in enumerate(clusters):
            if cluster:  # Verificar que el clúster no esté vacío
                cluster_points = list(zip(*cluster))
                plt.scatter(cluster_points[0], cluster_points[1], 
                            s=50, color=colors[cluster_idx % len(colors)], label=f'Cluster {cluster_idx}')
        
        # Graficar los centroides
        centroids = list(zip(*self.centroids))
        plt.scatter(centroids[0], centroids[1], 
                    s=200, color='black', marker='X', label='Centroids')

        # Personalizar el gráfico
        plt.title("Clusters Visualized with Centroids")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.grid(True)
        plt.show()
