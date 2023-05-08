from abc import ABC, abstractmethod
from system_access import SupportSystemAccess, SalesSystemAccess, ManagerSystemAccess


class Account(ABC):
    def __init__(self, username):
        self.username = username
        self.permission_list = []
        self.create_account()

    @abstractmethod
    def create_account(self):
        pass

    def show_permissions(self):
        return [permission.name for permission in self.permission_list]

    def add_permission(self, permission):
        self.permission_list.append(permission)


class SupportAccount(Account):
    def create_account(self):
        self.add_permission(SupportSystemAccess(True))


class SalesAndSupportAccount(Account):
    def create_account(self):
        self.add_permission(SalesSystemAccess(True))
        self.add_permission(SupportSystemAccess(True))


class ManagerAccount(Account):
    def create_account(self):
        self.add_permission(ManagerSystemAccess(True))
