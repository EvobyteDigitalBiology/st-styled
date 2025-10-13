# Release Process

This document describes the release process for st_yled.

## Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backward-compatible functionality additions  
- **PATCH** version for backward-compatible bug fixes

## Release Types

### Alpha Releases (0.x.x)
- Development versions
- Breaking changes allowed
- Published to TestPyPI first

### Beta Releases (1.0.0-beta.x)
- Feature complete for next major version
- API stabilizing
- Published to both TestPyPI and PyPI

### Stable Releases (1.x.x)
- Production ready
- Semantic versioning enforced
- Published to PyPI

## Release Process

### 1. Prepare Release
```bash
# Update version in pyproject.toml
poetry version [patch|minor|major|prerelease]

# Update CHANGELOG.md
# Add release notes

# Commit changes
git add .
git commit -m "chore: bump version to $(poetry version -s)"
```

### 2. Create Release
```bash
# Create and push tag
git tag "v$(poetry version -s)"
git push origin "v$(poetry version -s)"

# GitHub Actions will automatically:
# - Run CI tests
# - Build package
# - Create GitHub release
# - Publish to PyPI
```

### 3. Post-Release
```bash
# Start next development cycle
poetry version prerelease
git add pyproject.toml  
git commit -m "chore: start development of next version"
git push origin main
```

## Manual Release (if needed)

```bash
# Build package
poetry build

# Publish to TestPyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi

# Test installation
pip install --index-url https://test.pypi.org/simple/ st_yled

# Publish to PyPI
poetry publish
```

## Rollback Process

If a release has critical issues:

1. **Yank the release** on PyPI (don't delete)
2. **Create hotfix** branch from the problematic tag
3. **Fix the issue** and create new patch release
4. **Communicate** the issue and fix to users

## Release Checklist

- [ ] All tests passing
- [ ] Version updated in pyproject.toml
- [ ] CHANGELOG.md updated
- [ ] Documentation updated
- [ ] Breaking changes documented
- [ ] Migration guide created (if needed)
- [ ] Release notes prepared
- [ ] Tag created and pushed
- [ ] PyPI release successful
- [ ] GitHub release created
- [ ] Community notified (if major release)