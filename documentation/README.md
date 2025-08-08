# Documentation

This directory contains configuration for building API documentation using
[Doxygen](https://www.doxygen.nl/). Doxygen is configured to parse standard
Python docstrings through the [`doxypypy`](https://github.com/Feneric/doxypypy)
filter, so modules and functions should include docstrings.

## Generating the docs

1. Install Doxygen, Graphviz, and the `doxypypy` filter.

   - **Debian/Ubuntu:** `sudo apt-get install doxygen graphviz && pip install doxypypy`
   - **Windows:** download the installers from the [Doxygen](https://www.doxygen.nl/download.html) and [Graphviz](https://graphviz.org/download/) websites and run `pip install doxypypy` so `doxygen`, `dot`, and `doxypypy` are available in your `PATH`
2. From the project root, run:
   ```bash
   cd documentation
   doxygen Doxyfile
   ```
   The generated HTML will be placed under `documentation/build/html`. Open `index.html` in a browser to view the documentation.

