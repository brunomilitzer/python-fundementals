class ObjectCounter:

    number_of_objects = 0

    def __init__(self):
        ObjectCounter.number_of_objects+=1

    @staticmethod
    def display_count():
        print(ObjectCounter.number_of_objects)


o1 = ObjectCounter()
o2 = ObjectCounter()
o3 = ObjectCounter()

ObjectCounter.display_count()