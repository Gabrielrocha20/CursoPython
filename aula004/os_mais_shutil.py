import os
import shutil

caminho_original = r'C:\Users\G&M\Downloads\The.Good.Doctor.S05E01-07.720p.WEB-DL.DUAL'
caminho_novo = r'C:\Users\G&M\Downloads\serie2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} ja existe')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.dat' in file:
            os.remove(new_file_path)


