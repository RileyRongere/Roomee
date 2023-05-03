#Matching Algorithm

#New plan

def distance(user1, user2, question, score):
    score=abs(user1[question]-user2[question])
    return score


def remove(user1, user2, q1, q2,user_list):
    if user1[q1] == 1 and user2[q2]==0:
        user_list.remove(user2)



def gender(user1, user2, user_list):
    if user1["pref_gener"] != user2["gender"] and user2["pref_gender"] != user1["gender"]:
        user_list.remove(user2)
    if user1["gender"] == 3 and user2["pref_gender"] == 3:
        user_list.append(user2)

#mock user list
user_list=[Jilly, John, Joel]
user1=Kara

question_list=[id_1,id_2,id_3] #Needs to be a list that does not include pet, gender, and amoking questions

def main():
    high=[]
    med=[]
    low=[]
    for user in user_list:
        score=0
        gender(user1, user, user_list)
        if user in user_list:
            remove(user1, user2, have_pet, want_pet,user_list) 
        if user in user_list: 
            remove(user2, user1, have_pet, want_pet,user_list)
        if user in user_list:
            remove(user1, user2, smoke, smoke_ok,user_list) 
        if user in user_list:
            remove(user2, user1, smoke, smoke_ok,user_list)
        if user in user_list:
            for question in question_list:
                score = distance(user1, user, question, score) 
        if score < 3: #Need to be changed
            high.append(user)
        elif score > 15: #Need to be changed
            low.append(user)
        else:
            med.append(user)







