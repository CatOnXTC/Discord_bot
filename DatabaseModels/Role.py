class Role(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    member_roles = relationship("MemberRole", back_populates="role")