# Django Themes
#### Brandon R. Stoner <monokrome@monokro.me>

## What is this?
Django Themes provides a mechanism for theming media for your web applications. This is done by storing a Theme model that contains a name for your theme and it's related directory. You can then access the list of themes and the current theme through these custom context_processors:

### themes.context_processors.list

Gets the complete theme list and sets it to a context variable, theme_list

### themes.context_processors.current

Gets the current theme and sets it to a context variable, current_theme

## Future developments:
- Tie this system into the template system, so that themes can override other
  templates if needed.
- Provide template tags that are functionally equivalent to the currently
  provided context processors.

