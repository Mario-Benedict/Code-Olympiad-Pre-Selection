from mariar.interpreter import MariarInterpreter

def test_interpreter():
  interpreter = MariarInterpreter()

  assert interpreter.start is not None
