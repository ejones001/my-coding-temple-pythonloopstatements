import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Relaxed", "Anxious"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through the days of the week
for i in range(len(days_of_week)):
    # Select a random mood for the current day
    mood = random.choice(moods)
    # Print the mood for the current day
    print(f"On {days_of_week[i]}, I was feeling {mood}.")
