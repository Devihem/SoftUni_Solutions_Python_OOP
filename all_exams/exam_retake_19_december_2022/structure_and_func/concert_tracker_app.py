from oop.all_exams.exam_retake_19_december_2022.structure_and_func.concert import Concert
from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band import Band
from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band_members.singer import Singer
from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band_members.guitarist import Guitarist
from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band_members.drummer import Drummer


class ConcertTrackerApp:
    VALID_MUSICIAN = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    CONCERT_SKILLS_NEEDED = {"Rock": {"Guitarist": ["play rock"],
                                      "Drummer": ["play the drums with drumsticks"],
                                      "Singer": ["sing high pitch notes"]},

                             "Jazz": {"Guitarist": ["play jazz"],
                                      "Drummer": ["play the drums with drum brushes"],
                                      "Singer": ["sing high pitch notes", "sing low pitch notes"]},

                             "Metal": {"Guitarist": ["play metal"],
                                       "Drummer": ["play the drums with drumsticks"],
                                       "Singer": ["sing low pitch notes"]}}

    def __init__(self):
        self.bands = []  # obj
        self.musicians = []  # obj
        self.concerts = []  # obj

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")

        if self.searching_for_musician_by_name(name):
            raise Exception(f"{name} is already a musician!")

        created_musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(created_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.searching_for_band_by_name(name):
            raise Exception(f"{name} band is already created!")

        created_band = Band(name)
        self.bands.append(created_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        searched_concert = self.searching_for_concert_by_place(place)
        if searched_concert:
            raise Exception(f"{place} is already registered for {searched_concert.genre} concert!")

        created_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(created_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        searched_musician = self.searching_for_musician_by_name(musician_name)
        if not searched_musician:
            raise Exception(f"{musician_name} isn't a musician!")

        searched_band = self.searching_for_band_by_name(band_name)
        if not searched_band:
            raise Exception(f"{band_name} isn't a band!")

        searched_band.members.append(searched_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        searched_band = self.searching_for_band_by_name(band_name)
        if not searched_band:
            raise Exception(f"{band_name} isn't a band!")

        for member in searched_band.members:
            if member.name == musician_name:
                searched_member = member
                break
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        searched_band.members.remove(searched_member)  # if needed check by name , not with location
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        # Everything is  step by step. For better understanding.

        band_obj = self.searching_for_band_by_name(band_name)
        concert_obj = self.searching_for_concert_by_place(concert_place)

        concert_genre = concert_obj.genre
        members = band_obj.members

        skills_needed_dict = self.CONCERT_SKILLS_NEEDED[concert_genre]

        if not self.searching_for_musician_by_role_type(members):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for musician in members:
            musician_type = type(musician).__name__
            musician_skills = musician.skills

            needed_skills = skills_needed_dict[musician_type]

            for skill in needed_skills:
                if skill not in musician_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        # If all members can play at a concert !

        # profit = "(audience * ticket price) - expenses"
        profit = (concert_obj.audience * concert_obj.ticket_price) - concert_obj.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert_genre} concert in {concert_place}."

    # HELPERS ------------------------------------------------------------------------

    def searching_for_musician_by_name(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician

    def searching_for_band_by_name(self, band_name):
        for band in self.bands:
            if band.name == band_name:
                return band

    def searching_for_concert_by_place(self, concert_place):
        for concert in self.concerts:
            if concert.place == concert_place:
                return concert

    @staticmethod
    def searching_for_musician_by_role_type(musicians_list):
        members_role_dict = {"Drummer": 0, "Singer": 0, "Guitarist": 0}

        for musician in musicians_list:
            members_role_dict[type(musician).__name__] += 1

        if all(members_role_dict.values()):
            return True
        else:
            return False
