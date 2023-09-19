class MovieReview:
  def __init__(self, movie, story, actors, music):
    #Nome do filme
    self.movie_name = movie

    #Avaliação
    self.story_rating = story
    self.actor_rating = actors
    self.music_rating = music

    #Avaliações Médias
    self.avg = int((self.story_rating + self.actor_rating + self.music_rating)/3)

    #Informações do Filme
    self.myrating = {
        "Movie Name" : self.movie_name,
        "Story rating" : self.story_rating,
        "Actor Rating": self.actor_rating,
        "Music Rating": self.music_rating,
        "Avg Rating" : self.avg
    }
  
  def add_movie_ratings(self, movie_list):
        movie_list.append(self.myrating)
  
  
  def avg_star_ratings(self, movie_list):
    for movie in movie_list:
      if(movie["Avg Rating"] == 1 ):
        print("Obrigado pela resposta, você avaliou o filme com   *")
        print(movie)

      elif(movie["Avg Rating"] == 2 ):
        print("Obrigado pela resposta, você avaliou o filme comh   * * ")
        print(movie)

      elif(movie["Avg Rating"] == 3 ):
        print("Obrigado pela resposta, você avaliou o filme com   * * *")
        print(movie)

      elif(movie["Avg Rating"] == 4 ):
        print("Obrigado pela resposta, você avaliou o filme com   * * * *")
        print(movie)

      if(movie["Avg Rating"] == 5 ):
        print("Obrigado pela resposta, você avaliou o filme com   * * * * *")
        print(movie)
      
moviereviews = []

    #Digite o Nome do Filme; 
#Avalie o Ator, a História e a Música numa base de 1 a 5, sendo 5 a nota mais alta.

review1 = MovieReview ("A Vida é Bela", 1, 1, 3)
review1.add_movie_ratings(moviereviews)
review1.avg_star_ratings(moviereviews)


review2 = MovieReview("Titanic", 5, 5, 5)
review2.add_movie_ratings(moviereviews)
review2.avg_star_ratings(moviereviews)

review3 = MovieReview("Homem Aranha", 1, 1, 3)
review3.add_movie_ratings(moviereviews)
review3.avg_star_ratings(moviereviews)