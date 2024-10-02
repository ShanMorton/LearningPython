fav_movies = ["The Hunt for Red October", "Deuce Bigelow", "Field of Dreams"]

print(fav_movies[0])

print(fav_movies[1])

print(fav_movies[2])

#How long is the list, how many items are in the list?
print(len(fav_movies))

#Add an item to the end.
fav_movies.append("Major League")

#How long is the list, how many items are in the list?
print(len(fav_movies))

print(fav_movies)

#add a movie to the list but not at the end
fav_movies.insert(1, "The Rookie")

print(fav_movies)

del(fav_movies[2])
print(fav_movies)

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
print(fav_movies)


