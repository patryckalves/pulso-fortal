#!/usr/bin/env python3
"""Convert relatorio-final.md to PDF with proper styling."""
import markdown
from weasyprint import HTML
import os

INPUT = "/opt/data/pulso-fortal/docs/relatorio-final.md"
OUTPUT = "/opt/data/pulso-fortal/docs/relatorio-final.pdf"

# Read markdown
with open(INPUT) as f:
    md_content = f.read()

# Custom CSS for academic paper styling
css = """
@page {
    size: A4;
    margin: 2cm 2.5cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
}

h1 {
    font-size: 20pt;
    font-weight: 700;
    margin-top: 24pt;
    margin-bottom: 12pt;
    page-break-before: always;
    color: #1a1a1a;
    border-bottom: 2px solid #e8650a;
    padding-bottom: 6pt;
}

h1:first-of-type {
    page-break-before: avoid;
}

h2 {
    font-size: 14pt;
    font-weight: 600;
    margin-top: 18pt;
    margin-bottom: 8pt;
    color: #1a1a1a;
}

h3 {
    font-size: 12pt;
    font-weight: 600;
    margin-top: 14pt;
    margin-bottom: 6pt;
    color: #333;
}

p {
    margin: 6pt 0;
    text-align: justify;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10pt 0;
    font-size: 9pt;
}

th {
    background: #f3f1ed;
    padding: 6pt 8pt;
    text-align: left;
    font-weight: 600;
    border-bottom: 2px solid #e5e2db;
}

td {
    padding: 4pt 8pt;
    border-bottom: 1px solid #f0ede8;
}

code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt;
    background: #f3f1ed;
    padding: 1pt 4pt;
    border-radius: 3pt;
}

pre {
    background: #f3f1ed;
    padding: 8pt;
    border-radius: 4pt;
    font-size: 8pt;
    overflow-x: auto;
}

pre code {
    background: none;
    padding: 0;
}

blockquote {
    border-left: 3px solid #e8650a;
    padding: 6pt 12pt;
    margin: 10pt 0;
    background: #fef3e8;
    font-style: italic;
}

strong {
    font-weight: 600;
    color: #1a1a1a;
}

ul, ol {
    margin: 6pt 0;
    padding-left: 20pt;
}

li {
    margin: 2pt 0;
}

hr {
    border: none;
    border-top: 1px solid #e5e2db;
    margin: 16pt 0;
}

img {
    max-width: 100%;
    margin: 10pt 0;
    border: 1px solid #e5e2db;
    border-radius: 4pt;
}

a {
    color: #e8650a;
    text-decoration: none;
}
"""

# Convert to HTML then PDF
md_extensions = ['tables', 'fenced_code', 'codehilite', 'nl2br']
html_body = markdown.markdown(md_content, extensions=md_extensions)

# Wrap in full HTML with Google Fonts
full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>"""

# Generate PDF — base_url so relative image paths resolve
base_url = os.path.dirname(INPUT)
HTML(string=full_html, base_url=base_url).write_pdf(OUTPUT)
print(f"✅ PDF generated: {OUTPUT}")
print(f"   Size: {os.path.getsize(OUTPUT) / 1024:.1f} KB")
