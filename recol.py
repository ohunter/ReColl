from tqdm import trange, tqdm

solved = []

def eval(a, b):
    if a == b/2:
        return 0
    elif a == 3*b+1:
        return 1
    else:
        return -1

class ReCol():
    # @profile
    def __init__(self, v):
        if v % 1 != 0:
            return None
        self.value = v

        # Even value that resolves in current value
        self.evenPar = None
        self.evenChl = solved[v // 2 - 1] if len(solved) >= v // 2 and v % 2 == 0 else None

        # Odd value that resolves in current value
        self.oddPar = solved[v // 3 - 1] if len(solved) >= v // 3 and (v // 3) % 2 == 1 and v // 3 > 1 and v % 2 == 0 else None
        self.oddChl = None

        if self.evenChl:
            self.evenChl.evenPar = self
        if self.oddPar:
            self.oddPar.oddChl = self

        solved.append(self)

    # @profile
    def __str__(self):
        li = []

        root = self

        while root.evenChl or root.oddChl:
            if root.evenChl and root.evenChl in solved:
                root = root.evenChl
            elif root.oddChl and root.oddChl in solved:
                root = root.oddChl
            else:
                break

        ntv = [("", root, True)]

        while ntv:
            li.append(ntv[0])

            try:
                solved.pop(solved.index(ntv[0][1]))
            except ValueError:
                pass

            tmp = []

            if ntv[0][1].evenPar:
                tmp.append((
                    f"{ntv[0][0]}{'  ' if ntv[0][2] else '│ '}",
                    ntv[0][1].evenPar,
                    True if not ntv[0][1].oddPar else False
                ))

            if ntv[0][1].oddPar:
                tmp.append((
                    f"{ntv[0][0]}{'  ' if ntv[0][2] else '│ '}",
                    ntv[0][1].oddPar,
                    True
                ))
            ntv = tmp + ntv[1:]

        return "\n".join([f"{x[0]}{'└ ' if x[2] else '├ '}{x[1].value}" for x in li])

    def __repr__(self):
        if self.value % 2 == 0:
            return f"{self.value} {self.evenChl.value if self.evenChl else None}"
        else:
            return f"{self.value} {self.oddChl.value if self.oddChl else None}"

if __name__ == "__main__":

    for i in trange(1, 10000000):
        ReCol(i)

    # with open("sequence.out", "w") as fi:
    #     for x in tqdm(solved):
    #         print (x.__repr__(), file=fi)

    # with open("collatz.out", "w") as fi:
    #     for x in tqdm(solved):
    #         print (x, file=fi)