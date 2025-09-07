#!/usr/bin/python3
"""
4-hidden_discovery.py
Prints all names defined in hidden_4.pyc that do not start with __
Only runs when executed as a script, not when imported.
"""

if __name__ == "__main__":
    import importlib.util
    import os

    pyc_path = "/tmp/hidden_4.pyc"

    # Check if the file exists before trying to load it
    if os.path.isfile(pyc_path):
        # Load the compiled module
        spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Collect names that do not start with __
        names = [name for name in dir(module) if not name.startswith("__")]

        # Print in alphabetical order
        for name in sorted(names):
            print(name)
