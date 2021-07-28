project = "bug"
nitpicky = True
add_function_parentheses = False
html_show_sphinx = False
html_copy_source = False
extensions = (
  "sphinx.ext.autodoc",
  "sphinx.ext.intersphinx",
)
intersphinx_timeout = 5
autodoc_typehints = "description"
intersphinx_mapping = {
  "python": ("https://docs.python.org/3", None),
}

from sys import path
from pathlib import Path
this = Path(__file__)
path.append(f"{this.parent.parent}")
