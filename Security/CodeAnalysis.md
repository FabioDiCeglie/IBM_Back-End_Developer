## Understanding Static Code Analysis

Static code analysis, a debugging method that inspects source code, is performed in a non-runtime environment, meaning it examines the code without executing the program. This practice is also known as source code analysis.

While testing is traditionally carried out by the coder running the program, source code analysis can be done even before a program has been finished. This gives developers the advantage of catching any mistakes early.

Source code analysis tools, also known as Static Application Security Testing (SAST) tools, analyze your source code to find security flaws. SAST tools can be added into your IDE. They can help you detect issues during software development and can save time and effort, especially when compared to finding vulnerabilities later in the development cycle.

Ex: SonarQube

## Understanding Dynamic Analysis

It is the testing and evaluation of an application during runtime. Also referred to as dynamic code scanning, dynamic analysis can identify security issues that are too complicated for static analysis alone to reveal.

Dynamic application security testing (DAST) looks at the application from the outside-in — by simulating attacks against a web application and analyzing the application's responses to discover security vulnerabilities in the application.

Ex: OWASP ZAP ( https://owasp-juice.shop )