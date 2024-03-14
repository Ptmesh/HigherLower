import random
from art import logo, vs
from gamedata import data

def form_data(user):
    username = user["name"]
    user_desc = user["description"]
    user_country = user["country"]
    return f"{username} , a {user_desc} from {user_country}"
def get_random_account():
  return random.choice(data)
def check_ans(guess , a_follower , b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
should_continue = True
user_a = get_random_account()
user_b = get_random_account()

while should_continue:
    print(f"Total Score = {score}")
    user_a = user_b
    user_b = get_random_account()

    while user_a == user_b:
        user_b = get_random_account()

    print(f"Compare A : {form_data(user_a)}")
    print(vs)
    print(f"Compare B : {form_data(user_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

    a_count = user_a["follower_count"]
    b_count = user_b["follower_count"]

    is_correct = check_ans(guess, a_count, b_count)

    if is_correct:
        score += 1
        print(f"You're right!!🥳 ")
    else:
        print(f"Sorry , that's wrong 😔")
        should_continue = False