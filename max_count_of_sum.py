def opt_sum(n):
    acc = 0
    res_list = []
    if n == 1:
        res_list.append(1)
        return res_list
    if n == 2:
        res_list.append(2)
        return res_list
    arg = n
    for i in range(1, n):
        if (arg - i) == 0:
            res_list.append(arg)
            return res_list
        if (arg-i) < 0:
            res_list[-1] = res_list[-1] + arg
            return res_list
        else:
            if (arg - i) < i:
                res_list.append(arg)
                return res_list
            arg = arg-i
            res_list.append(i)
    return res_list




def main():
    n = int(input())
    result = opt_sum(n)
    print(len(result))
    print(*result)

if __name__ == "__main__":
    main()
