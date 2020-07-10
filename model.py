from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
Base=declarative_base()
DB_URI = ‘postgresql+psycopg2://vicky:vicky@123@localhost/contact_api’
class contact(Base):
 __tablename__=’contact’
 Contact_person = Column(String(50))
 Contact_number = Column(Integer)
 Contact_emailId = Column(String(50))
 
if __name__==”__main__”:
 from sqlalchemy import create_engine
 engine = create_engine(DB_URI)
 Base.metadata.drop_all(engine)
 Base.metadata.create_all(engine)