# Version 1：朴素二分
# 这里不直接在传参的部分直接hi = len(a)的原因：Python是一个边执行便解释的函数，直接放在传参行的话不能认出来a是一个列表，也就不能使用len函数
def bisect(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# Version 2：朴素二分check
# 可以额外传递一个函数
# 上面的例子中，如果说有一个check()函数，也是一个非递减函数，接收a[i]作为参数，求x > check[a[i]]的话，朴素二分（或者说内置库的二分函数bisect）就不起作用了
def bisect_check(a, x, lo=0, hi=None, check=lambda y: y):
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if x < check(a[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo
