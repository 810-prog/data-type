import os
def list_all():
    for x in os.listdir():
        print(x)

def list_folders():
    for x in os.listdir():
        if os.path.isdir(x):
            print(x)

def list_files():
    for x in os.listdir():
        if os.path.isfile(x):
            print(x)

def main():
    print("Mini Terminal Started! Type 'exit' to quit.")
    while True:
        command = input("\n ""Terminal> ").strip().lower()
        if command == "ls":
            list_all()
        elif command == "lsfolder":
            list_folders()
        elif command == "lsfiles":
            list_files()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("invalid command")
          
if __name__ == "__main__":
    main()
