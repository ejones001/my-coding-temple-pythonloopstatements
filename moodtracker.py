import random

# Define the list of moods
moods = ["sad", "happy", "energetic", "calm", "angry", "content", "excited"]

# Define the days of the week and times of the day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

# Simulate the mood tracker
for day in days:
    for time in times_of_day:
        # Randomly select a mood from the list
        mood = random.choice(moods)
        # Print the mood for the current day and time
        print(f"On {day} {time} you were {mood}")
