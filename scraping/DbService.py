import pymongo
from pymongo import MongoClient

class DbService:
  client = None
  db = None

  def __init__(self, db_url, db_name):
    self.client = MongoClient(db_url)
    self.db = self.client[db_name]

  def create_or_update_persona(self, rut, tipo, razon_social, rol_caso):
    personas = self.db.personas
    persona = personas.find_one({"rut": rut})
    if persona is None:
      persona = {"rut" : rut,
                 "tipo": tipo,
                 "razon_social": razon_social,
                 "rol_casos": [rol_caso] 
                }
      personas.insert(persona)
    else:
      personas.update({'_id': persona['_id']},{
        "rut": rut,
        "tipo": tipo,
        "razon_social": razon_social,
        "rol_casos": persona['rol_casos']
        })
      contains_rol = None
      for rol in persona['rol_casos']:
        if rol == rol_caso:
          contains_rol = 1
          break
      if not contains_rol:
        personas.update({ '_id': persona['_id'] },{"$push": {"rol_casos": rol_caso }})

  def create_or_update_caso(self, rol, info, events, litigants_ruts):
    casos = self.db.casos
    caso = casos.find_one({'rol': rol})
    if caso is None:
      caso = {
        'rol' : rol,
        'info' : info,
        'events': events,
        'litigants_ruts': litigants_ruts
      }
      casos.insert(caso)
    else:
      casos.update({'_id': caso['_id']}, {
          'rol' : rol,
          'info' : info,
          'events': events,
          'litigants_ruts': litigants_ruts
        })

  def clear_personas(self):
    personas = self.db.personas
    personas.remove({})


  def clear_casos(self):
    casos = self.db.casos
    casos.remove({})


  def close(self):
    self.client.close()