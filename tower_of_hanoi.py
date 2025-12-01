import math


def tower_of_hanoi_solver(n: int):
    a = [i for i in range(n, 0, -1)]
    b = []
    c = []
    state = {'A': a, 'B': b, 'C': c}
    print('Initial state: ',state)

    move_two_disks(state, 'A', [1], n)

    print('Final state: ',state)


def move_two_disks(state: dict[str, list[int]], from_d: str, i: int, n: int) -> None:
    isEven = n % 2 == 0
    to_d = next_key(state, from_d, isEven)
    temp_d = next(key for key in state.keys() if key not in (from_d, to_d))

    step(state, from_d, temp_d, i)

    step(state, from_d, to_d, i)

    step(state,temp_d, to_d, i)

    if len(state[to_d]) < n:
        f = from_d if get_top(state, from_d) < get_top(state, temp_d) else temp_d
        t = temp_d if f == from_d else from_d
        step(state, f, t, i)
        move_two_disks(state, to_d, i, n)


def step(state: dict[str, list[int]], from_d: str, to_d: str, i: int) -> None:
    current = state[from_d].pop()
    if len(state[to_d]) and state[to_d][-1] < current:
        print('!!!UPS.... SMTH wrong')
    else:
        state[to_d].append(current)
        print(f'№{i[0]} - Move disk from {from_d} to {to_d}: {current}')
        print('Temporary state: ',state)
        i[0] += 1


def next_key(d: dict, current: str, isEven: bool) -> str:
    step = -1 if isEven else 1
    keys = list(d.keys())
    idx = keys.index(current)
    next_idx = (idx + step) % len(keys)
    return keys[next_idx]


def get_top(state, disk):
    return state[disk][-1] if state[disk] else math.inf


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
tower_of_hanoi_solver(7)
print('-' * 100)