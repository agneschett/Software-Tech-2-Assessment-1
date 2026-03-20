count = 0

def main():
    n = eval(input("Enter number of disks: "))
    # Find the solution recursively
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')
# The function for finding the solution to move n disks
# from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global count
    if n == 1: # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)
        count += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        count += 1
        moveDisks(n - 1, auxTower, toTower, fromTower)

main() # Call the main function
print(f"Number of moves is {count}")