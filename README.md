# Django Themes
#### Brandon R. Stoner <monokrome@monokro.me>

## What is this?

Django Themes provides a mechanism for theming media for your web applications.
This is done by storing a Theme model that contains a name for your theme and
it's related directory. You can then access the list of themes and the current
theme through the provided template context processors.

## Getting started

Firstly, install the django-themes with your favorite PyPi utility:

        pip install django-themes

Next, append the **themes** package to your **INSTALLED_APPS** setting.

        INSTALLED_APPS = (
            # Other apps here...

            'themes',
        )

Add the context processors to your **TEMPLATE_CONTEXT_PROCESSORS** setting.

*Note that if this setting does not yet exist in your settings file, then it must be
created manually with the default value as provided at the Django documentation
[here](https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors)

        TEMPLATE_CONTEXT_PROCESSORS = (
            # Other context processors here...

            "themes.context_processors.list",
            "themes.context_processors.current_theme",
        )

## Usage

Now that Django themes has been installed, you can create a theme. You do this
by creating a new instance of the *themes.models.Theme* model, and setting
the following values as you'd like:

- name: A user-friendly name for this theme
- directory: The directory where this theme's files are stored
- sites_enabled: The sites where this theme is enabled as the default for
- sites_available: The sites that this theme is intended to be used on

*Note that the last two settings exist for multi-site installations. If you are
only hosting one site with your Django installation, then you can just add
that one site to both settings and things will work fine.*

After adding a theme, you can try something like the following code in order
to see the theme system in action.

        {% for theme in theme_list %}
        
          <link rel="{% if theme != current_theme %}alternate {% endif %}stylesheet"
                type=text/css
                href="{{ STATIC_URL }}themes/{{ theme.directory }}/style.css" />
        
        {% endfor %}

This will create links for all of your theme styles in your source. The default
theme will be set to the stylesheet of the page, while other themes are
accessible using the browser's native mechanism for accessing alternate stylesheets.

## Template context processors

### themes.context_processors.theme_list

Gets the complete theme list and sets it to a context variable, theme_list

### themes.context_processors.current_theme

Gets the current theme and sets it to a context variable, current_theme

## Future developments:

- Tie this system into the template system, so that themes can override other
  templates if needed.
- Provide template tags that are functionally equivalent to the currently
  provided context processors.

