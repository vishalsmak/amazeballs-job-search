class Company:
    """Class to hold all details for a Company"""

    def __init__(self, id: str, key: str, name: str, website: str, **kwargs):
        self._id = id
        self._key = key
        self._name = name
        self._website = website

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

    """ Name Getter"""

    @property
    def name(self):
        return self._name

    """ name Setter"""

    @name.setter
    def name(self, value):
        self._name = value

    """ Website Getter"""

    @property
    def website(self):
        return self._website

    """ Website Setter"""

    @website.setter
    def website(self, value):
        self._website = value

    @classmethod
    def from_json(self, data):
        return self(**data)
