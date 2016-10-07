#!/usr/bin/env python3

import os

# Mingi jama, see päris täpselt ei toimi vist.

os.rename("patternexaminer/database.py", "patternexaminer/database_main.py")
os.rename("patternexaminer/database_public.py", "patternexaminer/database.py")

from patternexaminer.database import init_db, populate_options, populatePublicData

from patternexaminer import database
print(database.engine)
init_db()
populate_options()
populatePublicData()


os.rename("patternexaminer/database.py", "patternexaminer/database_public.py")
os.rename("patternexaminer/database_main.py", "patternexaminer/database.py")