from cx_Freeze import setup, Executable

setup(
    name="GameChemy",
    version="0.55a",
    description="An unusual alchemy game",
    executables=[Executable("Gamechemy.py")])
