from cx_Freeze import setup, Executable

setup(
    name = "Name_project",
    version = "version",
    description = "About project",
    executables = [Executable("main.py")]
)
