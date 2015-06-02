def exitKeyWord():
  answer  = raw_input("\nWould you like to exit this program? Yes or no.")
  if "yes" in answer:
    exit()
  elif "no" in answer:
    theKeyWordModule()
  else:
    print "You did not answer yes or no, please type one."
    exitKeyWord()
def theKeyWordModule():
  print """Which type of keywords would you like to know? 
          a)data types
          b)general keywords
          c)string Formats
          d)string escape sequence
          e)operators
        """
  keywordEntered = raw_input("> ")
  if "data types" in keywordEntered:
    #list all datatypes
    print """
       true
       false
       None
       strings
       numbers
       floats
       lists
      """
    exitKeyWord()
  elif "general keywords" in keywordEntered:
    #list all general keywords
    print """
       and
       del
       from
       not
       while
       as
       elif
       global
       or
       with
       assert
       else
       if
       pass
       yield
       break
       except
       import
       print
       class
       exec
       in
       raise
       continue
       finally
       is
       return
       def
       for
       lambda
       try
      """
    exitKeyWord()
  elif "string formats" in keywordEntered:
    print """
       %d
       %i
       %o
       %u
       %x
       %X
       %e
       %E
       %f
       %F
       %g
       %G
    """
    exitKeyWord()
  elif "operators" in keywordEntered:
    print """
       +
       -
       *
       **
       /
       //
       %
       <
       >
       <=
       >=
       ==
       !=
       <>
       ( )
       [ ]
       { }
       @
       ,
       :
       .
       =
       ;
       +=
       -=
       *=
       /=
       //=
       %=
       **=
      """
    exitKeyWord()
  elif "string escape sequence" in keywordEntered:
    print """
       \\ 
       \"
       \a
       \b
       \f
       \n
       \r
       \t
       \v
       %c
       %r
       %s
       %%
      """
    exitKeyWord()
  else: 
    print "You did not enter a keyword, please try again"
    exitKeyWord()

theKeyWordModule()
