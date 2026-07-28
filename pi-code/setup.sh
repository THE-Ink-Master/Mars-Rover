sudo apt remove brltty
sudo apt update
sudo apt install python3-serial

python3 -m venv .venv
source .venv/bin/activate
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
fi

# Run this command manually replacing username with your user!
# sudo usermod -a -G dialout username
