#!/usr/bin/env python3

class UserData(object):
    def __init__(self, num, name):
        self.num = num
        self._name = name

    def __repr__(self):
        return "ID:{} Name:{}".format(self.num, self._name)


class NewUser(UserData):
    group = "shiyanlou-louplus"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print("ERROR")

    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id, name):
        return "{}'s id is {}".format(name, id)
    def __repr__(self):
        return "{}'s id is {}".format(self._name, self.num)


if __name__ == "__main__":
    print(NewUser.get_group())
    print(NewUser.format_userdata(109, "Lucy"))    


    """
    user1 = NewUser(101, "Jack")
    user1.name = "Lou"
    user1.name = "Jackie"
    user2 = NewUser(102, "Louplus")
    print(user1.name)
    print(user2.name)
    """
