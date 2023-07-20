import subprocess
from pathlib import Path
import gnsspy as gp

rnx2rtkp = Path.home() / "Desktop" / "geodesie" / "rtklib_2.4.2" / "bin" / "rnx2rtkp.exe" # idéalement, ajouter cette variable aux variables d'environnement
base_config = Path.cwd() / "DATA" / "rtk_conf" / "rin_header_static.conf"
observation_folder = Path.cwd() / "DATA"


#cmd_rtkp = f"{rnx2rtkp} -k {cfg} -o {output} {rover}o {base}o {base}n"



if __name__ == "__main__":
    cfg = base_config
    output_dir = Path.cwd() / "RESULTS"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    rover = observation_folder / "MILESSE" / "rover" / "45051980.23"
    
    base = observation_folder / "MILESSE" / "base" / "arna198z.23"
    base_obs = gp.read_obsFile(f"{str(base)}o")
    print(f"Base approx position : {base_obs.approx_position}")
    
    output = output_dir / "45051980_rnx2rtkp.pos"
    cmd_rtkp = f"{rnx2rtkp} -k {cfg} -o {output} {rover}o {base}o {base}n" # -r {base_obs.approx_position[0]} {base_obs.approx_position[1]} {base_obs.approx_position[2]}
    print(f"cmd line = {cmd_rtkp}")
    
    subprocess.run(cmd_rtkp, shell=True, check=True, capture_output=True, text=True)