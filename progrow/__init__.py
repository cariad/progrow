"""
**progrow** is a Python package for graphing the progress of work.

.. image:: example.png

## Installation

**progrow** requires Python 3.6 or later.

```bash
pip install progrow
```

## Examples

### Single row

To render a single row to a string, create a `Row` instance and call `Row.render`.

```python
from progrow import Row

row = Row("apple harvest", current=23, maximum=100)
print(row.render())
```

```text
apple harvest ████████▉
```

### Styling

To customise the render, pass a `Style` instance into `Row.render`.

```python
from progrow import Row, Style

row = Row("apple harvest", current=23, maximum=100)

style = Style(
    name_suffix=" progress: ",
    show_fraction=True,
    show_percent=True,
)

print(row.render(style=style))
```

```text
apple harvest progress: ███▌            23 / 100 • 23%
```

### Multiple rows

Create a `Rows` instance and call `Rows.append` for each row.

```python
from progrow import Rows, Style

rows = Rows()
rows.append("apple harvest", current=1, maximum=9)
rows.append("banana harvest", current=9, maximum=99)
rows.append("caramel harvest", current=100, maximum=100)

style = Style(show_fraction=True, show_percent=True)

print(rows.render(style))
```

```text
apple harvest   ██▎                    1 /   9 •  11%
banana harvest  █▊                     9 /  99 •   9%
caramel harvest ███████████████████▉ 100 / 100 • 100%
```


"""

from progrow.layout import Layout
from progrow.row import Row
from progrow.rows import Rows
from progrow.style import Style

__all__ = ["Layout", "Row", "Rows", "Style"]
