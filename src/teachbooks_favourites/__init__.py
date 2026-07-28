# -*- coding: utf-8 -*-
"""
teachbooks_favourites
~~~~~~~~~~~~~~~~~~~~~

A collection of our favourite Sphinx extensions for use in JupyterBooks.

"""

from typing import Any, Dict, List
from sphinx.application import Sphinx
from sphinx.errors import ConfigError


ALL_EXTENSIONS: List[str] = [
    "jupyterbook_patches",
    "download_link_replacer",
    "sphinx_image_inverter",
    "sphinx_iframes",
    "sphinx_exercise",
    "teachbooks_sphinx_tippy",
    "sphinx_named_colors",
    "sphinx_dropdown_toggle",
    "sphinx_proof",
    "sphinx_code_examples",
    "sphinx_accessibility",
    "sphinx_nb_execution_patterns",
    "sphinx-launch-buttons",
    "sphinx_github_alerts",
    "sphinx_metadata_figure",
    "sphinx_last_updated_by_git",
    "sphinx_gated_directives",
    "teachbooks_zoomies",
    "teachbooks_questions",
    "sphinx_sticky_margin",
    "teachbooks_fetch",
    "sphinx.ext.todo",
]


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("teachbooks_favourites_include", [], "env")
    app.add_config_value("teachbooks_favourites_exclude", [], "env")

    include: List[str] = app.config.teachbooks_favourites_include
    exclude: List[str] = app.config.teachbooks_favourites_exclude

    if include and exclude:
        raise ConfigError(
            "teachbooks_favourites: 'teachbooks_favourites_include' and "
            "'teachbooks_favourites_exclude' cannot both be set. "
            "Use one or the other."
        )

    unknown_include = [ext for ext in include if ext not in ALL_EXTENSIONS]
    if unknown_include:
        raise ConfigError(
            f"teachbooks_favourites: unknown extension(s) in "
            f"'teachbooks_favourites_include': {unknown_include}. "
            f"Valid names are: {ALL_EXTENSIONS}"
        )

    unknown_exclude = [ext for ext in exclude if ext not in ALL_EXTENSIONS]
    if unknown_exclude:
        raise ConfigError(
            f"teachbooks_favourites: unknown extension(s) in "
            f"'teachbooks_favourites_exclude': {unknown_exclude}. "
            f"Valid names are: {ALL_EXTENSIONS}"
        )

    if include:
        extensions_to_load = [ext for ext in ALL_EXTENSIONS if ext in include]
    elif exclude:
        extensions_to_load = [ext for ext in ALL_EXTENSIONS if ext not in exclude]
    else:
        extensions_to_load = ALL_EXTENSIONS

    for ext in extensions_to_load:
        app.setup_extension(ext)

    return {
        "version": "builtin",
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }
