"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    testing user

"""

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

from DCheat_Server.model import Base
from DCheat_Server.model.testInfo import TestInfo
from DCheat_Server.model.user import User

class TestingUser (Base) :
    
    __tablename__ = 'TestingUser'
    
    index = Column(INTEGER(unsigned = True),
            primary_key = True,
            autoincrement = True,
            nullable = False)
    testIndex = Column(INTEGER(unsigned = True),
                       ForeignKey(TestInfo.index,
                                  onupdate = 'CASCADE',
                                  ondelete = 'CASCADE'),
                       autoincrement = True,
                       nullable = False)
    userIndex = Column(INTEGER(unsigned = True),
                       ForeignKey(User.index,
                                  onupdate = 'CASCADE',
                                  ondelete = 'CASCADE'),
                       autoincrement = True,
                       nullable = False)