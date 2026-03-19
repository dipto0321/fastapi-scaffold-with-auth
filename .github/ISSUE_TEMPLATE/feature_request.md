# GitHub Feature Request Template

name: Feature Request
description: Suggest a new feature
title: "[FEATURE] "
labels: ["enhancement"]

body:

- type: textarea
    attributes:
      label: Description
      description: Clear description of the feature
      placeholder: What would you like to add?
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Use Case
      description: Why do you need this feature?
      placeholder: I would like this because...
    validations:
      required: true
  
- type: textarea
    attributes:
      label: Proposed Solution
      description: How do you envision this working?
      placeholder: This could work by...
    validations:
      required: false
  
- type: textarea
    attributes:
      label: Alternatives
      description: Any alternative approaches?
      placeholder: Other ways to solve this...
    validations:
      required: false
