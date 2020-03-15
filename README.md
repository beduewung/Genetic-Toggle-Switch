# Genetic-Toggle-Switch
A small python powered web application simulating a genetic toggle switch behaviour.

## Installation
1. Clone the repo
`git clone https://github.com/severinferard/Genetic-Toggle-Switch`
2. Install packages
`pip3 install matplotlib Flask flask_cors`

## Usage
1. `CD` into the cloned directory
2. Start the server with python 3.x
`python3 init.py` or `python init.py`
3. Open your favorite web browser and navigate to your localhost on port 5000 or http://127.0.0.1:5000/
4. If you would like to change some parameters of the simulation, you can do so while the simulation is running by just modifying `init.py` and resaving the file

## Explanations
The two red buttons allow you to add a specific inducer to the simulation for only 1 second before retrieving it. You can add and retrieve each inducer manually using the two switches in the left.

Each gene is responsible for the expression of a **protein**, and each protein is inhibiting the production of the opposit gene. When one of the inducer is added, only one protein is present in large concentration and thus only one gene is correctly expressed. Because of this particular system, even when the inducer is removed, the system state won't change until an opposit inducer is added. This behavior featuring a sort of biological **memory** can be compared to a **toggle switch**.

