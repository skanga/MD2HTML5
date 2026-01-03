
import os
import argparse
import markdown
from typing import Optional
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def print_logo() -> None:
    """Display the MD2HTML logo and information banner."""
    logo = r"""
███╗   ███╗██████╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗██╗     ███████╗
████╗ ████║██╔══██╗╚════██╗██║  ██║╚══██╔══╝████╗ ████║██║     ██╔════╝
██╔████╔██║██║  ██║ █████╔╝███████║   ██║   ██╔████╔██║██║     ███████╗
██║╚██╔╝██║██║  ██║██╔═══╝ ██╔══██║   ██║   ██║╚██╔╝██║██║     ╚════██║
██║ ╚═╝ ██║██████╔╝███████╗██║  ██║   ██║   ██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚══════╝
    """
    print("--------------------------------------------------")
    print(logo)
    print("MD2HTML5 - Markdown to HTML Converter")
    print("Made with 💜 by Shiraz Kanga. Based on MD2HTML by Zigao Wang.")
    print("This project is licensed under MIT License.")
    print("GitHub Repo: https://github.com/skanga/md2html/")
    print("--------------------------------------------------")


def convert_md_to_html(md_text: str, light_mode: bool = True) -> str:
    """
    Convert Markdown text to HTML with syntax highlighting.

    Args:
        md_text: Markdown content to convert
        light_mode: Use light theme for syntax highlighting (default: True)

    Returns:
        HTML string with syntax highlighting and copy buttons

    Note:
        The output HTML is not sanitized. Only convert trusted markdown content
        as malicious HTML/JavaScript in the input will be preserved in output.
    """
    html = markdown.markdown(md_text,
                             extensions=['fenced_code', 'tables', 'toc', 'footnotes', 'attr_list', 'md_in_html'])
    soup = BeautifulSoup(html, 'lxml')

    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if not code:
            continue

        # Handle class attribute being either a list or string
        classes = code.get('class', [])
        if isinstance(classes, str):
            classes = [classes]

        language = 'text'
        for class_name in classes:
            if class_name.startswith('language-'):
                language = class_name.replace('language-', '')
                break

        try:
            lexer = get_lexer_by_name(language, stripall=True)
        except Exception:
            # Fallback to plain text if lexer not found
            lexer = get_lexer_by_name('text', stripall=True)

        formatter = HtmlFormatter(style='default' if light_mode else 'monokai', nowrap=True)
        # Use get_text() instead of .string to handle code blocks with children
        highlighted_code = highlight(code.get_text(), lexer, formatter)

        new_pre = soup.new_tag('pre')
        new_pre['class'] = ['highlight']
        new_code = soup.new_tag('code')
        if language:
            new_code['class'] = [f'language-{language}']
        # Wrap in <code><pre> to preserve whitespace/indentation when parsing
        # BeautifulSoup strips leading whitespace in fragments without this context
        fragment = BeautifulSoup(f'<code><pre>{highlighted_code}</pre></code>', 'html.parser')
        pre_tag = fragment.find('pre')
        # Use list() to avoid modifying collection during iteration (append moves elements)
        contents = list(pre_tag.contents) if pre_tag else []
        for child in contents:
            new_code.append(child)
        new_pre.append(new_code)

        copy_button_html = f'''
        <div class="code-header">
            <span class="language-label">{language}</span>
            <button class="copy-button" onclick="copyCode(this)">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
                    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path>
                    <path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
                </svg>
            </button>
        </div>
        '''

        pre.replace_with(new_pre)
        new_pre.insert_before(BeautifulSoup(copy_button_html, 'html.parser'))

    # Add lazy loading to images for performance
    for img in soup.find_all('img'):
        img['loading'] = 'lazy'
        # Add alt text if missing for accessibility
        if not img.get('alt'):
            img['alt'] = 'Image'

    return str(soup)


def load_css_file(css_path: str) -> str:
    """
    Load CSS content from a file.

    Args:
        css_path: Path to CSS file

    Returns:
        CSS content as string, or empty string if file not found
    """
    try:
        if os.path.isfile(css_path):
            with open(css_path, 'r', encoding='utf-8') as css_file:
                return css_file.read()
    except Exception as e:
        print(f"Warning: Could not read CSS file '{css_path}': {e}")
    return ""


