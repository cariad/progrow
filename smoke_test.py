from progrow import Row, Style

row = Row("foo", maximum=10, current=3)
style = Style(color=False, show_fraction=True, show_percent=True, width=30)
assert row.render(style=style) == "foo ███▉          3 / 10 • 30%"
