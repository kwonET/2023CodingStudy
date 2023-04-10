def permutation(arr, r):
    used = [0 for _ in range(len(arr))]
    result = []

    def generate(chosen, used):
        if len(chosen) == r:
            result.append(tuple(chosen))
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

    return result


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    li = []
    a = []
    for i in range(len(numbers) + 1):
        li = li + list(set(permutation(list(numbers), i)))
    del li[0]
    for item in li:
        num_str = "".join(e for e in list(item))
        num_str.lstrip("0")
        num = int(num_str)
        if is_prime(num):
            a.append(num)
    answer = list(set(a))

    return len(answer)
