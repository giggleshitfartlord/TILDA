import csv



class Drama():

    def __init__(self, name, rating, actors, viewship, genre, director, writer, year, no_of_episodes, network):
        self.name = name
        self.rating = rating
        self.actors= actors
        self.viewship = viewship
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.no_of_episodes = no_of_episodes
        self.network = network

    def __str__(self):
        print(f"Dramat heter {self.name} och släpptes år {self.year} från nätverket {self.network}")

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        else:
            return False

    def episoder(self):
        print(f"Dramat {self.name} har {self.no_of_episodes} avsnitt")

    def info_om_dramat(self):
        print(f"Dramat heter {self.name} och är en {self.genre}serie. Den har en rating på {self.rating} och har setts {self.viewship}.\n Skådespelarna i filmen är {self.actors}, är producerad av {self.director} och skriven av {self.writer}.\n Den släpptes år {self.year} och gavs ut av {self.network}. Den har {self.no_of_episodes} avsnitt idag.")

def read_file(filename):
    drama_list = []
    with open (filename, mode = "r") as drama_file:
        csvfile = csv.reader(drama_file, delimiter= "\t" )
        next(csvfile)
        for line in csvfile:
            drama = line[0]
            drama = drama.split(",")
            drama_name = Drama(drama[0], drama[1], drama[2], drama[3], drama[4], drama[5], drama[6], drama[7], drama[8], drama[9])
            drama_list.append(drama_name)
            
        return drama_list
    
def search_drama_list(list):
    search_item = input("Vad för drama vill du söka efter, skriv namnet på dramat. ")
    for i in list:
        if i.name == search_item:
            print(f"Ja, {search_item} finns i listan")
            return
    print(f"Nej, {search_item} finns inte i listan")
        

if __name__ == "__main__":
    list = read_file("kdrama.csv")
    for i in list:
        print(i.info_om_dramat())

