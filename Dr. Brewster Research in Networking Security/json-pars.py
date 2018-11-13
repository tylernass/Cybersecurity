# This is a Python program that is designed to process and handle large JSON files with complex structures

import jsbeautifier
import json

# opt = {
#     "indent_size": "4",
#     "indent_char": " ",
#     "max_preserve_newlines": "5",
#     "preserve_newlines": True,
#     "keep_array_indentation": False,
#     "break_chained_methods": False,
#     "indent_scripts": "normal",
#     "brace_style": "collapse",
#     "space_before_conditional": True,
#     "unescape_strings": False,
#     "jslint_happy": False,
#     "end_with_newline": False,
#     "wrap_line_length": "0",
#     "indent_inner_html": False,
#     "comma_first": False,
#     "e4x": False
# }

res = jsbeautifier.beautify_file('5432-3pkts-out.json')
opts = jsbeautifier.default_options()
opts.indent_size = 4
opts.indent_char = " "
opts.max_preserve_newlines = "5"
opts.preserve_newlines = True
opts.keep_array_indentation = False
opts.break_chained_methods = False
opts.indent_scripts = "normal"
opts.brace_style = "collapse"
opts.space_before_conditional = True
opts.unescape_strings = False
opts.islint_happy = False
opts.end_with_newline = False
opts.wrap_line_length = "0"
opts.indent_inner_html = False
opts.comma_first = False
opts.e4x = False

res = jsbeautifier.beautify_file('5432-3pkts-out.json', opts)

# print(res)
