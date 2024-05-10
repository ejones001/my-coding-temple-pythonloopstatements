# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track counter
track_number = 1

# Loop through each genre
index = 0
while index < len(genres):
    genre = genres[index]
    print(f"Track {track_number}: This song belongs to the {genre} genre.")
    track_number += 1
    if genre == 'Hip-hop':
        print("The loop has stopped.")
        break
    index += 1
