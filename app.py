from flask import Flask, render_template, request, jsonify, abort
import os

app = Flask(__name__)

# Laboratoriya ma'lumotlari - barcha chalkashliklarni shu erda to'g'irlaymiz
LABS = {
    1: "Magnito-Optik Kerr effekti",
    2: "Gaz Xromatografiyasi",
    3: "Faradey effekti",
    4: "NYEM Spektri",
    5: "Pikering Seriyasi",
    6: "Nodir yer metallari",
    7: "Atom kuch mikroskopiyasi (AFM)",
    # Qolganlari uchun avtomatik "Mavzu kiritilmagan" yoziladi
}

@app.route('/')
def home():
    # 1 dan 30 gacha laboratoriyalar ro'yxatini shakllantiramiz
    lab_list = []
    for i in range(1, 31):
        lab_list.append({
            "id": i,
            "title": LABS.get(i, "Mavzu kiritilmagan")
        })
    return render_template('menu.html', labs=lab_list)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('fullname')
    phone = data.get('phone')
    # Bu yerda ma'lumotlarni bazaga saqlash mumkin
    print(f"Yangi foydalanuvchi: {full_name}, Tel: {phone}")
    return jsonify({"status": "success", "message": f"Rahmat, {full_name}!"})

@app.route('/lab<int:lab_id>')
def lab(lab_id):
    if 1 <= lab_id <= 30:
        template_name = 'index.html' if lab_id == 4 else f'lab{lab_id}.html'
        if os.path.exists(os.path.join(app.template_folder, template_name)):
            return render_template(template_name)
        return f"<h1>{lab_id}-Laboratoriya tayyorlanmoqda...</h1>"
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)