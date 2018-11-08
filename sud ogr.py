import copy
import time


def setLimits(bd, i, j):
    changeLater = []
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if bd[i][k] != 0:
            if bd[i][k] in values:
                values.remove(bd[i][k])
        if bd[k][j] != 0:
            if bd[k][j] in values:
                values.remove(bd[k][j])
    for p in range((i // 3) * 3, ((i // 3) * 3) + 3):
        for r in range((j // 3) * 3, ((j // 3) * 3) + 3):
            if bd[p][r] in values:
                values.remove(bd[p][r])
    if len(values) == 1:
        bd[i][j] = values[0]
    else:
        bd[i][j] = list(values)
    return bd


def changeLimits(bd, i, j):
    for k in range(9):
        if len(str(bd[i][k])) != 1:
            if bd[i][j] in bd[i][k]:
                bd[i][k].remove(bd[i][j])
        if len(str(bd[k][j])) != 1:
            if bd[i][j] in bd[k][j]:
                bd[k][j].remove(bd[i][j])
    for p in range((i // 3) * 3, ((i // 3) * 3) + 3):
        for r in range((j // 3) * 3, ((j // 3) * 3) + 3):
            if len(str(bd[p][r])) != 1:
                if bd[i][j] in bd[p][r]:
                    bd[p][r].remove(bd[i][j])
    return bd


def lastHero(num, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(str(board[i][j])) != 1:
                values = copy.deepcopy(board[i][j])
                if (len(board[i][j]) == 1):
                    board[i][j] = values[0]
                    num[0] -= 1
                    changeLimits(board, i, j)
                for p in range((i // 3) * 3, ((i // 3) * 3) + 3):
                    for r in range((j // 3) * 3, ((j // 3) * 3) + 3):
                        if len(str(board[p][r])) == 1:
                            if board[p][r] in values:
                                values.remove(board[p][r])
                        else:
                            if (i == p and j == r):
                                pass
                            else:
                                temp = copy.deepcopy(board[p][r])
                                for v in range(len(board[p][r])):
                                    if temp[v] in values:
                                        values.remove(temp[v])
                if len(values) == 1:
                    board[i][j] = values[0]
                    num[0] -= 1
                    changeLimits(board, i, j)
    return board


def lastHeroString(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(str(board[i][j])) != 1:
                values = copy.deepcopy(board[i][j])
                if len(str(board[i][j])) == 1:
                    if board[i][j] in values:
                        values.remove(board[i][j])
                else:
                    for k in range(len(board[i])):
                        if j != k:
                            temp = copy.deepcopy(board[i][k])
                            if len(str(board[i][k])) == 1:
                                if board[i][k] in values:
                                    values.remove(board[i][k])
                            else:
                                for v in range(len(temp)):
                                    if temp[v] in values:
                                        values.remove(temp[v])
                if len(values) == 1:
                    board[i][j] = values[0]
                    num[0] -= 1
                    changeLimits(board, i, j)
    return board


def PairsRow(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if len(str(board[i][j])) != 1:
                for k in range(len(board)):
                    values1 = copy.deepcopy(board[i][j])
                    values2 = copy.deepcopy(board[i][k])
                    if values1 == values2 and k != j and len(values1) == 2 and len(values2) == 2:
                        for m in range(9):
                            if len(str(board[i][m])) != 1 and m != j and m != k:
                                values2 = copy.deepcopy(board[i][m])
                                for v in range(len(values1)):
                                    if values1[v] in values2:
                                        values2.remove(values1[v])
                                board[i][m] = values2
                                if len(board[i][m]) == 1:
                                    lastHero(num, board)
    return board


def PairsColumn(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if len(str(board[i][j])) != 1:
                for k in range(len(board)):
                    values1 = copy.deepcopy(board[i][j])
                    values2 = copy.deepcopy(board[k][j])
                    if values1 == values2 and k != i and len(values1) == 2 and len(values2) == 2:
                        for m in range(9):
                            if len(str(board[m][j])) != 1 and m != i and m != k:
                                values2 = copy.deepcopy(board[m][j])
                                for v in range(len(values1)):
                                    if values1[v] in values2:
                                        values2.remove(values1[v])
                                board[m][j] = values2
                                if len(values2) == 1:
                                    lastHero(num, board)
    return board


def threeSome(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if len(str(board[i][j])) != 1:
                values1 = copy.deepcopy(board[i][j])
                if len(values1) == 3:
                    js = []
                    js.append(j)
                    values2 = []
                    values3 = []
                    for k in range(len(board)):
                        if values2 == [] and len(str(board[i][k])) != 1 and k != j:
                            values2 = copy.deepcopy(board[i][k])
                            if len(values2) <= len(values1):
                                js.append(k)
                                for v in range(len(values2)):
                                    if values2[v] in values1:
                                        pass
                                    else:
                                        values2 = []
                                        js.pop()
                                        break
                            else:
                                values2 = []
                        elif len(str(board[i][k])) != 1 and values3 == [] and k != j:
                            values3 = copy.deepcopy(board[i][k])
                            if len(values3) <= len(values1):
                                for v in range(len(values3)):
                                    if values3[v] in values1:
                                        pass
                                    else:
                                        values2 = []
                                        values3 = []
                                        js.pop()
                                        break
                            else:
                                values2 = []
                                values3 = []
                                js.pop()
                                break
                            js.append(k)
                        if values3 != []:
                            for m in range(len(board)):
                                if m != js[0] and m != js[1] and m != js[2] and len(str(board[i][m])) != 1:
                                    valChange = copy.deepcopy(board[i][m])
                                    for v in range(len(values1)):
                                        if values1[v] in valChange:
                                            valChange.remove(values1[v])
                                    board[i][m] = valChange
                                    if len(board[i][m]) == 1:
                                        lastHero(num, board)
                    js.clear()
    return board


def threeSomeColumn(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if len(str(board[i][j])) != 1:
                values1 = copy.deepcopy(board[i][j])
                if len(values1) == 3:
                    js = []
                    js.append(i)
                    values2 = []
                    values3 = []
                    for k in range(len(board)):
                        if values2 == [] and len(str(board[k][j])) != 1 and k != i:
                            values2 = copy.deepcopy(board[k][j])
                            if len(values2) < 4:
                                js.append(k)
                                for v in range(len(values2)):
                                    if values2[v] in values1:
                                        pass
                                    else:
                                        values2 = []
                                        js.pop()
                                        break
                            else:
                                values2 = []
                        elif len(str(board[k][j])) != 1 and values3 == [] and k != i:
                            values3 = copy.deepcopy(board[k][j])
                            if len(values3) < 4:
                                for v in range(len(values3)):
                                    if values3[v] in values1:
                                        pass
                                    else:
                                        values2 = []
                                        values3 = []
                                        js.pop()
                                        break
                            else:
                                values2 = []
                                values3 = []
                                js.pop()
                                break
                            js.append(k)
                        if values3 != []:
                            for m in range(len(board)):
                                if m != js[0] and m != js[1] and m != js[2] and len(str(board[m][j])) != 1:
                                    valChange = copy.deepcopy(board[m][j])
                                    for v in range(len(values1)):
                                        if values1[v] in valChange:
                                            valChange.remove(values1[v])
                                    board[m][j] = valChange
                                    if len(board[m][j]) == 1:
                                        lastHero(num, board)
                    js.clear()
    return board


def greatFour(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            for p in range((i // 3) * 3, ((i // 3) * 3) + 3):
                for r in range((j // 3) * 3, ((j // 3) * 3) + 3):
                    if len(str(board[p][r])) != 1:
                        values1 = copy.deepcopy(board[p][r])
                        if len(values1) == 4:
                            js = []
                            js += p, r
                            values2 = []
                            values3 = []
                            values4 = []
                            for k1 in range((i // 3) * 3, ((i // 3) * 3) + 3):
                                for k2 in range((j // 3) * 3, ((j // 3) * 3) + 3):
                                    if values2 == [] and len(str(board[k1][k2])) != 1:
                                        if k1 == p and k2 == r:
                                            break
                                        values2 = copy.deepcopy(board[k1][k2])
                                        if len(values2) <= len(values1):
                                            js += k1, k2
                                            for v in range(len(values2)):
                                                if values2[v] in values1:
                                                    pass
                                                else:
                                                    values2 = []
                                                    js.pop()
                                                    js.pop()
                                                    break
                                        else:
                                            values2 = []
                                    elif len(str(board[k1][k2])) != 1 and values3 == [] and values2 != []:
                                        if k1 == p and k2 == r:
                                            break
                                        values3 = copy.deepcopy(board[k1][k2])
                                        if len(values3) <= len(values1):
                                            js += k1, k2
                                            for v in range(len(values3)):
                                                if values3[v] in values1:
                                                    pass
                                                else:
                                                    values3 = []
                                                    for delete in range(2):
                                                        js.pop()
                                                    break
                                        else:
                                            values3 = []
                                    elif len(str(
                                            board[k1][k2])) != 1 and values4 == [] and values3 != [] and values2 != []:
                                        if k1 == p and k2 == r:
                                            break
                                        values4 = copy.deepcopy(board[k1][k2])
                                        if len(values4) <= len(values1):
                                            js += k1, k2
                                            for v in range(len(values4)):
                                                if values4[v] in values1:
                                                    pass
                                                else:
                                                    values4 = []
                                                    for delete in range(2):
                                                        js.pop()
                                                    break
                                        else:
                                            values4 = []
                                        if values4 != []:
                                            for m1 in range((i // 3) * 3, ((i // 3) * 3) + 3):
                                                for m2 in range((j // 3) * 3, ((j // 3) * 3) + 3):
                                                    toDelete = []
                                                    lenghtJs = int(len(js) / 2)
                                                    for it in range(lenghtJs):
                                                        f1 = js[2 * it]
                                                        f2 = js[2 * it + 1]
                                                        if m1 == f1 and m2 == f2:
                                                            toDelete = [2 * it, 2 * it + 1]
                                                    if toDelete != []:
                                                        js.pop(toDelete[1])
                                                        js.pop(toDelete[0])
                                                        toDelete = []
                                                    elif len(str(board[m1][m2])) != 1:
                                                        valChange = copy.deepcopy(board[m1][m2])
                                                        for v in range(len(values1)):
                                                            if values1[v] in valChange:
                                                                valChange.remove(values1[v])
                                                        board[m1][m2] = valChange
                                                        if len(valChange) == 1:
                                                            lastHero(num, board)
                            js.clear()
    return board


def hiddenPairs(board, num):
    return board


def solve(board):
    num = [81]
    bd = copy.deepcopy(board)
    changeLater = []
    for i in range(len(bd)):
        for j in range(len(bd[i])):
            if bd[i][j] == 0:
                setLimits(bd, i, j)
                if len(str(bd[i][j])) == 1:
                    changeLater += i, j
            else:
                num[0] -= 1
    for i in range(len(changeLater) - 1):
        changeLimits(bd, changeLater[i], changeLater[i + 1])
        i = i + 2
    num_check = 0
    while num_check != num:
        num_check = copy.copy(num)
        bd = lastHero(num, bd)
        bd = lastHeroString(bd, num)
        bd = PairsRow(bd, num)
        bd = PairsColumn(bd, num)
        bd = threeSome(bd, num)
        bd = threeSomeColumn(bd, num)
        bd = greatFour(bd, num)
    print(num)
    printBoard(bd)
    print()
    return True


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
    print()


def test():
    start_time = time.time()
    board = [[0 for x in range(9)] for x in range(9)]
    with open('task.txt', 'r') as f:
        for i in range(9):
            for j in range(9):
                board[i][j] = f.read(1)
                if board[i][j] == ".":
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
    printBoard(board)
    solve(board)
    print("--- %s seconds ---" % (time.time() - start_time))


test()
