X, Y, W, S = map(int, input().split())

if W <= S:
    case1 = (X+Y)*W
    case2 = min(X, Y)*S + (max(X,Y)-min(X,Y))*W
    print(min(case1, case2))
else:
    X, Y = max(X,Y), min(X, Y)
    case1 = Y*S
    if (X-Y)%2 == 0:
        case1 += ((X-Y)*S)
    else:
        case1 += (((X-Y-1)*S) + W)
    print(case1)