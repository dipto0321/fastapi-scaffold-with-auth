# GitHub Issue Template

name: Report a Bug
description: Report a bug to help us improve
title: "[BUG] "
labels: ["bug"]

body:

- type: textarea
    attributes:
      label: Description
      description: Clear description of the bug
      placeholder: What happened?
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Steps to Reproduce
      description: How do we reproduce the issue?
      placeholder: |
        1. Step 1
        2. Step 2
        3. ...
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Expected Behavior
      description: What should happen?
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Actual Behavior
      description: What actually happens?
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Environment
      description: |
        - Python version:
        - FastAPI version:
        - OS:
        - Anything else relevant
      placeholder: Python 3.11, FastAPI 0.128, macOS
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Additional Context
      description: Any other relevant information
