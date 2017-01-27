# Base1k / Base4k

Binary to text codecs using the most common 1024 or 4096 unambiguous Chinese characters.

"Unambiguous" means it prevents most errors in Simplified/Traditional conversion process.

The character frequency list is based on a 6.8 billion-character arbitrary selected Simplified Chinese corpus.

This is based on [xiaq](https://github.com/xiaq/base1k)'s idea.

Usage: `python3 base1k.py [-4k] [-d] < input > output`
