
def sortLength(inputlist):
        return len(inputlist)
def greatListSortValue(listSortValue, dictFileout):
    listValue, leftSect,rightSect = list(dictFileout.values()), 0, 0
    listValue.sort(key = sortLength)
    listValue.reverse()
    while len(listValue[rightSect]) > 1:
        if len(listValue[rightSect]) == len(listValue[rightSect + 1]):
            rightSect += 1
            continue
        listSubsidiary = sorted(listValue[leftSect:rightSect])
        listSubsidiary.reverse()
        listSortValue.extend(listSubsidiary)
        leftSect = rightSect              
        rightSect += 1 
    return listSortValue    
       
def anagrams(filein, fileout):
    with open(filein, encoding = "cp1251") as f:
        listFilein, dictFileout, listSortValue = (f.read()).split('\n'), {}, []
        setlistFilein = set(listFilein)
        for i in range(len(listFilein)):
            sortedWord = ''.join(sorted(listFilein[i]))
            if not sortedWord in dictFileout:
                dictFileout[sortedWord] = [listFilein[i]]
            else:    
                dictFileout[sortedWord].append(listFilein[i])         
        with open(fileout, "w") as f:
            listSortValue = greatListSortValue(listSortValue, dictFileout)             
            [f.write(str(listSortValue[i]) + "\n") for i in range(len(listSortValue))]
            print(len(listSortValue))

if __name__ == "__main__":
    anagrams("zaliznyak.txt", "anagrams.txt")
