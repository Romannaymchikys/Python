import io, os, re

def ListPunctRemovLower(listContentFiles):#замена пунктуации на пробелы и нижний регистр
    listContentFiles = re.sub(r'[.,;:!-?\s]',' ', listContentFiles)
    listContentFiles = re.sub(r'\s+', ' ', listContentFiles)# лишние пробелы
    listContentFiles = listContentFiles.lower()#нижний регтстр
    listContentFiles = listContentFiles.split(' ')#делаем список
    listContentFiles[len(listContentFiles) - 1] = ' '
    listContentFiles = list(set(listContentFiles))# удаляем дубликаты
    return listContentFiles

def WriteFileBackIndex(listContentAllFiles): 
    listKeys = list(listContentAllFiles.keys())
    print('write')
    listItems = list(listContentAllFiles.values())
    with open("listBackIndexWord.txt", 'w') as f:
        for i in range(len(listKeys)):
            f.write(str(listKeys[i]) + ' ')
    with open("listBackIndexFiles.txt", 'w') as f:
        for i in range(len(listItems)):
            f.write(str(listItems[i]) + '\n')

def GreatBackIndex(listContentAllFiles, listContentFiles, index):
    for i in range(len(listContentFiles)):
        if not str(listContentFiles[i]) in listContentAllFiles:
            listI = [index]
            listContentAllFiles.update({str(listContentFiles[i]): listI})
        else:
            value = listContentAllFiles.get(str(listContentFiles[i]))
            value.append(index)
            listContentAllFiles[str(listContentFiles[i])] = value
    return listContentAllFiles  
                    
def ListOpenEntryFiles():
    listNameFiles = os.listdir("C:/books")#закидываем в список название файлов"указывать путь где  лежит сам файл"
    listContentAllFiles ={}
    for i in range(len(listNameFiles)):
        with open(str(listNameFiles[i]), encoding = "Windows - 1251") as f:#закидываем в строку садержание файла 
            #listContentFiles = [line.strip() for line in f]
            listContentFiles = f.read()
            listContentFiles = ListPunctRemovLower(listContentFiles)
            listContentAllFiles = GreatBackIndex(listContentAllFiles, listContentFiles, i)      
    WriteFileBackIndex(listContentAllFiles)
    
ListOpenEntryFiles()

  
    
