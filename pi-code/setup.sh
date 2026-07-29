# brltty can prevent serial communication when installed, so we need to remove it
sudo apt remove brltty

# Install python3-serial to allow python to access serial ports
sudo apt update
sudo apt install python3-serial

# Create venv and add libraies
python3 -m venv .venv
source .venv/bin/activate
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
fi

# Run this command manually replacing username with your user!
# sudo usermod -a -G dialout username
