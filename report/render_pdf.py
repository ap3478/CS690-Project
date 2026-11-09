"""Render report/REPORT.md to report/CS690_M1_Report.pdf.

Needs: pip install markdown==3.7 weasyprint==63.1  (not part of requirements.txt;
only used to produce the submission PDF).
"""
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
md = (ROOT / "REPORT.md").read_text(encoding="utf-8")
body = markdown.markdown(md, extensions=["tables", "fenced_code", "attr_list", "toc"])

css = """
@page { size: Letter; margin: 0.7in 0.6in; @bottom-center { content: counter(page); font-size: 9pt; color: #555; } }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 9.5pt; line-height: 1.35; color: #111; }
h1 { font-size: 17pt; } h2 { font-size: 14pt; page-break-before: always; border-bottom: 1px solid #999; }
h2#toc { page-break-before: avoid; }
h3 { font-size: 11.5pt; margin-top: 1.2em; } h4 { font-size: 10.5pt; } h5 { font-size: 10pt; }
table { border-collapse: collapse; width: 100%; margin: 0.5em 0; font-size: 8.5pt; }
th, td { border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; text-align: left; }
th { background: #eee; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.3pt; }
td code { overflow-wrap: anywhere; }
pre { background: #f5f5f5; padding: 6px; white-space: pre-wrap; font-size: 7.8pt; }
blockquote { border-left: 3px solid #c90; margin-left: 0; padding-left: 8px; color: #333; }
a { color: #0645ad; text-decoration: none; }
a.pageref::after { content: target-counter(attr(href), page); }
"""
html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
out = ROOT / "CS690_M1_Report.pdf"
HTML(string=html).write_pdf(out)
print(f"wrote {out}")
