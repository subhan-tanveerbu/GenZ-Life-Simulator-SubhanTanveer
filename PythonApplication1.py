# Subhan Tanveer BSAI 3A (01-136242-041)
# 🌟🌟🌟 GenZ Gym Life Simulator 🌟🌟🌟
# --------------------------------------------------------
# welcome to the most chaotic yet motivating gym sim ever 😭💪
# this program lets u live ur best gym-rat fantasy fr
# vibey dialogues + workouts + stats = peak productivity ✨
# made for assignment but lowkey fun to play not gonna lie 😎
# --------------------------------------------------------

print("💫 welcome to the GenZ Gym Life Sim 💫")

name = input("👋 hey bestie, what’s ur name? ")

# lil chat before gym starts
print(f"\nsooo {name}, before we hit the gym... how’s life today?")
mood = input("how u feeling rn? (happy / tired / lazy / pumped / idk): ").lower().strip()

if mood == "happy":
    print("aww yess good vibes only 🥰 keep it up bestie")
elif mood == "tired":
    print("same 😩 but like... gym might wake us up a bit idk 🤷")
elif mood == "lazy":
    print("lol same 😭 let’s just move a lil and call it progress ok?")
elif mood == "pumped":
    print("YOOO that’s the spirit 🔥 let’s get that PR today!")
else:
    print("ok mysterious mood 😎 i respect the vibe")

# ask for gym goal
goal = input("\n🎯 what’s the goal for today? (muscle / weight loss / strength): ").lower().strip()

# player stats (NEW FIELD: confidence)
player = {
    "energy": 100,
    "motivation": 80,
    "progress": 0,
    "confidence": 50,   # NEW FIELD 🌟
    "mood": mood
}

# workout lists
workouts = {
    "muscle": [
        "🏋️ Bench press - 4x10",
        "💪 Bicep curls - 3x12",
        "🔥 Push-ups till failure",
        "🦵 Leg press - 4x10",
        "🍗 Eat protein after gym fr!"
    ],
    "weight loss": [
        "🏃 Jog or cycle - 30 mins",
        "🚶 Walk fast - 20 mins",
        "🤸 Jumping jacks - 3x30",
        "🧘 Chill yoga - 10 min cool down",
        "🥗 Eat light & drink water 💧"
    ],
    "strength": [
        "🏋️ Deadlifts - 5x5",
        "🦵 Squats - 4x8",
        "💥 Pull-ups - 4 sets",
        "🏋️ Overhead press - 3x8",
        "🥩 eat big sleep deep 😴"
    ]
}

# show stats
def show_stats():
    print("\n📊 ur current stats rn:")
    print(f"⚡ energy: {player['energy']}")
    print(f"🔥 motivation: {player['motivation']}")
    print(f"⭐ progress: {player['progress']}")
    print(f"💥 confidence: {player['confidence']}")   # NEW FIELD
    print(f"🧠 mood: {player['mood']}")
    print("--------------------------")

# show workout plan
def show_workout(goal):
    print("\n💪 today’s workout plan:")
    plan = workouts.get(goal)
    if not plan:
        print("😅 idk that goal tbh... try typing muscle / weight loss / strength again?")
        return
    for ex in plan:
        print("➡️", ex)

# menu
def menu():
    print("\nwhat we doing now?")
    print("1️⃣ workout time 💪")
    print("2️⃣ eat something healthy 🥗")
    print("3️⃣ take a rest day 😴")
    print("4️⃣ check stats 📊")
    print("5️⃣ quit 🚪")

# main game loop
while True:
    menu()
    choice = input("👉 pick (1-5): ").strip()

    if choice == "1":
        print(f"\n🔥 ok {name}, we going all in on that {goal.upper()} grind!!")
        show_workout(goal)
        player["energy"] -= 20
        player["progress"] += 10
        player["motivation"] += 5
        player["confidence"] += 7   # NEW 🌟
        player["mood"] = "💪 pumped"
        print("✅ workout done! lowkey proud of u rn 😎")

    elif choice == "2":
        print("\n🥗 nicee! u ate clean, that’s some discipline 🔋")
        player["energy"] += 15
        if player["energy"] > 100:
            player["energy"] = 100
        player["motivation"] += 5
        player["confidence"] += 3    # NEW 🌟
        player["mood"] = "😋 full & happy"
        print("food = serotonin = success 🍔✨")

    elif choice == "3":
        print("\n😴 rest dayyy let’s goo 💯 netflix counts as recovery right?")
        player["energy"] = 100
        player["motivation"] -= 5
        player["confidence"] -= 2    # NEW 🌟
        player["mood"] = "😴 chill"
        print("you feel relaxed but kinda lazy ngl 😂")

    elif choice == "4":
        show_stats()

    elif choice == "5":
        print(f"\n👋 aight {name}, proud of u for staying consistent 💪")
        show_stats()
        print("✨ drink water, stretch, and touch grass sometimes lol ✨")
        break

    else:
        print("💀 bruh that’s not even an option... try again pls 😂")

    # stat cleanup
    if player["energy"] < 0:
        player["energy"] = 0
    if player["motivation"] > 100:
        player["motivation"] = 100
    if player["motivation"] < 0:
        player["motivation"] = 0
    if player["progress"] > 100:
        player["progress"] = 100
    if player["confidence"] > 100:     # NEW LIMIT
        player["confidence"] = 100
    if player["confidence"] < 0:
        player["confidence"] = 0
