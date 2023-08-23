def orderByK(s, k, low, high):
    if low > high:
        return s
    if s[low] > k:
        print(s)
        s.append(s.pop(low))
        print(s)
        return orderByK(s, k, low, high - 1)
    
    return orderByK(s, k, low + 1, high)

arr = [3, 12, 15, 27, 1, 7, 8]

print(orderByK(arr, 10, 0, len(arr) - 1))