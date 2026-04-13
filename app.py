from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Мой Личный Сайт</title>
            <style>
                body { 
                    background: linear-gradient(45deg, #1a1a2e, #16213e); 
                    color: white; 
                    font-family: sans-serif; 
                    text-align: center; 
                    padding-top: 100px; 
                    height: 100vh;
                    margin: 0;
                }
                h1 { color: #00d2ff; font-size: 60px; text-shadow: 2px 2px 10px #00d2ff; }
                button { 
                    padding: 15px 30px; 
                    font-size: 20px; 
                    background: #e94560; 
                    color: white; 
                    border: none; 
                    border-radius: 10px; 
                    cursor: pointer;
                    transition: 0.3s;
                }
                button:hover { background: #ff4d6d; transform: scale(1.1); }
            </style>
        </head>
        <body>
            <h1>Привет, это сайт [Жоомарт]!</h1>
            <p>Я официально научился кодить на Python.</p>
            <br>
            <button onclick="alert('Ты лучший! Продолжай в том же духе 🚀')">Нажми на меня</button>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)