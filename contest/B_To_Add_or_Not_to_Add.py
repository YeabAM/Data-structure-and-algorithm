arrSize , k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

total = 0
left = 0
max_freq = 1
freq_num = nums[0]

for right in range(arrSize):
    total += nums[right]
    boundary = right - left + 1
    expected = boundary * nums[right] - total

    while expected > k:
        total -= nums[left]
        left += 1
        boundary = right - left + 1
        expected = boundary * nums[right] - total

    if max_freq < boundary:
        max_freq = boundary
        freq_num = nums[right]

print(max_freq, freq_num)