def load_markdown_file(md_path: str) -> Optional[str]:
    """
    Load Markdown content from a file.

    Args:
        md_path: Path to Markdown file

    Returns:
        Markdown content as string, or None if file cannot be read
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as md_file:
            return md_file.read()
    except FileNotFoundError:
        print(f"Error: File '{md_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: Could not read file '{md_path}': {e}")
        return None


def add_custom_style(html_content: str, css_content: Optional[str] = None, light_mode: bool = True) -> str:
    """
    Create a complete, well-formed HTML5 document from converted markdown.

    Args:
        html_content: HTML body content from converted markdown
        css_content: Optional CSS string to include in style tag

    Returns:
        Complete HTML5 document with:
        - Proper DOCTYPE and structure (html, head, body)
        - Meta tags for charset and viewport
        - Embedded CSS styling
        - Copy button functionality for code blocks
        - MathJax for mathematical notation
    """
    # Build the complete HTML5 document
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '    <meta name="generator" content="MD2HTML">',
        '    <title>Converted Markdown</title>',
    ]

    # Generate BOTH light and dark Pygments CSS for dynamic theme switching
    # Light mode Pygments (default theme)
    pygments_light = HtmlFormatter(style='default').get_style_defs('.highlight')
    # Dark mode Pygments (monokai theme) - scope to [data-theme="dark"]
    pygments_dark_raw = HtmlFormatter(style='monokai').get_style_defs('.highlight')
    # Wrap dark mode Pygments CSS in [data-theme="dark"] selector
    pygments_dark = '\n'.join(
        f'[data-theme="dark"] {line}' if line.strip() and not line.strip().startswith('/*') else line
        for line in pygments_dark_raw.split('\n')
    )

    combined_css = f"{pygments_light}\n\n/* Dark mode syntax highlighting */\n{pygments_dark}"
    if css_content:
        combined_css = f"{combined_css}\n{css_content}"

    # Add CSS if provided
    if combined_css:
        html_parts.extend([
            '    <style>',
            combined_css,
            '    </style>',
        ])

    # Add comprehensive JavaScript in head
    html_parts.extend([
        '    <script>',
        '        // Copy code functionality',
        '        function copyCode(button) {',
        '            const header = button.closest(\'.code-header\');',
        '            let pre = header ? header.nextElementSibling : null;',
        '            if (!pre || pre.tagName !== \'PRE\') {',
        '                pre = header ? header.parentElement.querySelector(\'pre\') : null;',
        '            }',
        '            const code = pre ? pre.innerText : \'\';',
        '            navigator.clipboard.writeText(code).then(() => {',
        '                button.innerHTML = \'<svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check"><path fill-rule="evenodd" d="M13.78 3.22a.75.75 0 0 1 0 1.06l-7.5 7.5a.75.75 0 0 1-1.06 0l-3.5-3.5a.75.75 0 0 1 1.06-1.06L6 10.44l7.22-7.22a.75.75 0 0 1 1.06 0z"></path></svg>\';',
        '                setTimeout(() => {',
        '                    button.innerHTML = \'<svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>\';',
        '                }, 2000);',
        '            });',
        '        }',
        '',
        '        // Dark mode toggle functionality',
        '        function toggleTheme() {',
        '            const root = document.documentElement;',
        '            const currentTheme = root.getAttribute(\'data-theme\');',
        '            const newTheme = currentTheme === \'dark\' ? \'light\' : \'dark\';',
        '            root.setAttribute(\'data-theme\', newTheme);',
        '            localStorage.setItem(\'theme\', newTheme);',
        '        }',
        '',
        '        // Initialize theme from localStorage or system preference',
        '        function initTheme() {',
        '            const savedTheme = localStorage.getItem(\'theme\');',
        '            if (savedTheme) {',
        '                document.documentElement.setAttribute(\'data-theme\', savedTheme);',
        '            } else if (window.matchMedia && window.matchMedia(\'(prefers-color-scheme: dark)\').matches) {',
        '                document.documentElement.setAttribute(\'data-theme\', \'dark\');',
        '            }',
        '        }',
        '',
        '        // Add heading anchor links',
        '        function addHeadingAnchors() {',
        '            const headings = document.querySelectorAll(\'h1, h2, h3, h4, h5, h6\');',
        '            const usedIds = new Map();',
        '            headings.forEach(heading => {',
        '                let baseId = heading.id;',
        '                if (!baseId) {',
        '                    baseId = heading.textContent.toLowerCase().replace(/[^a-z0-9]+/g, \'-\').replace(/^-+|-+$/g, \'\');',
        '                }',
        '                if (!baseId) {',
        '                    baseId = \'heading\';',
        '                }',
        '                const count = usedIds.get(baseId) || 0;',
        '                usedIds.set(baseId, count + 1);',
        '                const uniqueId = count === 0 ? baseId : baseId + \'-\' + count;',
        '                heading.id = uniqueId;',
        '                const anchor = document.createElement(\'a\');',
        '                anchor.className = \'heading-anchor\';',
        '                anchor.href = \'#\' + heading.id;',
        '                anchor.innerHTML = \'#\';',
        '                anchor.setAttribute(\'aria-label\', \'Link to this heading\');',
        '                heading.appendChild(anchor);',
        '            });',
        '        }',
        '',
        '        // Conditionally load MathJax if math content detected',
        '        function loadMathJaxIfNeeded() {',
        '            const hasMath = document.body.innerHTML.match(/\\$\\$|\\\\\\[|\\\\\\(/);',
        '            if (hasMath) {',
        '                const script = document.createElement(\'script\');',
        '                script.src = \'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\';',
        '                script.async = true;',
        '                document.head.appendChild(script);',
        '            }',
        '        }',
        '',
        '        // Initialize on DOM ready',
        '        document.addEventListener(\'DOMContentLoaded\', function() {',
        '            initTheme();',
        '            addHeadingAnchors();',
        '            loadMathJaxIfNeeded();',
        '        });',
        '    </script>',
        '</head>',
        '<body>',
        '    <!-- Skip to content link for accessibility -->',
        '    <a href="#main-content" class="skip-to-content">Skip to content</a>',
        '',
        '    <!-- Dark mode toggle button -->',
        '    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode">',
        '        <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">',
        '            <path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.415-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"/>',
        '        </svg>',
        '        <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">',
        '            <path d="M10 7a7 7 0 0 0 12 4.9v.1c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2h.1A6.977 6.977 0 0 0 10 7zm-6 5a8 8 0 0 0 15.062 3.762A9 9 0 0 1 8.238 4.938 7.999 7.999 0 0 0 4 12z"/>',
        '        </svg>',
        '    </button>',
        '',
        '    <!-- Main content wrapper -->',
        '    <main id="main-content">',
    ])

    # Add the converted markdown content without altering whitespace,
    # so code blocks preserve spaces and newlines.
    soup = BeautifulSoup(html_content, 'lxml')
    body_content = soup.find('body')
    if body_content:
        html_parts.append(body_content.decode_contents())
    else:
        html_parts.append(html_content)

    # Close main content wrapper and body
    html_parts.extend([
        '    </main>',
        '</body>',
        '</html>',
    ])

    return '\n'.join(html_parts)


def prompt_based_conversion() -> None:
    """
    Interactive prompt-based conversion mode.

    Prompts user for input file, mode selection, and output file name,
    then converts Markdown to HTML.
    """
    while True:
        md_file_path = input("Enter the path to your Markdown file (or 'q' to quit): ").strip()
        if md_file_path.lower() == 'q':
            print("Goodbye!")
            break

        md_text = load_markdown_file(md_file_path)
        if md_text is None:
            print("Please check the path and try again.")
            continue

        light_mode = input("Choose mode (light/dark, default is light): ").strip().lower() != 'dark'
        css_path = 'style_light.css' if light_mode else 'style_dark.css'
        css_content = load_css_file(css_path)

        html = convert_md_to_html(md_text, light_mode=light_mode)
        styled_html = add_custom_style(html, css_content, light_mode=light_mode)

        output_file = input("Enter the name of the output HTML file (default: output.html): ").strip() or 'output.html'
        try:
            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(styled_html)
            print(f"Markdown converted to HTML successfully! Output saved to {output_file}")
        except Exception as e:
            print(f"Error writing output file: {e}")
        break


def arg_based_conversion(args) -> None:
    """
    Command-line argument based conversion mode.

    Args:
        args: Parsed command-line arguments containing:
            - input_file: Path to input Markdown file
            - output_file: Name of output HTML file
            - output_dir: Directory for output file
            - css_file: Optional custom CSS file path
            - mode: 'light' or 'dark' theme mode
    """
    md_text = load_markdown_file(args.input_file)
    if md_text is None:
        return

    light_mode = args.mode.lower() != 'dark'

    # Determine CSS content priority:
    # 1. Custom CSS file from --css_file argument (highest priority)
    # 2. Default style_light.css or style_dark.css if they exist
    # 3. Hardcoded CSS as fallback (lowest priority)
    css_content = """
