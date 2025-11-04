#Even or Odd

def even_odd(*args):
    cmd = args[len(args) - 1]
    listNums = [int(args[i]) for i in range (0, len(args) - 1)]
    if cmd == "even":
        return [i for i in listNums if i % 2 == 0]
    elif cmd == "odd":
        return [i for i in listNums if i % 2 == 1]