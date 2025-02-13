# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): 
    if title == None or genre == None or rating == None:
        return None
    return {"title" : title, "genre" : genre, "rating" : rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0 

    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        sum += movie["rating"] 

    return sum / len(user_data["watched"]) 

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    
    genre_dictionary = {}
    
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dictionary:
            genre_dictionary[movie["genre"]] = 1
        else:
            genre_dictionary[movie["genre"]] += 1

    # gets max value from dictioanry and returns the key
    max_genre = max(genre_dictionary, key = genre_dictionary.get)

    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_watched_list(user_data):
    friend_watched_list = []
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friend_watched_list.append(friend_movie)
    return friend_watched_list


def get_unique_watched(user_data):
    friend_list = get_friend_watched_list(user_data)
    unique_list = []

    for movie in user_data["watched"]:
        if movie not in friend_list:
            unique_list.append(movie)

    return unique_list


def get_friends_unique_watched(user_data):
    friend_list = get_friend_watched_list(user_data)
    unique_list = []

    for movie in friend_list:
        if movie not in user_data["watched"] and movie not in unique_list:
            unique_list.append(movie)
    return unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_watched_list = (get_friends_unique_watched(user_data))
    recommended_movie_list = []
    
    for movie in friend_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movie_list.append(movie)

    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friend_watched_list = (get_friends_unique_watched(user_data))
    recommended_movie_list = []

    for movie in friend_watched_list:
        if movie["genre"] == most_watched_genre:
            recommended_movie_list.append(movie)
    
    return recommended_movie_list

def get_rec_from_favorites(user_data):
    user_watched_list = get_unique_watched(user_data)
    recommended_movie_list = []

    for movie in user_data["favorites"]:
        if movie in user_watched_list:
            recommended_movie_list.append(movie)
    
    return recommended_movie_list
