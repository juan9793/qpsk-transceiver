# Documentation

This directory contains configuration for building API documentation using
[Doxygen](https://www.doxygen.nl/). Doxygen parses standard Python docstrings
directly, so modules and functions should include docstrings. Diagrams used
throughout the documentation live under `diagrams/`.

### Diagram conversion

Use [Graphviz](https://graphviz.org/) to convert `.dot` files in `diagrams/` to `.svg` images:

```bash
dot -Tsvg qpsk_transmission_chain.dot -o qpsk_transmission_chain.svg
```

Regenerate diagrams whenever the underlying `.dot` files change or the signal chain is updated.

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

### GitHub Pages

The documentation workflow deploys the contents of `documentation/build/html`
to GitHub Pages. Ensure the repository's Pages **Source** is set to *GitHub
Actions* so the default branch deployment does not overwrite the generated
site.

