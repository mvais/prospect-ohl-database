class Utils:

    @classmethod
    def flatten(cls, lst):
        return [item for sublist in lst for item in sublist]

