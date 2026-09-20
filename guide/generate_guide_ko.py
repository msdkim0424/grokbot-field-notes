# -*- coding: utf-8 -*-
import os
import subprocess
import fitz

from pages_part1 import (
    render_page_01, render_page_02, render_page_03, render_page_04,
    render_page_05, render_page_06, render_page_07, render_page_08
)
from pages_part2 import (
    render_page_09, render_page_10, render_page_11, render_page_12,
    render_page_13, render_page_14, render_page_15, render_page_16
)
from pages_part3 import (
    render_page_17, render_page_18, render_page_19, render_page_20,
    render_page_21, render_page_22, render_page_23, render_page_24
)

HTML_HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>SpaceX 엔지니어들의 Grok Bot 가이드</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800;900&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Inter', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', sans-serif;
    color: #111111;
    background: #ffffff;
    word-break: keep-all;
    overflow-wrap: break-word;
    -webkit-font-smoothing: antialiased;
  }
  .page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    padding: 12.5mm 14mm 10.5mm 14mm;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    background: #ffffff;
  }
  .page.cover {
    padding: 0;
    background: #fefdfc;
    position: relative;
    display: flex;
    flex-direction: column;
  }
  .cover-header {
    padding: 22mm 18mm 0 18mm;
    z-index: 2;
  }
  .cover-title {
    font-family: 'Poppins', 'Noto Sans KR', sans-serif;
    font-size: 38pt;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -1.5px;
    margin: 0 0 12pt 0;
    color: #0d0d0d;
  }
  .cover-sub {
    font-size: 16pt;
    font-weight: 600;
    color: #222222;
    margin: 0;
    letter-spacing: -0.3px;
  }
  .cover-image-container {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 210mm;
    height: auto;
    z-index: 1;
  }
  .cover-image {
    width: 100%;
    display: block;
  }

  /* Universal Header */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 7pt;
    border-bottom: 1px solid #e6e4e1;
    margin-bottom: 12pt;
  }
  .header-left {
    display: flex;
    align-items: center;
    gap: 6pt;
    font-size: 7.4pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #111111;
  }
  .dot {
    width: 6.5px;
    height: 6.5px;
    background-color: #e4402e;
    border-radius: 50%;
    display: inline-block;
  }
  .header-right {
    font-size: 7.4pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #a9a7a4;
  }

  /* Universal Headings */
  .eyebrow {
    font-size: 7.6pt;
    font-weight: 700;
    color: #e4402e;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 4pt;
  }
  .page-title {
    font-family: 'Poppins', 'Noto Sans KR', sans-serif;
    font-size: 22pt;
    font-weight: 700;
    line-height: 1.2;
    color: #111111;
    letter-spacing: -0.5px;
    margin: 0 0 7pt 0;
  }
  .page-intro {
    font-size: 9.1pt;
    line-height: 1.5;
    color: #4a4a4a;
    margin: 0 0 11pt 0;
  }
  .page-intro strong {
    color: #111111;
    font-weight: 700;
  }

  .section-label {
    font-size: 7.8pt;
    font-weight: 700;
    color: #e4402e;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin: 9pt 0 6pt 0;
  }
  .section-label.dark {
    color: #111111;
  }

  /* Cards & Grids */
  .grid-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10pt;
    margin-bottom: 9pt;
  }
  .grid-3col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9pt;
    margin-bottom: 9pt;
  }
  .grid-4col {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8pt;
    margin-bottom: 9pt;
  }

  .card {
    background: #f4f3f1;
    border-radius: 9px;
    padding: 9pt 11pt;
  }
  .card-title {
    font-size: 9.3pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 4pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }
  .card-subtitle {
    font-size: 7.8pt;
    font-weight: 600;
    color: #777777;
    margin-top: -2pt;
    margin-bottom: 4pt;
  }
  .card-body {
    font-size: 8.1pt;
    line-height: 1.45;
    color: #3a3a3a;
  }
  .card-body strong {
    color: #111111;
    font-weight: 700;
  }
  .card-body p {
    margin: 0 0 4pt 0;
  }
  .card-body p:last-child {
    margin-bottom: 0;
  }

  /* Stat Card */
  .stat-card {
    background: #f4f3f1;
    border-radius: 9px;
    padding: 8.5pt 10.5pt;
  }
  .stat-val {
    font-family: 'Poppins', sans-serif;
    font-size: 19pt;
    font-weight: 800;
    color: #111111;
    line-height: 1.1;
    margin-bottom: 2pt;
  }
  .stat-desc {
    font-size: 7.5pt;
    line-height: 1.35;
    color: #555555;
  }

  /* Numbered List Items */
  .num-item {
    display: flex;
    align-items: flex-start;
    gap: 8pt;
    padding: 6.5pt 0;
    border-bottom: 1px solid #e6e4e1;
  }
  .num-item:last-child {
    border-bottom: none;
  }
  .num-badge {
    background: #111111;
    color: #ffffff;
    font-size: 7.4pt;
    font-weight: 700;
    width: 17px;
    height: 17px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1.5pt;
  }
  .num-content {
    font-size: 8.2pt;
    line-height: 1.45;
    color: #3a3a3a;
    flex: 1;
  }
  .num-content strong {
    color: #111111;
    font-weight: 700;
  }

  /* Callout Banners */
  .callout {
    background: #faf2f0;
    border-left: 3.5px solid #e4402e;
    border-radius: 7px;
    padding: 8.5pt 12pt;
    margin-top: auto;
    margin-bottom: 5pt;
    display: flex;
    gap: 8pt;
  }
  .callout-icon {
    width: 19px;
    height: 19px;
    background: #f6dcd6;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8.5pt;
    flex-shrink: 0;
    margin-top: 1pt;
  }
  .callout-body {
    flex: 1;
  }
  .callout-title {
    font-size: 8.7pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 2pt;
  }
  .callout-text {
    font-size: 7.9pt;
    line-height: 1.44;
    color: #3a3a3a;
    margin: 0;
  }
  .callout-text strong {
    color: #111111;
    font-weight: 700;
  }

  /* Quote Box */
  .quote-box {
    border-left: 3.5px solid #e4402e;
    padding-left: 11pt;
    margin: 7pt 0 9pt 0;
  }
  .quote-text {
    font-family: 'Poppins', 'Noto Sans KR', sans-serif;
    font-size: 11pt;
    font-weight: 700;
    line-height: 1.35;
    color: #111111;
    margin: 0 0 3pt 0;
  }
  .quote-author {
    font-size: 7.6pt;
    font-weight: 500;
    color: #777777;
    margin: 0;
  }

  /* Prompt Cards */
  .prompt-card {
    background: #f4f3f1;
    border-left: 3px solid #e4402e;
    border-radius: 6px;
    padding: 7pt 9.5pt;
    margin-bottom: 7pt;
  }
  .prompt-label {
    font-size: 7.3pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #e4402e;
    text-transform: uppercase;
    margin-bottom: 2.5pt;
  }
  .prompt-content {
    font-size: 8pt;
    line-height: 1.42;
    color: #111111;
    font-style: normal;
    margin-bottom: 2.5pt;
  }
  .prompt-meta {
    font-size: 7.3pt;
    color: #777777;
    line-height: 1.35;
  }

  /* Footnote */
  .footnote {
    font-size: 7.1pt;
    line-height: 1.35;
    color: #7e7e79;
    margin-bottom: 5pt;
  }

  /* Universal Footer */
  .footer {
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 5pt;
    font-size: 7.1pt;
    font-weight: 500;
    color: #b3b1ae;
    border-top: 1px solid #f2f0ed;
  }

  /* TOC Item */
  .toc-list {
    display: flex;
    flex-direction: column;
    gap: 0;
  }
  .toc-item {
    display: flex;
    align-items: baseline;
    padding: 5pt 0;
    border-bottom: 1px solid #f0eeeb;
    gap: 12pt;
  }
  .toc-num {
    font-size: 8.6pt;
    font-weight: 700;
    color: #888888;
    width: 20pt;
    flex-shrink: 0;
  }
  .toc-title {
    font-size: 8.6pt;
    font-weight: 700;
    color: #111111;
    width: 140pt;
    flex-shrink: 0;
  }
  .toc-desc {
    font-size: 7.7pt;
    color: #666666;
    flex: 1;
  }

  /* Bullet points */
  ul.custom-bullets {
    margin: 0;
    padding-left: 12pt;
  }
  ul.custom-bullets li {
    font-size: 8pt;
    line-height: 1.44;
    color: #3a3a3a;
    margin-bottom: 3.5pt;
  }
  ul.custom-bullets li:last-child {
    margin-bottom: 0;
  }
  ul.custom-bullets li strong {
    color: #111111;
  }

  /* Flow chart */
  .flow-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6pt;
    background: #f4f3f1;
    border-radius: 8px;
    padding: 7.5pt 11pt;
    margin-bottom: 9pt;
  }
  .flow-step {
    font-size: 8.1pt;
    font-weight: 700;
    color: #111111;
    text-align: center;
    flex: 1;
  }
  .flow-arrow {
    color: #e4402e;
    font-weight: 800;
    font-size: 11pt;
  }

  /* Failure item */
  .fail-item {
    border-bottom: 1px solid #f0eeeb;
    padding: 4.5pt 0;
  }
  .fail-item:last-child {
    border-bottom: none;
  }
  .fail-head {
    display: flex;
    justify-content: space-between;
    font-size: 8.2pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 1.5pt;
  }
  .fail-day {
    color: #888888;
    font-size: 7.4pt;
  }
  .fail-desc {
    font-size: 7.7pt;
    line-height: 1.38;
    color: #444444;
  }
  .fail-rule {
    font-size: 7.7pt;
    line-height: 1.38;
    color: #e4402e;
    font-weight: 600;
    margin-top: 1pt;
  }
