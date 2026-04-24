from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime
from utils.recommender import get_recommendation

app = Flask(__name__)

# Ensure data directory exists
os.makedirs('data', exist_ok=True)
if not os.path.exists('data/user_data.json'):
    with open('data/user_data.json', 'w') as f:
        json.dump({"history": []}, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/log', methods=['POST'])
def log_food():
    data = request.json
    
    # Process with Gemini
    result = get_recommendation(data)
    
    # Save to history
    try:
        with open('data/user_data.json', 'r+') as f:
            history_data = json.load(f)
            
            # Add to history
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "food": data.get('food'),
                "score": result.get('score'),
                "response": result.get('response')
            }
            history_data['history'].append(log_entry)
            
            f.seek(0)
            json.dump(history_data, f, indent=4)
            f.truncate()
    except Exception as e:
        print(f"Error saving to history: {e}")
        
    return jsonify(result)

@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        with open('data/user_data.json', 'r') as f:
            data = json.load(f)
            return jsonify(data)
    except FileNotFoundError:
        return jsonify({"history": []})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
