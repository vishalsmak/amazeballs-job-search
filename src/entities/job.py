from src.entities.company import Company
from src.logic.resume_parser.resume_parser import *


class Job:
    """Class to hold all details for a Job"""

    def __init__(
        self, id: str, key: str, title: str, description: str, **kwargs
    ):
        self._id = id
        self._key = key
        self._title = title
        self._description = description

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
    def from_json(cls, data):
        cls.company = Company.from_json(data["company"])
        retval = cls(**data)
        keywords = job_result_wrapper(
            " ".join([retval._title, retval._description]), False
        )
        retval.keywords = keywords["skills"] + [keywords["name"]]
        return retval

    @classmethod
    def list_from_hub_json(cls, data):
        return list(map(cls.from_json, data["docs"]))

    @classmethod
    def to_dict(cls):
        dic = {}
        for attr in vars(cls):
            attr_value = getattr(cls, attr)
            if isinstance(attr_value, Company):
                point_dict = vars(attr_value)
                dic[attr] = point_dict
            else:
                dic[attr] = attr_value
        return dic
