import random

def main():
    
    wins_user = 0
    wins_computer = 0
    draw = 0
    round = 1


    def options():
            options = ('piedra', 'papel', 'tijera')
            user_option = str(input("Eliga una opción: ")).lower()
            computer_option = random.choice(options)

            while user_option not in options:
                print("Opción invalida")
                user_option = str(input("Eliga una opción correcta: ")).lower()
                if user_option in options:
                    break

            return user_option, computer_option

    def who_wins(user_option, computer_option, wins_user, wins_computer, draw):
        win_decider = {'piedra':'tijera', 'papel':'piedra', 'tijera':'papel'}
        if win_decider[user_option] == computer_option:
                print(f"User ha ganado eligiendo {user_option} y computer {computer_option}")
                wins_user += 1
        elif user_option == computer_option:
                print(f"Ha sido un empate, ambos eligieron {user_option}")
                draw += 1
        else:
                print(f"User ha perdido eligiendo {user_option} y computer {computer_option}")
                wins_computer += 1
        return wins_user, wins_computer, draw
    

    while wins_user < 3 or wins_computer <= 3 or draw <= 3:
         print("*"*5)
         print(f"Round N.{round}")
         print("*"*5)

         user_option, computer_option = options()
         wins_user, wins_computer, draw = who_wins(user_option, computer_option, wins_user, wins_computer, draw)
         round += 1
         if wins_user == 3:
              print("Has ganado")
              break
         elif wins_computer ==3:
              print("Has perdido")
              break
         elif draw == 3:
              print("Han empatado")
              break
         
if __name__ == "__main__":
     main()
     print("Cri e kga")