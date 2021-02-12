class MemberRole(Base):
    __tablename__ = 'MemberRole'

    guid = Column(Text, primary_key=True)
    member_guid = Column(Text, ForeignKey('Members.guid'))
    role_id = Column(Integer, ForeignKey('Roles.id'))

    member = relationship("Member", back_populates="member_roles")
    role = relationship("Role", back_populates="member_roles")