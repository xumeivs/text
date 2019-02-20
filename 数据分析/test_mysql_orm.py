from sqlalchemy import create_engine
import pymysql
from sqlalchemy import Column,String,Integer,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine=create_engine('mysql+mysqlconnector://root:13579zheng@127.0.0.1:3306/news')
Base=declarative_base()
Session=sessionmaker(bind=engine)
class News(Base):
    __tablename__='news'
    id=Column(Integer,primary_key=True)
    title = Column(String(200),nullable=False)
    content = Column(String(2000),nullable=False)
    types = Column(String(10),nullable=False)
    image = Column(String(300),)
    autor = Column(String(20),)
    view_count = Column(String(20),)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)
class OrmTest():
    def __init__(self):
        self.session = Session()
    def add_one(self):
        new_obj=News(
            title='标题',
            content='内容',
            types='百家',)
        self.session.add(new_obj)
        self.session.commit()
        return new_obj
def main():
    obj=OrmTest()
    rest=obj.add_one()
    print(rest)
main()
