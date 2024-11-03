# ZX Spectrum Colour

This program has two functionalities:

1. Provides the ZX Spectrum colour from a given value.
2. Provides the attribute byte value from the selected ZX Spectrum colour/
   bright/ flash component values.

## Installation

To install this package locally, navigate to the package directory and run:

pip install .

## Usage

```
$ zxcolour -h
usage: zxcolour [-h] [--calculate] [attribute_byte]

Displays which ZX Spectrum colour a given attribute byte is.

positional arguments:
  attribute_byte  The attribute byte to use

options:
  -h, --help      show this help message and exit
  --calculate     Calculate the attribute byte from ink, paper, bright, flash inputs
```

### Example 1

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

### Example 2

Typing the following:
```
$ zxcolour --calculate
```

Would produce the following output:
```
Available colours:
0: BLACK (Bright: BLACK)
1: BLUE (Bright: BLUE)
2: RED (Bright: RED)
3: MAGENTA (Bright: MAGENTA)
4: GREEN (Bright: GREEN)
5: CYAN (Bright: CYAN)
6: YELLOW (Bright: YELLOW)
7: WHITE (Bright: WHITE)
Choose INK colour (0-7): 7
Choose PAPER colour (0-7): 5
Is BRIGHT mode on? (0=NO, 1=YES): 1
Is FLASH mode on? (0=NO, 1=YES): 0

Calculated attribute byte: 0x6F (decimal: 111)
```
