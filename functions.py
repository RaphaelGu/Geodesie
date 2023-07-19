import re

def extract_option_value(conf_file):
    variables = {}
    with open(conf_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                line = re.split(pattern=r"[=#]", string=line)
                variable = line[0]
                value = line[1]
                variable = variable.strip()
                value = value.strip()
                variables[variable] = value
    return variables

def update_option_value(conf_file, antenna):
    old_variables = extract_option_value(conf_file)
    new_variables = antenna.variables
    pass

def get_rinex_antenna(rinex):
    pass


class Rinex:
    #voir les fonctions du github pyGNSS (cloné sur pc perso)
    pass

class Antenna_conf:
    def __init__(self, conf_file, ant: str):      
        variables = extract_option_value(conf_file)
        self.ant = ant  
        self.type = variables[f"{ant}-anttype"]
        self.delu = float(variables[f"{ant}-antdelu"])
        self.deln = float(variables[f"{ant}-antdeln"])
        self.dele = float(variables[f"{ant}-antdele"])
        self.pos1 = float(variables[f"{ant}-pos1"])
        self.pos2 = float(variables[f"{ant}-pos2"])
        self.pos3 = float(variables[f"{ant}-pos3"])

    def __repr__(self):
        attributes = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in vars(self))
        return f"{self.__class__.__name__}({attributes})"
    
    def update_variables(self):
        #si un valeur est modifier, mettre a jour variables
        pass
        

if __name__ == "__main__":
    conf_file = r"G:\11-SERVICE_SUPPORT\11-2_METH_ET_INNO\2023\8971-Calculs_GNSS_IGN\2-PROCESS\RTKLIB\static.conf"
    ant1 = Antenna_conf(conf_file, "ant1")
    print(ant1)
    ant1.dele = 10
    print(ant1)
