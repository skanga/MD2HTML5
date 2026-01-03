# Contributing to MD2HTML5

Thank you for your interest in contributing to MD2HTML5! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Submitting Changes](#submitting-changes)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, trolling, or discriminatory language
- Personal attacks or insults
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:

1. **Check existing issues** to avoid duplicates
2. **Test with the latest version** to ensure the bug still exists
3. **Collect information** about the bug:
   - Python version (`python --version`)
   - Operating system and version
   - Browser (if output-related)
   - Input markdown sample
   - Expected vs actual output
   - Error messages or stack traces

Create an issue with the **bug** label and include:

```markdown
**Description**: Brief description of the bug

**Steps to Reproduce**:
1. Step one
2. Step two
3. ...

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Environment**:
- OS: Windows 10 / macOS 12 / Ubuntu 20.04
- Python: 3.9.5
- Browser: Chrome 96

**Sample Markdown**:
```markdown
# Your markdown here
```

**Error Output** (if applicable):
```
Error messages here
```
```

### Suggesting Features

Before suggesting a feature:

1. **Check existing feature requests** to avoid duplicates
2. **Consider if it fits the project scope**
3. **Think about implementation complexity**

Create an issue with the **enhancement** label and include:

```markdown
**Feature Description**: What you want to add

**Use Case**: Why this feature is needed

**Proposed Implementation**: How it could work (optional)

**Alternatives Considered**: Other approaches (optional)

**Examples**: Screenshots or mockups (if applicable)
```

### Contributing Code

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following [Coding Standards](#coding-standards)
4. **Test thoroughly** on multiple platforms
5. **Commit** with clear messages
6. **Push** to your fork
7. **Submit a Pull Request**

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- Text editor or IDE

### Setup Steps

1. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/md2html.git
   cd md2html
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a test file**:
   ```bash
   cp example.md test.md
   # Edit test.md as needed
   ```

5. **Test the script**:
   ```bash
   python md2html.py -i test.md -o test.html
   # Open test.html in browser
   ```

## Coding Standards

### Python Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/):

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Maximum 100 characters (120 for comments)
- **Imports**: One per line, grouped (standard library, third-party, local)
- **Naming**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`

### Type Hints

Always use type hints:

```python
def process_markdown(content: str, theme: str = 'light') -> str:
    """
    Process markdown content to HTML.

    Args:
        content: Markdown text to process
        theme: Color theme ('light' or 'dark')

    Returns:
        HTML string
    """
    # Implementation
    return html
```

### Docstrings

Use Google-style docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    Longer description if needed. Can span multiple lines
    and include details about the function's behavior.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param2 is negative

    Examples:
        >>> my_function("hello", 5)
        True
    """
```

### Comments

- Use comments for **why**, not **what**
- Keep comments up-to-date with code changes
- Write clear, concise comments

```python
# Good: Explains why
# Use lxml parser for better performance with large documents
soup = BeautifulSoup(html, 'lxml')

# Bad: Explains what (obvious from code)
# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'lxml')
```

### CSS Style

For CSS contributions:

- Use **2 spaces** for indentation
- Group related properties
- Use **CSS variables** for colors and values
- Add comments for complex sections
- Keep selectors specific but not overly nested

```css
/* Good */
.code-header {
    /* Layout */
    display: flex;
    justify-content: space-between;
    align-items: center;

    /* Styling */
    background: var(--bg-tertiary);
    padding: 8px 12px;
    border: 1px solid var(--border-color);
    border-radius: 6px 6px 0 0;
}
```

### JavaScript Style

- Use **4 spaces** for indentation
- Use `const` and `let`, not `var`
- Use arrow functions where appropriate
- Add comments for complex logic

```javascript
// Good
const initTheme = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    }
};
```

## Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Fix: Handle empty code blocks without crashing"
git commit -m "Feature: Add support for custom CSS variables"
git commit -m "Docs: Update README with new installation steps"

# Bad
git commit -m "fix bug"
git commit -m "updates"
git commit -m "wip"
```

**Format**:
```
Type: Brief description (50 chars max)

Longer explanation if needed (wrap at 72 chars).
Explain the problem and how this fixes it.

Fixes #123
```

**Types**:
- `Fix:` Bug fixes
- `Feature:` New features
- `Docs:` Documentation changes
- `Style:` Code style changes (formatting, no logic change)
- `Refactor:` Code refactoring
- `Test:` Adding or updating tests
- `Chore:` Maintenance tasks

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Update CHANGES.md** with your changes
4. **Ensure all tests pass**
5. **Fill out the PR template**:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing Done
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] Tested light mode
- [ ] Tested dark mode
- [ ] Tested mobile responsiveness
- [ ] Tested with custom CSS

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests added/updated

## Related Issues
Fixes #123
Related to #456

## Screenshots (if applicable)
[Add screenshots or GIFs]
```

## Testing

### Manual Testing

Test your changes on:

1. **Operating Systems**:
   - Windows 10/11
   - macOS (latest)
   - Linux (Ubuntu/Fedora)

2. **Python Versions**:
   - Python 3.7
   - Python 3.8
   - Python 3.9
   - Python 3.10+

3. **Browsers** (for HTML output):
   - Chrome/Chromium
   - Firefox
   - Safari
   - Edge

4. **Features**:
   - Light mode
   - Dark mode
   - Code highlighting
   - Copy buttons
   - Tables
   - Math rendering
   - Mobile responsiveness
   - Print output
   - Custom CSS

### Test Checklist

- [ ] Run with `example.md`
- [ ] Test with empty file
- [ ] Test with large file (>1000 lines)
- [ ] Test with various code languages
- [ ] Test with custom CSS
- [ ] Test both CLI modes (arguments and interactive)
- [ ] Check HTML validation (W3C validator)
- [ ] Check accessibility (WAVE, axe DevTools)
- [ ] Test keyboard navigation
- [ ] Test on mobile device or emulator
- [ ] Test print output

### Automated Testing

Currently, the project doesn't have automated tests. If you'd like to contribute a test suite:

1. Use `pytest` for testing
2. Aim for >80% code coverage
3. Test both success and failure cases
4. Include edge cases

Example test structure:
```python
import pytest
from md2html import convert_md_to_html

def test_basic_conversion():
    markdown = "# Hello\n\nWorld"
    html = convert_md_to_html(markdown)
    assert "<h1>" in html
    assert "Hello" in html
    assert "World" in html

def test_code_block_highlighting():
    markdown = "```python\nprint('test')\n```"
    html = convert_md_to_html(markdown)
    assert "python" in html.lower()
    assert "copy-button" in html

def test_empty_input():
    html = convert_md_to_html("")
    assert html is not None
```

## Documentation

### README Updates

Update README.md when adding:

- New features
- New command-line options
- New dependencies
- Installation steps
- Usage examples

### Code Documentation

- Add docstrings to new functions
- Update existing docstrings if behavior changes
- Include examples in docstrings when helpful

### CHANGES.md

Add an entry to CHANGES.md for notable changes:

```markdown
## [Unreleased]

### Added
- New feature X that does Y

### Fixed
- Bug in Z that caused crash

### Changed
- Improved performance of W
```

## Questions?

If you have questions about contributing:

1. Check existing [issues](https://github.com/skanga/md2html/issues)
2. Read the [README](README.md) and [FAQ](README.md#-faq)
3. Open a new issue with the `question` label

## Recognition

Contributors will be recognized in:

- README.md contributors section
- CHANGES.md for each release
- Git commit history

Thank you for contributing to MD2HTML5! 🎉
