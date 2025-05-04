from django import template
from decimal import Decimal

register = template.Library()

class MultiplyNode(template.Node):
    def __init__(self, value, arg):
        self.value = value
        self.arg = arg

    def render(self, context):
        try:
            return str(Decimal(str(self.value.resolve(context))) * Decimal(str(self.arg.resolve(context))))
        except (ValueError, TypeError):
            return ''

@register.tag
def multiply(parser, token):
    try:
        tag_name, value, arg = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly two arguments" % token.contents.split()[0]
        )
    return MultiplyNode(
        parser.compile_filter(value),
        parser.compile_filter(arg)
    )

class GetItemNode(template.Node):
    def __init__(self, dictionary, key):
        self.dictionary = dictionary
        self.key = key

    def render(self, context):
        try:
            return str(self.dictionary.resolve(context).get(self.key.resolve(context)))
        except (ValueError, TypeError, AttributeError):
            return ''

@register.tag
def get_item(parser, token):
    try:
        tag_name, dictionary, key = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly two arguments" % token.contents.split()[0]
        )
    return GetItemNode(
        parser.compile_filter(dictionary),
        parser.compile_filter(key)
    ) 