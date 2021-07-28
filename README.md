# `sphinx-build-dataclasses-initvar`

Run the following:

```
sphinx-build \
  -W \
  -j auto \
  -b dirhtml \
  -d sphinx/doctree \
  -c sphinx \
  bug \
  sphinx/html
```

Exposing this `InitVar` related bug:

```
Running Sphinx v4.0.0
loading intersphinx inventory from https://docs.python.org/3/objects.inv...
building [mo]: targets for 0 po files that are out of date
building [dirhtml]: targets for 2 source files that are out of date
updating environment: [new config] 2 added, 0 changed, 0 removed
reading sources... [ 50%] dataclass
reading sources... [100%] index

looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done

Warning, treated as error:
sphinx-build-dataclasses-initvar/bug/dataclass.py:docstring of bug.dataclass.Bug::py:class reference target not found: InitVar
```
