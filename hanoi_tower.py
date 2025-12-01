def tower_of_hanoi_solver(level: int):
    a = [i for i in range(level, 0, -1)]
    b = []
    c = []
    state = {'A': a, 'B': b, 'C': c}
    print('Initial state: ',state)

    if level == 2:
        # from_d = 'A'
        # to_d = 'C'
        # temp_d = 'B'
        move_tower_2(state, 'A', 'C','B', [1])
    if level == 3:
        from_d = 'A'
        to_d = 'B'
        temp_d = 'C'
        move_tower_3(state, 'A', 'B', 'C', [1])
    if level == 4:
        from_d = 'A'
        to_d = 'C'
        temp_d = 'B'
        move_tower_4(state, 'A', 'C','B', [1])
    if level == 5:
        move_tower_5(state, 'A', 'B', 'C', [1])
    if level == 6:
        move_tower_6(state, 'A', 'C','B', [1])

def move_tower_6(state, from_d, to_d, temp_d, i):
    move_tower_5(state, from_d, to_d, temp_d, i)

def move_tower_5(state, from_d, to_d, temp_d, i):
    # move_tower_4(state, from_d, to_d, temp_d, i)
    move_tower_3_5(state, 't', 't','t', i, 1)
    move_tower_3_5(state, 't', 't','t', i, 2)
    move_tower_3_5(state, 't', 't','t', i, 3)
    move_tower_3_5(state, 't', 't','t', i, 4)

def move_tower_6(state, from_d, to_d, temp_d, i):
    # move_tower_4(state, from_d, to_d, temp_d, i)
    move_tower_3_6(state, 't', 't','t', i, 1)
    move_tower_3_6(state, 't', 't','t', i, 2)
    move_tower_3_6(state, 't', 't','t', i, 3)
    move_tower_3_6(state, 't', 't','t', i, 4)
    move_tower_3_6(state, 't', 't','t', i, 5)
    move_tower_3_6(state, 't', 't','t', i, 6)
    move_tower_3_6(state, 't', 't','t', i, 7)
    move_tower_3_6(state, 't', 't','t', i, 8)


def move_tower_4(state, from_d, to_d, temp_d, i):
    move_tower_3_4(state, 't', 't','t', i, 1)
    move_tower_3_4(state, 't', 't','t', i, 2)
    # temp = from_d
    # from_d = to_d
    # to_d = temp_d
    # temp_d = temp
    # move_tower_3(state, from_d, to_d, temp_d, i)
    # move_tower_3(state, 'B','C', 'A', i)

def move_tower_3(state, from_d, to_d, temp_d, i):
    move_tower_2(state,  'A', 'B', 'C', i)
    step(state, 'A', 'C', i)
    move_tower_2(state,'B', 'C', 'A', i)
    # step(state, from_d, temp_d, i)
    # temp = from_d
    # from_d = to_d
    # to_d = temp_d
    # temp_d = temp
    # move_tower_2(state, from_d, to_d, temp_d, i)
    # 
def move_tower_3_5(state, from_d, to_d, temp_d, i, n):
    if n == 1:
        move_tower_2(state,  'A', 'B', 'C', i)
        step(state, 'A', 'C', i)
        move_tower_2(state,'B', 'C', 'A', i)
        step(state, 'A', 'B', i)
    elif n == 2:
        move_tower_2(state,  'C', 'A', 'B', i)
        step(state, 'C', 'B', i)
        move_tower_2(state,'A', 'B', 'C', i)
        step(state, 'A', 'C', i)
    elif n == 3:
        move_tower_2(state, 'B', 'C', 'A', i)
        step(state, 'B', 'A', i)
        move_tower_2(state,'C', 'A', 'B', i)
        step(state, 'B', 'C', i)
    elif n == 4:
        move_tower_2(state,  'A', 'B', 'C', i)
        step(state, 'A', 'C', i)
        move_tower_2(state,'B', 'C', 'A', i)

def move_tower_3_6(state, from_d, to_d, temp_d, i, n):
    if n == 1:
        move_tower_2(state,  'A', 'C', 'B', i)
        step(state, 'A', 'B', i)
        move_tower_2(state,'C', 'B', 'A', i)
        step(state, 'A', 'C', i)
    elif n == 2:
        move_tower_2(state,  'B', 'A', 'C', i)
        step(state, 'B', 'C', i)
        move_tower_2(state,'A', 'C', 'B', i)
        step(state, 'A', 'B', i)
    elif n == 3:
        move_tower_2(state, 'C', 'B', 'A', i)
        step(state, 'C', 'A', i)
        move_tower_2(state,'B', 'A', 'C', i)
        step(state, 'C', 'B', i)
    elif n == 4:
        move_tower_2(state,  'A', 'C', 'B', i)
        step(state, 'A', 'B', i)
        move_tower_2(state,'C', 'B', 'A', i)
        step(state, 'A', 'C', i)
    elif n == 5:
        move_tower_2(state,'B', 'A', 'C', i)
        step(state, 'B', 'C', i)
        move_tower_2(state,'A', 'C', 'B', i)
        step(state, 'B', 'A', i)
    elif n == 6:
        move_tower_2(state, 'C', 'B', 'A', i)
        step(state, 'C', 'A', i)
        move_tower_2(state, 'B', 'A', 'C', i)
        step(state, 'B', 'C', i)
    elif n == 7:
        move_tower_2(state, 'A', 'C', 'B', i)
        step(state, 'A', 'B', i)
        move_tower_2(state, 'C', 'B', 'A', i)
        step(state, 'A', 'C', i)
    elif n == 8:
        move_tower_2(state, 'B', 'A', 'C', i)
        step(state, 'B', 'C', i)
        move_tower_2(state, 'A', 'C', 'B', i)

def move_tower_3_4(state, from_d, to_d, temp_d, i, n):
    if n == 1:
        move_tower_2(state,  'A', 'C', 'B', i)
        step(state, 'A', 'B', i)
        move_tower_2(state,'C', 'B', 'A', i)
        step(state, 'A', 'C', i)
    elif n == 2:
        move_tower_2(state,  'B', 'A', 'C', i)
        step(state, 'B', 'C', i)
        move_tower_2(state,'A', 'C', 'B', i)

    

def move_tower_2(state, from_d, to_d, temp_d, i):
    step(state, from_d, temp_d, i)

    step(state, from_d, to_d, i)

    step(state,temp_d, to_d, i)



def step(state, from_d, to_d, i):
    current = state[from_d].pop()
    if len(state[to_d]) and state[to_d][-1] < current:
        print('!!!UPS.... SMTH wrong')
    else:
        state[to_d].append(current)
        print(f'{i[0]} - Move disk from {from_d} to {to_d}: {current}')
        print('Temporary state: ',state)
        i[0] += 1


# def move_tower_3(state, i, test):
#     if test == 1:
#         move_tower_2(state, 'A', 'B', 'C', i)
#     elif test == 2:
#         move_tower_2(state, 'A', 'C', 'B', i)
#     if test:
#         step(state, 'A', 'C', i)
#     else:
#         step(state, 'A', 'B', i)
#     if test:
#         move_tower_2(state, 'B', 'C', 'A', i)
#     else:
#         move_tower_2(state, 'C', 'B', 'A', i)


tower_of_hanoi_solver(2)
print('-' * 100)
tower_of_hanoi_solver(3)
print('-' * 100)
tower_of_hanoi_solver(4)
print('-' * 100)
tower_of_hanoi_solver(5)
print('-' * 100)
tower_of_hanoi_solver(6)
print('-' * 100)