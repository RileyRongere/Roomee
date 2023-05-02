#Matching Algorithm

#Testing testing

print("testing")

match_list = []

def clean(user1, user2, score):
    if user1["clean"] == user2["clean"]:
        score = score + 3
    if user1["clean"]+1 == user2["clean"]:
        score = score + 2
    if user1["clean"]-1 == user2["clean"]:
        score = score + 2
    if user1["clean"]+2 == user2["clean"]:
        score = score + 1
    if user1["clean"]-2 == user2["clean"]:
        score = score + 1

def noise(user1, user2, score):
    if user1["noise"] == user2["noise"]:
        score = score + 3
    if user1["noise"]+1 == user2["noise"]:
        score = score + 2
    if user1["noise"]-1 == user2["noise"]:
        score = score + 2
    if user1["noise"]+2 == user2["noise"]:
        score = score + 1
    if user1["noise"]-2 == user2["noise"]:
        score = score + 1

def space(user1, user2, score):
    if user1["space"] == user2["space"]:
        score = score + 3
    if user1["space"]+1 == user2["space"]:
        score = score + 2
    if user1["space"]-1 == user2["space"]:
        score = score + 2
    if user1["space"]+2 == user2["space"]:
        score = score + 1
    if user1["space"]-2 == user2["space"]:
        score = score + 1

def busy_week(user1, user2, score):
    if user1["busy_week"] == user2["busy_week"]:
        score = score + 3
    if user1["busy_week"]+1 == user2["busy_week"]:
        score = score + 2
    if user1["busy_week"]-1 == user2["busy_week"]:
        score = score + 2
    if user1["busy_week"]+2 == user2["busy_week"]:
        score = score + 1
    if user1["busy_week"]-2 == user2["busy_week"]:
        score = score + 1

def busy_weekend(user1, user2, score):
    if user1["busy_weekend"] == user2["busy_weekend"]:
        score = score + 3
    if user1["busy_weekend"]+1 == user2["busy_weekend"]:
        score = score + 2
    if user1["busy_weekend"]-1 == user2["busy_weekend"]:
        score = score + 2
    if user1["busy_weekend"]+2 == user2["busy_weekend"]:
        score = score + 1
    if user1["busy_weekend"]-2 == user2["busy_weekend"]:
        score = score + 1

def age(user1, user2, score):
    if user1["age"] == user2["age"]:
        score = score + 3
    if user1["age"]+1 == user2["age"]:
        score = score + 2
    if user1["age"]-1 == user2["age"]:
        score = score + 2
    if user1["age"]+2 == user2["age"]:
        score = score + 1
    if user1["age"]-2 == user2["age"]:
        score = score + 1

# both users must have same gender preference to be matched
def gender(user1, user2):
    if user1["pref_gender"] == 3 and user2["pref_gender"] == 3:
        match_list.append(user2)
    elif user1["pref_gener"] == user2["gender"] and user2["pref_gender"] == user1["gender"]:
        match_list.append(user2)
        