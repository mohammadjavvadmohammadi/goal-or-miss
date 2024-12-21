import random

# تابع برای گرفتن ورودی معتبر
def get_guess(player_name):
    while True:
        guess = input(f"{player_name} (goal / miss) نوبت خودته ، یه غیب بگو ببینیم  ").strip()
        if guess in ["goal", "miss"]:
            return guess
        else:
            print("حدس نامعتبر است(goal or miss).")

# تابع اصلی بازی
def game():
    print("به بازی گل یا پوچ خوش آمدید")
    
    # گرفتن نام دو بازیکن
    player1_name = input(":نام کامل بازیکن اول را وارد کنید ").strip()
    player2_name = input(":نام کامل بازیکن اول را وارد کنید ").strip()
    
    # امتیاز اولیه برای هر بازیکن
    player1_score = 0
    player2_score = 0
    
    # تعداد دورهای بازی
    rounds = 1
    
    while True:
        print(f"\n---راند{rounds} ---")
        
        # انتخاب تصادفی "گل" یا "پوچ"
        result = random.choice(["goal", "miss"])
        
        # بازیکن اول حدس می‌زند
        print(f"\nنوبت {player1_name}:")
        player1_guess = get_guess(player1_name)
        if player1_guess == result:
            print(f"{player1_name} ایول! عجب حدسی: {result}")
            player1_score += 1
        else:
            print(f"{player1_name} اه، اشتباه بود ، اما عب نداره ادامه بده:{result}")
        
        # بازیکن دوم حدس می‌زند
        print(f"\nturn{player2_name}:")
        player2_guess = get_guess(player2_name)
        if player2_guess == result:
            print(f"{player2_name} ایول! عجب حدسی: {result}")
            player2_score += 1
        else:
            print(f"{player2_name}اه ، اشتباه بود ، اما عب نداره ادامه بده {result}")
        
        # نمایش امتیازات
        print(f"\nامتیازات فعلی")
        print(f"{player1_name}: {player1_score} امتیاز")
        print(f"{player2_name}: {player2_score} امتیاز")
        
        # سوال برای ادامه بازی
        play_again = input("\nبنظر من یدست دیگه هم بازی کن ، میخوای ؟(بله/خیر) ").strip().lower()
        if play_again != "بله":
            print("\nبازی تموم شد")
            if player1_score > player2_score:
                print(f"\n{player1_name} برنده شد ، بالاخره به حقش رسید{player1_score} - {player2_score}")
            elif player2_score > player1_score:
                print(f"\n{player2_name} برنده شد ، خیلی ام تلاش کرد {player2_score} - {player1_score}")
            else:
                print(f"\nمساوی شد ، همه چی به نفع داورس {player1_score} - {player2_score}")
            break
        
        # افزایش تعداد دورها
        rounds += 1

# اجرای بازی
game()