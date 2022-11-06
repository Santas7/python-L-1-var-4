import os
import shutil
import annotation
from annotation import Data
from typing import Type


def make_dir(obj: type(Data)) -> None:
    """
        проверка на сущ-ю директорию + создание новой директории "new_dataset"
    """
    try:
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"
    except OSError:
        shutil.rmtree("new_dataset")
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"


def teleport_dir(obj: type(Data), path: str, class_name: str) -> None:
    """
        данная функция создает новую папку new_dataset и переносит туда каталог class_name со всеми ее под-каталогами
        так что имена новых под-каталогов начинаются с class_name. В конце цикла добавляем в файл аннотация.
        :later_dir: - предыдущая директория ( нужно сохранить )
    """
    later_dir = obj.dir_name
    make_dir(obj)
    for i in range(1000):
        os.rename(os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'),
                  os.path.join(later_dir, class_name, f'{class_name}_{(i+1):04d}.jpg'))
        shutil.copy(os.path.join(later_dir, class_name, f'{class_name}_{(i+1):04d}.jpg'), obj.dir_name)
        os.rename(os.path.join(later_dir, class_name, f"{class_name}_{(i+1):04d}.jpg"),
                  os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'))
        obj.add(os.path.join(path, obj.dir_name, class_name), class_name, f'{class_name}_{(i+1):04d}.jpg')  # добавление строки в файл аннотация

if __name__ == "__main__":
    teleport_dir(Data("dataset"), "D:\Program Files\programmingLabs\Python\python-L-2-var-4\Lab2", annotation.CLASS_DEFAULT[0])
