# MD2HTML5 Feature Showcase

Welcome to the **MD2HTML5** example document! This file demonstrates all the features of the markdown to HTML converter.

[TOC]

## Typography Examples

### Headings

You can see headings from H1 to H6. Hover over any heading to see the **anchor link** appear!

#### This is H4

##### This is H5

###### This is H6

### Text Formatting

This paragraph contains **bold text**, *italic text*, ***bold and italic***, ~~strikethrough~~, and `inline code`.

You can also use <mark>highlighted text</mark> with HTML.

## Lists

### Unordered List

- First item
- Second item
  - Nested item 1
  - Nested item 2
    - Deeply nested item
- Third item

### Ordered List

1. First step
2. Second step
   1. Sub-step A
   2. Sub-step B
3. Third step

### Task List

- [x] Completed task
- [x] Another completed task
- [ ] Pending task
- [ ] Another pending task

## Code Examples

### Inline Code

Use the `print()` function in Python or `console.log()` in JavaScript.

### Python Code Block

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
for num in fibonacci(10):
    print(num, end=' ')
```

### JavaScript Code Block

```javascript
// Async/await example
async function fetchData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

// Usage
fetchData('https://api.example.com/data')
    .then(data => console.log(data));
```

### Bash/Shell Code Block

```bash
#!/bin/bash
# Deploy script example

echo "Starting deployment..."

# Build the project
npm run build

# Run tests
npm test

# Deploy to production
rsync -avz dist/ user@server:/var/www/html/

echo "Deployment complete!"
```

### SQL Code Block

```sql
-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (username, email) VALUES
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com');

-- Query with join
SELECT u.username, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.username
ORDER BY post_count DESC;
```

## Links

### Internal Links

- [Jump to Typography](#typography-examples)
- [Jump to Code Examples](#code-examples)
- [Jump to Tables](#tables)

### External Links

- [GitHub](https://github.com) - Notice the ↗ indicator for external links
- [Python Documentation](https://docs.python.org)
- [MDN Web Docs](https://developer.mozilla.org)

## Images

![Placeholder Image](https://via.placeholder.com/800x400/007aff/ffffff?text=Example+Image)

*Note: Images are lazy-loaded for better performance and have a hover zoom effect!*

## Blockquotes

> "The best way to predict the future is to invent it."
> — Alan Kay

> This is a multi-paragraph blockquote.
>
> It can contain **formatted text** and even `code snippets`.
>
> Very useful for highlighting important information!

## Tables

### Simple Table

| Feature | Status | Notes |
|---------|--------|-------|
| Dark Mode | ✅ | Toggle in top-right |
| Responsive | ✅ | Mobile optimized |
| Syntax Highlighting | ✅ | 500+ languages |
| Copy Buttons | ✅ | One-click copy |
| Math Support | ✅ | LaTeX via MathJax |
| Print Stylesheet | ✅ | Clean print output |

### Aligned Table

| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Apple        | 1              | $1.50 |
| Banana       | 12             | $2.00 |
| Orange       | 6              | $3.50 |

*Tables have zebra striping and hover effects!*

## Mathematical Notation

### Inline Math

The Pythagorean theorem is $a^2 + b^2 = c^2$, and Einstein's famous equation is $E = mc^2$.

### Block Math

The quadratic formula:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

The Gaussian integral:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

Matrix notation:

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
ax + by \\
cx + dy
\end{bmatrix}
$$

## Horizontal Rules

You can separate sections with horizontal rules:

---

Like that one above!

---

## Footnotes

Here's a sentence with a footnote[^1]. And here's another one[^2].

You can also use named footnotes[^note] for better organization.

[^1]: This is the first footnote. It will appear at the bottom of the document.

[^2]: This is the second footnote with **formatted text** and [a link](https://example.com).

[^note]: Named footnotes are easier to manage in long documents.

## HTML Elements

You can embed HTML directly:

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3 style="margin-top: 0;">Custom HTML Block</h3>
    <p>This is a custom-styled div with gradient background. You can mix HTML and <strong>Markdown</strong> freely!</p>
</div>

<details markdown="1">
<summary>Click to expand collapsible section</summary>

This content is hidden by default. You can put any markdown here:

- Lists
- **Formatted text**
- `Code snippets`

```python
print("Even code blocks!")
```

</details>

## Keyboard Shortcuts

Use HTML `<kbd>` tags for keyboard shortcuts:

- Save: <kbd>Ctrl</kbd> + <kbd>S</kbd> (Windows/Linux) or <kbd>Cmd</kbd> + <kbd>S</kbd> (Mac)
- Copy: <kbd>Ctrl</kbd> + <kbd>C</kbd>
- Paste: <kbd>Ctrl</kbd> + <kbd>V</kbd>
- Toggle Dark Mode: Click the 🌙/☀️ button in top-right

## Emojis

MD2HTML5 supports emojis: 🎉 🚀 💻 📱 ✨ ⚡ 🔥 💡 📝 ✅ ❌ ⚠️ 📊 🎨 🔧

## Special Features

### Accessibility

- ♿ **Keyboard Navigation**: Tab through interactive elements
- 👀 **Screen Reader Friendly**: Semantic HTML with ARIA labels
- 🎯 **Focus Indicators**: Clear focus states on all interactive elements
- ⏭️ **Skip to Content**: Press Tab on page load to skip to main content

### Responsive Design

- 💻 **Desktop**: Optimized for large screens (900px max-width)
- 📱 **Tablet**: Adjusted layout for medium screens (≤768px)
- 📲 **Mobile**: Full optimization for small screens (≤480px)
- 👆 **Touch-Friendly**: 44px minimum touch targets on touch devices

### Dark Mode

Try clicking the theme toggle button in the top-right corner!

Features:
- 🌙 Automatic system preference detection
- 💾 Saves your preference to localStorage
- 🎨 Smooth transitions between themes
- 🔄 Keyboard accessible (Tab + Enter)

### Copy Code Buttons

Hover over any code block to see the copy button with tooltip. Click to copy the entire code block to your clipboard!

## Tips and Tricks

1. **Deep Linking**: Share direct links to sections using heading anchors
2. **Print Output**: Press Ctrl+P / Cmd+P for a clean, print-optimized version
3. **Custom Styling**: Use the `-c` option to provide your own CSS
4. **Batch Convert**: Use shell scripts to convert multiple files at once
5. **Math Mode**: Only includes MathJax if your document contains math notation

## Conclusion

This example demonstrates all the major features of MD2HTML5:

✅ Beautiful typography and spacing
✅ Syntax highlighting for code
✅ Responsive tables with enhancements
✅ Mathematical notation support
✅ Dark mode with toggle
✅ Accessibility features
✅ Mobile-responsive design
✅ Print-optimized output
✅ Interactive elements (copy buttons, anchor links)
✅ And much more!

Try converting this file with:

```bash
python md2html.py -i example.md -o example.html
```

Then open `example.html` in your browser and explore all the features!

---

<div align="center" markdown="1">

**Made with 💜 using MD2HTML5**

[View on GitHub](https://github.com/skanga/md2html) | [Report Issue](https://github.com/skanga/md2html/issues)

</div>
