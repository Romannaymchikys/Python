
def collatz(n):
    dictCollatz, keyMaxTraject = {}, 1
    for i in range(n):
        chisloK, pathLength = i + 1, 0
        while chisloK:
            if not chisloK in dictCollatz and chisloK != 1:
                if not chisloK % 2:
                    chisloK //= 2
                else:
                    chisloK = 3 * chisloK + 1
                pathLength += 1
            else:
                if chisloK == 1:
                    dictCollatz.update({i + 1: pathLength})
                else:
                    pathLength += dictCollatz[chisloK]
                    dictCollatz.update({i + 1: pathLength})
                chisloK = 0
        if dictCollatz[keyMaxTraject] < pathLength:
            keyMaxTraject = i        
    tupleCollatz = (keyMaxTraject, dictCollatz[keyMaxTraject])       
    return tupleCollatz            
if __name__ == "__main__":
    tupleCollatz = collatz(1000000)
    print(tupleCollatz)
