from flask import Flask
from babel import numbers

def _currency_filter(value: float):
    return numbers.format_currency(value, 'BRL', locale='pt_BR')

def _percent_filter(value: float):
    return numbers.format_percent(value, format=u'#,##%', locale='pt_BR')

def init_app(app: Flask):
    app.jinja_env.filters['currency'] = _currency_filter
    app.jinja_env.filters['percent'] = _percent_filter

