echo "Cloning Repo...."
git clone https://github.com/Ayush64047/mdisk-render.git /mdisk-render
cd /mdisk-render
pip3 install -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 main.py
