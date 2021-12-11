sudo apt install mongodb
mongo
use uncursedforge
db.createCollection('modsinfo')
sudo apt install gunicorn
mkdir ~/uncursedforge
cd ~/uncursedforge
git clone https://gitee.com/Xiaoming_TX/Uncursed-Forge.git
cd Uncursed-Forge/website/server
gunicorn -w 4 -b 0.0.0.0:8000 server:app
