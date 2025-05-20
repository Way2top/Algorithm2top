# Leetcode ：406

def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
    people.sort(key=lambda x: (-x[0], x[1]))
    # [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    ans = []
    for i, p in enumerate(people):
        h, k = p[0], p[1]
        if i == k:
            ans.append(p)
        elif i > k:
            ans.insert(k, p)
    return ans


res = reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(res)
