import random
#random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...

def scores_grades():
    for i in range(0, 10):
        random_num = random.randint(60, 100)
        
        if random_num >= 60 and random_num <= 69:
            print "Score: {}; Your grade is D".format(random_num)
        elif random_num >= 70 and random_num <= 79:
            print "Score: {}; Your grade is C".format(random_num)
        elif random_num >= 80 and random_num <= 89:
            print "Score: {}; Your grade is B".format(random_num)
        elif random_num >= 90 and random_num <= 100:
            print "Score: {}; Your grade is A".format(random_num)

scores_grades()