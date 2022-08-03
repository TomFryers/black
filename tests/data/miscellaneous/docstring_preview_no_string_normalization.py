class ALonelyClass:
    '''
    A multiline class docstring.
    '''
    def AnEquallyLonelyMethod(self):
        '''
        A multiline method docstring'''
        pass


def one_function():
    '''This is a docstring with a single line of text.'''
    pass


def shockingly_the_quotes_are_normalized():
    '''This is a multiline docstring.
    This is a multiline docstring.
    This is a multiline docstring.
    '''
    pass


def foo():
  """This is a docstring with             
  some lines of text here
  """
  return


def baz():
  '''"This" is a string with some
  embedded "quotes"'''
  return


def poit():
  """
  Lorem ipsum dolor sit amet.       

  Consectetur adipiscing elit:
   - sed do eiusmod tempor incididunt ut labore
   - dolore magna aliqua
     - enim ad minim veniam
     - quis nostrud exercitation ullamco laboris nisi
   - aliquip ex ea commodo consequat
  """
  pass


def under_indent():
  """
  These lines are indented in a way that does not
make sense.
  """
  pass


def over_indent():
  """
  This has a shallow indent
    - But some lines are deeper
    - And the closing quote is too deep
    """
  pass


def single_line():
    """But with a newline after it!

    """
    pass


def this():
    r"""
    'hey ho'
    """


def that():
  """ "hey yah" """


def and_that():
  """
  "hey yah" """


def and_this():
  ''' 
  "hey yah"'''


def believe_it_or_not_this_is_in_the_py_stdlib(): ''' 
"hey yah"'''


def shockingly_the_quotes_are_normalized_v2():
    '''
    Docstring Docstring Docstring
    '''
    pass


def do_not_touch_this_prefix():
    R"""There was a bug where docstring prefixes would be normalized even with -S."""


def do_not_touch_this_prefix2():
    FR'There was a bug where docstring prefixes would be normalized even with -S.'


def do_not_touch_this_prefix3():
    u'''There was a bug where docstring prefixes would be normalized even with -S.'''

# output

class ALonelyClass:
    '''A multiline class docstring.'''

    def AnEquallyLonelyMethod(self):
        '''A multiline method docstring'''
        pass


def one_function():
    '''This is a docstring with a single line of text.'''
    pass


def shockingly_the_quotes_are_normalized():
    '''
    This is a multiline docstring.
    This is a multiline docstring.
    This is a multiline docstring.
    '''
    pass


def foo():
    """
    This is a docstring with
    some lines of text here
    """
    return


def baz():
    '''
    "This" is a string with some
    embedded "quotes"
    '''
    return


def poit():
    """
    Lorem ipsum dolor sit amet.

    Consectetur adipiscing elit:
     - sed do eiusmod tempor incididunt ut labore
     - dolore magna aliqua
       - enim ad minim veniam
       - quis nostrud exercitation ullamco laboris nisi
     - aliquip ex ea commodo consequat
    """
    pass


def under_indent():
    """
    These lines are indented in a way that does not
    make sense.
    """
    pass


def over_indent():
    """
    This has a shallow indent
      - But some lines are deeper
      - And the closing quote is too deep
    """
    pass


def single_line():
    """But with a newline after it!"""
    pass


def this():
    r"""'hey ho'"""


def that():
    """ "hey yah" """


def and_that():
    """ "hey yah" """


def and_this():
    '''"hey yah"'''


def believe_it_or_not_this_is_in_the_py_stdlib():
    '''"hey yah"'''


def shockingly_the_quotes_are_normalized_v2():
    '''Docstring Docstring Docstring'''
    pass


def do_not_touch_this_prefix():
    R"""There was a bug where docstring prefixes would be normalized even with -S."""


def do_not_touch_this_prefix2():
    FR'There was a bug where docstring prefixes would be normalized even with -S.'


def do_not_touch_this_prefix3():
    u'''There was a bug where docstring prefixes would be normalized even with -S.'''
