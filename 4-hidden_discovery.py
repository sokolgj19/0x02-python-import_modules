#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    import importlib.util

    pyc_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(n for n in dir(module) if not n.startswith("__")):
        print(name)
