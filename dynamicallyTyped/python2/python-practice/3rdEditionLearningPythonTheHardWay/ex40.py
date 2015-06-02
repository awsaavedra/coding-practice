#Objects, Modules, and classes
#Y[x] = "get X from Y"

#Objects: State (variables are things an obj has) and behaviors(things an obj does)

class Song(object):
  def __init__(self,lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line

  def rap_to_me(self):
    for line in self.lyrics:
      print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", "with a pocket full of shells"])
wutang_clan = Song(['Wutang clan aint', 'nottin to fuck with'])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wutang_clan.rap_to_me()