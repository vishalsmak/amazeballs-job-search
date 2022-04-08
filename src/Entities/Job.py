from src.Entities.Company import Company

class Job:
    """ Class to hold all details for a Job"""

    def __init__(self, 
    id: str,
    key: str,
    title: str,
    description: str,
    email: str,
    isRemote: bool,
    **kwargs):
        self._id = id
        self._key = key
        self._title = title
        self._description = description
        self._email = email
        self._is_remote = isRemote

    """ ID Getter"""
    @property
    def id(self):
        return self._id

    """ ID Setter"""
    @id.setter
    def id(self, value):
        self._id = value

    """ Key Getter"""
    @property
    def key(self):
        return self._key

    """ Key Setter"""
    @key.setter
    def key(self, value):
        self._key = value

    """ Title Getter"""
    @property
    def title(self):
        return self._title

    """ Title Setter"""
    @title.setter
    def title(self, value):
        self._title = value

    """ Company Getter"""
    @property
    def company(self):
        return self._company

    """ Company Setter"""
    @company.setter
    def company(self, value):
        self._company = value

    """ Description Getter"""
    @property
    def description(self):
        return self._description

    """ Description Setter"""
    @description.setter
    def description(self, value):
        self._description = value

    """ Email Getter"""
    @property
    def email(self):
        return self._email

    """ Email Setter"""
    @email.setter
    def email(self, value):
        self._email = value

    """ Is Remote Getter"""
    @property
    def is_remote(self):
        return self._is_remote

    """ Is Remote Setter"""
    @is_remote.setter
    def is_remote(self, value):
        self._is_remote = value

    """ Keywords Getter"""
    @property
    def keywords(self):
        return self._keywords

    """ Keywords Setter"""
    @keywords.setter
    def keywords(self, value):
        self._keywords = value

    @classmethod
    def from_json(self, data):
        self.company = Company.from_json(data["company"])
        retval =  self(**data)
        retval.keywords = [] #TODO : Parse keywords from retval.description and add here
        return retval

    @classmethod
    def list_from_json(self, data):
        return list(map(self.from_json, data["docs"]))
