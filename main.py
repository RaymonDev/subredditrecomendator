

namesarray = [] #array that stores all the recomendation values

#gathers and creates the CSV with the History data
def datagathering():

    import sqlite3
    import csv
    try:

        con = sqlite3.connect(r"YOUR PATH TO HISTORY FILE ") #connect to the History file on the path
        c = con.cursor()
        c.execute("select url, title, visit_count, last_visit_time from urls") #query the results
        results = c.fetchall() #fetch the results


        with open('data.csv', 'w', newline='', encoding='utf-8') as file: #create the file witht the custom name
            writer = csv.writer(file)

            for r in results:
                title = r[1]


                writer.writerow([title]) #writes all the information in the columns
        print("\n---------------------------")
        print("File created succesfully")
        print("\n---------------------------")
    except:
        print("\n---------------------------")
        print("Error generating the data")
        print("\nIf you have Google Chrome open, please close it")
        print("\nIf the error continues, please change the \"History\" path in line 12 of source code")
        print("---------------------------\n")
        input("\nPress enter to continue...")
        quit()


#saves all the clean data in the array
def datarecomendation(filename):



    from csv import reader #import the reader

    #read the csv
    with open(filename, 'r', encoding="utf-8") as read_obj:

        print("\n- CSV created successfully")

        csv_reader = reader(read_obj)

        for rowname in csv_reader:

            #clean the string
            stringtext = str(rowname)
            stringtext = stringtext.replace("['", "")
            stringtext = stringtext.replace("']", "")

            try:
                if str(list(stringtext)[0]).isupper() == True:

                    splitarray = stringtext.split()[0]
                    splitarray = splitarray.replace(":", "")
                    splitarray = splitarray.replace("|", "")
                    if splitarray not in namesarray:
                        namesarray.append(splitarray) #save the string if it's not already in the array
            except:
                pass

        #print(namesarray)


#writes all the recomended subreddits and descriptions on a txt file
def returnresults():

    import praw as pr
    from tqdm import tqdm #import the progress bar


    #generate the client for the Reddit API
    reddit = pr.Reddit(
        client_id="x",  # Client ID of the Reddit bot
        client_secret="x",  # Secret Client ID
        user_agent="testscript by YOUR NAME",  # brief description
        username="x",  # Username (to avoid some 403 errors)
        password=""  # password (to avoid some 403 errors)
    )

    counter = 0

    #generate the file with the recomendations
    with open("recommended_subreddits.txt", "w+", encoding="utf-8") as file:
        print("\n- Recommendation file created successfully, writing the recomendations in file...\n")
        for i in tqdm(namesarray): #progress bar
            try:
                subreddit = reddit.subreddit(str(i))

                if subreddit.public_description != "":

                    #writes the name and the description of the subreddit
                    file.write(f"\n- The recommended subreddit is \"r/{subreddit}\" with description \"{subreddit.public_description}\"")

            except:
                pass

    file.close()


#final function
def final_action():
    import os
    os.remove("data.csv") #removes the CSV
    print("\n- CSV removed successfully")


#main
if __name__ == '__main__':
    datagathering()
    datarecomendation("data.csv")
    returnresults()
    final_action()
    print("\n")
    print("\nProcess finished successfully")
    print("\n")
    input("Press enter to continue...")
