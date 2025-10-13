# Contributing to st_yled

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and clone** the repository
2. **Install dependencies**:
   ```bash
   poetry install --with dev
   poetry run pre-commit install
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Quality

We use several tools to maintain code quality:

- **Ruff** for linting and formatting
- **mypy** for type checking  
- **pytest** for testing
- **pre-commit** for automated checks

Run quality checks:
```bash
make ci  # Runs all checks
```

## Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

feat: add new component wrapper
fix: resolve CSS injection issue  
docs: update API documentation
test: add unit tests for styler
refactor: improve component structure
chore: update dependencies
```

## Pull Request Process

1. **Ensure tests pass**: `make test`
2. **Update documentation** if needed
3. **Add tests** for new functionality
4. **Follow code style** guidelines
5. **Write clear commit messages**
6. **Submit PR** with detailed description

## Testing

- Add tests for new features in `tests/`
- Ensure all tests pass: `poetry run pytest`
- Aim for >80% test coverage
- Test with multiple Streamlit versions when possible

## Documentation

- Update docstrings for public APIs
- Add examples for new components
- Update README.md if needed
- Test documentation examples

## Questions?

- Open an issue for bugs or feature requests
- Join discussions in GitHub Discussions
- Check existing issues before creating new ones