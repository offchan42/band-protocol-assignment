"""
As Boss Baby's assistant, your task is to check if Boss Baby has sought revenge
for every shot aimed at him at least once and hasn't initiated any shooting himself.

The task above is simply about evaluating the value of 2 predicates:
1. whether boss Baby has sought revenge for every shot aimed at him
2. whether boss Baby has initiated shooting himself
He is a good boy if both of these predicates are true. Otherwise, he is a bad boy.

The second predicate is less computationally expensive, so we will evaluate it
first. We can check whether the first character in the list of events is an 'R'
(retaliation) or not. This is O(1) time complexity.

The first predicate is more computationally expensive, so we will evaluate it
after the second predicate. We will iterate over the list of events and track the
number shots that Boss Baby has to revenge.
At the end of the iteration, we will check whether the number of shots to revenge
is zero or not. If it is zero, then Boss Baby is a good boy. Otherwise, he is a
bad boy.

This is O(n) time complexity. n is the number of events in the input string.
And O(1) memory complexity because we are not storing any additional other than
the the shots counter. The input string is not counted as part of the memory
complexity because it is referenced rather than copied.
"""


def is_good_boy(events):
    # if Boss Baby initiates shooting, then he is a bad boy
    if events[0] == "R":
        return False

    shots_to_revenge = 0
    for event in events:
        if event == "S":
            shots_to_revenge += 1
        elif event == "R":
            if shots_to_revenge > 0:
                shots_to_revenge -= 1

    # if there are no shots to revenge, then Boss Baby is a good boy
    return shots_to_revenge == 0


if __name__ == "__main__":
    inp = input()
    answer = "Good boy" if is_good_boy(inp) else "Bad boy"
    print(answer)
