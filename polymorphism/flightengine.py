class Flight:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


class AirBusEngine:
    def start(self):
        print("Starting Airbus engine")

class BoeingEngine:
    def start(self):
        print("Starting Boeing engine")


ae = AirBusEngine()
f1 = Flight(ae)
f1.start_engine()


be = BoeingEngine()
f2 = Flight(be)
f2.start_engine()
