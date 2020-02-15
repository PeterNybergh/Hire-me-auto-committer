from datetime import timedelta, date
import os
import random as rd



hire_me_arr =  [[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0],
                [1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1], 
                [1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0],
                [1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0],
                [1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1],
                [1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1,0]]



def MakeCommits(lokaldir, foldername, date):
    os.system("mkdir " + foldername)
    os.chdir("my_collection")
    os.system("git init")
    #os.system("git init")
    for i in range(hire_me_arr[0].__len__()):
        for j in range(hire_me_arr.__len__()):
            if hire_me_arr[j][j] == 1:
                for commits in range(10):
                    with open("interesting_numbers.txt", "w+") as f:
                        interesting_number = rd.randint(0,10000)
                        f.write(str(interesting_number) + "\n")
                        f.close()
                    #print('git add interesting_numbers.txt')
                    #print('git commit -m' + str(interesting_number) +  '--date="' + date.isoformat() + 'T00:00:00+0300"')
                    os.system('git add interesting_numbers.txt')
                    os.system('git commit -m' + str(interesting_number) +  '--date="' + date.isoformat() + 'T00:00:00+0300"')
            date = date + timedelta(days = 1)
    os.chdir("..")


def PushAll(dir, foldername, remotedir):
    os.chdir(foldername)
    os.system("git remote add origin " + remotedir)
    os.system("git push -u origin master")
    os.chdir("..")
    
def CreateStartDate():
    current_date = date.today()
    potential_date = current_date - timedelta(days = 316) # 365 - 7 weeks, so the text fits nicely
    
    while(potential_date.weekday() != 6): # 6 = Sunday
        potential_date = potential_date - timedelta(days = 1)

    return potential_date




def main(lokaldir, foldername, remotedir, dates):
    MakeCommits(lokaldir, foldername, dates)
    PushAll(remotedir, foldername, remotedir)


if __name__ == "__main__":

    start_date = CreateStartDate()
    folder_name = "my_collection"
    main(os.getcwd(),
        folder_name,
        'https://github.com/PeterNybergh/Hire-me-auto-committer',
        start_date)

