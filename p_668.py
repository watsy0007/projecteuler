from math import sqrt
from sympy.ntheory import primefactors
from multiprocessing import Pool


def check_num(n: int) -> bool:
    sqrt_v = sqrt(n)
    p_f = primefactors(n)
    if p_f and p_f[-1] < sqrt_v:
        return True
    return False


def solution(item) -> int:
    start_n, end_n = item
    result = [i for i in range(start_n, end_n) if check_num(i)]
    return len(result)


def run(nums, each_step: int, workers: int = 10):
    step = nums // each_step
    print('nums:', nums, "\nstep:", step, "\neach step:", each_step, "\nworkers:", workers)
    params = [[i * each_step, (i + 1) * each_step] for i in range(step)]
    print(params[0], '...', params[-1])
    with Pool(workers) as p:
        return sum(p.map(solution, params))


print(run(100_000_000, 100_000, 8))
# print(run(1_000_000, 1_000, 4))
