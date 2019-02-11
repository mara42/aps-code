def dfs_preorder(arr):
    mid = len(arr) // 2
    if mid == 0:
        return arr
    return [arr[mid]] + dfs_preorder(arr[:mid]) + dfs_preorder(arr[mid+1:])


if __name__ == '__main__':
    import sys
    lines = []
    try:
        for line in sys.stdin:
            lines.append([int(n) for n in line.split(' ')])
    except TypeError as e:
        print(e)
        sys.exit()
    del lines[0]
    bsts = (dfs_preorder(sorted(arr[1:])) for arr in lines)
    for bst in bsts:
        print(*bst)
