#!/usr/bin/python3
"""
The __init__.py file is a special Python file
 that is used to define a package.
"""
from AirBnB.models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
