from PIL import Image
import os
import sys
from PyQt5.QtWidgets import *
# FIXED_PARAMETERS = {
    #     'width': 315,
    #     'height': 236
    # }
class Form(QMainWindow):

    def __init__(self, parent=None,width=315,height=236):
        super().__init__(parent)
        self.width = width
        self.height = height

    def get_directory_element_path(self):  # <-----
        return QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")

    def get_file_path(self):  # <-----
        # return QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        return QFileDialog.getOpenFileName(self, "Выбрать файл", ".")[0]

    def config_photo_size(self,element_path):
        with Image.open(f'{element_path}') as img:
            img.load()
            img = img.resize((self.width,self.height))
            filename = element_path.split('/')[-1]
            format = filename.split('.')[-1]
            dir_path = element_path.replace(filename,'')
            if format.lower() == 'png':
                previous_dir = '/'.join(element_path.split('/')[0:-2])
                former_dir = element_path.split('/')[-2]
                if not os.path.isdir(f"{previous_dir}/New_{former_dir}"):
                    os.mkdir(f"{previous_dir}/New_{former_dir}")
                img.save(f"""{previous_dir}/New_{former_dir}/{filename.split('.')[0]}_315x236.{format}""", 'PNG')

            elif format.lower() == 'jpg':
                previous_dir = '/'.join(element_path.split('/')[0:-2])
                former_dir = element_path.split('/')[-2]
                if not os.path.isdir(f"{previous_dir}/New_{former_dir}"):
                    os.mkdir(f"{previous_dir}/New_{former_dir}")
                img.save(f"""{previous_dir}/New_{former_dir}/{filename.split('.')[0]}_315x236.{format}""", 'JPEG')
            else:
                pass

    def config_photos_size(self,path_for_elements):
        real_path_to_elements = [f'{path_for_elements}/{i}' for i in os.listdir(path=path_for_elements)]
        for item_path in real_path_to_elements:
            self.config_photo_size(element_path=item_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    #
    # ##one
    # file_path = ex.get_file_path()
    # ex.config_photo_size(file_path)
    ##many
    elements_from_dir = ex.get_directory_element_path()
    ex.config_photos_size(elements_from_dir)





