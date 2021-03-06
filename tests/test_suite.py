from unittest.suite import TestSuite
import unittest
from tests import baitap01, baitap02, baitap03, baitap04, baitap05, baitap07, baitap08, baitap06,baitap10, baitap09 ,baitap11,baitap12,baitap13
if __name__ == "__main__":
    # create the suite from the test classes
    suite_create_account = TestSuite()
    # load the tests
    tests = unittest.TestLoader()
    # add the tests to the suite from modules

    suite_create_account.addTests(tests.loadTestsFromModule(baitap01))

    # suite.addTests(tests.loadTestsFromModule(test))
    # suite_create_account.addTests(tests.loadTestsFromTestCase(MyTestCase))
    # alltestNames = tests.getTestCaseNames(MyTestCase)
    # suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_createAccountFail"))
    # suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_createAcountSuccess"))
    # suite_create_account.addTests(tests.loadTestsFromModule("test.FinalProject.test_submit_newsletter"))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap02))

    # suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_createAccountSuccessfully"))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap03))

    # suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_submit_newsletter"))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap04))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap05))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap06))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap07))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap08))

    suite_create_account.addTests(tests.loadTestsFromModule(baitap09))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap10))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap11))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap12))
    suite_create_account.addTests(tests.loadTestsFromModule(baitap13))

    # -----------------------------------END-------------------------------------#
    # -------------------------------THANK YOU-----------------------------------#

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite_create_account)
