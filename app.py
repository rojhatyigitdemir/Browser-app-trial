from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Veritabanını başlatan fonksiyon
def init_db():
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kunden (
            email TEXT PRIMARY KEY,
            newsletter_optin INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Grepery Stüssihof Direkt Yorum Linki
REVIEW_LINK = "https://search.google.com/local/writereview?placeid=ChIJYUeEdL2hmkcRFa37o7FFCN0"

HTML_SABLONU = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grepery - Gratis-Getränk</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            text-align: center; 
            margin-top: 50px; 
            background-color: #fdfaf6; /* Çok hafif, sıcak bir kırık beyaz */
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.08);
            max-width: 400px;
            margin: auto;
            text-align: left;
        }
        h2 { 
            text-align: center; 
            color: #ff8c00; /* Grepery için sıcak bir turuncu başlık */
            margin-bottom: 20px;
        }
        input[type="email"] { 
            padding: 12px; 
            margin: 15px 0; 
            font-size: 16px; 
            width: 90%;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-sizing: border-box;
            background-color: #fafafa;
        }
        input[type="email"]:focus {
            outline: none;
            border-color: #ff8c00;
        }
        .checkbox-container {
            font-size: 14px;
            margin-bottom: 25px;
            color: #555;
            display: flex;
            align-items: flex-start;
            line-height: 1.4;
        }
        .checkbox-container input {
            margin-top: 3px;
            margin-right: 10px;
        }
        button { 
            padding: 14px 20px; 
            font-size: 16px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;
            width: 100%;
            transition: 0.3s;
        }
        .btn-submit { 
            background-color: #ff8c00; /* Sıcak Turuncu */
            color: white; 
            font-weight: bold;
        }
        .btn-submit:hover { background-color: #e67e00; }
        
        .btn-google { 
            background-color: #4285F4; 
            color: white; 
            font-weight: bold; 
            margin-top: 10px;
        }
        .btn-google:hover { background-color: #3367d6; }
        
        .error { color: #e74c3c; font-weight: bold; text-align: center; font-size: 15px; }
        .success-text { color: #ff8c00; font-size: 22px; font-weight: bold; text-align: center; margin-bottom: 5px;}
        
        /* Yeni, Sempatik Bilgi Kutusu */
        .friendly-box { 
            background-color: #fff8e1; /* Krep/Güneş sarısı pastel ton */
            color: #d35400; /* Sıcak kahverengi/turuncu metin */
            font-size: 15px; 
            text-align: center; 
            padding: 18px; 
            border-radius: 12px; 
            margin-bottom: 20px;
            line-height: 1.5;
            box-shadow: 0 2px 5px rgba(0,0,0,0.04);
        }
        
        .footer-text { font-size: 12px; color: #999; margin-top: 20px; text-align: center;}
    </style>
</head>
<body>
    <div class="container">
        <h2>🍹 Dein Gratis-Getränk</h2>
        
        {% if mesaj %}
            <p class="error">{{ mesaj }}</p>
        {% endif %}
        
        {% if basarili %}
            <p class="success-text">Herzlichen Dank! 💛</p>
            
            <div class="friendly-box">
                <b>Fast geschafft! 🎉</b><br><br>
                Klicken Sie auf den Button unten, um uns zu bewerten. Zeigen Sie danach einfach den Bewertungsbildschirm unserem Team, und schon bringen wir Ihnen Ihr Erfrischungsgetränk! 🥂
            </div>
            
            <a href="{{ review_link }}" target="_blank" style="text-decoration: none;">
                <button class="btn-google">⭐ Auf Google bewerten</button>
            </a>
        {% else %}
            <p style="text-align: center; color: #555;">Geben Sie Ihre E-Mail-Adresse ein, um Ihr Gratis-Getränk zu erhalten:</p>
            <form method="POST" action="/">
                <input type="email" name="email" placeholder="beispiel@email.com" required>
                
                <label class="checkbox-container">
                    <input type="checkbox" name="newsletter" value="1">
                    Ich möchte über leckere Neuigkeiten und Events von Grepery informiert werden. 🥞
                </label>
                
                <button class="btn-submit" type="submit">Weiter ➔</button>
            </form>
            <p class="footer-text">* Jede E-Mail-Adresse kann nur einmal teilnehmen.</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def ana_sayfa():
    if request.method == "POST":
        email = request.form.get("email")
        newsletter_optin = 1 if request.form.get("newsletter") else 0
        
        conn = sqlite3.connect('restoran.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM kunden WHERE email = ?", (email,))
        kayit = cursor.fetchone()
        
        if kayit:
            conn.close()
            return render_template_string(HTML_SABLONU, mesaj="Sie haben mit dieser E-Mail-Adresse bereits ein Getränk erhalten. 😊", basarili=False)
        else:
            cursor.execute("INSERT INTO kunden (email, newsletter_optin) VALUES (?, ?)", (email, newsletter_optin))
            conn.commit()
            conn.close()
            
            return render_template_string(HTML_SABLONU, basarili=True, review_link=REVIEW_LINK)
            
    return render_template_string(HTML_SABLONU, basarili=False)

if __name__ == "__main__":
    init_db()
    app.run(port=5000, debug=True, use_reloader=False)