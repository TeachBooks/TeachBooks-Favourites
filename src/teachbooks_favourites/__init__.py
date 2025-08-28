# -*- coding: utf-8 -*-
"""
sphinx_accessibility
~~~~~~~~~~~~~~~~~~~~

A collection of our favourite Sphinx extensions for use in JupyterBooks.

"""

from typing import Any, Dict
from sphinx.application import Sphinx


def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension("jupyterbook_patches")
    app.setup_extension("download_link_replacer")
    app.setup_extension("sphinx_image_inverter")
    app.setup_extension("sphinx_iframes")
    # waiting for merge of https://github.com/executablebooks/sphinx-exercise/pull/75,
    # after merge, remove "teachbooks_",
    app.setup_extension("teachbooks_sphinx_exercise")
    app.setup_extension("teachbooks_sphinx_tippy")
    app.setup_extension("sphinx_named_colors")
    app.setup_extension("sphinx_dropdown_toggle")
    app.setup_extension("sphinx_proof")
    app.setup_extension("sphinx_code_examples")
    app.setup_extension("sphinx_accessibility")

    return {
        "version": "builtin",
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }