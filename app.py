from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veritabanını başlatan fonksiyon
def init_db()
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
REVIEW_LINK = httpssearch.google.comlocalwritereviewplaceid=ChIJYUeEdL2hmkcRFa37o7FFCN0

# 1. ANA SAYFA (QR KOD OKUTULUNCA AÇILACAK LİNK MENÜSÜ)
HTML_LANDING = 
!DOCTYPE html
html lang=de
head
    meta charset=UTF-8
    meta name=viewport content=width=device-width, initial-scale=1.0
    titleWillkommen bei Greperytitle
    style
        body { 
            font-family 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color #fdfaf6; 
            margin 0; 
            padding 20px; 
            display flex; 
            flex-direction column; 
            align-items center; 
        }
        .logo-container { 
            text-align center; 
            margin-bottom 35px; 
            margin-top 30px; 
        }
        .logo-container h1 { 
            color #800020;  Bordo 
            font-size 36px; 
            margin 0; 
            letter-spacing 1px;
        }
        .logo-container p { 
            color #777; 
            margin-top 8px; 
            font-size 16px;
        }
        .links-container { 
            width 100%; 
            max-width 380px; 
            display flex; 
            flex-direction column; 
            gap 16px; 
        }
        .link-btn { 
            display flex; 
            align-items center; 
            justify-content center; 
            width 100%; 
            padding 16px; 
            background-color white; 
            border 2px solid #800020;  Bordo 
            border-radius 14px; 
            color #800020;  Bordo 
            font-size 18px; 
            font-weight bold; 
            text-decoration none; 
            box-shadow 0 4px 6px rgba(128, 0, 32, 0.08); 
            transition all 0.3s ease; 
            box-sizing border-box; 
        }
        .link-btnhover { 
            background-color #800020;  Bordo 
            color white; 
            transform translateY(-3px); 
            box-shadow 0 8px 15px rgba(128, 0, 32, 0.2); 
        }
        .link-btn.highlight { 
            background-color #800020;  Bordo 
            color white; 
            border none;
            box-shadow 0 6px 12px rgba(128, 0, 32, 0.3);
        }
        .link-btn.highlighthover { 
            background-color #5c0017;  Koyu Bordo 
            transform translateY(-3px); 
            box-shadow 0 10px 18px rgba(128, 0, 32, 0.4);
        }
        .emoji { 
            margin-right 12px; 
            font-size 24px; 
        }
    style
head
body
    div class=logo-container
        h1🥞 Greperyh1
        pSchön, dass Sie da sind!p
    div
    
    div class=links-container
        !-- 1. Menu Linki --
        a href=httpswww.grepery.chmenu class=link-btn target=_blank
            span class=emoji📖span Speisekarte
        a
        
        !-- 3. Hediye İçecek Linki (Dikkat çekici renk) --
        a href=gratis-getraenk class=link-btn highlight
            span class=emoji🍹span Gratis-Getränk sichern
        a
        
        !-- 2. Sosyal Medya Linki --
        a href=httpswww.instagram.comgrepery class=link-btn target=_blank
            span class=emoji📸span Instagram
        a
        
        !-- 4. Website Linki --
        a href=httpswww.grepery.ch class=link-btn target=_blank
            span class=emoji🌐span Webseite
        a
    div
body
html


