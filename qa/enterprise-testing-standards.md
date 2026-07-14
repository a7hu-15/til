# Enterprise QA & Testing Standards

## The Right Tools
- **Frontend (Web/Mobile UI):** Use tools like **Selenium** and **Appium**.
- **Backend APIs:** Use tools like **Jest** and **Supertest**.

## Manual vs Automated Testing
- **Manual API Testing:** Typically done using tools like **Postman** to visually prove an endpoint works.
- **Automated Testing:** Scripted integration testing (e.g., using Jest) to ensure robustness across continuous updates.

## Database Mocking
It is incredibly dangerous to run automated tests against a live production database. If you run your test suite and hit an `ECONNREFUSED` error on localhost, it means the app is attempting to connect to a real database that isn't running or available. 

To solve this, use Jest to **mock** the database so tests pass securely, instantly, and without mutating real data.

## The 12 Dimensions of QA
A comprehensive QA test ledger should cover:
- Functional Testing
- Security Testing
- Vulnerability Testing
- Load Testing
- Regression Testing
- Database Testing
- ...and more, ensuring full coverage before generating a formal sign-off report.
