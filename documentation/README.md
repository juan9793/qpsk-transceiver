# Documentation

This directory contains configuration for building API documentation using [Doxygen](https://www.doxygen.nl/).

## Generating the docs

1. Install Doxygen and Graphviz.

   - **Debian/Ubuntu:** `sudo apt-get install doxygen graphviz`
   - **Windows:** download the installers from the [Doxygen](https://www.doxygen.nl/download.html) and [Graphviz](https://graphviz.org/download/) websites and ensure `doxygen` and `dot` are available in your `PATH`
2. From the project root, run:
   ```bash
   cd documentation
   doxygen Doxyfile
   ```
   The generated HTML will be placed under `documentation/build/html`. Open `index.html` in a browser to view the documentation.

