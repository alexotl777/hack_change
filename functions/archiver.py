from fastapi.responses import StreamingResponse
import os, io
import zipfile

def archivate_documents(path = 'тестовые файлы'):
    with zipfile.ZipFile('Документы пользователей/тестовые файлы.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))

def is_file_in_archive():
    with zipfile.ZipFile('Документы пользователей/тестовые файлы.zip', 'r') as zipf:
        return 'тестовые файлы/Документы о доходе в PDF.pdf' in zipf.namelist()




# def zipfiles():
#     zip_bytes_io = io.BytesIO()
#     with zipfile.ZipFile(zip_bytes_io, 'w', zipfile.ZIP_DEFLATED) as zipped:
#         for dirname, subdirs, files in os.walk('тестовые файлы'):
#             zipped.write(dirname)
#             for filename in files:
#                 zipped.write(os.path.join(dirname, filename))

#     response = StreamingResponse(
#                 iter([zip_bytes_io.getvalue()]),
#                 media_type="application/zip",
#                 headers = {"Content-Disposition":f"attachment;filename=Ivan_Ivanov.zip",    # 'attachment' automatically downloads the file if IDM extension is enabled on browser. Use 'inline' to avoid that.
#                             "Content-Length": str(zip_bytes_io.getbuffer().nbytes)}
#             )
#     zip_bytes_io.close()
#     return response
