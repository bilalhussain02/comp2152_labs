import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

def main():
    try:
        weaponRoll = random.randint(1, 6)

        print(f"Weapon roll {weaponRoll}")
        print(f"Hero's weapon {weapons[weaponRoll - 1]}")

        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll <= 4:
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend")

        if weaponRoll != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


