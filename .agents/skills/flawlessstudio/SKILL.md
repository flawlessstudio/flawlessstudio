```markdown
# flawlessstudio Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the `flawlessstudio` Python codebase. You'll learn about file naming, import/export styles, commit message conventions, and how to structure and run tests. This guide ensures consistency and efficiency when contributing to the project.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `imageProcessor.py`, `userProfileManager.py`

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .utils import parseConfig
    from .models import User
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    __all__ = ['ImageProcessor', 'UserProfileManager']
    ```

### Commit Messages
- Follow **conventional commits** with these prefixes:
  - `feat`: New features
  - `docs`: Documentation changes
  - `test`: Test-related changes
  - `ci`: Continuous integration changes
- Keep commit messages concise (average ~45 characters).
  - Example:
    ```
    feat: add user authentication module
    docs: update README with setup instructions
    test: add tests for imageProcessor
    ci: update GitHub Actions workflow
    ```

## Workflows

### Feature Development
**Trigger:** When implementing a new feature  
**Command:** `/feature-dev`

1. Create a new branch: `git checkout -b feat/short-description`
2. Write code following camelCase file naming and relative imports.
3. Add/update tests in corresponding `*.test.*` files.
4. Commit changes using the `feat:` prefix.
5. Open a pull request for review.

### Documentation Update
**Trigger:** When updating or adding documentation  
**Command:** `/docs-update`

1. Edit or add documentation files as needed.
2. Commit changes with the `docs:` prefix.
3. Open a pull request for review.

### Testing
**Trigger:** When adding or updating tests  
**Command:** `/run-tests`

1. Write tests in files matching the `*.test.*` pattern.
2. Use the project's preferred (unknown) test framework.
3. Run tests locally to ensure they pass.
4. Commit with the `test:` prefix.

### Continuous Integration
**Trigger:** When updating CI configurations  
**Command:** `/ci-update`

1. Edit CI configuration files (e.g., GitHub Actions).
2. Commit changes with the `ci:` prefix.
3. Push to trigger CI workflows.

## Testing Patterns

- Test files follow the pattern: `*.test.*` (e.g., `imageProcessor.test.py`)
- Place tests alongside or within a dedicated test directory.
- Use the project's (unspecified) test framework.
- Example test file:
  ```python
  # imageProcessor.test.py
  from .imageProcessor import ImageProcessor

  def test_process_image():
      processor = ImageProcessor()
      result = processor.process('test.jpg')
      assert result is not None
  ```

## Commands
| Command         | Purpose                                      |
|-----------------|----------------------------------------------|
| /feature-dev    | Start a new feature development workflow     |
| /docs-update    | Update or add documentation                  |
| /run-tests      | Run or add tests                             |
| /ci-update      | Update continuous integration configuration  |
```