contacts = []
while True:
    print("\nContact Book")
    print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    choice=input("Choose an option: ")
    if choice=="1":
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        email=input("Enter email: ")
        address=input("Enter address: ")
        contacts.append({"name":name,"phone":phone,"email":email,"address":address})
        print("Contact added successfully!")
    elif choice=="2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print(f"Name:{contact['name']},Phone:{contact['phone']}")
    elif choice=="3":
        search=input("Enter name or phone number: ")
        found=False
        for contact in contacts:
            if contact['name']==search or contact['phone']==search:
                print(f"Name:{contact['name']},Phone:{contact['phone']},Email:{contact['email']},Address:{contact['address']}")
                found=True
                break
        if not found:
            print("Contact not found.")
    elif choice=="4":
        search=input("Enter the name: ")
        for contact in contacts:
            if contact['name']==search:
                contact['phone']=input("Enter new phone number: ")
                contact['email']=input("Enter new email: ")
                contact['address']=input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")
    elif choice=="5":
        search=input("Enter the name: ")
        for contact in contacts:
            if contact['name']==search:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")
    elif choice=="6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice, please try again.")
