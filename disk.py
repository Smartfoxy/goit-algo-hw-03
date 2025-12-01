def tower_of_hanoi_solver(level: int):
    a = [i for i in range(level, 0, -1)]
    b = []
    c = []
    state = {'A': a, 'B': b, 'C': c}
    print('Initial state: ',state)

    if level == 2:
        from_d = 'A'
        to_d = 'C'
        temp_d = 'B'
        move_test_2(state, from_d, to_d, temp_d, [1])
    if level == 3:
        from_d = 'A'
        to_d = 'B'
        temp_d = 'C'
        move_test_3(state, from_d, to_d, temp_d, [1])
    if level == 4:
        from_d = 'A'
        to_d = 'C'
        temp_d = 'B'
        move_test_4(state, from_d, to_d, temp_d, [1])

def move_test_2(state, from_d, to_d, temp_d, i):
    test(state, from_d, to_d, temp_d, i, 2)

def move_test_3(state, from_d, to_d, temp_d, i):
    # step(state,from_d, to_d, i)
    # i += 1

    # step(state,from_d,temp_d, i)
    # i += 1

    # step(state,to_d,temp_d, i)
    # i += 1

        # i = move_test_base(state, from_d, to_d, temp_d, i)

        # step(state, from_d, temp_d, i)
        # i += 1

        # temp = from_d
        # from_d = to_d
        # to_d = temp_d
        # temp_d = temp

        # move_test_base(state, from_d, to_d, temp_d, i)

    test(state, from_d, to_d, temp_d, i, 3)

    # step(state,temp_d,from_d, i)
    # i += 1

    # step(state,temp_d,to_d, i)
    # i += 1

    # step(state,from_d, to_d, i)
    # i += 1
def test(state, from_d, to_d, temp_d, i, level):
    print('LEVEL - ', level, 'from - ', from_d, 'to -', to_d, 'temp -', temp_d)

    if level > 2:
        level -= 1
        move_test_base(state, from_d, to_d, temp_d, i)
        step(state, from_d, temp_d, i)
        temp = from_d
        from_d = to_d
        to_d = temp_d
        temp_d = temp
        # step(state, to_d, temp_d , i)
        test(state, from_d, to_d, temp_d, i, level)
    else:
        move_test_base(state, from_d, to_d, temp_d, i)


def move_test_4(state, from_d, to_d, temp_d, i):
    test(state, from_d, to_d, temp_d, i, 4)
    # i = move_test_2(state, from_d, temp_d, to_d, i)

    # step(state,from_d, to_d, i)
    # i += 1

    # i = move_test_2(state, temp_d, to_d, from_d, i)

    # step(state,from_d, temp_d, i)
    # i += 1

    # i = move_test_2(state, to_d,  from_d, temp_d, i)

    # step(state,to_d, temp_d, i)
    # i += 1

    # i = move_test_2(state, from_d, temp_d, to_d, i)

def move_test_base(state, from_d, to_d, temp_d, i):
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


tower_of_hanoi_solver(2)
print('-' * 100)
# tower_of_hanoi_solver(3)
# print('-' * 100)
tower_of_hanoi_solver(4)
print('-' * 100)
# tower_of_hanoi_solver(5)