from flask import Flask, render_template, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Asosiy menyuni yuklash"""
    return render_template('menu.html')

@app.route('/lab<int:lab_id>')
def lab(lab_id):
    """1 dan 30 gacha bo'lgan barcha laboratoriyalarni yuklash"""
    if 1 <= lab_id <= 30:
        # Maxsus holat: lab4 -> index.html (Sizning kodingizdagi mantiq bo'yicha)
        target_template = 'index.html' if lab_id == 4 else f'lab{lab_id}.html'
        
        # Fayl mavjudligini tekshirish
        template_path = os.path.join(app.template_folder, target_template)
        
        if os.path.exists(template_path):
            return render_template(target_template)
        else:
            # Fayl yo'q bo'lsa, xatolik o'rniga chiroyli xabar
            return f"""
            <body style="background:#020617; color:white; font-family:sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; flex-direction:column;">
                <h1 style="color:#4ade80;">{lab_id}-Laboratoriya</h1>
                <p>Ushbu laboratoriya ishi ustida ish olib borilmoqda.</p>
                <a href="/" style="color:#38bdf8; text-decoration:none;">← Menyoga qaytish</a>
            </body>
            """
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)