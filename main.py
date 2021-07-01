import sys
import steganography
import decode_stega

while(True):
    print("Do you want to : ")
    print("\t 1. Hide an image")
    print("\t 2. Decode an image")
    print("\t Press any other number to exit")

    choice = int(0)
    try:
        choice = int(input("Enter your choice : "))
    except Exception as e:
        print(f"Error Msg : {e}")

    if(choice == 1):
        steganography.main()

    elif(choice == 2):
        decode_stega.main()

    else:
        sys.exit()
