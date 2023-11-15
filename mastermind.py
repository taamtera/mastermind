class Mastermind:
    def __init__(self) -> None:
        self._secret,self.gus = [random.randint(1, 6) for _ in range(4)],0

    def guess(self, guess: list[int], cbf, fin):
        if len(guess) != 4: return [print('Invalid guess'),self.guess(cbf(), cbf, fin)]
        print('Your guess is:', guess) ; self.gus += 1
        ans = ''.join(["*" for i, j in enumerate(self._secret) if str(j) == guess[i]])
        ans += ans.join(["o" for i, j in enumerate(self._secret) if str(j) != guess[i] and str(j) in guess])
        print(ans)
        return fin(self.gus) if ans == '****' else self.guess(cbf(), cbf, fin)


import random
print('Playing Mastermind with 6 colors and 4 positions.')
def ip(): return input('what is your guess?: ')
def win(x): return print(f'you solved it after {x} rounds')
Mastermind().guess(ip(), ip, win)