from bs4 import BeautifulSoup
import re



#Wyatt Chrisman
#CS 021
#Create a program that allows users to find leading statistics in a certain
#category in the NHL

def main():
    print("You will be getting statistics from the NHL") #print opening statement
    

    with open('NHL_Stats.html') as html_file: #open html and remove data
        soup = BeautifulSoup(html_file, 'html.parser')

    div_values = soup.find_all('div', class_="styles__LeaderListContainer-owf6ne-4 cOAcdw") #divide data
     
    all_players, leaders = get_data(div_values) #send data to getdata() and receive list of players
                                                #and a list of the leaders of each category

    count1 = 0 #set all counts to 0
    count2 = 0
    count3 = 0
    count4 = 0

    names, scores, leader_name, leader_score = split_data(all_players, leaders, count1, count2)
    #send list of players and leaders as well as 2 counts and recieve the players name and score in seperate lists

    skaters_final, goalies_final, defenseman_final, rookies_final = sort_data(names, scores, leader_name, leader_score,count3)
    #send lists of players,scores, and a counter to receive the names and scores in the same list but in their correct categories

    choice = prompt_user()
    #supply user with all choices and receive submission

    results(choice, skaters_final, goalies_final, defenseman_final, rookies_final, count4)
    #send user choice, skaters_final, goalies_final, defenseman_final, rookies_final, and a counter to results() to finish the program

def results(choice, skaters_final, goalies_final, defenseman_final, rookies_final, count): #takes in the users choice for what they want to do,
    #as well as all the player's names and corresponding points in their correct categories.  This will then be formatted based on their choice
    #and is formatted with print() statements for visual appeal.  At the end of each choice, they will be sent to continue_program() to see if they
    #would like to continue or end
    if choice == '1': #choice one takes the first skaters name (the one with the most points) and their points total which follows
        print()       #and is formatted in a sentence for the user
        print(f"The skater with the most points is {skaters_final[0]} with {skaters_final[1]} points.")
        print()
        continue_program() 
    elif choice == '2': #choice 2 usese a while loop and a conuter to parse through the skater_final list and prints the skaters
        print()         #name and points total in a table
        print("Skater Name     Points")
        while count <= 19:
            print(f"  {skaters_final[count]:15} {skaters_final[count+1]}")
            count+=2
        print()
        continue_program()
    elif choice == '3': #choice 3 does the same as choice one but with defenseman
        print()
        print(f"The defenseman with the most points is {defenseman_final[0]} with {defenseman_final[1]} points")
        print()
        continue_program() 
    elif choice == '4': #choice 4 does the same as choice two but with defenseman
        print()
        print("Defenseman Name     Points")  
        while count <= 19:
            print(f"    {defenseman_final[count]:17} {defenseman_final[count+1]}")
            count+=2
        print()
        continue_program()
    elif choice == '5': #choice 5 does the same as choice one but with rookies
        print()
        print(f"The rookie with the most points is {rookies_final[0]} with {rookies_final[1]} points.")
        print()
        continue_program()
    elif choice == '6': #choice 6 does the same as choice two but with rookies
        print()
        print("Rookie Name     Points")
        while count <= 19:
            print(f"  {rookies_final[count]:15} {rookies_final[count+1]}")
            count+=2
        continue_program()
    elif choice == '7': #choice 7 ends the program and thanks user
        print()
        print("Thank you for using this program!!!")
        return
    else: #else statement validates user's input and brings them back to main if it is invalid
        print()
        print("Error: value not accepted")
        print("Please enter a valid response")
        main()
            
            

def prompt_user(): #this does not take anything in but provides the user with all their
    print()        #choices and what each on will do and then returns user's choice
    print("What statistic would you like?")
    print("Skater points leader: 1")
    print("Top 10 Skater points leaders: 2")
    print("Defenseman points leader: 3")
    print("Top 10 Defenseman points leaders: 4")
    print("Rookie points leader: 5")
    print("Top 10 Rookie points: leader 6")
    print("End Program: 7")
    print()
    print("Please enter the number corresponding to the statistic.")
    user_choice = input()
    return user_choice
    