/* CSS Variables for theming */
:root {
    --bg-primary: #ffffff;
    --bg-secondary: #f9f9f9;
    --bg-tertiary: #f4f4f4;
    --text-primary: #333333;
    --text-secondary: #666666;
    --text-tertiary: #777777;
    --border-color: #eaeaea;
    --border-accent: #007aff;
    --link-color: #007aff;
    --code-bg: #f4f4f4;
    --code-text: #333333;
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
    --transition-speed: 0.2s;
}

[data-theme="dark"] {
    --bg-primary: #1a1a1a;
    --bg-secondary: #222222;
    --bg-tertiary: #2d2d2d;
    --text-primary: #e0e0e0;
    --text-secondary: #b0b0b0;
    --text-tertiary: #888888;
    --border-color: #404040;
    --border-accent: #4a9eff;
    --link-color: #4a9eff;
    --code-bg: #2d2d2d;
    --code-text: #e0e0e0;
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.3);
}

/* Auto dark mode based on system preference */
@media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
        --bg-primary: #1a1a1a;
        --bg-secondary: #222222;
        --bg-tertiary: #2d2d2d;
        --text-primary: #e0e0e0;
        --text-secondary: #b0b0b0;
        --text-tertiary: #888888;
        --border-color: #404040;
        --border-accent: #4a9eff;
        --link-color: #4a9eff;
        --code-bg: #2d2d2d;
        --code-text: #e0e0e0;
        --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
    line-height: 1.7;
    margin: 0 auto;
    max-width: 900px;
    padding: 40px 20px;
    color: var(--text-primary);
    background-color: var(--bg-primary);
    transition: background-color var(--transition-speed), color var(--transition-speed);
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Typography - Headings with improved spacing */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary);
    font-weight: 600;
    line-height: 1.3;
    margin-top: 2em;
    margin-bottom: 0.5em;
    position: relative;
}

