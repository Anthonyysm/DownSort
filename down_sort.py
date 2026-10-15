import os
import shutil

DOWNLOADS_FOLDER_PATH = f'{__file__}'.replace(
    'Desktop/down_sort.py', 'Downloads')

for file in os.listdir(DOWNLOADS_FOLDER_PATH):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]

    folder_to_organize_file = f'{DOWNLOADS_FOLDER_PATH}/{file_extension}'

    if not os.path.isdir(folder_to_organize_file):
        os.mkdir(folder_to_organize_file)

    shutil.move(f'{DOWNLOADS_FOLDER_PATH}/{file}',
                f'{folder_to_organize_file}/{file}')
