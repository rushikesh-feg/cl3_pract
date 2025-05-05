import Pyro5.api

@Pyro5.api.expose
class Concatenator:
    def concatenate(self, a, b):
        return a + b