h1 {
    font-size: 2.5em;
    margin-top: 0;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.3em;
}

h2 {
    font-size: 2em;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 0.3em;
}

h3 {
    font-size: 1.5em;
}

h4 {
    font-size: 1.25em;
}

/* Heading anchor links */
h1:hover .heading-anchor,
h2:hover .heading-anchor,
h3:hover .heading-anchor,
h4:hover .heading-anchor,
h5:hover .heading-anchor,
h6:hover .heading-anchor {
    opacity: 1;
}

.heading-anchor {
    opacity: 0;
    margin-left: 0.5em;
    font-size: 0.8em;
    color: var(--text-tertiary);
    text-decoration: none;
    transition: opacity var(--transition-speed);
}

.heading-anchor:hover {
    color: var(--link-color);
}

/* Paragraph spacing */
p {
    margin: 1em 0;
}

/* Enhanced code blocks */
pre {
    background: var(--code-bg);
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    position: relative;
    color: var(--code-text);
    margin: 1.5em 0;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
    transition: box-shadow var(--transition-speed), transform var(--transition-speed);
}

pre:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}

/* Inline code */
code {
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Consolas', monospace;
    font-size: 0.9em;
    color: var(--code-text);
    border: 1px solid var(--border-color);
}

/* Code blocks - remove inline code styling when inside pre */
pre code {
    background: none;
    padding: 0;
    border: none;
    font-size: 0.875em;
}

