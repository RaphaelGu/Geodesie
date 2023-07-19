import subprocess
from pathlib import Path
import gnsspy as gp

rnx2rtkp = Path.home() / "Desktop" / "geodesie" / "rtklib_2.4.2" / "bin" / "rnx2rtkp.exe" # idéalement, ajouter cette variable aux variables d'environnement
base_config = rnx2rtkp.parent / "static.conf"
observation_folder = Path.cwd() / "DATA"


#cmd_rtkp = f"{rnx2rtkp} -k {cfg} -o {output} {rover}o {base}o {base}n"



if __name__ == "__main__":
    cfg = base_config
    output_dir = Path.cwd() / "RESULTS"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    rover = observation_folder / "MILESSE" / "base" / "brmz198z.23"
    
    base = observation_folder / "MILESSE" / "base" / "man2198z.23"
    base_obs = gp.read_obsFile(f"{str(base)}o")
    print(f"Base approx position : {base_obs.approx_position}")
    
    output = output_dir / "brmz198z.pos"
    cmd_rtkp = f"{rnx2rtkp} -k {cfg} -r {base_obs.approx_position[0]} {base_obs.approx_position[1]} {base_obs.approx_position[2]} -o {output} {rover}o {base}o {base}n"
    print(f"cmd line = {cmd_rtkp}")
    
    subprocess.run(cmd_rtkp, shell=True, check=True, capture_output=True, text=True)