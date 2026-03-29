import requests
RAWG_API_KEY="90519375c4e741ba885741b6abe537c7"
GPU_TIERS={"No dedicated GPU (Integrated graphics)": 1, "NVIDIA GeForce GTX1050": 2, "NVIDIA GeForce GTX 1050 Ti": 3,
    "NVIDIA GeForce GTX 1060 3GB": 3, "NVIDIA GeForce GTX 1060 6GB": 4, "NVIDIA GeForce GTX 1070": 5,
    "NVIDIA GeForce GTX 1070 Ti": 5, "NVIDIA GeForce GTX 1080": 6, "NVIDIA GeForce GTX 1080 Ti": 7,
    "NVIDIA GeForce GTX 1650": 3, "NVIDIA GeForce GTX 1650 Super": 4, "NVIDIA GeForce GTX 1660": 4,
    "NVIDIA GeForce GTX 1660 Super": 5, "NVIDIA GeForce GTX 1660 Ti": 5, "NVIDIA GeForce RTX 2060": 6,
    "NVIDIA GeForce RTX 2060 Super": 6, "NVIDIA GeForce RTX 2070": 7, "NVIDIA GeForce RTX 2070 Super": 7,
    "NVIDIA GeForce RTX 2080": 8, "NVIDIA GeForce RTX 2080 Super": 8, "NVIDIA GeForce RTX 2080 Ti": 9,
    "NVIDIA GeForce RTX 3050": 4, "NVIDIA GeForce RTX 3060": 6, "NVIDIA GeForce RTX 3060 Ti": 7,
    "NVIDIA GeForce RTX 3070": 7, "NVIDIA GeForce RTX 3070 Ti": 8, "NVIDIA GeForce RTX 3080": 9,
    "NVIDIA GeForce RTX 3080 Ti": 9, "NVIDIA GeForce RTX 3090": 10, "NVIDIA GeForce RTX 3090 Ti": 10,
    "NVIDIA GeForce RTX 4060": 6, "NVIDIA GeForce RTX 4060 Ti": 7, "NVIDIA GeForce RTX 4070": 8,
    "NVIDIA GeForce RTX 4070 Super": 8, "NVIDIA GeForce RTX 4070 Ti": 9, "NVIDIA GeForce RTX 4070 Ti Super": 9,
    "NVIDIA GeForce RTX 4080": 9, "NVIDIA GeForce RTX 4080 Super": 10, "NVIDIA GeForce RTX 4090": 10,}
def game_demand(year_str):
    try:
        year=int(year_str)
    except:
        return 5
    if year<2005:
        return 1
    elif year<2010:
        return 2
    elif year<2014:
        return 3
    elif year<2018:
        return 4
    elif year<2021:
        return 6
    elif year<2023:
        return 7
    else:
        return 8
def ram_tier(ram_str):
    try:
        ram=int(ram_str.split()[0])
    except:
        return 3
    if ram<=8:
        return 2
    elif ram<=16:
        return 4
    elif ram<=32:
        return 6
    else:
        return 8
def cpu_tier(cpu_str):
    cpu_str=cpu_str.lower()
    if "i3" in cpu_str or "ryzen 3" in cpu_str:
        return 2
    elif "i5" in cpu_str or "ryzen 5" in cpu_str:
        return 4
    elif "i7" in cpu_str or "ryzen 7" in cpu_str:
        return 6
    elif "i9" in cpu_str or "ryzen 9" in cpu_str:
        return 8
    else:
        return 4
def perf_label(gpu_tier, demand):
    diff=gpu_tier-demand
    if diff>=3:
        return "Runs great"
    elif diff>=1:
        return "Runs well"
    elif diff>=0:
        return "Runs OK"
    else:
        return "May struggle"
GENRE_MAP={"Action": ("action", None), "Action RPG": ("role-playing-games-rpg", "action"), "Adventure": ("adventure", None),
           "Battle Royale": ("shooter", "massively-multiplayer"), "City Builder": ("strategy", "simulation"),
           "Co-op Multiplayer": ("action", "massively-multiplayer"), "Fighting": ("fighting", None), "First-Person Shooter (FPS)": ("shooter", None),
           "Horror": ("action", "adventure"), "Open World": ("action", "adventure"), "Platform/Platformer": ("platformer", None),
           "Puzzle": ("puzzle", None), "Racing": ("racing", None), "RPG": ("role-playing-games-rpg", None), "AAA Blockbuster": ("action", "adventure"),
           "Simulation": ("simulation", None), "Sports": ("sports", None), "Strategy": ("strategy", None), "Indie": ("indie", None),}
def get_recommendations(ram, cpu, gpu, genre):
    genre_slugs=GENRE_MAP.get(genre, ("action", None))
    gpu_tier = next((v for k, v in GPU_TIERS.items() if gpu.lower() in k.lower()), 5)
    ram_score = ram_tier(ram)
    cpu_score = cpu_tier(cpu)
    system_score = int((gpu_tier * 0.5) + (cpu_score * 0.3) + (ram_score * 0.2))
    genre_param=genre_slugs[0]
    if genre_slugs[1]:
        genre_param+=f",{genre_slugs[1]}"
    url=(f"https://api.rawg.io/api/games"
        f"?key={RAWG_API_KEY}"
        f"&genres={genre_param}"
        f"&platforms=4"
        f"&ordering=-metacritic"
        f"&page_size=6"
        f"&metacritic=60,100")
    try:
        res=requests.get(url, timeout=10)
        data=res.json()
    except Exception as e:
        print("API Error:", e)
        return []
    games=data.get("results", [])
    results=[]
    for game in games:
        title=game.get("name", "Unknown")
        year=str(game.get("released", "N/A"))[:4]
        rating=game.get("rating", 0)

        demand=game_demand(year)
        perf=perf_label(system_score, demand)
        results.append({"title": title, "description": f"{title} ({year}) — {perf}",
            "rating": f"{rating:.1f}/5", "year": year})
    return results
         
    
