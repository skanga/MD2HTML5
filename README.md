# MD2HTML5 - Professional Markdown to HTML Converter

> Transform your Markdown files into beautiful, responsive HTML documents with a single command.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Cross-platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/skanga/md2html)

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Command-Line Options](#-command-line-options)
- [Custom Styling](#-custom-styling)
- [Features in Detail](#-features-in-detail)
- [Examples](#-examples)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)
- [Credits](#-credits)

---

## ✨ Features

### Core Features
- 🎨 **Beautiful Default Styling** - Professional, modern design out of the box
- 🌓 **Dark Mode** - Automatic dark mode with manual toggle and system preference detection
- 📱 **Fully Responsive** - Perfect on desktop, tablet, and mobile devices
- ♿ **Accessibility First** - WCAG 2.1 AA compliant with keyboard navigation
- 🎯 **Syntax Highlighting** - Code blocks with Pygments highlighting for 500+ languages
- 📊 **Rich Markdown Support** - Tables, footnotes, TOC, code blocks, and more

### Advanced Features
- 🔗 **Heading Anchors** - Clickable # links on all headings for deep linking
- 📋 **Copy Code Buttons** - One-click copy for all code blocks with tooltips
- 🖼️ **Lazy Loading Images** - Better performance with native lazy loading
- 🧮 **Conditional MathJax** - Loads only when mathematical notation is detected
- 🖨️ **Print Optimized** - Clean, professional print stylesheet
- 🎭 **External Link Indicators** - Visual ↗ indicator for external links
- ⚡ **Performance Optimized** - Fast loading with minimal dependencies

### Developer Features
- 🎨 **Custom CSS Support** - Bring your own stylesheet
- 🎛️ **Theme Variables** - CSS custom properties for easy customization
- 📝 **Semantic HTML5** - Clean, well-structured output
- 🔧 **No Build Step** - Single Python script, no compilation needed
- 📦 **Standalone** - All CSS and JavaScript embedded in output

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install markdown beautifulsoup4 lxml pygments
```

Or use the requirements file if:

```bash
pip install -r requirements.txt
```

### Download

**Option 1: Clone the repository**
```bash
git clone https://github.com/skanga/md2html.git
cd md2html
```

**Option 2: Download the script directly**
```bash
curl -O https://raw.githubusercontent.com/skanga/md2html/main/md2html.py
```

**Option 3: Make it globally accessible (Linux/macOS)**
```bash
chmod +x md2html.py
sudo cp md2html.py /usr/local/bin/md2html
```

---

## ⚡ Quick Start

### Basic Usage

Convert a Markdown file to HTML:

```bash
python md2html.py -i document.md
```

This creates `output.html` in the current directory.

### Interactive Mode

Run without arguments for interactive prompts:

```bash
python md2html.py
```

You'll be prompted for:
1. Input Markdown file path
2. Theme mode (light/dark)
3. Output HTML file name

---

## 📖 Usage

### Basic Conversion

```bash
# Convert with default settings (light mode)
python md2html.py -i input.md

# Output to specific file
python md2html.py -i input.md -o output.html

# Output to specific directory
python md2html.py -i input.md -o myfile.html -d /path/to/directory
```

### Theme Selection

```bash
# Light mode (default)
python md2html.py -i input.md -m light

# Dark mode
python md2html.py -i input.md -m dark
```

### Custom CSS

```bash
# Use your own stylesheet
python md2html.py -i input.md -c mystyle.css
```

### Complete Example

```bash
python md2html.py \
  -i documentation.md \
  -o docs.html \
  -d ./output \
  -c custom.css \
  -m dark
```

---

## 🎛️ Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--input_file` | `-i` | Path to input Markdown file | None (required) |
| `--output_file` | `-o` | Name of output HTML file | `output.html` |
| `--output_dir` | `-d` | Output directory path | `.` (current) |
| `--css_file` | `-c` | Path to custom CSS file | Built-in CSS |
| `--mode` | `-m` | Theme mode: `light` or `dark` | `light` |
| `--help` | `-h` | Show help message | - |

### CSS Priority

The tool uses CSS in this priority order:

1. **Custom CSS** (via `-c` option) - Highest priority
2. **Default CSS files** (`style_light.css` or `style_dark.css` if present)
3. **Built-in CSS** - Fallback (always available)

---

## 🎨 Custom Styling

### Using External CSS Files

Create `style_light.css` or `style_dark.css` in the same directory:

```css
/* style_light.css */
:root {
    --bg-primary: #ffffff;
    --text-primary: #333333;
    --link-color: #007aff;
    /* ... more variables ... */
}

body {
    font-family: 'Georgia', serif;
    max-width: 1000px;
}
```

The tool will automatically use these files based on the selected mode.

### CSS Variables Reference

The built-in theme uses CSS custom properties you can override:

```css
:root {
    /* Colors */
    --bg-primary: #ffffff;        /* Main background */
    --bg-secondary: #f9f9f9;      /* Secondary background */
    --bg-tertiary: #f4f4f4;       /* Tertiary background */
    --text-primary: #333333;      /* Main text */
    --text-secondary: #666666;    /* Secondary text */
    --text-tertiary: #777777;     /* Tertiary text */
    --border-color: #eaeaea;      /* Borders */
    --border-accent: #007aff;     /* Accent color */
    --link-color: #007aff;        /* Links */
    --code-bg: #f4f4f4;          /* Code background */
    --code-text: #333333;        /* Code text */

    /* Effects */
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
    --transition-speed: 0.2s;
}
```

### Using Custom CSS with -c Option

```bash
python md2html.py -i input.md -c my-custom-theme.css
```

Your custom CSS will completely replace the built-in styles.

---

## 🔍 Features in Detail

### 1. Dark Mode

**Automatic Detection**
- Respects system dark mode preference
- Saves user's manual preference to localStorage
- Smooth transitions between themes

**Manual Toggle**
- Floating button in top-right corner
- Sun/moon icons
- Keyboard accessible

**How it works:**
1. First visit: Uses system preference
2. User toggles: Saves to localStorage
3. Next visit: Restores saved preference

### 2. Syntax Highlighting

Supports 500+ languages via Pygments:

```markdown
```python
def hello():
    print("Highlighted!")
```
```

Features:
- Language label displayed
- Copy button for each code block
- Line wrapping for long lines
- Horizontal scroll on mobile

### 3. Responsive Design

**Breakpoints:**
- **Desktop**: 900px max-width, centered
- **Tablet** (≤768px): Full width, adjusted typography
- **Mobile** (≤480px): Optimized for small screens
- **Touch devices**: 44px minimum touch targets

**Mobile Optimizations:**
- Edge-to-edge code blocks
- Full-width images
- Readable font sizes (16px minimum)
- No accidental zoom on iOS
- Touch-friendly buttons

### 4. Accessibility

**WCAG 2.1 AA Compliant:**
- ✅ Keyboard navigation
- ✅ Screen reader friendly
- ✅ Focus indicators
- ✅ Skip-to-content link
- ✅ ARIA labels
- ✅ Sufficient color contrast
- ✅ Semantic HTML structure

**Keyboard Shortcuts:**
- `Tab`: Navigate interactive elements
- `Enter/Space`: Activate buttons
- `Shift+Tab`: Navigate backwards

### 5. Heading Anchors

All headings get automatic anchor links:

```markdown
## My Section
```

Becomes:
```html
<h2 id="my-section">
    My Section
    <a href="#my-section" class="heading-anchor">#</a>
</h2>
```

Share direct links: `https://example.com/doc.html#my-section`

### 6. Copy Code Buttons

Every code block gets a copy button:

**Features:**
- Hover tooltip: "Copy code"
- Click feedback (checkmark icon)
- Auto-resets after 2 seconds
- Keyboard accessible
- Hidden on print

### 7. Mathematical Notation

Supports LaTeX math via MathJax:

```markdown
Inline: $E = mc^2$

Block:
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

**Smart Loading:**
- Only loads MathJax if `$$`, `\[`, or `\(` detected
- Saves ~150KB when no math present
- Async loading (non-blocking)

### 8. Tables

Enhanced table styling:

```markdown
| Feature | Status | Notes |
|---------|--------|-------|
| Tables  | ✅     | Beautiful! |
| Sorting | ❌     | Coming soon |
```

Features:
- Zebra striping (alternating rows)
- Hover highlighting
- Sticky headers (on scroll)
- Responsive (horizontal scroll on mobile)

### 9. External Links

External links get visual indicators:

```markdown
[Internal](./page.html) → No indicator
[External](https://example.com) → Shows ↗
```

**Behavior:**
- 0.6 opacity on desktop
- 1.0 opacity on mobile (always visible)
- Doesn't apply to localhost links

### 10. Print Stylesheet

**Optimizations:**
- Clean black & white output
- URLs printed after links
- Page-break control
- Hidden interactive elements
- 12pt font size
- Proper margins

Print with: `Ctrl+P` / `Cmd+P`

---

## 📚 Examples

### Example 1: Simple Document

**Input** (`simple.md`):
```markdown
# My Blog Post

This is a paragraph with **bold** and *italic* text.

## Code Example

```python
print("Hello, World!")
```

## Links

- [Internal link](#code-example)
- [External link](https://example.com)
```

**Command:**
```bash
python md2html.py -i simple.md -o blog.html
```

**Result:**
- Beautiful HTML with syntax highlighting
- Dark mode toggle
- Copy button on code block
- Responsive layout

### Example 2: Technical Documentation

**Input** (`api-docs.md`):
```markdown
# API Documentation

## Authentication

Use Bearer tokens:

```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com
```

## Rate Limits

| Endpoint | Rate Limit |
|----------|------------|
| /users   | 100/hour   |
| /posts   | 1000/hour  |

## Mathematical Formula

The complexity is $O(n \log n)$.
```

**Command:**
```bash
python md2html.py -i api-docs.md -m dark -o docs.html
```

**Result:**
- Dark mode by default
- Table with zebra striping
- MathJax formula rendering
- Professional documentation look

### Example 3: Custom Styled Blog

**Custom CSS** (`blog-theme.css`):
```css
:root {
    --link-color: #e74c3c;
    --border-accent: #e74c3c;
}

body {
    font-family: 'Georgia', serif;
    max-width: 800px;
    font-size: 18px;
}

h1 {
    font-size: 3em;
    text-align: center;
}
```

**Command:**
```bash
python md2html.py -i post.md -c blog-theme.css -o post.html
```

**Result:**
- Custom red accent color
- Georgia serif font
- Larger base font size
- Centered main heading

---

## ⚙️ Configuration

### Default CSS Files

Place these in the same directory as `md2html.py`:

- `style_light.css` - Used for light mode
- `style_dark.css` - Used for dark mode

These are automatically detected and used if present.

### Markdown Extensions

The following Python-Markdown extensions are enabled:

1. **fenced_code** - GitHub-style code blocks with ```
2. **tables** - Table support
3. **toc** - Table of contents generation
4. **footnotes** - Footnote support
5. **attr_list** - Add attributes to elements
6. **md_in_html** - Markdown inside HTML blocks

### Syntax Highlighting Themes

Code highlighting uses Pygments with:
- **Light mode**: `default` style
- **Dark mode**: `monokai` style

To change, modify line 65 in `md2html.py`:
```python
formatter = HtmlFormatter(style='your-style-here')
```

Available styles: `default`, `monokai`, `vim`, `github`, `solarized-dark`, etc.

---

## 🔧 Troubleshooting

### Problem: Import errors

**Error:**
```
ModuleNotFoundError: No module named 'markdown'
```

**Solution:**
```bash
pip install markdown beautifulsoup4 lxml pygments
```

### Problem: File not found

**Error:**
```
Error: File 'input.md' not found.
```

**Solution:**
- Check file path is correct
- Use absolute path: `python md2html.py -i /full/path/to/file.md`
- Check current directory: `pwd` (Linux/Mac) or `cd` (Windows)

### Problem: Permission denied

**Error:**
```
PermissionError: [Errno 13] Permission denied: 'output.html'
```

**Solution:**
- Check output directory is writable
- Run with appropriate permissions
- Change output directory: `-d ~/Documents`

### Problem: Dark mode not working

**Issue:** Page always shows light mode

**Solution:**
1. Check browser supports localStorage
2. Clear browser cache and localStorage
3. Try toggling manually (top-right button)
4. Check browser console for JavaScript errors

### Problem: Code not highlighting

**Issue:** Code blocks show as plain text

**Solution:**
1. Ensure Pygments is installed: `pip install pygments`
2. Check language is supported: `pygmentize -L lexers`
3. Verify code fence syntax:
   ```markdown
   ```python
   code here
   ```
   ```

### Problem: Slow conversion

**Issue:** Large files take a long time

**Solution:**
- Normal for files >1MB
- MathJax detection scans entire document
- Consider splitting large documents
- Image lazy loading helps render performance

### Problem: Math not rendering

**Issue:** LaTeX formulas show as text

**Solution:**
1. Check syntax: Use `$$...$$` or `$...$`
2. Wait for MathJax to load (2-3 seconds)
3. Check browser console for errors
4. Verify internet connection (MathJax loads from CDN)

---

## ❓ FAQ

### Can I use this commercially?

**Yes!** MIT license allows commercial use. See [License](#-license).

### Does it work offline?

**Mostly.** The generated HTML is standalone except for:
- MathJax (loads from CDN if math detected)
- External images (if referenced in markdown)

To make fully offline, self-host MathJax or remove math support.

### Can I customize colors?

**Yes!** Three ways:
1. Override CSS variables in custom CSS
2. Provide complete custom stylesheet with `-c`
3. Modify built-in CSS in the Python file (lines 341-1098)

### Is the output SEO-friendly?

**Yes!** Features for SEO:
- Semantic HTML5 structure
- Proper heading hierarchy
- Meta tags (charset, viewport)
- Clean URLs with heading anchors
- Fast loading time

Add your own meta tags by editing line 156.

### Can I convert multiple files at once?

**Currently no,** but you can use a shell script:

**Bash (Linux/Mac):**
```bash
for file in *.md; do
    python md2html.py -i "$file" -o "${file%.md}.html"
done
```

**PowerShell (Windows):**
```powershell
Get-ChildItem *.md | ForEach-Object {
    python md2html.py -i $_.Name -o "$($_.BaseName).html"
}
```

### Does it support footnotes?

**Yes!** Use standard Markdown footnote syntax:

```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

### Can I add a table of contents?

**Yes!** Use the `[TOC]` marker:

```markdown
# My Document

[TOC]

## Section 1
## Section 2
```

### How do I add images?

Standard Markdown syntax:

```markdown
![Alt text](path/to/image.png)
![Remote image](https://example.com/image.jpg)
```

Images get:
- Lazy loading
- Responsive sizing
- Rounded corners and shadows
- Hover zoom effect

### Can I embed HTML?

**Yes!** HTML is allowed in Markdown:

```markdown
<div class="custom-class">
This is **markdown** inside HTML.
</div>
```

### Is there a GUI version?

**No,** but the interactive mode (`python md2html.py`) provides prompts.

For a GUI, consider:
- Wrapping in a simple Tkinter/PyQt interface
- Using as a backend for a web app
- Creating an Electron wrapper

### How do I update?

```bash
# If cloned from git
cd md2html
git pull

# If downloaded directly
# Download new version and replace file
```

### What's the file size of generated HTML?

Typical sizes:
- Small doc (1 page): ~20-30KB
- Medium doc (10 pages): ~50-80KB
- Large doc (50 pages): ~200-400KB

Most size is embedded CSS (~25KB) and JavaScript (~3KB).

---

## 🤝 Contributing

Contributions are welcome! Here's how:

### Reporting Bugs

1. Check [existing issues](https://github.com/skanga/md2html/issues)
2. Create new issue with:
   - Python version
   - OS and browser
   - Input markdown sample
   - Expected vs actual output
   - Error messages (if any)

### Suggesting Features

1. Check [existing feature requests](https://github.com/skanga/md2html/issues?q=is%3Aissue+label%3Aenhancement)
2. Create new issue describing:
   - Use case
   - Proposed behavior
   - Example if possible

### Pull Requests

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes
4. Test thoroughly
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open Pull Request

### Code Style

- Follow PEP 8
- Add type hints
- Include docstrings
- Comment complex logic
- Test on multiple platforms

### Testing

Before submitting:
- [ ] Test on Windows, macOS, and Linux
- [ ] Test with Python 3.7, 3.8, 3.9, 3.10+
- [ ] Test light and dark modes
- [ ] Test on mobile browsers
- [ ] Test with custom CSS
- [ ] Check accessibility (keyboard navigation)
- [ ] Verify print output

---

## 📄 License

**MIT License**

Copyright (c) 2026 Shiraz Kanga

Based on MD2HTML by Zigao Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 👏 Credits

### Original Author
**Zigao Wang** - Original MD2HTML project
- GitHub: [ZigaoWang/md2html](https://github.com/ZigaoWang/md2html/)
- Website: [zigao.wang](https://zigao.wang)

### Enhancements & Modernization
**Shiraz Kanga** - MD2HTML5 enhancements
- GitHub: [@skanga](https://github.com/skanga)
- Repository: [skanga/md2html](https://github.com/skanga/md2html/)

### Technologies Used
- **Python-Markdown** - Markdown parsing
- **BeautifulSoup4** - HTML manipulation
- **Pygments** - Syntax highlighting
- **MathJax** - Mathematical notation
- **Modern CSS** - Responsive design

### Inspiration
- GitHub Markdown styling
- Medium's reading experience
- Modern documentation sites
- Accessibility best practices

---

## 🔗 Links

- **GitHub Repository**: [https://github.com/skanga/md2html](https://github.com/skanga/md2html)
- **Original Project**: [https://github.com/ZigaoWang/md2html](https://github.com/ZigaoWang/md2html)
- **Issue Tracker**: [https://github.com/skanga/md2html/issues](https://github.com/skanga/md2html/issues)
- **Changelog**: [CHANGES.md](CHANGES.md)

---

## 📞 Support

Need help?

1. **Read the docs** - Check this README and FAQ
2. **Search issues** - Someone may have had the same problem
3. **Ask questions** - Open an issue with the `question` label
4. **Report bugs** - Open an issue with detailed info

---

## 🎯 Roadmap

Planned features for future releases:

- [ ] Batch conversion mode (multiple files)
- [ ] Custom template support
- [ ] PDF export option
- [ ] Diagram support (Mermaid)
- [ ] i18n (internationalization)
- [ ] Plugin system
- [ ] GUI version
- [ ] Configuration file support (`.md2htmlrc`)

---

## 📊 Statistics

- **Lines of Python**: ~280
- **Lines of CSS**: ~756
- **Lines of JavaScript**: ~65
- **Supported Languages**: 500+ (via Pygments)
- **Markdown Extensions**: 6
- **CSS Variables**: 12+
- **Responsive Breakpoints**: 3
- **Dependencies**: 4

---

<div align="center">

**Made with 💜 by [Shiraz Kanga](https://github.com/skanga)**

Based on [MD2HTML](https://github.com/ZigaoWang/md2html/) by [Zigao Wang](https://github.com/ZigaoWang)

⭐ Star this repo if you find it useful!

</div>
