#!/usr/bin/env python3

import sys
import argparse
from .zx_spectrum_colour import ZXSpectrumColour

COLOURS = [
        ("BLACK", "\x1b[30m", "\x1b[90m"),
        ("BLUE", "\x1b[34m", "\x1b[94m"),
        ("RED", "\x1b[31m", "\x1b[91m"),
        ("MAGENTA", "\x1b[35m", "\x1b[95m"),
        ("GREEN", "\x1b[32m", "\x1b[92m"),
        ("CYAN", "\x1b[36m", "\x1b[96m"),
        ("YELLOW", "\x1b[33m", "\x1b[93m"),
        ("WHITE", "\x1b[37m", "\x1b[97m"),
]


def main():
	parser = argparse.ArgumentParser(description="Displays what ZX Spectrum colour a given attribute byte is.")
	parser.add_argument("attribute_byte", help="The attribute byte to use")

	args = parser.parse_args()

	try:
		attribute_byte = int(args.attribute_byte, 0)
	except ValueError:
		print("Error: attribute_byte must be an integer or hex value (e.g., 0x42).")
		sys.exit(1)
	ZXColour = ZXSpectrumColour(attribute_byte)
	ink, paper, bright, flash = ZXColour.run()

	ink_name, ink_colour_code, ink_bright_code = COLOURS[ink]
	paper_name, paper_colour_code, paper_bright_code = COLOURS[paper]
	ink_colour_code = ink_bright_code if bright else ink_colour_code
	paper_colour_code = paper_bright_code if bright else paper_colour_code
	bright_status = "ON" if bright else "OFF"
	flash_status = "ON" if flash else "OFF"

	half_and_half = f"{paper_colour_code}▐\x1b[0m{ink_colour_code}▌\x1b[0m"

	print(f"Ink:    {ink:02X} == {ink_name}")
	print(f"Paper:  {paper:02X} == {paper_name}")
	print(f"Colour: {half_and_half}")
	print(f"Bright: {bright_status}")
	print(f"Flash:  {flash_status}")

if __name__ == "__main__":
	main()
