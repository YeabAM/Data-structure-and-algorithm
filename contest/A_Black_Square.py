from typing import Counter


def main():
    energy = list(map(int, input().split()))
    calorie = {}
    for idx, value in enumerate(energy):
        calorie[idx + 1] = value

    seq = list(map(int, input()))
    # print(seq, calorie, "s")
    count = 0
    for s in seq:
        count += calorie[s]

    print(count)



main()