# 2. ÜCRETSİZ İÇECEK FORMU (E-posta Alma Sayfası)
HTML_GRATIS = 
!DOCTYPE html
html lang=de
head
    meta charset=UTF-8
    meta name=viewport content=width=device-width, initial-scale=1.0
    titleGrepery - Gratis-Getränktitle
    style
        body { 
            font-family 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            text-align center; 
            margin-top 30px; 
            background-color #fdfaf6; 
        }
        .back-link {
            display inline-block;
            margin-bottom 20px;
            color #777;
            text-decoration none;
            font-size 15px;
            font-weight bold;
            transition color 0.3s;
        }
        .back-linkhover { color #800020;  Bordo  }
        .container {
            background-color white;
            padding 30px;
            border-radius 15px;
            box-shadow 0 8px 20px rgba(0,0,0,0.06);
            max-width 400px;
            margin auto;
            text-align left;
            position relative;
        }
        h2 { 
            text-align center; 
            color #800020;  Bordo 
            margin-bottom 20px;
        }
        input[type=email] { 
            padding 14px; 
            margin 15px 0; 
            font-size 16px; 
            width 100%;
            border 1px solid #e0e0e0;
            border-radius 10px;
            box-sizing border-box;
            background-color #fafafa;
            transition border 0.3s;
        }
        input[type=email]focus {
            outline none;
            border-color #800020;  Bordo 
            background-color #fff;
        }
        .checkbox-container {
            font-size 14px;
            margin-bottom 25px;
            color #555;
            display flex;
            align-items flex-start;
            line-height 1.5;
            background-color #fafafa;
            padding 12px;
            border-radius 8px;
            border 1px solid #eee;
        }
        .checkbox-container input {
            margin-top 4px;
            margin-right 12px;
            transform scale(1.2);
        }
        button { 
            padding 15px 20px; 
            font-size 16px; 
            border none; 
            border-radius 10px; 
            cursor pointer;
            width 100%;
            transition 0.3s;
        }
        .btn-submit { 
            background-color #800020;  Bordo 
            color white; 
            font-weight bold;
            box-shadow 0 4px 10px rgba(128, 0, 32, 0.2);
        }
        .btn-submithover { 
            background-color #5c0017;  Koyu Bordo 
            transform translateY(-2px);
        }
        .btn-google { 
            background-color #4285F4; 
            color white; 
            font-weight bold; 
            margin-top 15px;
            box-shadow 0 4px 10px rgba(66, 133, 244, 0.2);
        }
        .btn-googlehover { 
            background-color #3367d6; 
            transform translateY(-2px);
        }
        .error { 
            color #e74c3c; 
            font-weight bold; 
            text-align center; 
            font-size 15px; 
            background-color #fdf2f0;
            padding 10px;
            border-radius 8px;
        }
        .success-text { 
            color #800020;  Bordo 
            font-size 24px; 
            font-weight bold; 
            text-align center; 
            margin-bottom 10px;
        }
        .friendly-box { 
            background-color #f8eef0;  Açık BordoPembe Arka Plan 
            color #5c0017;  Koyu Bordo Metin 
            font-size 15px; 
            text-align center; 
            padding 20px; 
            border-radius 12px; 
            margin-bottom 20px;
            line-height 1.6;
            border 1px dashed #800020;  Bordo Kesik Çizgi 
        }
        .footer-text { 
            font-size 12px; 
            color #aaa; 
            margin-top 20px; 
            text-align center;
        }
    style
head
body
    a href= class=back-link⬅️ Zurück zum Menüa
    
    div class=container
        h2🍹 Dein Gratis-Getränkh2
        
        {% if mesaj %}
            p class=error{{ mesaj }}p
        {% endif %}
        
        {% if basarili %}
            p class=success-textHerzlichen Dank! ❤️p
            
            div class=friendly-box
                bFast geschafft! 🎉bbrbr
                Klicken Sie auf den Button unten, um uns zu bewerten. Zeigen Sie danach einfach den Bewertungsbildschirm unserem Team, und schon bringen wir Ihnen Ihr Erfrischungsgetränk! 🥂
            div
            
            a href={{ review_link }} target=_blank style=text-decoration none;
                button class=btn-google⭐ Auf Google bewertenbutton
            a
        {% else %}
            p style=text-align center; color #555; margin-bottom 20px;Geben Sie Ihre E-Mail-Adresse ein, um Ihr Gratis-Getränk zu erhaltenp
            form method=POST action=gratis-getraenk
                input type=email name=email placeholder=beispiel@email.com required
                
                label class=checkbox-container
                    input type=checkbox name=newsletter value=1
                    Ich möchte über leckere Neuigkeiten und Events von Grepery informiert werden. 🥞
                label
                
                button class=btn-submit type=submitWeiter ➔button
            form
            p class=footer-text Jede E-Mail-Adresse kann nur einmal teilnehmen.p
        {% endif %}
    div
body
html


# Route 1 QR Kod okutulunca açılan ana menü
@app.route(, methods=[GET])
def ana_sayfa()
    return render_template_string(HTML_LANDING)

# Route 2 Bedava İçecek  E-posta Alma sayfası
@app.route(gratis-getraenk, methods=[GET, POST])
def gratis_getraenk()
    if request.method == POST
        email = request.form.get(email)
        newsletter_optin = 1 if request.form.get(newsletter) else 0
        
        conn = sqlite3.connect('restoran.db')
        cursor = conn.cursor()
        
        # E-posta adresinin daha önce kullanılıp kullanılmadığını kontrol et
        cursor.execute(SELECT  FROM kunden WHERE email = , (email,))
        kayit = cursor.fetchone()
        
        if kayit
            conn.close()
            # E-posta bulunduysa hata mesajı göster
            return render_template_string(HTML_GRATIS, mesaj=Sie haben mit dieser E-Mail-Adresse bereits ein Getränk erhalten. 😊, basarili=False)
        else
            # E-posta bulunamadıysa kaydet ve başarılı sayfasını göster (Sadece 1 kez hakkı oluyor)
            cursor.execute(INSERT INTO kunden (email, newsletter_optin) VALUES (, ), (email, newsletter_optin))
            conn.commit()
            conn.close()
            
            return render_template_string(HTML_GRATIS, basarili=True, review_link=REVIEW_LINK)
            
    # GET isteği gelirse boş formu göster
    return render_template_string(HTML_GRATIS, basarili=False)

if __name__ == __main__
    init_db()
    app.run(port=5000, debug=True, use_reloader=False)