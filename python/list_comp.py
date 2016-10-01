# http://stackoverflow.com/questions/39783916/what-does-a-number-mean-before-a-for-loop

max_index = 4
adjacency_matrix = []
for j in range(max_index + 1):
    inner_list = []
    for i in range(max_index + 1):
        inner_list.append(0)
    adjacency_matrix.append(inner_list)

print adjacency_matrix



max_index = 4
adjacency_matrix = adjacency_matrix = [[True for i in range(max_index + 1)] for j in range(max_index + 1)]
adjacency_matrix
# [[True, True, True, True, True],
#  [True, True, True, True, True],
#  [True, True, True, True, True],
#  [True, True, True, True, True],
#  [True, True, True, True, True]]
