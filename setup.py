from setuptools import setup, find_packages

setup(
	name="zx_spectrum_colour",
	version="0.2.0",
	packages=find_packages(),
	author="Paul Maddern",
	author_email="paul@arcadegeek.co.uk",
	description="ZX Spectrum colour kit; provides a way to show what colours an attribute byte is, and vice-versa.",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	url="https://github.com/pobtastic/zx_spectrum_colour",
	entry_points={
		'console_scripts': [
			'zxcolour=zxcolour.cli:main',
		],
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
)
