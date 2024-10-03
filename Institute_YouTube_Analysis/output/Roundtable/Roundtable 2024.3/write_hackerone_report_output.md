```
**Title:** Lack of Input Validation on API Endpoints Leading to Potential Injection Attacks

## Summary:
The application exposes multiple API endpoints that do not properly validate user input, allowing attackers to inject malicious payloads. This vulnerability can potentially lead to SQL Injection, Command Injection, or other types of injection attacks, which could compromise the integrity and security of the application.

## Description:
The API endpoints, particularly `/renderHTML` and others, accept user input without adequate sanitization or validation. For example, the endpoint `/renderHTML?HTMLCode=<h1>XSSHERE` takes the `HTMLCode` parameter and reflects it back in the response without any form of escaping. This lack of input validation allows an attacker to inject arbitrary code into the application.

In the case of the `HTMLCode` parameter, an attacker can craft a request such as:
```
GET /renderHTML?HTMLCode=<script>alert(1)</script>
```
This would result in the script being executed in the context of the user's browser, leading to a Reflected XSS vulnerability. Furthermore, if the application interacts with a database or executes commands based on user input, this vulnerability could escalate to SQL Injection or Command Injection, allowing an attacker to manipulate the database or execute arbitrary commands on the server.

## Steps To Reproduce:
1. Access the application and log in as a normal user.
2. Open your web browser's developer tools (F12) to monitor requests.
3. Send a GET request to the endpoint with the following payload:
   ```
   GET /renderHTML?HTMLCode=<script>alert(1)</script>
   ```
4. Observe that the script executes in the context of your browser, confirming the presence of XSS vulnerability.
5. If applicable, attempt similar payloads in other endpoints to test for SQL Injection or Command Injection vulnerabilities.

## Supporting Material/References:

## Impact:
The vulnerability allows for various types of injection attacks, which can lead to serious consequences including data breaches, unauthorized access to user accounts, and manipulation of sensitive data. The ability to execute arbitrary code or commands could allow an attacker to gain full control over the application, potentially leading to a complete compromise of the server or its database. This vulnerability significantly undermines the trust and security of the application and its users.
```
