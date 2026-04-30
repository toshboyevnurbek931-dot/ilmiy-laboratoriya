from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    """Asosiy menyuni yuklash"""
    return render_template('menu.html')

@app.route('/lab<int:lab_id>')
def lab(lab_id):
    """
    1 dan 30 gacha bo'lgan barcha laboratoriyalarni dinamik yuklash.
    Masalan: /lab3 -> lab3.html ni yuklaydi.
    """
    # Laboratoriya raqami 1 va 30 oralig'ida ekanligini tekshiramiz
    if 1 <= lab_id <= 30:
        # Maxsus holatlar uchun (agar fayl nomi boshqacha bo'lsa)
        if lab_id == 4:
            return render_template('index.html')
        
        # Qolgan barcha laboratoriyalar uchun (lab1.html, lab2.html...)
        try:
            return render_template(f'lab{lab_id}.html')
        except:
            # Agar fayl hali yaratilmagan bo'lsa, xatolik bermaslik uchun
            return f"<h1>{lab_id}-Laboratoriya ishi tayyorlanmoqda...</h1><p>Tez kunda yuklanadi.</p>"
    else:
        # Agar 30 dan katta raqam kiritilsa 404 xatosi
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)