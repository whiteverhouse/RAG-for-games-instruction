from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from main import initialize_system, update_vector_db
import os

app = Flask(__name__, static_folder='static')
CORS(app)

rag_processor = None
conversation_history = []

def initialize():
    global rag_processor
    rag_processor = initialize_system()

# initialize system when the app starts
threading.Thread(target=initialize).start()

# set up a scheduled task to update the vector database periodically
scheduler = BackgroundScheduler()
scheduler.add_job(func=update_vector_db, trigger="interval", hours=24)
scheduler.start()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory(app.static_folder, 'style.css', mimetype='text/css')

@app.route('/script.js')
def serve_js():
    return send_from_directory(app.static_folder, 'script.js', mimetype='application/javascript')

@app.route('/query', methods=['POST'])
def query():
    global rag_processor, conversation_history
    data = request.json
    query = data['query']
    
    if rag_processor is None:
        return jsonify({"error": "System is still initializing. Please try again later."}), 503

    response = rag_processor.process_query(query)
    conversation_history.append({"query": query, "response": response})
    
    return jsonify({"response": response})

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(conversation_history)

@app.route('/new_chat', methods=['POST'])
def new_chat():
    global conversation_history
    conversation_history = []
    return jsonify({"message": "New conversation started"})

if __name__ == '__main__':
    app.run(debug=True)