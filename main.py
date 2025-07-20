from flask import Flask
from bot import bot_run
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

def run_flask():
    app.run(host='0.0.0.0', port=5001)

if __name__ == '__main__':
    # Start the bot in a separate thread
    bot_thread = threading.Thread(target=bot_run, daemon=True)
    bot_thread.start()
    # Run the Flask app in the main thread
    run_flask()