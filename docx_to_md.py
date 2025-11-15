#!/usr/bin/env python3

"""
MVP: Convert .docx files to Markdown (.md) using pandoc.

Usage:
    python docx_to_md.py input.docx [output.md]

Requirements:
    - pandoc must be installed and available in PATH.
"""

import subprocess
import sys
from pathlib import Path


def run_pandoc(input_path: Path, output_path: Path) -> None:
    cmd = [
        "pandoc",
        str(input_path),
        "-t",
        "markdown",
        "-o",
        str(output_path),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("Error: pandoc no está instalado o no está en el PATH.")
        print("Instálalo (por ejemplo en Ubuntu/Debian): sudo apt-get install pandoc")
        sys.exit(1)

    if result.returncode != 0:
        print("Error al ejecutar pandoc:")
        if result.stderr:
            print(result.stderr)
        sys.exit(result.returncode)

    print(f"OK: {input_path.name} -> {output_path}")


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Uso: python docx_to_md.py input.docx [output.md]")
        sys.exit(1)

    input_path = Path(argv[1]).expanduser().resolve()

    if not input_path.exists():
        print(f"Error: no existe el archivo: {input_path}")
        sys.exit(1)

    if input_path.suffix.lower() != ".docx":
        print(f"Advertencia: la extensión no es .docx ({input_path.suffix}), continúo igual...")

    if len(argv) >= 3:
        output_path = Path(argv[2]).expanduser().resolve()
    else:
        output_path = input_path.with_suffix(".md")

    run_pandoc(input_path, output_path)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv)
