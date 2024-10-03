```
**Title:** Vulnerability in Active Inference Project's GitHub Integration Allows Unauthorized Access to Sensitive Data

## Summary:
The Active Inference Project's integration with GitHub has a vulnerability that allows unauthorized access to sensitive data, including research outputs and potentially private information. This vulnerability arises due to improper access controls during the release process on GitHub.

## Description:
During the process of pushing updates and creating releases on GitHub, sensitive data may be inadvertently exposed due to a lack of proper access controls. For example, when a user performs a push or release operation, they might unintentionally include sensitive files or configurations that should not be publicly accessible. This could lead to unauthorized users accessing these files, potentially containing research data, user credentials, or API keys.

The vulnerability is particularly concerning because it allows an attacker to exploit the GitHub repository's public visibility to retrieve sensitive information without any authentication checks. The risk escalates if sensitive data, such as access tokens or private API keys, is included in the pushed files.

## Steps To Reproduce:
1. Clone the Active Inference Project repository from GitHub.
2. Create a new branch and make changes that include sensitive information (e.g., API keys, access tokens).
3. Push the changes to the remote repository.
4. Create a new release in GitHub, ensuring that the sensitive files are part of the release.
5. Access the release page and observe that the sensitive information is publicly accessible.

## Impact:
This vulnerability can lead to significant security risks, including unauthorized access to sensitive data and potential abuse of the exposed information. An attacker could use exposed API keys to interact with services as if they were the legitimate user, leading to data breaches or manipulation of research outputs. This could compromise the integrity of the Active Inference Project and damage the reputation of the organization involved.

```
