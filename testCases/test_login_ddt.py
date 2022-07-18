# import time
#
# from utilities.readProperties1 import ReadConfig
# from PageObjects.LoginPage import LoginPage
# from utilities import XLUtils
# from utilities.customLogger import LogGen
#
#
# # creating test cases for login and checking titles of the login page and dashboard page
# class Test_002_DDT_Login:
#     baseURL=ReadConfig.getApplicationURL()  # collection data from readProperties configuration file
#     path='./TestData/TestData.xlsx'
#     logger=LogGen.logegn()
#
#
#     def test_login_ddt(self,setup):
#         self.logger.info('**********Test_002_DDT_Login**************')
#         self.logger.info("********** Verifying login Page **********")
#         self.driver=setup
#         self.driver.get(self.baseURL)
#         self.lp=LoginPage(self.driver)
#         self.rows=XLUtils.getRowCount(self.path,"Sheet1")
#         print('number of i in excel:',self.rows)
#
#
#         lst_status=[]     #Empty List variables
#         for r in range(2,self.rows+1):
#             self.user=XLUtils.readData(self.path,'Sheet1',r,1)
#             self.password=XLUtils.readData(self.path, 'Sheet1', r, 2)
#             self.exp=XLUtils.readData(self.path, 'Sheet1', r, 3)
#
#             self.lp.setUserName(self.user)
#             self.lp.setPassword(self.password)
#             self.lp.clicklogin()
#             time.sleep(5)
#
#             act_title=self.driver.title
#             exp_title="Dashboard / nopCommerce administration"
#
#             if act_title==exp_title:
#                 if self.exp=='Pass':
#                     self.logger.info('**** test passed ****')
#                     self.lp.clicklogout();
#                     lst_status.append('Pass')
#                 elif self.exp=='Fail':
#                     self.logger.info('**** test Failed ****')
#                     self.lp.clicklogout();
#                     lst_status.append('Fail')
#             elif act_title!=exp_title:
#                 if self.exp=='Pass':
#                    self.logger.info('***** Test failed ****')
#                    self.lp.clicklogout();
#                    lst_status.append('Fail')
#                 elif self.exp=='Fail':
#                     self.logger.info('**** test passed *****')
#                     self.lp.clicklogout();
#                     lst_status.append('Pass')
#
#         if "Fail" not in lst_status:
#             self.logger.info('*************Test_002_DDT_Login passed ************** ')
#             self.driver.close()
#             assert True
#         else:
#             self.logger.info('*************Test_002_DDT_Login passed ************** ')
#             self.driver.close()
#             assert False
#         self.logger.info('*********** Test_002_DDT_Login Completed ****************')
#
#
# #pytest -s -v --html=Reports\report.html testCases/test_login_ddt.py --browser chrome
#
#
# #this test is not running so i have made my changes and run that test_login_ddt_my.py file