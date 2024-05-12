import math

def euclideanDistance(p1, p2):

    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance:.2f}")
