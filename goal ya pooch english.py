import random

# تابع برای گرفتن ورودی معتبر
def get_guess(player_name):
    while True:
        guess = input(f"{player_name} (goal / miss)your turn's ").strip()
        if guess in ["goal", "miss"]:
            return guess
        else:
            print("invalid(goal or miss).")

# تابع اصلی بازی
def game():
    print("Weolcome to game")
    
    #  نام دو بازیکن
    player1_name = input("please enter your ful number player1: ").strip()
    player2_name = input("please enter your ful number player1:").strip()
    
    # امتیاز اولیه برای هر بازیکن
    player1_score = 0
    player2_score = 0
    
    # تعداد دورهای بازی
    rounds = 1
    
    while True:
        print(f"\n---round{rounds} ---")
        
        #انتخاب تصادفی
        result = random.choice(["goal", "miss"])
        
        # بازیکن اول حدس می‌زند
        print(f"\nturn {player1_name}:")
        player1_guess = get_guess(player1_name)
        if player1_guess == result:
            print(f"{player1_name} exellent work: {result}")
            player1_score += 1
        else:
            print(f"{player1_name} oh I'm sorry:{result}")
        
        # بازیکن دوم حدس می‌زند
        print(f"\nturn{player2_name}:")
        player2_guess = get_guess(player2_name)
        if player2_guess == result:
            print(f"{player2_name}good job {result}")
            player2_score += 1
        else:
            print(f"{player2_name} oh I'm sorry{result}")
        
        # نمایش امتیازات
        print(f"\nscore")
        print(f"{player1_name}: {player1_score} score")
        print(f"{player2_name}: {player2_score} score")
        
        # سوال برای ادامه بازی
        play_again = input("\n you want play again(yes / no) ").strip().lower()
        if play_again != "بله":
            print("\n finish game")
            if player1_score > player2_score:
                print(f"\n{player1_name}winner{player1_score} - {player2_score}")
            elif player2_score > player1_score:
                print(f"\n{player2_name} winner {player2_score} - {player1_score}")
            else:
                print(f"\nresult {player1_score} - {player2_score}")
            break
        
        # افزایش تعداد دورها
        rounds += 1
game()