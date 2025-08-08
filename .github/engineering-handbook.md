# Engineering Handbook

This handbook codifies the core engineering practices for our team. All engineers and automation (including GitHub Copilot) must adhere to these standards. This document is referenced by `copilot-instructions.md` to ensure compliance during code reviews and development.

---

## 1. Language & Tooling

- **Primary Language:** Python is the only approved language for application and infrastructure code.
- **Python Environment Consistency:** The same Python kernel (interpreter/environment) must be used for both application and test code to ensure compatibility and reproducibility.
- **Unit Testing:** All code must be covered by unit tests using `pytest`.
- **Linting & Formatting:**
  - Linting is enforced with `pylint`.
  - Formatting is enforced with `black`.
  - Both are run automatically by the CI pipeline. No manual recommendations are needed.
  - A `Makefile` must exist with targets for `lint` (pylint) and `format` (black).

## 2. Version Control & CI/CD

- **Repository:** All code is managed in GitHub repositories.
- **CI/CD:**
  - GitHub Actions is the only approved CI/CD system.
  - The pipeline is enterprise-standard and not customizable beyond allowed configuration.
  - All deployments are triggered via GitHub Actions workflows.

## 3. Deployment & Cloud

- **Cloud Provider:** AWS is the only approved cloud provider.
- **Core AWS Services:**
  - S3, IAM, Lambda, SNS, SQS, CloudWatch Logs are the primary services used.
  - All infrastructure must be defined as code (e.g., using AWS CDK, CloudFormation, or Terraform if permitted).
- **Security:**
  - IAM policies must follow least privilege.
  - No hardcoded secrets or credentials in code or configuration.

## 4. Copilot Usage

- All engineers have access to an Enterprise Copilot license.
- Copilot suggestions must be reviewed for correctness, security, and compliance with this handbook.
- Copilot must not be used to generate or accept code that violates these standards.

## 5. Testing

- **Unit Tests:**
  - All new code must include or update `pytest` unit tests.
  - Tests must be isolated, repeatable, and not depend on external systems unless explicitly required.
  - Test coverage must be maintained or improved with each change.

## 6. Documentation

- All public modules, classes, and functions must include docstrings.
- README and relevant documentation must be updated with any significant change.

## 7. Makefile Example

```makefile
.PHONY: lint format test

lint:
 pylint src/ tests/

format:
 black src/ tests/

test:
 pytest
```

---

## 8. Enforcement

- All code reviews and Copilot interactions must reference this handbook.
- Any deviation must be justified and documented in the pull request.

---

_This handbook is a living document. Updates require team consensus and must be reflected in both this file and `copilot-instructions.md`._
