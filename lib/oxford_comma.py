def oxford_comma(items):
    if len(items) == 1: return items[0]
    if len(items) == 2: return " and ".join(items)

    last_item = items.pop()
    return ", ".join(items) + f", and {last_item}"
