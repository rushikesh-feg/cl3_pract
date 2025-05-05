import Pyro5.server
from concat_class import Concatenator

# Start the Pyro5 daemon and register the object
def main():
    daemon = Pyro5.server.Daemon()  # start the server
    uri = daemon.register(Concatenator)
    print("Server is ready. Object uri:", uri)

    # Start request loop
    daemon.requestLoop()

if __name__ == "__main__":
    main()
