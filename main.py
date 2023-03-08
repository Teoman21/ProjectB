
def showPrompt():
    print("şirket ekleme<")


def insert_compay():


    while True:
        command = input("istediğiniz komutu girin: ")
        if command == "şirket ekleme":
            name = input("şirkte ismi girin: ")
            information = input("şirket bilgilkerini girin: ")
            companyList = {name: information}

        if command == "şirketleri gör":
            for company in companyList:
                print(company)

        if command == "çık":
            break

insert_compay()