/* Links */
a {
    color: var(--link-color);
    text-decoration: none;
    transition: color var(--transition-speed), text-decoration var(--transition-speed);
    border-bottom: 1px solid transparent;
}

a:hover {
    border-bottom-color: var(--link-color);
}

a:focus {
    outline: 2px solid var(--link-color);
    outline-offset: 2px;
    border-radius: 2px;
}

/* External links indicator */
a[href^="http"]:not([href*="localhost"])::after {
    content: "↗";
    font-size: 0.8em;
    margin-left: 0.2em;
    opacity: 0.6;
}

/* Lists */
ul, ol {
    padding-left: 2em;
    margin: 1em 0;
}

li {
    margin: 0.5em 0;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid var(--border-accent);
    padding: 1em 1.5em;
    margin: 1.5em 0;
    background: var(--bg-secondary);
    color: var(--text-secondary);
    border-radius: 0 4px 4px 0;
    font-style: italic;
}

blockquote p:first-child {
    margin-top: 0;
}

blockquote p:last-child {
    margin-bottom: 0;
}

/* Copy button improvements */
.copy-button {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    cursor: pointer;
    padding: 4px 8px;
    transition: all var(--transition-speed);
    position: relative;
    color: var(--text-primary);
}

.copy-button:hover {
    background: var(--border-accent);
    border-color: var(--border-accent);
    transform: scale(1.05);
}

.copy-button:hover::after {
    content: "Copy code";
    position: absolute;
    right: 100%;
    top: 50%;
    transform: translateY(-50%);
    background: var(--text-primary);
    color: var(--bg-primary);
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    margin-right: 8px;
    pointer-events: none;
}

.copy-button:focus {
    outline: 2px solid var(--border-accent);
    outline-offset: 2px;
}

.copy-button svg {
    display: block;
    fill: currentColor;
}

/* Code header */
.code-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-tertiary);
    padding: 8px 12px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    border: 1px solid var(--border-color);
    border-bottom: none;
}

.code-header + pre {
    margin-top: 0;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}

.language-label {
    font-weight: 600;
    font-size: 0.85em;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Images */
img {
    display: block;
    margin: 2em auto;
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: var(--shadow-md);
    transition: transform var(--transition-speed), box-shadow var(--transition-speed);
}

img:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

img[loading="lazy"] {
    background: var(--bg-secondary);
}

figcaption {
    text-align: center;
    font-size: 0.9em;
    color: var(--text-secondary);
    font-style: italic;
    margin-top: 0.5em;
}

/* Syntax highlighting adjustments */
code[class*="language-"], pre[class*="language-"] {
    color: var(--code-text);
    background: none;
    font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Consolas', monospace;
    font-size: 0.875em;
    text-align: left;
    white-space: pre;
    word-spacing: normal;
    word-break: normal;
    word-wrap: normal;
    line-height: 1.6;
    tab-size: 4;
    hyphens: none;
}

/* Enhanced tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 2em 0;
    box-shadow: var(--shadow-sm);
    border-radius: 8px;
    overflow: hidden;
}

thead {
    position: sticky;
    top: 0;
    z-index: 10;
}

th, td {
    border: 1px solid var(--border-color);
    padding: 12px 16px;
    text-align: left;
}

th {
    background-color: var(--bg-tertiary);
    font-weight: 600;
    color: var(--text-primary);
    text-transform: uppercase;
    font-size: 0.85em;
    letter-spacing: 0.5px;
}

/* Zebra striping */
tbody tr:nth-child(even) {
    background-color: var(--bg-secondary);
}

tbody tr {
    transition: background-color var(--transition-speed);
}

tbody tr:hover {
    background-color: var(--bg-tertiary);
}

/* Responsive tables on mobile */
@media (max-width: 768px) {
    table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }
}

/* ============================================
   MOBILE RESPONSIVENESS
   ============================================ */

