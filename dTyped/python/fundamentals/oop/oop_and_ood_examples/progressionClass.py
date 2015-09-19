#This is the class all mathematical progessions will inherit from: addition, sub, etc.
class Progression:
  """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
  """

  def __init__(self, start= 0):
    self._current = start

  def _advanced(self):
    """
    Update self. current to a new value.
    This should be overridden by a subclass to customize progression.
    By convention, if current is set to None, this designates the
    end of a finite progression.
    """
    self. current += 1
  
  def __next__(self):
    if self. current is None:
      raise StopIteration()
    else:
      answer = self._current
      self._advance()
      return answer

  def __iter__(self):
    return self

  def print_progression(self, n):
    print( ' '.join(str(next(self)) for j in range(n)))

#subclass
class ArithmeticProgression(Progression):
  # inherit from Progression
  # Iterator producing an arithmetic progression
  def init (self, increment=1, start=0):
    # Create a new arithmetic progression.
    # increment the fixed constant to add to each term (default 1)
    # start
    # the first term of the progression (default 0)
    # # initialize base class
    super( ).__init__(start)
    self._increment = increment
  # # override inherited version
  def _advance(self):
    # Update current value by adding the fixed increment.
    self._current += self._increment
