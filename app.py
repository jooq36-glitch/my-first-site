from flask import Flask, render_template_string, request, session
import random

app = Flask(__name__)
app.secret_key = 'blackjack_secret_key'

def get_score(hand):
    score = 0
    aces = 0
    values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
    for card in hand:
        score += values[card]
        if card == 'A': aces += 1
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'deck' not in session or (request.method == 'POST' and 'reset' in request.form):
        session['deck'] = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4
        random.shuffle(session['deck'])
        session['player'] = [session['deck'].pop(), session['deck'].pop()]
        session['dealer'] = [session['deck'].pop(), session['deck'].pop()]
        session['status'] = 'playing'
    
    if request.method == 'POST' and session['status'] == 'playing':
        if 'hit' in request.form:
            session['player'].append(session['deck'].pop())
            if get_score(session['player']) > 21:
                session['status'] = 'Вы проиграли! (Перебор)'
        elif 'stand' in request.form:
            while get_score(session['dealer']) < 17:
                session['dealer'].append(session['deck'].pop())
            p_score, d_score = get_score(session['player']), get_score(session['dealer'])
            if d_score > 21 or p_score > d_score: session['status'] = 'Вы выиграли!'
            elif d_score > p_score: session['status'] = 'Дилер выиграл!'
            else: session['status'] = 'Ничья!'
            
    return render_template_string('''
        <style>body { font-family: sans-serif; text-align: center; background: #2c3e50; color: white; padding-top: 50px; }</style>
        <h1>🃏 Блэкджек</h1>
        <p>Ваши карты: <b>{{ session['player']|join(', ') }}</b> (Очки: {{ score_p }})</p>
        <p>Дилер: <b>{{ session['dealer']|join(', ') if session['status'] != 'playing' else session['dealer'][0] + ', ?' }}</b></p>
        <h2>{{ session['status'] if session['status'] != 'playing' else '' }}</h2>
        <form method="post">
            <button name="hit" style="padding:10px 20px">Взять карту</button>
            <button name="stand" style="padding:10px 20px">Хватит</button>
            <button name="reset" style="padding:10px 20px">Новая игра</button>
        </form>
    ''', score_p=get_score(session['player']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
