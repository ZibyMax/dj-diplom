from django import template


register = template.Library()


@register.filter
def is_child_exist(parent, sections):
    for section in sections:
        if section.parent == parent:
            return True
    return False

