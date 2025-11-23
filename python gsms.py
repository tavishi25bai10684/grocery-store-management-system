# ============================================================
# MODULE 1: LOAD ITEMS FROM FILE
# ============================================================
def load_items(filepath):
    itemAvailableDict = {}

    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("⚠️ Error: Items file not found!")
        return {}

    print("\n****************** ITEMS AVAILABLE IN OUR STORE *********************")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        try:
            price = float(parts[-1])
        except ValueError:
            continue

        name = " ".join(parts[:-1]).title()
        print(f"{name}: {price}")
        itemAvailableDict[name] = price

    print("*********************************************************************")
    return itemAvailableDict


# ============================================================
# MODULE 2: ADD ITEMS TO CART
# ============================================================
def add_to_cart(itemAvailableDict):
    shoppingDict = {}

    proceed = input("\nDo you want to proceed shopping? (yes/no): ").lower()

    while proceed == "yes":
        item = input("Add an item: ").title()

        if item in itemAvailableDict:
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("⚠️ Invalid quantity! Enter a number.")
                continue

            subtotal = itemAvailableDict[item] * qty

            shoppingDict[item] = {
                "quantity": qty,
                "SubTotal": subtotal
            }

            print("\nItem added:", shoppingDict)

        else:
            print("⚠️ Item not found!")

        proceed = input("Add more items? (yes/no): ").lower()

    return shoppingDict


# ============================================================
# MODULE 3: GENERATE BILL
# ============================================================
def generate_bill(shoppingDict):
    print("\n*********************** BILL SUMMARY ************************")
    print(f"{'Item':15} {'Qty':6} {'SubTotal'}")
    print("--------------------------------------------------------------")

    total = 0

    for item in shoppingDict:
        qty = shoppingDict[item]["quantity"]
        sub = shoppingDict[item]["SubTotal"]
        total += sub

        print(f"{item:15} {qty:6} {sub}")

    print("--------------------------------------------------------------")
    print(f"TOTAL BILL: {total}")
    print("********************* THANK YOU ******************************")
    print("Hope to see you back soon!")


# ============================================================
# MAIN PROGRAM
# ============================================================
# Welcome message
user = input("Please enter your name: ").upper()
msg = f"WELCOME TO MY STORE {user}"
print("\n" + "*" * len(msg))
print(msg)
print("*" * len(msg))

# Load items
filepath = r"C:\Users\admin\Downloads\grocery store management.txt"
itemAvailableDict = load_items(filepath)

# If file loaded successfully
if itemAvailableDict:
    # Add items to cart
    shoppingDict = add_to_cart(itemAvailableDict)

    # Generate final bill
    if shoppingDict:
        generate_bill(shoppingDict)
    else:
        print("\nNo items were added. Exiting...")