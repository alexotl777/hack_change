import os
import zipfile

def archivate_documents():
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    with zipfile.ZipFile('Документы пользователей/тестовые файлы.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('тестовые файлы/', zipf)