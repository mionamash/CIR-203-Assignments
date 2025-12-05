
node1 = {"data": "Apple", "next": None}
node2 = {"data": "Banana", "next": None}
node3 = {"data": "Cherry", "next": None}
node4 = {"data": "Date", "next": None}


node1["next"] = node2
node2["next"] = node3
node3["next"] = node4


head = node1

current = head

print("Linked List (Fruits):")
while current is not None:
    print(current["data"])
    current = current["next"]
