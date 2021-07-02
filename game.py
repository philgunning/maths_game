import random

def game(player, my_score, max_scorer, max_score):
    
    operators = ['+', '-', '*']
    score = 0
    lives = 3
    streak = 0
    alive = True
    diff1 = 1
    diff2 = 10

    while alive:
        n1 = random.randint(diff1, diff2)
        n2 = random.randint(diff1, diff2)
        op = operators[random.randint(0,2)]
        problem = (f"{n1} {op} {n2}")
        solution = eval(problem)
   
        print()
        print(f"BEST SCORE: {max_scorer} - {max_score}")
        print(f"{player}'s BEST SCORE: {my_score}")
        print(f"STREAK: {streak}")
        print(f"SCORE: {score}")
        print(f"LIVES: {lives}")
        print()
        print(f"What is {problem}?")
        answer = False
        while type(answer) != int:
            try:
                answer = int(input("Answer: "))
            except:
                print(f"Sorry that doesn't seem like a number, try again.")
        print()

        test = answer == solution

        if test:
            print(f"Correct, {problem} = {solution}")
            score += 1
            streak += 1
        else:
            print(f"Sorry, the answer to {problem} was {solution}")
            streak = 0
            lives -= 1
            diff1 = 1
            diff2 = 10

        if streak %10 == 0 and streak != 0:
            diff1 -= 5
            diff2 += 5

        if lives == 0:
            alive = False
            print("You have ran out of lives, GAME OVER!")
            return score


def start():
    player = input("What is your name?: ").title()
    scores = get_scores()
    max_scorer = ''
    max_score = 0
    my_score = 0
    for user,score in scores.items():
        if score > max_score:
            max_scorer = user
            max_score = score
        if user == player:
            my_score = score


    play = True
    while play:
        this_score = game(player, my_score, max_scorer, max_score)
        if this_score > my_score:
            my_score = this_score

        scores[player] = my_score
        if my_score > max_score:
            max_score = my_score
            max_scorer = player

        ip = input(f"\n\nWould you like to play again, {player}? (Y/N): ").upper()
        if ip == 'N':
            play = False
        elif ip == 'Y':
            continue
        else:
            print("Couldn't understand your input, game exiting.")
            play = False
        
    set_scores(scores)
    

def set_scores(scores):
    with open('hiscores.txt', 'w+') as w:
        for k,v in scores.items():
            w.write(f"{k},{v}\n")

def get_scores():
    try:
        with open('hiscores.txt', 'r+') as r:
            scores = [s.strip('\n').split(',') for s in r.readlines()]
            scores = dict(scores)
            for k,v in scores.items():
                scores[k] = int(v)
    except:
        scores = {}
    return scores

        
if __name__ == "__main__":
    start()
 