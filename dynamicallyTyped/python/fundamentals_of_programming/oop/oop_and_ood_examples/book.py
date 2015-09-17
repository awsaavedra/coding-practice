#http://blog.teamtreehouse.com/operator-overloading-python

class Book:
  title = ''
  pages = 0

  def __init__(self, title='', pages=0):
    self.title = title
    self.pages = pages

  def __str__(self):
    return self.title

  def __radd__(self, other):
    return self.pages + other

  def __add__(self, other):
      return self.pages + other
  
  def __lt__(self, other):
    return self.pages < other

  def ___le__(self, other):
      return self.pages <= other

  def __eq__(self, other):
      return self.pages == other

  def __ne__(self, other):
      return self.pages != other

  def __gt__(self, other):
      return self.pages > other

  def __ge__(self, other):
      return self.pages >= other

  def __le__(self, other):
    if isinstance(other, Book):
        return self.pages <= other.pages
    elif isinstance(other, (int, float)):
        return self.pages <= other
    else:
        return NotImplemented

  def __ge__(self, other):
    if isinstance(other, Book):
        return self.pages >= other.pages
    elif isinstance(other, (int, float)):
        return self.pages >= other
    else:
        return NotImplemented

#enter the python shell ( >>python) and type the following line by line...
"""
book1 = Book('Fluency', 381)
book2 = Book('The Martian', 385)
book3 = Book('Ready Player One', 386)
sum([book1, book2, book3])
"""
