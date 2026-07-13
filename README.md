# LaTeX2Word-Pandoc

This project provides a lightweight Python script to automate the conversion of **LaTeX (`.tex`) documents** into **Microsoft Word (`.docx`)** using **Pandoc**. It is designed for researchers, students, and engineers who need a quick and reliable way to convert manuscripts while preserving citations, references, tables, figures, and document structure.

---

## Features

- **Automatic Conversion:** Converts a LaTeX manuscript directly into a Microsoft Word document.
- **Bibliography Support:** Automatically detects and processes `.bib` files using Pandoc Citeproc.
- **Standalone Execution:** No command-line arguments are required.
- **Portable:** Uses a local `pandoc.exe`, avoiding system PATH configuration.
- **Minimal Setup:** Place all required files in one directory and run the script.
---

## Usage Instructions

1. Download or clone this repository.

2. Place the following files in the project directory:

- `Manuscript.tex`
- `References.bib`
- `pandoc.exe`

3. Run the script using Python:

```bash
python LaTeX2Word-Pandoc.py
```

4. The "LaTeX2Word-Pandoc.py" will:

- Verify the required files.
- Detect the bibliography automatically.
- Convert the LaTeX document into Microsoft Word.
- Save the output as:

```text
Manuscript.docx
```

---

## Requirements

- Python 3.x
- Pandoc (tested with **Pandoc 3.10**)
- A valid LaTeX manuscript (`.tex`)
- Optional bibliography (`.bib`)

---

## Notes

- This script "LaTeX2Word-Pandoc.py" assumes that `pandoc.exe (pandoc-3.10-windows-x86_64)` is located in the same folder as the "LaTeX2Word-Pandoc.py".
- Standard LaTeX documents convert well, including sections, tables, figures, and references.
- Complex mathematical equations may require additional post-processing depending on the LaTeX packages used.
- Mathematical equations may require manual editing after conversion.

---

## Credits

This project is a Python automation utility built around **Pandoc**. All document conversion functionality is provided by the excellent **Pandoc** project created and maintained by **John MacFarlane** and contributors.

- **Pandoc Website:** https://pandoc.org/
- **Pandoc GitHub Repository:** https://github.com/jgm/pandoc

If you use this tool in your workflow, please consider supporting and citing the Pandoc project where appropriate.

---

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project. Credit is appreciated if you build upon it.

**Note:** This repository is an independent utility and is not affiliated with or endorsed by the Pandoc project.

---

## Developer Info

- **Developer:** Tufail Mabood
- **GitHub:** https://github.com/tufailmab
- **Contact:** https://wa.me/+923440907874

Contributions, suggestions, and improvements are always welcome.
