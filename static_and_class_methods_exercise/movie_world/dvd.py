import calendar


class DVD:
    def __init__(self, name: str, id_dvd: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_dvd
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_dvd_crt: int, name: str, date: str, age_restriction: int):
        reformated_date = date.split('.')
        year = int(reformated_date[2])
        mount = calendar.month_name[int(reformated_date[1])]

        return cls(name, id_dvd_crt, year, mount, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
