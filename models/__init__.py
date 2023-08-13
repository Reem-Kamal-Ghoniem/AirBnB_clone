#!/usr/bin/python3
"""init file that reloads json storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
