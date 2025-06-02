
echo "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'API activa'" > app.py
git add app.py
git commit -m "Endpoint raíz funcionando con Flask"
