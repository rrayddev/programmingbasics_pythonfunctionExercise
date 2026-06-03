#function called convert_minutes
#parameters: number_of_episodes, duration_per_episode (in minutes)
#calculate into hour and remaining minutes

number_of_episodes = float(input("Masukan Jumlah Episode: "))
duration_per_episodes = float(input("Masukan durasi episode (In Minute): "))

def convert_minutes(number_of_episodes, duration_per_episodes):
    total_minutes = number_of_episodes * duration_per_episodes
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    return hours, remaining_minutes

jam, menit = convert_minutes(number_of_episodes, duration_per_episodes)
print("\n==========================================")
print("          DURASI TONTONAN ANIME           ")
print("==========================================")
print(f"Total Episode  : {number_of_episodes} Episode")
print(f"Durasi / Eps   : {duration_per_episodes:.0f} Menit")
print("------------------------------------------")
print(f"Total Waktu    : {jam:.0f} Jam {menit:.0f} Menit")
print("==========================================\n")