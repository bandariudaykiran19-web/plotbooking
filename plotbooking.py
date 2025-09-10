print("1. 1BHK")
print("2. 2BHK")
print("3. 3BHK")
print("4. 4BHK")

ch=float(input("Enter ur choice:"))
match(ch):
    case 1:
        print("1.Room,1 Hall")
        print("price=2,00,000")
        c=float(input("Book your room with money:"))
        d=c-200000
        print("remaining money is=({})".format(d))
       
    case 2:
        print("2,Rooms,1,hall,1 kictchen")
        print("price=5,00,000")
        c=float(input("BOok your room with money:"))
        d=c- 500000
        print("Remaining money is=({})".format(d)) 
    
    case 3:
        print("3.Rooms,1 hall,2 Bedrroms")
        print("price=12,00,000")
        c=float(input("Book your room with money:"))
        d=c-1200000
        print("Remaining money is=({})".format(d))
    
    case 4:
        print("4rooms,1 hall,1 kictech,2 room")
        print("price=24,00,000")
        c=float(input("BOOk your room with money:"))
        d=c-2400000
        print("remaining money is=({})".format(d))
    
print("thank your for coming")
       