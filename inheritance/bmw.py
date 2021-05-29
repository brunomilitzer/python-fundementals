from abc import abstractmethod, ABC


class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        # print("Starting the car")
        pass

    @abstractmethod
    def stop(self):
        # print("Stopping the car")
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):

    def __init__(self, cruise_control_enabled, make, model, year):
        super().__init__(make, model, year)
        self.cruise_control_enabled = cruise_control_enabled

    def display(self):
        print(self.cruise_control_enabled)

    def start(self):
        super().start()
        print("Button Start")

    def stop(self):
        super().stop()
        print("Stopping Three Series")

    def drive(self):
        print("Three Series driving")


class FiveSeries(BMW):

    def __init__(self, parking_assisted_enabled, make, model, year):
        super().__init__(make, model, year)
        self.parking_assisted_enabled = parking_assisted_enabled

    def display(self):
        print(self.parking_assisted_enabled)

    def start(self):
        super().start()
        print("Remote Start")

    def stop(self):
        super().stop()
        print("Stopping Five Series")

    def drive(self):
        print("Five Series driving")


threeSeries = ThreeSeries(True, "BMW", "328i", "2021")
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.display()

threeSeries.start()
threeSeries.stop()
threeSeries.drive()

fiveSeries = FiveSeries(True, "BMW", "530i", "2021")
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.display()

fiveSeries.start()
fiveSeries.stop()
fiveSeries.drive()