import os
from download import InstaDownload, YTDownload

# List to store command history
command_history = []

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            # Display the custom prompt header
            print("\033[1;32m●─\033[1;34mo Select:\033[0m")
            print("\033[1;32m┢── \033[1;34m1. YouTube\033[0m")
            print("\033[1;32m┣── \033[1;34m2. Instagram\033[0m")
            print("\033[1;32m┣── \033[1;31m3. History\033[0m")
            print("\033[1;32m┣── \033[1;31mCtrl + C : Exit\033[0m")
            print("\033[1;32m┗────➡ \033[0m", end="")

            # Capture the user input
            choice = int(input())
            if choice == 1:
                url = input("Enter Youtube Video URL : ")
                YTDownload(url)
                command_history.append(f"YouTube Download  : {url}")
            elif choice == 2:
                url = input('Enter Instagram video link: ')
                InstaDownload(url)
                command_history.append(f"Instagram Download: {url}")
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31m●─\033[1;34mo Command History:\033[0m")
                for idx, command in enumerate(command_history, start=1):
                    print(f"\033[1;32m┣ {idx}. {command}\033[0m")
                input("\nPress Enter to continue...")
            else:
                print("Invalid choice. Please select again.")
                input("\nPress Enter to continue...")
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print('\n\033[1;31mExiting...\033[0m')
            break

if __name__ == '__main__':
    main()
