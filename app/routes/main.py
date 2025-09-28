from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from app.models import stock_model
import random
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    prediction = None
    close_price = None
    if request.method == 'POST':
        close_price = float(request.form.get('close_price', 0))
        prediction = stock_model.predict_next_close(close_price)
    return render_template('index.html', prediction=prediction, close_price=close_price)



@main_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You have been logged out.")
    return redirect(url_for('main.login'))

@main_bp.route('/')
def home():
    return render_template('home.html')


@main_bp.route('/stocks')
def stocks_table():
    stock_names = [
        "ApexTech", "Maxion", "Genexis", "Quantica", "Triton", "Vortex", "Synergix", "Lumina", "Novaris", "Zenith",
        "Pinnacle", "Meridian", "Helix", "Stratus", "NovaCore", "Vertex", "Orion", "Celestia", "Echelon", "Ionix",
        "Nimbus", "Quantum", "Fusion", "Nexus", "Eonix", "Polarix", "Dynex", "Stellar", "Axion", "Solara"
    ]
    
    companies = [
        # your existing 30 companies
        "Pinnacle Solutions", "Crystal Dynamics", "NovaTech Industries", "BrightHome Electronics",
        "Vertex Innovations", "CyberNet Software", "Zenexa Systems", "Rhythm Microsystems",
        "Falcon Solar", "Quantum Net Services", "Prism Data Analytics", "Horizon Logistics",
        "Tranquil Networks", "KZL Digital Media", "Jaxpal Technologies", "Lavyss Manufacturing",
        "Xtreme Computing", "Westmount Technologies", "Nebula Research Labs", "Clifex Energy",
        "Zykon Communications", "Davlin Solutions", "Vimore Electronics", "Fortex Electronics",
        "Yutex Software", "Grevio Network", "HattonX Innovations", "Planix Security",
        "Quasar Manufacturing", "Draven Software"
    ]
    
    page = request.args.get('page', default=1, type=int)
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    
    page_stocks = stock_names[start:end]
    page_companies = companies[start:end]
    
    random.shuffle(page_stocks)
    random.shuffle(page_companies)
    
    stocks = []
    for stock, company in zip(page_stocks, page_companies):
        stocks.append({
            "stocks": stock,
            "name": company,
            "price": round(random.uniform(100, 4000), 2),
            "change": round(random.uniform(-3, 3), 2),
            "volume": random.randint(50000, 7000000)
        })
    
    total_pages = (len(stock_names) + per_page - 1) // per_page
    
    return render_template('stocks_table.html', stocks=stocks, page=page, total_pages=total_pages)


@main_bp.route('/analytics')
def analytics():
    return render_template('analytics.html')

@main_bp.route('/news')
def news():
    return render_template('news.html')
