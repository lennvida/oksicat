# -*- coding: utf-8 -*-

import re

from django import template

from triadatv.structure.models import StructureNode

register = template.Library()

@register.filter
def get_parent_level(node, level):
    '''
    Возвращает родительский элемент заданного уровня
    '''
    level = int(level)
    if node.level == level: return node
    else: parent = node.parent
    while parent.level > level:
        parent = parent.parent
    return parent

@register.tag
def get_menu_level(parser, token):
    '''
    возвращает эелменты меню заданного уровня
    '''
    try:
        _, level, parent, result = token.split_contents()
        level = int(level)
    except (IndexError, AssertionError, ValueError):
        raise template.TemplateSyntaxError
    return GetMenu(level, parent, result)

class GetMenu(template.Node):
    def __init__(self, level, parent, result):
        self.result = result
        self.level = level
        self.parent = template.Variable(parent)

    def render(self, context):
        parent = self.parent.resolve(context)
        if parent == 'all':
            qset = StructureNode.objects.menu_visible().filter(level=self.level)
        else:
            qset = StructureNode.objects.menu_visible().filter(level=self.level, parent=parent)
        context.update({self.result: qset})
        return ''




# Старые теги, со временем удалятся ненужные

# @register.tag
# def language_switcher(parser, token):
#     try:
#         _, code = token.split_contents()
#     except (IndexError, AssertionError, ValueError):
#         raise template.TemplateSyntaxError
#     return LanguageSwitcher(code)

# class LanguageSwitcher(template.Node):
#     def __init__(self, code):
#         self.code = code
#     def render(self, context):
#         path = context.get('request').META['PATH_INFO']
#         if path != '/':
#             path = re.sub(r'^/(%s)/' % code , '/%s/' % self.code, path)
#         else:
#             path = '/%s/' % self.code
#         obj = StructureNode.objects.get_by_path(path)
#         if obj:
#             return obj.path
#         return '/%s/' % self.code    

# @register.tag
# def load_lang_node(parser, token):
#     try:
#         _, lang_code, result = token.split_contents()
#     except (IndexError, AssertionError, ValueError):
#         raise template.TemplateSyntaxError
#     return LoadLangNode(lang_code, result)

# class LoadLangNode(template.Node):
#     def __init__(self, lang_code, result):
#         self.result = result
#         self.lang_code = template.Variable(lang_code)
#     def render(self, context):
#         lang_code = self.lang_code.resolve(context)
#         try:
#             node = StructureNode.objects.get(slug=lang_code)
#         except StructureNode.DoesNotExist:
#             node = None
#         context.update({self.result: node})
#         return ''

# @register.filter
# def get_descendants(node):
#     return node.get_descendants().filter(menu_visible=True)

# @register.filter
# def get_descendants_of_type(node, typ):
#     return node.get_descendants().filter(menu_type=typ, menu_visible=True)

# @register.filter
# def get_children_of_type(node, typ):
#     return node.get_children().filter(menu_type=typ, menu_visible=True)