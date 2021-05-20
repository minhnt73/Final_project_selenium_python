from unittest.suite import TestSuite
import unittest
from tests import test

if __name__ == "__main__":
    # create the suite from the test classes
    suite_create_account = TestSuite()
    # load the tests
    tests = unittest.TestLoader()
    # add the tests to the suite from modules

    suite_create_account.addTests(tests.loadTestsFromModule(test))

    # suite.addTests(tests.loadTestsFromModule(test))
    # suite_create_account.addTests(tests.loadTestsFromTestCase(MyTestCase))
    # alltestNames = tests.getTestCaseNames(MyTestCase)
    suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_createAccountFail"))
    suite_create_account.addTests(tests.loadTestsFromName("test.FinalProject.test_createAcountSuccess"))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite_create_account)