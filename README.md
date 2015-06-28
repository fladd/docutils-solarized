# docutils-solarized
A stylesheet for rst2html5.py


# About

[Solarized](http://ethanschoonover.com/solarized) light and dark docutils css stylesheet, inspired by the default [html-base.css](http://sourceforge.net/p/docutils/code/7892/tree/trunk/docutils/docutils/writers/html_base/html-base.css) by Günter Milde and [docutils_basic.css](https://github.com/matthiaseisen/docutils-css) by Matthias Eisen.


# Demo

http://stuff.fladd.de/docutils-solarized


# Usage

1. Install the latest docutils snapshot

2. Clone this repository

3. In a terminal run:

   ```
   python rst2html5.py --stylesheet=docutils_solarized_light.css document.rst document_light.html
   ```

4. To get create the dark version, in a terminal run:

   ```
   python docutils_solarized_invert.py docutils_solarized_light.css docutils_solarized_dark.css
   ```

5. In a terminal run:

   ```
   python rst2html5.py --stylesheet=docutils_solarized_dark.css document.rst document_dark.html
   ```
