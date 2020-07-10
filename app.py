from sqlalchemy import create_engine
import falcon
from falcon_autocrud.middleware import Middleware
import psycopg2
from resources import *
db_engine = create_engine(‘postgresql+psycopg2://vicky:vicky@123@localhost/contact_api’)
app = application = falcon.API(middleware=[Middleware()])
app.add_route(‘/contact’,contactrCollectionResource(db_engine))
#id=1 for add 
#id=2 for update
#id=3 for delete
#id =4 for filter
app.add_route(‘/contact/{id}’,contactResource(db_engine))

