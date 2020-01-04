import random
def Game(n, debug = False):
  class GameOver(Exception):
    pass
  cakes = n
  def plural(x):
    if x == 1: return str(x) + " cake"
    else: return str(x) + " cakes"
  if cakes <= 0: raise RuntimeError("At least one cake required")
  new_player = Player(cakes)
  #first ask player if he wish to move first
  first = new_player.firstmove(cakes)
  last = 0
  if debug: print plural(cakes), "on the table. You decided to move", "first" if first else "last"
  # now, let's game begin
  while 1:
    # my move
    if not first:
      allow = []
      for i in range(1,4):
        if cakes >= i and i != last:
          allow.append(i)
      if not len(allow): raise GameOver("Stalemate")
      last = random.choice(allow)
      cakes -= last
      if not cakes:
        if debug: print "Yum! I ate the last cake, you win!"
        return True
      if debug: print "I ate ", plural(last), ", ", plural(cakes), " still left"
    else: first = False
    # your move
    if cakes == 1 and last == 1:
      if debug: print "I lead you to stalemate, so you are winner"
      return True
    move = new_player.move(cakes, last)
    if move > 4: raise RuntimeError("You are so greedy! Don't try to eat more than 3 cakes.")
    if not move in [1,2,3]: raise RuntimeError("Illegal move (must be 1, 2 or 3, type Number)")
    if move == last: raise RuntimeError("You cannot eat the same quantity of cakes as you opponent on previous move")
    if move > cakes: raise RuntimeError("Don't try to eat more cakes that left on table")
    if move == cakes: raise GameOver("You ate the last cake!")
    cakes -= move
    last = move
    if debug: print "You ate ", plural(move), ",", plural(cakes), "still left"
