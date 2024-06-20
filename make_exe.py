import os

CMD = 'pyinstaller --onefile --noconsole -n autoclass2.1 --clean --add-data="12345.jpg;." --icon=C:/Users/hmins/pyside/12345.ico app.py'
os.system(CMD)

