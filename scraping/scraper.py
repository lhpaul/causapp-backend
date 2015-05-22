import Constants
from Constants import db_url, db_name

import DbService
from DbService import DbService

dbService = DbService(db_url, db_name)


################# Crear Personas ######################################

dbService.create_or_update_persona("176988703", "persona", "", "RTTTSCC")
dbService.create_or_update_persona("176988567", "persona", "", "RTTTSCC")
dbService.create_or_update_persona("176988567", "abogado", "", "FILO")




################# Crear Casos ##########################################

info = {
  'estado_adm': 'Sin archivar',
  'etapa': '0 Tratacion',
  'Tribunal': '1 Juzgado Civil Santiago',
  'nombre': 'CERTISING CERTIFICADORA IN',
  'proc': 'Tramitacion Exhorto Internacional',
  'fecha_ing': '09/02/2015',
  'ubicacion': 'LETRA',
  'estado_proc': 'Tramitacion',
  'texto_demanda': 'http://civil.poderjudicial.cl/CIVILPORWEB/img/Comun/DocVacio.JPG',
  'foja': '43' 
}

historias = [
  {
    'link_doc': 'http://civil.poderjudicial.cl/CIVILPORWEB/img/Comun/edit.jpg',
    'etapa': 'Tramitacion',
    'tramite': 'NOT',
    'descripcion': 'Exhorto Internacional',
    'fecha': '09/02/2015',
    'foja': 44
  },
  {
    'link_doc': 'http://civil.poderjudicial.cl/CIVILPORWEB/img/Comun/edit.jpg',
    'etapa': 'Tramitacion',
    'tramite': 'NOT',
    'descripcion': 'Exhorto Internacional',
    'fecha': '09/02/2015',
    'foja': 45
  }
]

rut_litigants = [
  '176988703',
  '176988567'
]
dbService.create_or_update_caso('RTTTSCC', info, historias, rut_litigants)



  
dbService.close()