#!/usr/bin/env python3

class ZXSpectrumColour:

	def __init__(self, attribute: int):
		self._attribute = attribute

	@property
	def attribute(self) -> int:
		return self._attribute

	def run(self):
		ink = self.attribute&0x07
		paper = (self.attribute>>0x03)&0x07
		bright = (self.attribute>>0x06)&0x01
		flash = (self.attribute>>0x07)&0x01
		return ink, paper, bright, flash
