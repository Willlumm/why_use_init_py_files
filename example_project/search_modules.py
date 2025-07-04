from pkgutil import iter_modules

import example_project

for _, name, ispkg in iter_modules(example_project.__path__):
    print(f"{name:<20}{ispkg=}")
