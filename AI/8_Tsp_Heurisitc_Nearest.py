import math
def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def nearest_neighbor(points):
    n = len(points)
    unvisited = set(range(n))
    tour = [0]
    unvisited.remove(0)
    
    while unvisited:
        current_point = tour[-1]
        nearest_point = min(unvisited,key=lambda x:distance(points[current_point],points[x]))
        tour.append(nearest_point)
        unvisited.remove(nearest_point)
        
    tour.append(tour[0])
    return tour

if __name__ == "__main__":
    points = [(0,0), (1,2), (2,3), (3,4), (4,2)]
    tour = nearest_neighbor(points)
    print("Optimal Tour: ", tour)