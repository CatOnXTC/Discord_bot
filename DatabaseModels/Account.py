from sqlalchemy import Integer, Text, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = 'Accounts'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    member_guid = Column(Text, ForeignKey('Members.guid'))

    member = relationship("Member", back_populates="accounts")