</style>
</head>
<body>
"""

HTML_FOOT = """
</body>
</html>
"""

def generate_html():
    pages = [
        render_page_01(),
        render_page_02(),
        render_page_03(),
        render_page_04(),
        render_page_05(),
        render_page_06(),
        render_page_07(),
        render_page_08(),
        render_page_09(),
        render_page_10(),
        render_page_11(),
        render_page_12(),
        render_page_13(),
        render_page_14(),
        render_page_15(),
        render_page_16(),
        render_page_17(),
        render_page_18(),
        render_page_19(),
        render_page_20(),
        render_page_21(),
        render_page_22(),
        render_page_23(),
        render_page_24()
    ]
    
    full_html = HTML_HEAD + "\n".join(pages) + HTML_FOOT
    return full_html

def main():
    guide_dir = "/Users/msdk/dev/grokbot-field-notes/guide"
    html_path = os.path.join(guide_dir, "grok-bot-guide-ko.html")
    pdf_path = os.path.join(guide_dir, "grok-bot-guide-by-spacex-engineers-ko.pdf")
    
    html_content = generate_html()
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML at {html_path}")
    
    chrome_path = "/Users/msdk/.cache/puppeteer/chrome/mac_arm-148.0.7778.97/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    print("Running Chrome print-to-pdf...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error compiling PDF:", res.stderr)
        return
    
    print(f"Compiled PDF at {pdf_path}")
    doc = fitz.open(pdf_path)
    print(f"Total pages in compiled PDF: {len(doc)}")
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text().strip()
        first_line = text.split('\n')[0] if text else "IMAGE/COVER"
        print(f"Page {i+1:02d}: {first_line[:40]} (chars: {len(text)})")

if __name__ == "__main__":
    main()
