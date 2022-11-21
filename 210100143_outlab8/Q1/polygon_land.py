def minCost(values):
    r"""
        This function accepts list
        It returns the result as cost.
    """
    values1 = values.copy()
    values2 = values.copy()
    return min(calc1(values),calc2(values1),calc3(values2))


def calc1(values):
    if len(values) != 0 and len(values) !=3:
        mincost = values[0]*values[1]*values[2]
        values.pop(1)
        mincost += minCost(values)
        return mincost
    elif len(values) == 3:
        return values[0]*values[1]*values[2]
    else:
        return 0

def calc2(values):
    if(len(values) != 0 and len(values) !=3):
        mincost = values[0]*values[len(values)-1]*values[len(values)-2]
        values.pop(len(values)-1)
        mincost += minCost(values)
        return mincost
    elif(len(values) == 3):
        return values[0]*values[1]*values[2]
    else:
        return 0

def calc3(values):
    if(len(values) != 0 and len(values) !=3):
        mincost = values[0]*values[1]*values[len(values)-1]
        values.pop(0)
        mincost += minCost(values)
        return mincost
    elif(len(values) == 3):
        return values[0]*values[1]*values[2]
    else:
        return 0

if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--values",  nargs="*",  type=int, default=[1, 2, 3])
    args = CLI.parse_args()
    print("values: %r" % args.values)
    cost = minCost(args.values)
    print(cost)