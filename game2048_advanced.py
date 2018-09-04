import random
def shifter(list_input, directions):
    """
    This function takes a list 1-d and shifts the element according to the second parameters
    passed to it
    Args:
    Input: a vector and a dimension in which we need to shift all the element
    Output: a vector
    """
    # there are only four possibilities,
    # it depends on whether we have recieved a column vector or row vector
    # 'w' - shift upward
    # 'a' - shift left
    # 's' - shift downward
    # 'd' - shift right
    rows = len(list_input)
    modified_list = []
    # -------------------------------------------------------------------------
    # case - 1, when direction is either 'a' or 'd'
    if directions == 'a':
        # shift left
        total_zeros = list_input.count(0)
        modified_list = [i for i in list_input if i != 0]
        # append the 0 to the right
        count = 0
        while count != total_zeros:
            modified_list.append(0)
            count += 1
        return modified_list

    elif directions == 'd':
        # shift right
        total_zeros = list_input.count(0)
        modified_list = [i for i in list_input if i != 0]
        # append the zeros to the left
        count = 0
        while (count != total_zeros):
            modified_list = [0] + modified_list
            count += 1
        return modified_list

    # -------------------------------------------------------------------------
    # case - 2, when direction is either 'w' or 's'
    # in this we expect a column vector

    elif directions == 'w':
        modified_list = [[0 for i in range(1)] for j in range(rows)]
        # shift upward
        i_index = 0
        for i in range(rows):
            if list_input[i][0] != 0:
                modified_list[i_index][0] = list_input[i][0]
                i_index += 1
        # add the zeros to the end
        for i in range(i_index, rows):
            modified_list[i][0] = 0
        return modified_list

    elif directions == 's':
        modified_list = [[0 for i in range(1)] for j in range(rows)]
        # shifts downward
        i_index = rows - 1
        for i in range(rows):
            if list_input[rows - i - 1][0] != 0:
                modified_list[i_index][0] = list_input[rows - i - 1][0]
                i_index -= 1
        # add zeros to the beginning
        for i in range(0, i_index):
            modified_list[i_index][0] = 0
        return modified_list


def put_together(list_input_2d, directions):
    """
    This function takes a 2d matrix and directions, based on which it returns a 2d matrix
    having appropriate changes
    Args:
    Input: 2d Matrix and direction
    Output: 2d Matrix
    """
    if directions == 'a':
        # shift all the elements of matrix to the left
        for i in range(len(list_input_2d)):
            list_input_2d[i][:] = shifter(list_input_2d[i][:], directions)

    elif directions == 'd':
        # shift all the elements of matrix to the right
        for i in range(len(list_input_2d)):
            list_input_2d[i][:] = shifter(list_input_2d[i][:], directions)

    elif directions == 'w':
        # shift all the elements of matrix to the top
        for i in range(len(list_input_2d[:][0])):
            # converting the list to a column vector
            column_vector = [[0 for k in range(1)] for j in range(len(list_input_2d))]
            temp1 = [elem[i] for elem in list_input_2d]
            for l in range(len(list_input_2d)):
                column_vector[l][0] = temp1[l]

            temp2 = shifter(column_vector, directions)
            for l in range(len(list_input_2d)):
                list_input_2d[l][i] = temp2[l][0]

    elif directions == 's':
        # shift all the elements of matrix to the bottom
        for i in range(len(list_input_2d[:][0])):
            column_vector = [[0 for k in range(1)] for j in range(len(list_input_2d))]
            temp1 = [elem[i] for elem in list_input_2d]
            for l in range(len(list_input_2d)):
                column_vector[l][0] = temp1[l]
            temp2 = shifter(column_vector, directions)

            for l in range(len(list_input_2d)):
                list_input_2d[l][i] = temp2[l][0]

    return list_input_2d


def merge(list_input_2d, directions):
    """
    This function merges any two consecutive same element if they came in the same path
    Args:
    input: a 2d matrix
    output: a 2d matrix but merged elements
    """
    if directions == 'a':
        # merge left
        for i in range(len(list_input_2d)):
            for j in range(len(list_input_2d[i][:]) - 1):
                if list_input_2d[i][j] == list_input_2d[i][j + 1]:
                    temp = list_input_2d[i][j] + list_input_2d[i][j + 1]
                    list_input_2d[i][j] = temp
                    list_input_2d[i][j + 1] = 0

        return list_input_2d
    elif directions == 'd':
        # merge right
        for i in range(len(list_input_2d)):
            no_of_col = len(list_input_2d[i][:])
            for j in range(no_of_col - 1):
                if list_input_2d[i][no_of_col - j - 1] == list_input_2d[i][no_of_col - j - 2]:
                    temp = list_input_2d[i][no_of_col - j - 1] + list_input_2d[i][no_of_col - j - 2]
                    list_input_2d[i][no_of_col - j - 1] = temp
                    list_input_2d[i][no_of_col - j - 2] = 0

        return list_input_2d

    elif directions == 'w':
        # merge upward
        no_of_col = len(list_input_2d[0][:])
        for i in range(no_of_col):
            for j in range(len(list_input_2d) - 1):
                if list_input_2d[j][i] == list_input_2d[j + 1][i]:
                    temp = list_input_2d[j][i] + list_input_2d[j + 1][i]
                    list_input_2d[j][i] = temp
                    list_input_2d[j + 1][i] = 0
        return list_input_2d

    elif directions == 's':
        # merge downward
        no_of_col = len(list_input_2d[0][:])
        no_of_row = len(list_input_2d)
        for i in range(no_of_col):
            for j in range(no_of_row - 1):
                if list_input_2d[no_of_row - j - 1][i] == list_input_2d[no_of_row - j - 2][i]:
                    temp = list_input_2d[no_of_row - j - 1][i] + list_input_2d[no_of_row - j - 2][i]
                    list_input_2d[no_of_row - j - 1][i] = temp
                    list_input_2d[no_of_row - j - 2][i] = 0
        return list_input_2d


def generate_random():
    """
    This function return a random number between 2 and 4
    Args:
    Input: None
    Output: 2 or 4
    """
    return random.choice([2, 4])


A = [[4, 2, 0, 2], [2, 0, 0, 4], [2, 2, 0, 8], [4, 4, 0, 8]]
for i in range(len(A)):
    print(A[i][:])
while True:
    direction = str(input('enter direction'))
    if direction == 'q':
        break
    b = put_together(merge(put_together(A, direction), direction), direction)

    random_index = [k for k in range(len(b))]
    # print(random_index)
    #
    random.shuffle(random_index)
    # print(random_index)
    flag = 0
    for i in random_index:
        for j in range(len(A[0][:])):
            if b[i][j] == 0:
                b[i][j] = generate_random()
                flag =1
                break
        if flag == 1:
            break

    for i in range(len(b)):
        print(b[i][:])
    A = b

    # count the number of zeros also
    total_zeros = 0
    for i in random_index:
        for j in range(len(A[0][:])):
            if b[i][j] == 0:
                total_zeros += 1

    if total_zeros == 0:
        print("Game Over")
        break
