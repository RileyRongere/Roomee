#Matching Algorithm

#mock user list
user_list=[]


def sleep(user1, user2, score):
    if user1["sleep"]=user2["sleep"]:
        score=score+3
    if user1["sleep"]+1=user2["sleep"]:
        score=score+2
    if user1["sleep"]-1=user2["sleep"]:
        score=score+2
    if user1["sleep"]+2=user2["sleep"]:
        score=score+1
    if user1["sleep"]-2=user2["sleep"]:
        score=score+1
    retun score

def wake_up(user1,user2,score):
    if user1["wake"]=user2["wake"]:
        score=score+3
    if user1["wake"]+1=user2["wake"]:
        score=score+2
    if user1["wake"]-1=user2["wake"]:
        score=score+2
    if user1["wake"]+2=user2["wake"]:
        score=score+1
    if user1["wake"]-2=user2["wake"]:
        score=score+1
    return score
    
def pet(user1,user2,user_list):
    if user1["want_pets"]=0 and user2["have_pets"]=1:
        user_list.remove(user2)
    if user1["have_pets"]=1 and user2["want_pets"]=0:
        user_list.remove(user2)

def friends_over(user1,user2,score):
    if user1["friends"]=user2["friends"]:
        score=score+3
    if user1["friends"]+1=user2["friends"]:
        score=score+2
    if user1["friends"]-1=user2["friends"]:
        score=score+2
    if user1["friends"]+2=user2["friends"]:
        score=score+1
    if user1["friends"]-2=user2["friends"]:
        score=score+1
    return score

def smoking(user1,user2,user_list):
    if user1["smokes"]=1 and user2["allows_smoking"]=0:
        user_list.remove(user2)
    if user1["allows_smoking"]=0 and user2["smokes"]=1:
        user_list.remove(user2)

def intro_extro(user1,user2,user_list):
    if user1['type_e_i']=user2['type_e_i']:
        score=score+2

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
    if user1["pref_gener"] != user2["gender"] and user2["pref_gender"] != user1["gender"]:
        user_list.remove(user2)
    if user1["gender"] == 3 and user2["pref_gender"] == 3:
        user_list.append(user2)






def main:
    high=[]
    med=[]
    low=[]
    for users in users_list:
        score=0
        smoking(user1,user,user_list)
        if user in user_list:
            pet(user1,user,user_list)
        if user in user_list:
            gender(user1,user,user_list)
        if user in user_list:
            score1=intro_extro(user1,user,score)
            score2=friends_over(user1,user,score1)
            score3=wake_up(user1,user,score2)
            score4=clean(user1,user,score3)
            score5=noise(user1,user,score4)
            score6=space(user1,user,score5)
            score7=busy_week(user1,user,score6)
            score8=busy_weekend(user1,user,score7)
            score9=age(user1,user,score8)
            final_score=sleep(user1,user,score9)
            if final_score < 5:
                low.append(user)
            elif final_score > 0:
                high.append(user)
            else:
                med.append(user)




        
