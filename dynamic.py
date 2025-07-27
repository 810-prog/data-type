def print_structure(data, indent=0):
    """Recursively prints nested dictionaries, lists, tuples, and sets."""
    space = "  " * indent

    if isinstance(data, dict):
        print(f"{space}{{")
        for key, value in data.items():
            print(f"{space}  {repr(key)}: ", end="")
            print_structure(value, indent + 2)
        print(f"{space}}}")

    elif isinstance(data, (list, tuple, set)):
        open_bracket, close_bracket = ("[", "]") if isinstance(data, list) else ("(", ")") if isinstance(data, tuple) else ("{", "}")
        print(f"{space}{open_bracket}")
        for item in data:
            print_structure(item, indent + 2)
        print(f"{space}{close_bracket}")

    else:
        print(f"{space}{repr(data)}")
dynamic_data = {
    "name": "dheeraj sain",
    "age": 22,
    "skills": ["Python", "Data Science", {"level": "Advanced"}],
    "projects": {
        "AI": ["Chatbot", "Image Recognition"],
        "Web": {"frameworks": ["Django", "Flask","vs code"]}
    }
}

print("Dynamic Structure:\n")
print_structure(dynamic_data)

# .......................................................................................................................
# output
# Dynamic Structure:

# {
#   'name':     'dheeraj sain'
#   'age':     22
#   'skills':     [
#         'Python'
#         'Data Science'
#         {
#           'level':             'Advanced'
#         }
#     ]
#   'projects':     {
#       'AI':         [
#             'Chatbot'
#             'Image Recognition'
#         ]
#       'Web':         {
#           'frameworks':             [
#                 'Django'
#                 'Flask'
#                 'vs code'
#             ]
#         }
#     }
# }