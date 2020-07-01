import cx_Freeze

executables = [cx_Freeze.Executable(script="game.py", icon="assets/icone.ico")]
cx_Freeze.setup(
    name = "Kings of Road",
    options = {"build_exe":{"packages":["pygame"],
    "include_files": ["assets"]
    } },
    executables = executables
)