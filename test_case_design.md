# Banking Transaction System
## Formal Test Case Design

| Test ID | Test Scenario | Input | Precondition | Expected Result | Technique |
|---|---|---|---|---|---|
| TC01 | Check balance | 1000 | Account exists | Balance = 1000 | Functional |
| TC02 | Deposit money | 500 | Account exists | Balance = 1500 | Functional |
| TC03 | Withdraw money | 200 | Balance = 1000 | Balance = 800 | Functional |
| TC04 | Negative deposit | -100 | Account exists | ValueError | Negative |
| TC05 | Zero deposit | 0 | Account exists | ValueError | Boundary |
| TC06 | Insufficient withdrawal | 2000 | Balance = 1000 | ValueError | Error handling |
| TC07 | Negative withdrawal | -100 | Account exists | ValueError | Negative |
| TC08 | Successful transfer | 200 | Sender = 1000, Receiver = 500 | Sender = 800, Receiver = 700 | Functional |
| TC09 | Insufficient transfer | 2000 | Sender = 1000 | ValueError | Error handling |
| TC10 | Withdraw exact balance | 1000 | Balance = 1000 | Balance = 0 | Boundary |
| TC11 | Zero transfer | 0 | Accounts exist | ValueError | Boundary |
| TC12 | Negative transfer | -100 | Accounts exist | ValueError | Negative |
| TC13 | Decimal deposit | 100.50 | Balance = 1000 | Balance = 1100.50 | Functional |