name: Pull Request
description: Template for submitting pull requests to AI Vibes
title: "[PR] "
body:
  - type: markdown
    attributes:
      value: |
        Thank you for contributing to AI Vibes! Please fill out this template to help us review your pull request.

  - type: textarea
    id: description
    attributes:
      label: "📋 Description"
      description: "Provide a clear and concise description of what this PR accomplishes"
      placeholder: "This PR implements..."
    validations:
      required: true

  - type: dropdown
    id: type
    attributes:
      label: "🏷️ Type of Change"
      description: "What type of change does this PR introduce?"
      options:
        - "🐛 Bug fix (non-breaking change which fixes an issue)"
        - "✨ New feature (non-breaking change which adds functionality)"
        - "💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)"
        - "📚 Documentation update"
        - "🎨 Style/formatting changes (no functional changes)"
        - "♻️ Code refactoring (no functional changes)"
        - "⚡ Performance improvements"
        - "🧪 Adding or updating tests"
        - "🤖 AI tool integration or enhancement"
        - "🔧 Chore (maintenance, dependencies, etc.)"
    validations:
      required: true

  - type: textarea
    id: related_issues
    attributes:
      label: "🔗 Related Issues"
      description: "Link any related issues this PR addresses"
      placeholder: |
        Closes #123
        Fixes #456
        Related to #789

  - type: checkboxes
    id: ai_assistance
    attributes:
      label: "🤖 AI Assistance"
      description: "Check all that apply regarding AI tool usage in this PR"
      options:
        - label: "Used GitHub Copilot for code generation"
        - label: "Used ChatGPT/Claude for problem-solving"
        - label: "Used AI tools for documentation"
        - label: "Used AI for test generation"
        - label: "Used AI for code review and optimization"
        - label: "No AI assistance used"

  - type: textarea
    id: ai_details
    attributes:
      label: "🔍 AI Assistance Details"
      description: "If you used AI tools, please provide details about how they were used"
      placeholder: |
        - GitHub Copilot: Generated boilerplate code for authentication module
        - ChatGPT: Helped design the API structure and error handling
        - Human validation: Reviewed all AI suggestions, added custom logic for edge cases

  - type: checkboxes
    id: testing
    attributes:
      label: "🧪 Testing"
      description: "Testing checklist"
      options:
        - label: "I have added tests that prove my fix is effective or that my feature works"
        - label: "New and existing unit tests pass locally with my changes"
        - label: "I have tested AI-generated code thoroughly"
        - label: "I have tested edge cases and error conditions"

  - type: checkboxes
    id: documentation
    attributes:
      label: "📚 Documentation"
      description: "Documentation checklist"
      options:
        - label: "I have updated relevant documentation"
        - label: "I have added docstrings/comments for new code"
        - label: "I have updated API documentation if applicable"
        - label: "I have documented AI tool usage where appropriate"

  - type: textarea
    id: testing_instructions
    attributes:
      label: "🔧 Testing Instructions"
      description: "Describe how reviewers can test your changes"
      placeholder: |
        1. Clone the branch
        2. Run `pip install -r requirements.txt`
        3. Execute `python test_script.py`
        4. Verify that...

  - type: textarea
    id: screenshots
    attributes:
      label: "📸 Screenshots/Videos"
      description: "If applicable, add screenshots or videos to demonstrate the changes"
      placeholder: "Drag and drop images/videos here or paste links"

  - type: checkboxes
    id: code_quality
    attributes:
      label: "✅ Code Quality Checklist"
      description: "Code quality and standards checklist"
      options:
        - label: "My code follows the project's style guidelines"
        - label: "I have performed a self-review of my own code"
        - label: "I have made corresponding changes to the documentation"
        - label: "My changes generate no new warnings"
        - label: "I have added tests that prove my fix is effective or that my feature works"
        - label: "New and existing unit tests pass locally with my changes"

  - type: checkboxes
    id: security
    attributes:
      label: "🔒 Security Checklist"
      description: "Security considerations"
      options:
        - label: "I have not introduced any security vulnerabilities"
        - label: "No sensitive information is exposed in the code"
        - label: "AI-generated code has been reviewed for security issues"
        - label: "Input validation is properly implemented"
        - label: "Error messages don't expose sensitive information"

  - type: dropdown
    id: breaking_changes
    attributes:
      label: "💥 Breaking Changes"
      description: "Does this PR introduce any breaking changes?"
      options:
        - "No breaking changes"
        - "Yes, breaking changes (details in description)"
    validations:
      required: true

  - type: textarea
    id: breaking_details
    attributes:
      label: "💥 Breaking Changes Details"
      description: "If yes, describe the breaking changes and migration path"
      placeholder: |
        - Changed API endpoint from `/api/v1/users` to `/api/v2/users`
        - Migration: Update client code to use new endpoint
        - Backwards compatibility: Old endpoint deprecated, will be removed in v3.0

  - type: textarea
    id: performance_impact
    attributes:
      label: "⚡ Performance Impact"
      description: "Describe any performance implications of your changes"
      placeholder: |
        - Improved query performance by 50% through better indexing
        - Added caching layer reducing API response time
        - Memory usage increased by ~10MB due to new caching

  - type: textarea
    id: additional_notes
    attributes:
      label: "📝 Additional Notes"
      description: "Any additional information for reviewers"
      placeholder: |
        - This is the first part of a larger feature
        - Known limitation: doesn't handle edge case X (tracked in issue #123)
        - Special attention needed for the authentication logic

  - type: checkboxes
    id: reviewer_guidance
    attributes:
      label: "👀 Review Guidance"
      description: "Guide reviewers on what to focus on"
      options:
        - label: "Focus on code logic and algorithms"
        - label: "Pay attention to security implications"
        - label: "Review AI-generated code carefully"
        - label: "Check performance impact"
        - label: "Verify documentation accuracy"
        - label: "Test user experience"
        - label: "Validate API design"

  - type: markdown
    attributes:
      value: |
        ## 🚀 Ready for Review!
        
        Once you've completed this template, your PR will be ready for review. Our team will:
        1. Review the code for quality, security, and adherence to standards
        2. Validate AI-assisted code if applicable
        3. Test the functionality
        4. Provide constructive feedback
        
        Thank you for contributing to AI Vibes! 🎉
