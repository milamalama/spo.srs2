import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

players = [
    {"id": 1, "name": "Милана Щедрова",
     "position": "Центральный блокирующий",
     "number": 9,  "height": 176,
     "birth_year": 2007,
     "bio": "Лучший бомбардир прошлого сезона. Участник Первенства России и Чемпионта Москвы"},

    {"id": 16, "name": "Ева Шемелина",
     "position": "Либеро",
     "number": 1,  "height": 174,
     "birth_year": 2007,
     "bio": "Участник Чемпионта Москвы"},

    {"id": 11, "name": "Людмила Макарова",
     "position": "Связующий",
     "number": 20,  "height": 167,
     "birth_year": 2005,
     "bio": "Лучший игрок Высшей лиги А прошлого сезона"},

    {"id": 2, "name": "Виктория Акименко",
     "position": "Либеро",
     "number": 18,  "height": 160,
     "birth_year": 2008,
     "bio": "Участник МССИ"},

     {"id": 3, "name": "Евгения Глушкова",
     "position": "Диагональный",
     "number": 4,  "height": 187,
     "birth_year": 2007,
     "bio": "Участник МССИ"},

    {"id": 4, "name": "Полина Грешнева",
     "position": "Диагональный",
     "number": 14,  "height": 184,
     "birth_year": 2007,
     "bio": "Участник МССИ. Участник Чемпионата Москвы"},

     {"id": 5, "name": "Станислава Жердева",
     "position": "Доигровщик",
     "number": 8,  "height": 174,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 6, "name": "Кира Кан",
     "position": "Доигровщик",
     "number": 6,  "height": 175,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 7, "name": "Полина Канаева",
     "position": "Центральный блокирующий",
     "number": 15,  "height": 179,
     "birth_year": 2005,
     "bio": "Участник МССИ"},

     {"id": 8, "name": "Мария Котова",
     "position": "Центральный блокирующий",
     "number": 3,  "height": 178,
     "birth_year": 2006,
     "bio": "Участник МССИ"},

     {"id": 9, "name": "Татьяна Лукьянова",
     "position": "Центральный блокирующий",
     "number": 10,  "height": 177,
     "birth_year": 2005,
     "bio": "Участник МССИ"},

     {"id": 10, "name": "Екатерина Макарова",
     "position": "Центральный блокирующий",
     "number": 5,  "height": 180,
     "birth_year": 2003,
     "bio": "Участник МССИ"},

     {"id": 12, "name": "Жанна Мозговая",
     "position": "Связующий",
     "number": 13,  "height": 160,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 13, "name": "Дарья Поровицына",
     "position": "Либеро",
     "number": 12,  "height": 160,
     "birth_year": 2007,
     "bio": "Участник МССИ. Легионер"},

     {"id": 14, "name": "Светлана Соколова",
     "position": "Доигровщик",
     "number": 11,  "height": 187,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},

     {"id": 15, "name": "Екатерина Чуркина",
     "position": "Доигровщик",
     "number": 7,  "height": 174,
     "birth_year": 2008,
     "bio": "Только пришедший в команду игрок"},
]

gallery_photos = [
    {"file": "team1.jpg", "title": "Разминка перед игрой",        "desc": "Сезон 2025/2026"},
    {"file": "team2.jpg", "title": "Победа",                      "desc": "Счёт 3:1"},
    {"file": "team3.jpg", "title": "МАИ-МГСУ",                    "desc": "Счёт 23:11"},
    {"file": "team4.jpg", "title": "Игра с РУДН",                 "desc": "Чемпионат Москвы"},
    {"file": "team5.jpg", "title": "Игра с РУДН",                 "desc": "Лучший игрок"},
    {"file": "team6.jpg", "title": "Общая фотография состава",    "desc": "Конец сезона"},
    {"file": "team7.jpg", "title": "Награждение",                 "desc": "Второе место"},
    {"file": "team8.jpg", "title": "Тренировка",                  "desc": "Начало сезона"},
    {"file": "team9.jpg", "title": "МАИ-МГСУ",                    "desc": "Непередаваемые эмоции"},
    {"file": "team10.jpg", "title": "МАИ-ВШЭ",                    "desc": "Приветствие"},
    {"file": "team11.jpg", "title": "МАИ-ВШЭ",                    "desc": "Победное фото"},
    {"file": "team12.jpg", "title": "МАИ-МИИТ",                   "desc": "Тайм-аут"},
]

@app.context_processor
def inject_photo_helper():
    def photo_url(filename):
        return url_for("static", filename="images/" + filename)
    return {"photo_url": photo_url}

@app.route("/")
def index():
    return render_template("index.html", players_count=len(players))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/players")
def players_list():
    position = request.args.get("position", "").strip()
    if position:
        filtered = [p for p in players if position.lower() in p["position"].lower()]
    else:
        filtered = players
    return render_template("players.html", players=filtered, position=position)

@app.route("/player/<int:player_id>")
def player_detail(player_id):
    player = next((p for p in players if p["id"] == player_id), None)
    if player is None:
        return render_template("player_detail.html", player=None), 404
    return render_template("player_detail.html", player=player)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", photos=gallery_photos)

@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    errors = []
    form_data = {
        "name": "",
        "position": "",
        "number": "",
        "height": "",
        "birth_year": "",
    }

    if request.method == "POST":
        form_data["name"]       = request.form.get("name", "").strip()
        form_data["position"]   = request.form.get("position", "").strip()
        form_data["number"]     = request.form.get("number", "").strip()
        form_data["height"]     = request.form.get("height", "").strip()
        form_data["birth_year"] = request.form.get("birth_year", "").strip()

        if not form_data["name"]:
            errors.append("Укажите имя игрока.")
        elif len(form_data["name"]) < 2:
            errors.append("Имя должно содержать минимум 2 символа.")

        if not form_data["position"]:
            errors.append("Укажите амплуа игрока.")

        if not form_data["number"].isdigit():
            errors.append("Номер должен быть числом.")
        else:
            number = int(form_data["number"])
            if number < 1 or number > 99:
                errors.append("Номер должен быть в диапазоне от 1 до 99.")
            elif any(p["number"] == number for p in players):
                errors.append(f"Номер {number} уже занят другим игроком.")

        if not form_data["height"].isdigit():
            errors.append("Рост должен быть числом.")
        else:
            height = int(form_data["height"])
            if height < 150 or height > 200:
                errors.append("Рост должен быть от 150 до 200 см.")

        if not form_data["birth_year"].isdigit():
            errors.append("Год рождения должен быть числом.")
        else:
            year = int(form_data["birth_year"])
            if year < 2000 or year > 2010:
                errors.append("Год рождения должен быть от 2000 до 2010.")

        if not errors:
            new_id = max((p["id"] for p in players), default=0) + 1
            new_player = {
                "id": new_id,
                "name": form_data["name"],
                "position": form_data["position"],
                "number": int(form_data["number"]),
                "height": int(form_data["height"]),
                "birth_year": int(form_data["birth_year"]),
                "bio": "Новый игрок команды.",
            }
            players.append(new_player)
            return redirect(url_for(
                "result",
                name=new_player["name"],
                number=new_player["number"],
            ))

    return render_template(
        "add_player.html",
        errors=errors,
        form_data=form_data,
    )

@app.route("/result")

def result():
    name = request.args.get("name", "Неизвестный игрок")
    number = request.args.get("number", "—")
    return render_template("result.html", name=name, number=number)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
        app.run(debug=True)