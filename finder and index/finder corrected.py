import io, os, re
#import msvcrt 
def ReadFromFile (listBackIndexWord, listBackIndexFiles):
    with open("listBackIndexWord.txt", 'r') as f:
       listBackIndexWord = f.read()
       listBackIndexWord = listBackIndexWord.split(' ')#делаем список по словам
    with open("listBackIndexFiles.txt", 'r') as f:
       listBackIndexFiles = f.read()
       
       listBackIndexFiles = re.sub(r',','', listBackIndexFiles)
       listBackIndexFiles = listBackIndexFiles.split('\n')#делаем список по индексам
       for i in range(len(listBackIndexFiles)):
           #убираем квадратные скобки
           listBackIndexFiles[i] = listBackIndexFiles[i].strip('[]')
           #создаем из строки вложенные списки
           listBackIndexFiles[i] = listBackIndexFiles[i].split(' ')   
    return listBackIndexWord, listBackIndexFiles

def SearchEngine():
    listNameFiles = os.listdir("C:/books")
    listBackIndexWord, listBackIndexFiles =[],[]
    listBackIndexWord, listBackIndexFiles = ReadFromFile (listBackIndexWord, listBackIndexFiles)
    
    while True: 
        #pressedWord = msvcrt.getch() - не понил как работает поэтому сделал так
        pressedWord = input("Input word(To exit press 'q'): ")
        pressedWord =  pressedWord.lower()
        if pressedWord == 'q':
            break
        else:
            if pressedWord in listBackIndexWord: #проверяем есть ли слово в списке
                # берем последовательность индексов 
                index = listBackIndexWord.index(pressedWord) 
                for i in range(len(listBackIndexFiles[index])):
                    print(listNameFiles[int(listBackIndexFiles[index][i])],' ')
            else:
                print("There is no such word!")               
SearchEngine()               
                
