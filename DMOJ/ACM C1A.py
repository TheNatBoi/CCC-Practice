N = int(input())
for i in range(N):
    choice = str(input())
    if choice == 'Scissors':
        print("Rock")
    elif choice == 'Paper':
        print("Scissors")
    elif choice == 'Rock':
        print("Paper")
    elif choice == 'Fox':
        print("Foxen")
    elif choice == "Foxen":
        break