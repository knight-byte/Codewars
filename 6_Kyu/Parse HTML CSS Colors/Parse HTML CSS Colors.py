def parse_html_color(color):
    color = PRESET_COLORS.get(color.lower(), color)

    if len(color) == 7:
        r, g, b = (int(color[i:i+2], 16) for i in range(1, 7, 2))
    else:
        r, g, b = (int(color[i+1]*2, 16) for i in range(3))

    return dict(zip("rgb", (r, g, b)))
