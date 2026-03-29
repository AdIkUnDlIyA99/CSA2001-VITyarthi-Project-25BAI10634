from utils import get_recommendations
print("🎮 GameMatch AI (CLI Model)\n")
ram=input("Enter RAM (e.g. 16 GB): ")
cpu = input("Enter CPU: ")
gpu = input("Enter GPU: ")
genre = input("Enter Genre: ")
results = get_recommendations(ram, cpu, gpu, genre)
print("\n🔥 Recommendations:\n")
for game in results:
    print(f"🎮 {game['title']}")
    print(f"   {game['description']}")
    print(f"   ⭐ {game['rating']} | {game['year']}\n")
