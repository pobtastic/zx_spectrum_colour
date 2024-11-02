# ZX Spectrum Colour

Provides the ZX Spectrum colour from a given value.

## Installation

To install this package locally, navigate to the package directory and run:

pip install .

## Usage

```
$ zxcolour --help
usage: zxcolour [-h] attribute_byte

Displays what ZX Spectrum colour a given attribute byte is.

positional arguments:
  attribute_byte  The attribute byte to use

options:
  -h, --help      show this help message and exit
```

### Example

Typing the following:
```
$ zxcolour 0x23
```

Would produce the following output:
```
Ink:    03 == MAGENTA
Paper:  04 == GREEN
Colour: ▐▌
Bright: OFF
Flash:  OFF
```
(Colour will appear as $${\color{magenta}▐\color{green}▌}$$)

Noting that this is the same as typing:
```
zxcolour 35
```
