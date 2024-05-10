import random

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Loop through each genre by index
for i in range(len(genres)):
    genre = random.choice(genres)
    track_number = i + 1  # Adding 1 to index to get the track number

    # Check if genre is suitable for the light show
    if genre == 'Classical':
        print(f"Skipping track {track_number} as Classical genre is not suitable for the light show.")
        continue

    print(f"Track {track_number}: The light show is ready for the {genre} genre.")
