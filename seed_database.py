import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb book_review")
os.system("createdb book_review")
os.system("psql book_review < seed.sql")
model.connect_to_db(server.app)
model.db.create_all()

