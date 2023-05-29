import os 
import re
import jokeHandler


def osclear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    
    osclear()
    print('\tFörläng Livet med skratt och en rolig historia')


    url = 'https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky?blacklistFlags=religious,political,nsfw&type=single'
    JSONStringExt = 'joke'

    jokeCounter = 1
    jokeObject = jokeHandler.jokeHandler(url, JSONStringExt)


    while True:
        t_Joke = jokeObject.getJoke()
        t_Joke = re.sub("(\n)", "\n\t\t", t_Joke) # Replaces the \n in the API output with \n\t\t so it's nicely formatted

        print(f'''\n\n\t\t{jokeCounter}. {t_Joke}''')

        jokeCounter += 1
        anotherone = input(f'\n\n\tDo you want to hear another joke? y/N')
        if anotherone != 'y':
            break
        
    

main()