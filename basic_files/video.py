class WrongDurationError(Exception):
    def __init__(self):
        pass


class WrongYearError(Exception):
    def __init__(self):
        pass



class Video:
    def __init__(self, name: str, duration: int, year: int) -> None:
        try:
            self.name = name
            self.duration = duration
            self.year_of_production = year
            if not isinstance(self.duration, int):
                raise WrongDurationError()

            if not isinstance(self.year_of_production, int):
                raise WrongYearError()

        except WrongDurationError:
            print("Musisz podać długość filmu używając samych cyfr!")

        except WrongYearError:
            print("Musisz podać rok produkcji filmu używając samych cyfr!")

    def show_vid_information(self):
            print(f"film o tytule {self.name}, trwa {self.duration} minut, z {self.year_of_production} roku")






