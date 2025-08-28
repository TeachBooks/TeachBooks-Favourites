# TeachBooks Favourites

A collection of our favourite Sphinx extensions for use in JupyterBooks.

## Introduction
This Sphinx extension provides a single extension that includes and activates our favourite Sphinx extensions for use in JupyterBooks:

- Jupyterbook patches:
  - Various patches by TeachBooks
  - Repository: https://github.com/TeachBooks/JupyterBook-Patches
  - Manual: https://teachbooks.io/manual/external/JupyterBook-Patches/README.html
- Download link replacer:
  - Allows you to replace and add downloadable files to a page header
  - Repository: https://github.com/TeachBooks/Download-Link-Replacer
  - Manual: https://teachbooks.io/manual/external/Download-Link-Replacer/README.html
- Sphinx image inverter
  - Inverts images for dark mode
  - Repository: https://github.com/TeachBooks/sphinx-image-inverter
  - Manual: https://teachbooks.io/manual/external/Sphinx-Image-Inverter/README.html
- Sphinx iframes
  - Eases the embedding of iframes
  - Repository: https://github.com/TeachBooks/sphinx-iframes
  - Manual: https://teachbooks.io/manual/external/sphinx-iframes/README.html
- Sphinx exercise:
  - Allows you to add exercise admonitions to your book
  - Repository: https://github.com/TeachBooks/sphinx-exercise
  - Manual: https://ebp-sphinx-exercise.readthedocs.io/en/latest/
  - Remark: Currently this is set to the TeachBooks fork, waiting for merge of https://github.com/executablebooks/sphinx-exercise/pull/75
- Teachbooks Sphinx tippy
  - Enables hover over tips
  - Repository: https://github.com/TeachBooks/teachbooks-sphinx-tippy
  - Manual: https://teachbooks.io/manual/external/teachbooks-sphinx-tippy/README.html
  - Remark: This is a fork of https://github.com/executablebooks/sphinx-tippy specifically adapted for TeachBooks
- Sphinx named colors
  - Allows you to use custom colors in your book
  - Repository: https://github.com/TeachBooks/sphinx-named-colors
  - Manual: https://teachbooks.io/manual/external/Sphinx-Named-Colors/README.html
- Sphinx dropdown toggle
  - Adds a button to toggle all dropdowns with one click
  - Repository: https://github.com/TeachBooks/sphinx-dropdown-toggle
  - Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Dropdown-Toggle/main/MANUAL.html
- Sphinx proof:
  - Allows you to add various common math admonitions such as theorems to your book
  - Repository: https://github.com/TeachBooks/sphinx-proof
  - Manual: https://sphinx-proof.readthedocs.io/en/latest/
  - Remark: Currently this is set to the TeachBooks fork, waiting for merge of https://github.com/executablebooks/sphinx-proof/pull/146
- Sphinx code examples
  - Allows you to include code blocks and alternative visuals in examples
  - Repository: https://github.com/TeachBooks/sphinx-code-examples
  - Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_sphinx-code-examples/main/MANUAL.html
- Sphinx accessibility
  - Allows dyslexic-friendly fonts and high contrast mode
  - Repository: https://github.com/TeachBooks/sphinx-accessibility
  - Manual: https://teachbooks.io/manual/accessibility/_git/github.com_TeachBooks_Sphinx-Accessibility/manual/README.html
- Sphinx toggle button
  - Allows you to add a toggle button to elements in your book
  - Repository: https://github.com/TeachBooks/sphinx-togglebutton
  - Manual: https://sphinx-togglebutton.readthedocs.io/en/latest/
  - Remark: Currently this is set to the TeachBooks fork, waiting for merge of https://github.com/executablebooks/sphinx-togglebutton/pull/66


## Installation
To install TeachBooks-Favourites, follow these steps:

**Step 1: Install the Package**

Install the `teachbooks-favourites` package using `pip`:
```
pip install teachbooks-favourites
```

**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
teachbooks-favourites
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        - teachbooks_favourites
```

## Usage

For using the various package we refer to the different manuals linked above.

## Contribute

Do you think we missed an extension that should really be included? Let us know by either

- creating a fork of this repository and submitting a pull request, in which you added the extension to the files
  - `README.md`
  - `pyproject.toml`
  - `src\teachbooks_favourites\__init__.py`
- opening an issue.