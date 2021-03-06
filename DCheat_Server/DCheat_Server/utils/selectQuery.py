'''
Select Query
:copyright: (c) 2016 Lee Jong Seok
'''
from DCheat_Server.database import dao
from DCheat_Server.model.banProgram import BanProgram
from DCheat_Server.model.banList import BanList
from DCheat_Server.model.allowSite import AllowSite
from DCheat_Server.model.allowList import AllowList
from DCheat_Server.model.testInfo import TestInfo
from DCheat_Server.model.user import User
from DCheat_Server.model.testingUser import TestingUser
from DCheat_Server.model.master import Master
from datetime import datetime
from sqlalchemy import func, and_

def select_user_in_course(courseIndex, userIndex):
    return dao.query(TestingUser.index).\
              filter(TestingUser.userIndex == userIndex,
                     TestingUser.testIndex == courseIndex).first().index

def select_user_info(userIndex):
    return dao.query(User.id,
                     User.name).\
              filter(User.index == userIndex).first()

def select_user_index(userId):
    return dao.query(User.index).\
              filter(User.id == userId).first().index
              
def select_user_process_info(testIndex, userIndex):
    return dao.query(TestingUser.processInformation).\
              filter(TestingUser.testIndex == testIndex,
                     TestingUser.userIndex == userIndex).first()

def select_master_index(masterId):
    return dao.query(Master.index).\
               filter(Master.id == masterId).first().index
              
def select_master_info(masterIndex):
    return dao.query(Master.id,
                     Master.email).\
              filter(Master.index == masterIndex).first()
              
def select_master_check(masterId):
    return dao.query(Master.index,
                     Master.password).\
              filter(Master.id == masterId).first()
              
def select_course_index(courseName):
    return dao.query(TestInfo.index).\
              filter(TestInfo.testName == courseName).first().index
              
def get_course_end_date(courseIndex):
    return dao.query(TestInfo.endDate).\
               filter(TestInfo.index == courseIndex).first().endDate
              
def select_course(masterIndex):
    return dao.query(TestInfo.index).\
              filter(TestInfo.masterIndex == masterIndex).first().index   
        
def select_allow_site_list():
    return dao.query(AllowSite.siteURL,
                     AllowSite.siteName).all()

def select_allow_list_index(testIndex):
    return dao.query(AllowList.webIndex).\
              filter(AllowList.testIndex == testIndex,
                     AllowList.isDeleted == 'FALSE').all()

def select_allow_site_in_test():
    return dao.query(AllowSite.siteURL,
                     AllowSite.siteName).\
                join(AllowList,
                     AllowList.webIndex == AllowSite.index).\
                join(TestInfo,
                     TestInfo.index == AllowList.testIndex).all()
                     
def select_ban_list_index(testIndex):
    return dao.query(BanList.banIndex).\
              filter(BanList.testIndex == testIndex,
                     BanList.isDeleted == 'FALSE').all()
                    
def select_ban_program_in_test():
    return dao.query(BanProgram.processName,
                     BanProgram.processPath1,
                     BanProgram.processPath2,
                     BanProgram.processPort).\
                join(BanList,
                     BanList.banIndex == BanProgram.index).\
                join(TestInfo,
                     TestInfo.index == BanList.testIndex).all()

def select_ban_program_name(programIndex):
    return dao.query(BanProgram.programName).\
            filter(BanProgram.index == programIndex).first()
            
def select_ban_list_in_test(testIndex):
    return dao.query(BanList.banIndex).all()

def select_unfinished_test_course_for_user(userIndex):
    return dao.query(TestInfo.testName).\
                join(TestingUser,
                     TestingUser.testIndex == TestInfo.index).\
                join(User,
                     User.index == userIndex).\
                filter(TestingUser.userIndex == userIndex,
                       and_(TestInfo.endDate > datetime.now(),
                            TestInfo.startDate <= datetime.now())).all()
        
def select_unfinished_test_course_for_master(masterIndex):
    return dao.query(TestInfo.index,
                     TestInfo.testName,
                     TestInfo.startDate,
                     TestInfo.endDate).\
                join(Master,
                     Master.index == masterIndex).\
                filter(TestInfo.endDate > datetime.now()).all()
                
def select_user_count(testIndex):
    return dao.query(TestingUser).\
              filter(TestingUser.testIndex == testIndex).count()
              
def select_master_email(courseName):
    return dao.query(Master.emailAddress).\
                join(TestInfo,
                     TestInfo.masterIndex == Master.index).\
                filter(TestInfo.testName == courseName).first()

def select_end_course_for_chart():
    return dao.query(TestInfo.index, TestInfo.masterIndex, TestInfo.testName).\
                filter(TestInfo.endDate <= datetime.now(), TestInfo.makeChart == 'FALSE').all()

def select_user_in_end_course(courseIndex):
    tempQuery = dao.query(TestingUser).\
                filter(TestingUser.testIndex == courseIndex).subquery()

    return dao.query(User.name, tempQuery.firstLogin, tempQuery.lastLogin, tempQuery.lastLogout, tempQuery.individualInfomation).\
                join(User,
                     User.index == tempQuery.userIndex).all()