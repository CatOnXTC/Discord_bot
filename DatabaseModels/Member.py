class Member(Base):
    __tablename__ = 'Members'

    guid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    accounts = relationship("Account", back_populates="member")