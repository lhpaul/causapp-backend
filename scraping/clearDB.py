import Constants
from Constants import db_url, db_name

import DbService
from DbService import DbService

dbService = DbService(db_url, db_name)
dbService.clear_personas()
dbService.clear_casos()
dbService.close()