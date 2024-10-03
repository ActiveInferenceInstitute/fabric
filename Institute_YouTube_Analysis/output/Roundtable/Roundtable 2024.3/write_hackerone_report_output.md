```
**Title:** Vulnerable Endpoint Exposes Sensitive User Data via Lack of Input Validation

## Summary:
A vulnerability exists in the endpoint `/renderHTML` on `https://site.com` that allows an attacker to exploit a lack of input validation in the `HTMLCode` parameter, leading to the potential for arbitrary JavaScript execution (XSS). This can ultimately allow for the theft of sensitive user data, such as access tokens stored in LocalStorage.

## Description:
The vulnerability is located in the `/renderHTML` endpoint, which accepts an `HTMLCode` parameter. The application reflects the input back to the user without proper validation or sanitization. An attacker can craft a URL that includes malicious JavaScript code in this parameter, which will then be executed in the context of the victim's browser when they visit the URL.

For example, an attacker can construct a URL like:
`https://site.com/renderHTML?HTMLCode=<script>alert(document.domain)</script>`

This will result in the following output:
`<html>Here is your code: <script>alert(document.domain)</script></html>`

If a victim is tricked into clicking this link, the attacker can execute arbitrary JavaScript code in the victim's browser. This can include exfiltrating sensitive data from LocalStorage, such as the `access_token`, which is used for authentication.

## Steps To Reproduce:
1. Log in to the application as a normal user to ensure the `access_token` is stored in LocalStorage.
2. Visit the crafted URL: `https://site.com/renderHTML?HTMLCode=<script>alert(localStorage.getItem("access_token"))</script>`.
3. Observe that the alert shows the `access_token`, demonstrating that the attacker has successfully accessed sensitive data.

## Supporting Material/References:

## Impact:
This vulnerability poses a significant risk to user security as it allows attackers to execute arbitrary code in the context of the victim's browser. By exploiting this XSS vulnerability, attackers can gain access to sensitive authentication tokens stored in LocalStorage, leading to potential account takeover and unauthorized access to user data and actions within the application.
```
