#!/bin/bash
# pyinstaller can compile Python code to an executable but it can not cross compile!
# so use a Windows machine to create a Windows executable!

pyinstaller --clean --onefile --name Python_RPG main.py func.py Dungeon.py Player.py