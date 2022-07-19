import os
from PIL import Image


def main(main_imagens_folder, new_width=800):
    if not os.path.isdir(main_imagens_folder):
        raise NotADirectoryError(f'{main_imagens_folder} não existe.')

    for root, dirs, files in os.walk(main_imagens_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            print(file_full_path)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            '''if converted_tag in file_full_path:
                os.remove(file_full_path)'''

            if extension != '.png' and extension != '.JPEG':
                print('isso nao e uma imagen ')
                continue
            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} ja existe')
                continue

            if converted_tag in file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            new_height = round((new_width * height) / width)
            new_img = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            new_img.save(new_file_full_path, optimize=True, quality=70)

            new_img.close()
            img_pillow.close()
            os.remove(file_full_path)

if __name__ == '__main__':
    main_imagens_folder = r'C:\Users\G&M\Pictures\Epic Captures'
    main(main_imagens_folder, 1000)
