from mariar.utils import helper
from mariar.constant.core import UNDERLINE, END

def test_generate_input_text():
  res = helper.generate_input_text('Test')
  expect = f'{UNDERLINE}Test{END} > '

  assert res == expect
