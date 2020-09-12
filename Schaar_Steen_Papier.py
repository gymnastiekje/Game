import random

class bcolors:
    ENDC='\033[0m'
    BOLD='\033[01m'         # vet
    DISABLE='\033[02m'      # lichter
    UNDERLINE='\033[04m'    # onderlijnt
    REVERSE='\033[07m'      # witte achtergrond
    STRIKETHROUGH='\033[09m'
    INVISIBLE='\033[08m'    # onzichtbaar
class text:   
    BLACK='\033[30m'
    RED='\033[31m'
    GREEN='\033[32m'
    ORANGE='\033[33m'
    BLUE='\033[34m'
    PURPLE='\033[35m'
    CYAN='\033[36m'
    LIGHTGREY='\033[37m'
    DARKGREY='\033[90m'
    LIGHTRED='\033[91m'
    LIGHTGREEN='\033[92m'
    YELLOW='\033[93m'
    LIGHTBLUE='\033[94m'
    PINK='\033[95m'
    LIGHTCYAN='\033[96m'
class background:    
    BLACK='\033[40m'
    RED='\033[41m'
    GREEN='\033[42m'
    ORANGE='\033[43m'
    BLUE='\033[44m'
    PURPLE='\033[45m'
    CYAN='\033[46m'
    LIGHTGREY='\033[47m'



keuzes = ["Schaar","Steen","Papier"]
def speler_input():
    keuze_speler = input("Uw keuze:")
    while (keuze_speler not in keuzes):
        keuze_speler = input("Dit was geen optie lolbroek. Opnieuw!\U0001F913")
    return keuze_speler


def computer_input():
    computer_keuze = keuzes[random.randint(0,2)]    # kiest element uit lijst; 0, 1 of 2
    return computer_keuze

def who_wins():
    winnaar = 0
    while (winnaar == 0):   # while zorgt ervoor dat het blijft verder gaan als winnaar = 0
        computer = computer_input()
        speler = speler_input()
        if speler == computer:
            winnaar = 0
            print("De computer had ook", computer,", opnieuw!")
            continue
        winnaar = 1 # de volgende if/elif zorgt ervoor dat als jij zou winnen winnaar = 2, anders blijft winnaar 1
        if speler == "Papier" and computer == "Steen":
            winnaar = 2
        elif speler == "Schaar" and computer =="Papier":
            winnaar = 2
        elif speler == "Steen" and computer == "Schaar":
            winnaar = 2
    return(winnaar, speler, computer) # zorgen dat de if/elif statemets in de loop staan
# geen [] bij return als dat niet ndg is. [] duid een lijst aan; () of niets een tupel. 
# lijst = kan aangepast worden; tupel = kan niet aangepast worden




# werking: Dictionary = {"key":value
#                       "key":value
#                        etc.}
# dictionary[key]=value

# emojis["papier"] geeft \U...
emojis ={ "Schaar": "\U0001F596",
         "Steen": "\U0001F44A",
         "Papier": "\U0001F91A"}
# avatar["Kakje"] geeft \U...
avatar ={"Kakje":"\U0001F4A9",
          "Raket":"\U0001F680",
          "Smiley":"\U0001F600"}
# avatar["Kakje"] geeft text.
cavatar ={"Kakje": text.ORANGE,
          "Raket": text.CYAN,
          "Smiley": text.YELLOW}

avatar_keuze = ["Kakje", "Raket", "Smiley"]

print("Welkom bij schaar, steen, papier tegen de \U0001F63A \n"
      "Je kan je figuur kiezen uit:(Hoofdlettergevoelig): \n"
      ,text.ORANGE," \U0001F4A9",bcolors.ENDC,"Kakje \n"
      ,text.CYAN," \U0001F680",bcolors.ENDC," Raket \n"
      ,text.YELLOW," \U0001F600",bcolors.ENDC," Smiley")
avatar_speler = input("Maak uw keuze:")
while (avatar_speler not in avatar_keuze):
    avatar_speler = input("Dit is geen optie lolbroek.")
    


print(text.YELLOW,"Nu kunnen we beginnen.\n"
      "Je kan kiezen tussen: (Hoofdlettergevoelig): \n"
      "\U0001F596 Schaar\n"
      "\U0001F44A Steen\n"
      "\U0001F91A Papier")


score_speler = 0
score_computer = 0

while(1):   # while(x) herhaalt enkel als uw x niet gelijk is aan 0
    winnaar, speler, computer = who_wins() # volgorde is belangrijk! Hier heb je who_wins() die [winnaar, speler, computer] bevat. 
    if winnaar == 1:                       # Daarna stel ik dat winnaar=winnnaar, speler=speler, computer=computer; als volgorde verschillend is stel ik bv. computer=speler
        print(emojis[speler],"verliest tegen", emojis[computer])
        score_computer += 1
    elif winnaar == 2:
        print(emojis[speler], "wint tegen", emojis[computer])
        score_speler += 1
    if score_computer<score_speler:
        print(cavatar[avatar_speler]+avatar[avatar_speler]+bcolors.ENDC, text.GREEN, score_speler, bcolors.ENDC,"-", text.RED,score_computer,bcolors.ENDC, text.DARKGREY+"\U0001F63A"+bcolors.ENDC)
    elif score_computer>score_speler:
        print(cavatar[avatar_speler]+avatar[avatar_speler]+bcolors.ENDC, text.RED,score_speler, bcolors.ENDC,"-", text.GREEN,score_computer,bcolors.ENDC, text.DARKGREY+"\U0001F63A"+bcolors.ENDC )
    else:
        print(cavatar[avatar_speler] + avatar[avatar_speler], bcolors.ENDC, text.PURPLE, score_speler, bcolors.ENDC,"-", text.PURPLE, score_computer, bcolors.ENDC, text.DARKGREY+"\U0001F63A"+bcolors.ENDC)
    a=input("Press 1 to quit, Enter to continue")
    

    

# schaar verliest steen
# steen verliest papier
# papier verliest schaar

# gelijk = 0
# computer gewonnen = 1
# speler gewonnen = 2
