# Parking Lot
My Orginal Github : <br>
https://github.com/gauravgola96
## Project Structure
Majorly has three parts:
1.  **config** : Env specific configurations with `COMMAND_DICT` in `common.py` which is a map of expected of commands
2. **parking_system** : Parking system package with core parking logic and required mappings
    * **constants.py** :  All constants related to parking system
    * **driver.py** :  Driver class with age attribute 
    * **exceptions.py** :  Custom execptions related to parking system
    * **main.py** :  `RunParkingSystem` class to run logics according to input commands. Basically a pythonic switch-case
    * **parking_system.py** : **Singleton** design pattern based parking system class. 
                            Includes all the logics required to park or leave a car. 
                            Car assignment is done with **min-heap** data structure  
    * **utils.py** :  Utility class for helper methods
    * **vehicles.py** :  Vehicle base class and its sub classes 
3. **run.py** : Script to run the parking system algorithm
## Getting started
* Clone the project and ```cd parking_system/```
* Requirements : ``Python3.6+``

### Shell
* `run.sh` : Executes user command and run parking system algorithm
  * Configure `PARKING_SYSTEM_ENV` according to required environment. Default is `production`
  * To trace more detailed logs configure `PARKING_SYSTEM_ENV` to `development` or `pre-production`
* Give permissions : ```sudo chmod +x run.sh``` 
* Run from filepath : ```./run.sh filepath=./files/input.txt```. Change filepath for your requirement
* Run interactively on terminal ```./run.sh interactive```
#### Console Output 
![output](imgs/console_out.png?raw=true "console output")

### Python
* Default environment : `development`
* Run from filepath :`python run.py --filepath=./files/input.txt`. Change filepath for your requirement
* Run interactively on terminal:  `python run.py --interactive`

##  Design Thoughts

* Used singleton design pattern for ParkingSystem class. Only one instance of ParkingSystem will be available all the time. 
I chose not to raise exception and exit the system because may be real-world scenario that is not feasible rather I recreate instance
with with new params on same address. 
* For car parking logics used **min-heap** data structure
* Since the code is asked to be **production** ready I used logger in the entire package `(parking_system/__init__.py)`. For production env
`LOG_LEVEL` is `INFO` and for pre-production/development as `DEBUG`. To change the env `export PARKING_SYSTEM_ENV=xxxx`. So in near future
if we want to store our logs in production env this will help
* Created Vehicle base class and extends car from it so that the system can be scaled in future for other vehicle types as well
* Kept checks on input command outside `parking_system` package. `helper.py` verifies the command validity and number of params for a particular command 
and `main.py` gives the interface between input command and parking system package
* No external library is used 





