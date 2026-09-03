import requests
import json
import re


URL = "https://interact32-z.webapp.easebar.com/x20namwzfysslzs/x20mwzfysslzs_pc_data/?callback=jQuery111306603225898180926_1788407037572&_=1788407037573"

response = requests.get(URL)

text = response.text

match = re.search(r'\((\{.*\})\)$', text, re.DOTALL)

role_names = {
    "捍卫者": "Vanguard",
    "决斗家": "Duelist",
    "策略家": "Strategist"
}
hero_names = {
    # Vanguards
    "班纳": "Bruce Banner",
    "奇异博士": "Doctor Strange",
    "美国队长": "Captain America",
    "格鲁特": "Groot",
    "毒液": "Venom",
    "万磁王": "Magneto",
    "索尔": "Thor",
    "潘妮·帕克": "Peni Parker",
    "石头人": "The Thing",
    "艾玛·弗斯特": "Emma Frost",
    "安吉拉": "Angela",
    "死侍": "Deadpool",
    "恶魔恐龙": "Devil Dinosaur",
    "小淘气": "Rogue",

    # Duelists
    "惩罚者": "The Punisher",
    "暴风女": "Storm",
    "霹雳火": "Human Torch",
    "鹰眼": "Hawkeye",
    "海拉": "Hela",
    "黑豹": "Black Panther",
    "魔剑客": "Magik",
    "月光骑士": "Moon Knight",
    "松鼠女": "Squirrel Girl",
    "黑寡妇": "Black Widow",
    "钢铁侠": "Iron Man",
    "蜘蛛侠": "Spider-Man",
    "猩红女巫": "Scarlet Witch",
    "神奇先生": "Mister Fantastic",
    "冬兵": "Winter Soldier",
    "星爵": "Star-Lord",
    "刀锋战士": "Blade",
    "纳摩": "Namor",
    "灵蝶": "Psylocke",
    "金刚狼": "Wolverine",
    "林烈": "Iron Fist",
    "凤凰女": "Phoenix",
    "夜魔侠": "Daredevil",
    "艾尔莎·血石": "Elsa Bloodstone",
    "黑猫": "Black Cat",
    "雷光眼": "Cyclops",

    # Strategists
    "洛基": "Loki",
    "曼蒂斯": "Mantis",
    "火箭浣熊": "Rocket Raccoon",
    "斗篷与匕首": "Cloak & Dagger",
    "奥创": "Ultron",
    "冰月花雪": "Luna Snow",
    "亚当术士": "Adam Warlock",
    "杰夫": "Jeff the Land Shark",
    "隐形女": "Invisible Woman",
    "牌皇": "Gambit",
    "白狐": "White Fox",
    "百光花火": "Jubilee"
}
if match:
    data = json.loads(match.group(1))
    stats = data["data"]
    print(stats)

    lines = stats.splitlines()

    for line in lines:
        columns = line.split("\t")

        if len(columns) >= 4:
            role = columns[0]
            hero = columns[1]
            pick_rate = columns[2]
            win_rate = columns[3]

            english_role = role_names.get(role, role)
            english_hero = hero_names.get(hero, hero)

            printf({english_role, english_hero, pick_rate, win_rate)