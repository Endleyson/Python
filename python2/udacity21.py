import os
def rename_files():
    #consiga o nome dos arquivos que estao na pasta
    file_list = os.listdir(r'C:\Users\endle\Desktop\_estudos com vs code\prank')
    saved_path = os.getcwd()
    print('diretorio corrent: ', saved_path)
    os.chdir(r'C:\Users\endle\Desktop\_estudos com vs code\prank')
    print(file_list)
    #procure por um arquivo e renomei-o
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        os.rename (file_name, file_name.translate(table))
        print('old name - ', file_name)
        print('new name - ', file_name.translate(table))
    os.chdir(saved_path)

rename_files()
