from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *
import random,string
connection = psycopg2.connect(host=’localhost’, database=’contact_api’, user=’vicky', password=’vicky@123')
cursor = connection.cursor()
class contactCollectionResource(CollectionResource):
 model=contact
class contactResource(SingleResource):
 model=contact
