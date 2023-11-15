class Mastermind:
    def __init__(self):
        # self._secret, self.gus = [random.randint(1, 6) for _ in range(4)], 0
        self._secret, self.gus = [i for i in range(4)], 0

    def guess(self, guess: list[int], cbf):
        if len(guess) != 4: return [self.get_insults(0, 'what?!?'), self.guess(cbf(), cbf)]
        self.gus += 1
        ans = ''.join(["*" for i, j in enumerate(self._secret) if str(j) == guess[i]])
        ans += ans.join(["o" for i, j in enumerate(self._secret)if str(j) != guess[i] and str(j) in guess])
        print(ans)
        if ans == '****': return [self.get_insults(2,self.gus)]  
        if '*' in ans:
            return [self.get_insults(1,f"'{guess}'"),self.guess(cbf(), cbf)]
        return [self.get_insults(0,f"'{guess}'"),self.guess(cbf(), cbf)]

    
    def get_insults(self, x=0,y=0):
        insults = [
            [
            f"Your guess is {y} How pathetic! Are you even trying?",
            f"Your guess is {y} Ugh, your brain must be as dull as a rusty spoon.",
            f"Your guess is {y} Did you even read the instructions, or are you just pretending to be dumb?",
            f"Your guess is {y} Oh, look who's here, the embodiment of failure.",
            f"Your guess is {y} You're so hopeless, it's almost adorable...almost.",
            f"Your guess is {y} Wow, your logic skills are on par with a potato. Congratulations!",
            f"Your guess is {y} A+ for effort, F for intelligence.",
            f"Your guess is {y} Your answer is as incorrect as your life choices.",
            f"Your guess is {y} Did you mistake this game for a cakewalk? You're way out of your league.",
            f"Your guess is {y} Pathetic. Just...pathetic."
            ], [
            f"Your guess is {y} Are you even trying? Your answer is completely wrong, but at least you managed to write it in a somewhat legible manner.",
            f"Your guess is {y} Did your brain go on vacation? Your answer couldn't be more off, but I'll give you a smidge of credit for your impressive ability to be consistently clueless.",
            f"Your guess is {y} I can't believe I have to deal with your incompetence. Your answer is so wrong that it's almost impressive... in a sad, pitiful way.",
            f"Your guess is {y} Seriously, why are you even here? Your answer is absolutely incorrect, but hey, you've mastered the art of getting things totally and utterly wrong. Impressive, I guess.",
            f"Your guess is {y} Do you enjoy embarrassing yourself? Because your answer is so far from the mark that it's almost amusing...in a painful way. At least you're consistent in your failures."
            ], [
            f"Your persistence in trying for {y} times is, I suppose, somewhat respectable.",
             f"I guess your efforts aren't completely worthless. Only takes {y} rounds. Keep it up, I suppose.",
             f"Your performance, though subpar and {y} long, is still better than nothing. Just barely."
             ]
        ]
        print(insults[x][random.randint(0, len(insults) - 1)])

#mastermind tsundere ver.
import random
def ip(): return input('what is your guess?: ')
Mastermind().guess(ip(), ip)
