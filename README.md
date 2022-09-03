# DLL-Injector
A python DLL Injector
## How to build
### Auto-Py-To-Exe:
<br>* Select the "hax.py" as the file to compile
<br>* Add additional files "writer.py" and "weld.py"
<br>* add the parameter  --uac-admin so it starts as administrator
### PyInstaller:
<br>* Use command `pyinstaller --noconfirm --onefile --console --uac-admin --add-data "fhf93ht94h9rh9h.py;." --add-data "weld.py;." "hax.py"`
<br>
## How to use
Get the DLL you wish to inject and put it in the same directory as the program, next get the ProcessID of the program you wish to inject into it should inject and should work
