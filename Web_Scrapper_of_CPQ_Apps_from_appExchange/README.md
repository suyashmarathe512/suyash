# OCR + Playwright CPQ Analyzer

A reproducible Colab notebook + helper scripts that use Playwright to capture Salesforce AppExchange listing tabs, run Tesseract OCR on the screenshots, compute term-frequency (TF) statistics, and save outputs for analysis and visualization.

> Intention: capture the `default`, `e`, and `d` tabs for AppExchange listings, OCR those screenshots, compute top terms, and produce per-listing and consolidated CSVs.

---

## Table of contents

* [What this does](#what-this-does)
* [Repository layout](#repository-layout)
* [Prerequisites](#prerequisites)
* [Quick start (Colab)](#quick-start-colab)
* [How it works](#how-it-works)
* [Configuration](#configuration)
* [Running](#running)
* [Outputs](#outputs)
* [Visualization examples](#visualization-examples)
* [Troubleshooting](#troubleshooting)
* [Extending / notes](#extending--notes)
* [License](#license)

---

## What this does

1. Visits an AppExchange listing by `listingId`.
2. Visits the `default`, `e`, and `d` tabs for each listing and captures full-page screenshots.
3. Runs Tesseract OCR on captured screenshots and aggregates text per listing.
4. Computes simple term-frequency (TF) counts (tokenize → remove stopwords → count).
5. Writes per-listing CSVs and a consolidated `all_cpq_tf_from_ocr_tabs.csv` suitable for pivoting and visualization.

---

## Repository layout

```
.
├─ notebook.ipynb             # Colab notebook with the full pipeline
├─ README.md                  # This file
├─ screenshots_cpq_tabs/      # saved full-page screenshots
├─ ocr_text_cpq_tabs/         # combined OCR text files per listing
├─ tf_cpq_tabs/               # per-listing TF CSVs
├─ all_cpq_tf_from_ocr_tabs.csv
└─ src/                       # optional helper scripts (capture, ocr, tf, viz)
```

---

## Prerequisites

* Linux (Ubuntu recommended) or Google Colab.
* Python 3.8+.
* Tesseract OCR (system package) and (optionally) language packs.
* Playwright (Python package) and Playwright browser binaries.
* Python packages: `pytesseract`, `pillow`, `pandas`, `playwright`, `matplotlib`, `seaborn`.

Optional: `pdf2image` and `poppler-utils` if you want to OCR PDFs.

---

## Quick start (Colab)

Run these cells at the top of the notebook (exact commands used in the provided Colab):

```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr

pip install pytesseract pillow pandas
pip install playwright
playwright install

# Playwright host dependencies (Linux)
sudo apt-get install -y libxcomposite1 libgtk-3-0 libatk1.0-0 libxtst6 at-spi2-core
```

Windows note: install Tesseract via the official installer and set `pytesseract.pytesseract.tesseract_cmd` to the installed path.

---

## How it works

* `CPQ_APPS` maps `app_name -> listingId` (edit this dict to add apps).
* For each listing the script builds URLs:

  * `https://appexchange.salesforce.com/appxListingDetail?listingId={listingId}`
  * and adds `&tab=e` and `&tab=d` as required.
* Playwright navigates to each URL and saves a full-page PNG.
* `pytesseract` reads each PNG and returns text; texts for all tabs are concatenated and saved.
* `compute_tf()` tokenizes, removes STOPWORDS, and counts tokens to produce the top N terms per listing.

---

## Configuration

Edit the `CPQ_APPS` dictionary in the notebook to include the listings you want to analyze:

```python
CPQ_APPS = {
  "PandaDoc": "a0N3A00000DvMrEUAV",
  "YourApp": "a0N3A00000XXXXXXX",
}
```

Adjust constants in the code:

* `APPEX_BASE_URL` — base AppExchange endpoint.
* `TABS` — list of `(tab_name, tab_param)` tuples.
* `STOPWORDS` — set of words filtered before counting.
* `compute_tf(... top_n=25)` — change `top_n` to control output size.

Timeouts and Playwright settings are in the notebook (e.g., `page.goto(..., timeout=60000)`, `headless=True`).

---

## Running

From the notebook execute the async batch runner cell:

```python
await run_batch()
```

The runner will create directories, visit listings, save screenshots and OCR text, compute TF, and write a consolidated CSV.

---

## Outputs

* `screenshots_cpq_tabs/{listing_slug}_tab-{tab}.png` — screenshots.
* `ocr_text_cpq_tabs/{listing_slug}_combined_ocr.txt` — combined OCR text per listing.
* `tf_cpq_tabs/{listing_slug}_tf.csv` — per-listing top TF counts.
* `all_cpq_tf_from_ocr_tabs.csv` — consolidated TF rows for all apps.

---

## Visualization examples

The notebook includes cells that pivot the consolidated CSV and create plots. Example pivoting:

```python
import pandas as pd

df_all = pd.read_csv('all_cpq_tf_from_ocr_tabs.csv')
df_filtered = df_all[df_all['tf'] != 1]
df_pivot = df_filtered.pivot_table(index='app_name', columns='term', values='tf', fill_value=0)
```

Plotting uses `matplotlib` and `seaborn`. If running headless, save figures to files instead of displaying.

---

## Troubleshooting

**Playwright missing host deps**: Run `playwright install-deps` or install packages shown in the error message (example above).

**Short/empty OCR output**: verify screenshots are full-page and not blocked by lazy-loaded content; increase page wait or add explicit waits for selectors.

**Tesseract quality**: preprocess images (resize, denoise, threshold), or install language packs and pass `lang='eng'` to `pytesseract.image_to_string`.

**Debconf warnings in Colab**: non-interactive apt will print frontend warnings—these are usually non-fatal.

---

## Extending / notes

* The TF pipeline is intentionally simple; replace with TF-IDF, lemmatization, or n-grams for more advanced analysis.
* Add rate limiting and exponential backoff for larger batches to be polite to AppExchange.
* To OCR PDFs, convert pages with `pdf2image` and then run `pytesseract`.

---

## License

MIT — use, modify, and redistribute with attribution.

---

If you want a standalone `scrape_listings.py` CLI, a modular split (`capture.py`, `ocr.py`, `tf.py`, `visualize.py`), or a small unit-test scaffold, tell me which and I will generate the files.

