from mariar.constant.core import END, UNDERLINE

def generate_input_text(text: str) -> str:
  return f'{UNDERLINE}{text}{END} > '
