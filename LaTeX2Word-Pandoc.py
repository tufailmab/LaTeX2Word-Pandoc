import os
import subprocess

# File names (must be in the same folder as this script)
TEXFILE = "Manuscript.tex"
BIBFILE = "References.bib"
PANDOC = "pandoc.exe" # pandoc-3.10-windows-x86_64 (I used this version)


def convert():
    # Folder where this script is located
    folder = os.path.dirname(os.path.abspath(__file__))

    tex_path = os.path.join(folder, TEXFILE)
    bib_path = os.path.join(folder, BIBFILE)
    pandoc_path = os.path.join(folder, PANDOC)
    docx_path = os.path.join(folder, "Manuscript.docx")

    # Check files
    if not os.path.exists(pandoc_path):
        print("ERROR: pandoc.exe not found.")
        print("Expected location:")
        print(pandoc_path)
        return

    if not os.path.exists(tex_path):
        print("ERROR: Manuscript.tex not found.")
        return

    if not os.path.exists(bib_path):
        print("WARNING: References.bib not found.")
        use_bib = False
    else:
        use_bib = True

    # Check pandoc
    try:
        result = subprocess.run(
            [pandoc_path, "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout.splitlines()[0])
    except Exception as e:
        print("Cannot start pandoc.")
        print(e)
        return

    # Build command
    cmd = [
        pandoc_path,
        tex_path,
        "-o",
        docx_path,
        "--from",
        "latex",
        "--to",
        "docx",
        "--standalone"
    ]

    if use_bib:
        cmd.extend([
            "--bibliography",
            bib_path,
            "--citeproc"
        ])

    print("\nConverting...")

    try:
        result = subprocess.run(
            cmd,
            cwd=folder,
            capture_output=True,
            text=True,
            check=True
        )

        print("\n===================================")
        print("SUCCESS!")
        print("Word file created:")
        print(docx_path)
        print("===================================")

    except subprocess.CalledProcessError as e:
        print("\nPandoc Error:")
        print(e.stderr)


if __name__ == "__main__":
    convert()