def sort_data(names, scores, leader_name, leader_score,count):
    #this takes in the lists of all the player's names and scores as well as the leaders
    #in seperate lists and sorts them into the corresponding and correct section and
    #returns those lists to the user
    
    skaters_final = []
    goalies_final = []
    defenseman_final = []
    rookies_final = []
    #set blank lists to put the information into
    
    for name in names: #parsing throgh all of the information and placing data into
        #proper sections 9 at a time and using the counter to do that correctly
        while 0<=count<=8 :
            skaters_final.append(names[count])
            skaters_final.append(scores[count])
            count+=1
        while 9<=count<=17:
            goalies_final.append(names[count])
            goalies_final.append(scores[count])
            count+=1
        while 18<=count<=26:
            defenseman_final.append(names[count])
            defenseman_final.append(scores[count])
            count+=1
        while 27<=count<=35:
            rookies_final.append(names[count])
            rookies_final.append(scores[count])
            count+=1                     

    #placing all of the leaders and points into their corresponding section
    skaters_final.insert(0, leader_name[0])
    skaters_final.insert(1, leader_score[0])

    goalies_final.insert(0, leader_name[1])
    goalies_final.insert(1, leader_score[1])

    defenseman_final.insert(0, leader_name[2])
    defenseman_final.insert(1, leader_score[2])

    rookies_final.insert(0, leader_name[3])
    rookies_final.insert(1, leader_score[3])

    
    return skaters_final, goalies_final, defenseman_final, rookies_final
    
def split_data(players,leaders,count1, count2): #takes in the list of all the players and leaders which are connected to their points
    #total and splits up the data and puts them into seperate list

    #creating all needed blank lists
    name_and_number = []
    leader_name_and_number = []
    name_list = []
    number_list = []
    leader_names = []
    leader_numbers = []
    
    

    while count1 < 36: #taking in the first 36 players and points and splitting them up and putting them into a
                       #list that has each player with their points being the next thing in the list
        data = players[count1]
        split_up = [re.findall(r'(\w+?)(\d+)', data)[0]]
        name_and_number.append(split_up)
        count1+=1
        
    while count2 < 4: #same process is repeated for the leaders
        stats = leaders[count2]
        split = [re.findall(r'(\w+?)(\d+)', stats)[0]]
        leader_name_and_number.append(split)
        count2+=1
    

    for name in name_and_number: #appending player names into a list
        name_list.append(name[0][0]) 

    for number in name_and_number: #appending player points into a list
        number_list.append(number[0][1])

    for name in leader_name_and_number: #putting leader name into a list
        leader_names.append(name[0][0])

    for number in leader_name_and_number: #putting leader points into a list
        leader_numbers.append(number[0][1])
        
    return name_list, number_list, leader_names, leader_numbers


def get_data(div): #takes in list of all data together and splits by div, ul, then li and returns large sum of data

    #setting blank lists to add to 
    player_data = []
    leaders_data = []
    
    for name in div:
        ul_tags = name.find_all(class_="styles__LeaderList-owf6ne-5 ANxrZ leaders-list") #opens ul
        for li in ul_tags:
            li_tags = li.find_all(class_="styles__LeaderListItem-owf6ne-6 eTUABY") #opens li for all players that arent the leader
            li_leader = li.find_all(class_="styles__LeaderListItem-owf6ne-6 eTUABY active") #opens li for the leader of each category

            for names in li_tags: #adds players and their points to a list
                names = names.text
                player_data.append(names)

            for leaders in li_leader: #adds leaders and their points to a list
                leaders = leaders.text
                leaders_data.append(leaders)
            
    return player_data, leaders_data
                

def continue_program(): #validates if the user would like to continue the program or quit
    print()
    answer = input("Would you like to continue? (Y/N) ") #ask user
    answer = answer.lower() #set response to lowercase

    if answer == 'y': #continue if y
        main()
    elif answer == 'n': #end if n and thank user
        print()
        print("Thank you for using this program!!!")
        return
    else:
        print("Error: character not accepted.") #have user resubmit if not y or n
        print()
        continue_program()
        
    

main()
