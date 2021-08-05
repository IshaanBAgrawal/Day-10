# functions with outputs

def format_name(f_name, l_name):
  # docstrings
  """Take the first and last name and format it
   to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You did not provide valid inputs"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
formatted_string = format_name("isHAAN", "")
print(formatted_string)
