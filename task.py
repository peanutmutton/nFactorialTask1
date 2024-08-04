

class UserManager():
    userDict = {}
    idCount = 0
    def addUser(self, name:str):
        self.idCount += 1
        self.userDict.update({self.idCount:name})
        return self.idCount

    def getUser(self, id:int):
        for key in self.userDict.keys():
            if id == key:
                return self.userDict[key]
        return None
    def deleteUser(self, id:int):
        if self.getUser(id) == None:
            return False
        else:
            self.userDict.pop(id)
            return True

    def findUserByName(self, name:str):
        listOfMatches = []
        for dict_item in self.userDict.items():
            if dict_item[1] == name:
                listOfMatches.append(dict_item[0])
        return listOfMatches



# #Пример использования на Python:
# userManager = UserManager()
#
# id1 = userManager.addUser("Jarasar")
# id2 = userManager.addUser("Adil")
# id3 = userManager.addUser("Jarasar")
#
#
# print(userManager.getUser(id1))  # Вернет "Jarasar"
# print(userManager.getUser(id2))  # Вернет "Adil"
# print(userManager.getUser(999))  # Вернет None
#
# print(userManager.findUserByName("Jarasar"))  # Вернет [id1, id3]
# print(userManager.findUserByName("Baha"))  # Вернет []
#
# print(userManager.deleteUser(id2))  # Вернет True
# print(userManager.deleteUser(999))  # Вернет False
#
# print(userManager.getUser(id2))  # Вернет None
#
