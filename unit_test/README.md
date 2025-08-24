How to Write Great Unit Tests in Python (based on this video https://youtu.be/EIV_ixKGPmc?si=UZlnAerr-j9ARO8F):

# Unit tests
## What
- Unit tests validate the behavior of a small isolated piece of code. That's usually a single function or method. 
- These unit tests are typically fast, deterministic, and easy to run.

## Why
- catch up bugs
- make refactoring safer
- document how code is supposed to behave

## Other types of test
- end to end test: verify complete
user workflows
- security tests: protect against vulnerabilities
- data consistency tests: make sure data stays reliable

## How
### dependence
- python built-in unittest module
- pytest (recommended)

### monkey patching
- dynamically replacing a function or attribute at runtime


### mocking