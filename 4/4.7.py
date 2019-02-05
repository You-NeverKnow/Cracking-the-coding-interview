from collections import defaultdict


# -----------------------------------------------------------------------------|
def main():
    """

    """

    tasks = 'a', 'b', 'c', 'd', 'e', 'f'
    dependency_list = ('a', 'd'), ('f', 'b'), \
                      ('b', 'd'), ('f', 'a'), ('d', 'c')

    dac = defaultdict(list)
    for x, y in dependency_list:
        dac[y].append(x)

    # 0: Not done, 1: Currently queued, 2: Done
    done = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
    }

    for task in tasks:
        do_task(dac, task, done)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def do_task(dac: dict, task: str, done: dict) -> None:
    """

    """

    if done[task] == 1:
        raise ValueError('Circular dependency detected!')

    if done[task] == 2:
        return
    else:
        done[task] = 1

    for dependency in dac[task]:
        do_task(dac, dependency, done)

    done[task] = 2
    print(task, ' ')
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