/* Mobile: Reduce body padding */
@media (max-width: 768px) {
    body {
        padding: 20px 16px;
        max-width: 100%;
    }

    /* Responsive typography - smaller on mobile */
    h1 {
        font-size: 2em;
    }

    h2 {
        font-size: 1.75em;
    }

    h3 {
        font-size: 1.35em;
    }

    h4 {
        font-size: 1.15em;
    }

    /* Reduce heading margins on mobile */
    h1, h2, h3, h4, h5, h6 {
        margin-top: 1.5em;
    }

    /* Better code block handling */
    pre {
        padding: 12px;
        font-size: 0.85em;
        margin: 1em -16px; /* Bleed to edges */
        border-radius: 0;
        border-left: none;
        border-right: none;
    }

    .code-header {
        margin: 1em -16px 0; /* Align with pre */
        border-radius: 0;
        border-left: none;
        border-right: none;
        padding: 6px 16px;
    }

    /* Inline code adjustments */
    code {
        font-size: 0.85em;
        word-break: break-word;
    }

    /* Images - full width on mobile */
    img {
        margin: 1.5em -16px;
        border-radius: 0;
        max-width: calc(100% + 32px);
        width: calc(100% + 32px);
    }

    /* Blockquotes */
    blockquote {
        margin: 1em -8px;
        padding: 1em 1em;
        font-size: 0.95em;
    }

    /* Lists - less padding */
    ul, ol {
        padding-left: 1.5em;
    }

    /* Tables on mobile already handled above */
}

/* Small mobile devices (phones in portrait) */
@media (max-width: 480px) {
    body {
        padding: 16px 12px;
        font-size: 16px; /* Prevent iOS zoom on inputs */
        line-height: 1.6;
    }

    h1 {
        font-size: 1.75em;
    }

    h2 {
        font-size: 1.5em;
    }

    h3 {
        font-size: 1.25em;
    }

    /* Even smaller code on tiny screens */
    pre {
        font-size: 0.8em;
        padding: 10px;
        margin: 1em -12px;
    }

    .code-header {
        margin: 1em -12px 0;
        padding: 6px 12px;
        font-size: 0.8em;
    }

    /* Adjust copy button size */
    .copy-button {
        padding: 6px 10px;
    }

    .copy-button svg {
        width: 14px;
        height: 14px;
    }

    /* Hide copy button tooltip on small screens */
    .copy-button:hover::after {
        display: none;
    }

    /* Images */
    img {
        margin: 1em -12px;
        max-width: calc(100% + 24px);
        width: calc(100% + 24px);
    }

    /* Blockquotes */
    blockquote {
        margin: 1em -6px;
        padding: 0.75em 1em;
    }
}

/* Touch-friendly interactive elements */
@media (hover: none) and (pointer: coarse) {
    /* Increase touch targets */
    .copy-button {
        min-width: 44px;
        min-height: 44px;
        padding: 8px 12px;
    }

    a {
        padding: 2px 0;
    }

    .heading-anchor {
        padding: 4px;
    }

    /* Remove hover effects on touch devices */
    pre:hover {
        transform: none;
    }

    img:hover {
        transform: none;
    }

    /* Make external link indicator always visible on mobile */
    a[href^="http"]:not([href*="localhost"])::after {
        opacity: 1;
    }
}

/* Dark mode toggle button */
.theme-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: 50%;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: var(--shadow-md);
    transition: all var(--transition-speed);
    z-index: 1000;
    color: var(--text-primary);
}

