Automated Testing of Banking Transaction System Using Python and pytest

1. Introduction

This project focuses on automated testing of a Banking Transaction System using Python and the pytest testing framework.

2. Objectives

- To understand automated software testing.
- To test banking operations.
- To identify errors in banking transactions.
- To generate test execution and code coverage reports.

3. Tools and Technologies

- Python 3.13
- Visual Studio Code
- pytest 9.2.0
- pytest-cov
- pytest-html

4. Banking System Features

- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts

5. Testing Techniques

- Functional Testing
- Boundary Testing
- Negative Testing
- Error Handling Testing

6. Test Execution

Command:
"python -m pytest -v"

7. HTML Test Report

Command:
"python -m pytest --html=reports/report.html --self-contained-html"

8. Code Coverage

Command:
"python -m pytest --cov=banking --cov-report=html"

Achieved code coverage: initial=95%  after 100%.

9. Conclusion

The project demonstrates automated testing of banking operations using pytest. The test cases verify valid and invalid transactions. Code coverage analysis helps identify untested statements.