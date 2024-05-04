import itertools
grid = [[0, 50, 30, 110],
        [50, 0, 120, 38],
        [30, 120, 0, 75],
        [110, 38, 75, 0]]


def total_distance(path, dist_matrix):

    dist = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        dist += dist_matrix[path[i]][path[i+1]]
    dist += dist_matrix[path[-1]][path[0]]
    return dist


def traveling_salesman(dist_matrix):
    num_cities = len(dist_matrix)

    all_permutations = itertools.permutations(range(num_cities))
    min_distance = float('inf')
    best_path = None
    for permutation in all_permutations:
        d = total_distance(permutation, dist_matrix)

        print(permutation, d)
        if d < min_distance:
            min_distance = d
            best_path = permutation
    return best_path, min_distance


best_path, min_distance = traveling_salesman(grid)
# print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
8
dictionary = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

print("Best path : ")
for i in best_path:
    print(dictionary[i], end=" -> ")