.theme-toggle:hover {
    transform: scale(1.1) rotate(20deg);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.theme-toggle:focus {
    outline: 2px solid var(--border-accent);
    outline-offset: 2px;
}

.theme-toggle svg {
    width: 24px;
    height: 24px;
    fill: currentColor;
}

/* Hide sun icon in light mode, moon in dark mode */
[data-theme="dark"] .theme-toggle .sun-icon,
:root:not([data-theme="dark"]) .theme-toggle .moon-icon {
    display: none;
}

/* Mobile adjustments for theme toggle */
@media (max-width: 768px) {
    .theme-toggle {
        top: 16px;
        right: 16px;
        width: 44px;
        height: 44px;
    }

    .theme-toggle svg {
        width: 20px;
        height: 20px;
    }
}

@media (max-width: 480px) {
    .theme-toggle {
        top: 12px;
        right: 12px;
        width: 40px;
        height: 40px;
    }

    .theme-toggle svg {
        width: 18px;
        height: 18px;
    }

    /* Disable rotation animation on very small screens */
    .theme-toggle:hover {
        transform: scale(1.05);
    }
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 2px solid var(--border-color);
    margin: 3em 0;
}

/* Selection color */
::selection {
    background-color: var(--border-accent);
    color: var(--bg-primary);
}

/* Focus visible for accessibility */
*:focus-visible {
    outline: 2px solid var(--border-accent);
    outline-offset: 2px;
}

/* Skip to content link for accessibility */
.skip-to-content {
    position: absolute;
    top: -40px;
    left: 0;
    background: var(--border-accent);
    color: var(--bg-primary);
    padding: 8px 16px;
    text-decoration: none;
    border-radius: 0 0 4px 0;
    z-index: 100;
    transition: top var(--transition-speed);
}

.skip-to-content:focus {
    top: 0;
}

/* Print styles */
@media print {
    body {
        background: white;
        color: black;
        max-width: 100%;
        padding: 20px;
        font-size: 12pt;
    }

    .theme-toggle {
        display: none;
    }

    .copy-button {
        display: none;
    }

    .heading-anchor {
        display: none;
    }

    .skip-to-content {
        display: none;
    }

    a {
        color: black;
        text-decoration: underline;
    }

    a[href^="http"]::after {
        content: " (" attr(href) ")";
        font-size: 0.8em;
        word-wrap: break-word;
    }

    pre, blockquote {
        page-break-inside: avoid;
        border: 1px solid #ccc;
        background: #f9f9f9;
        padding: 10px;
    }

    .code-header {
        background: #e9e9e9;
        border: 1px solid #ccc;
        padding: 5px 10px;
    }

    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
        page-break-inside: avoid;
    }

    img {
        max-width: 100%;
        page-break-inside: avoid;
        box-shadow: none;
    }

    table {
        border-collapse: collapse;
        page-break-inside: avoid;
    }

    th, td {
        border: 1px solid #333;
    }

    /* Remove shadows and transitions for print */
    * {
        box-shadow: none !important;
        text-shadow: none !important;
        transition: none !important;
    }
}
"""

    # Load CSS with priority: custom CSS file > default CSS file > hardcoded CSS
    if args.css_file:
        custom_css = load_css_file(args.css_file)
        if custom_css:
            css_content = custom_css
            print(f"Using custom CSS from: {args.css_file}")
    else:
        css_path = 'style_light.css' if light_mode else 'style_dark.css'
        default_css = load_css_file(css_path)
        if default_css:
            css_content = default_css
            print(f"Using CSS from: {css_path}")
        else:
            print("Using built-in CSS")

    html = convert_md_to_html(md_text, light_mode=light_mode)
    styled_html = add_custom_style(html, css_content, light_mode=light_mode)

    output_path = os.path.join(args.output_dir, args.output_file)
    try:
        with open(output_path, 'w', encoding='utf-8') as html_file:
            html_file.write(styled_html)
        print(f"Markdown converted to HTML successfully! Output saved to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")


def main() -> None:
    """
    Main entry point for the MD2HTML converter.

    Parses command-line arguments and routes to either argument-based
    or interactive prompt-based conversion mode.
    """
    print_logo()

    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML.")
    parser.add_argument("-i", "--input_file", help="Path to the input Markdown file.")
    parser.add_argument("-o", "--output_file", default="output.html", help="Name of the output HTML file.")
    parser.add_argument("-d", "--output_dir", default=".", help="Directory where the output HTML file will be saved.")
    parser.add_argument("-c", "--css_file", help="Path to a custom CSS file.")
    parser.add_argument("-m", "--mode", default="light", help="Choose mode (light/dark). Default is light.")

    args = parser.parse_args()

    if args.input_file:
        arg_based_conversion(args)
    else:
        prompt_based_conversion()


if __name__ == "__main__":
    main()
