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
    app.setup_extension("sphinx_exercise")
    app.setup_extension("teachbooks_sphinx_tippy")
    app.setup_extension("sphinx_named_colors")
    app.setup_extension("sphinx_dropdown_toggle")
    app.setup_extension("sphinx_proof")
    app.setup_extension("sphinx_code_examples")
    app.setup_extension("sphinx_accessibility")
    app.setup_extension("sphinx_nb_execution_patterns")
    app.setup_extension("sphinx-launch-buttons")
    app.setup_extension("sphinx_github_alerts")
    app.setup_extension("sphinx_metadata_figure")

    return {
        "version": "builtin",
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }
