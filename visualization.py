from flask import Flask, render_template
from database import get_daily_summaries, get_alerts

app = Flask(__name__)

# Route to display daily weather summaries
@app.route('/')
def index():
    # Retrieve the daily weather summaries from the database
    summaries = get_daily_summaries()
    return render_template('index.html', summaries=summaries)

# Route to display alerts
@app.route('/alerts')
def alerts():
    # Retrieve the triggered alerts from the database or alert log
    alerts_list = get_alerts()
    return render_template('alerts.html', alerts=alerts_list)

if __name__ == '__main__':
    app.run(debug=True)
