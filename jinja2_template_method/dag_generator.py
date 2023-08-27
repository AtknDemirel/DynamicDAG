from jinja2 import Environment, FileSystemLoader
import yaml
import os

file_dir = os.path.dirname(os.path.abspath(__file__)) 
print(file_dir)
env = Environment(loader=FileSystemLoader(file_dir))
template = env.get_template('dag_template.jinja2')

for filename in os.listdir(file_dir):
    print(filename)
    if filename.endswith('.yaml'):
        with open(f"{file_dir}/{filename}", "r") as input_file:
            inputs = yaml.safe_load(input_file)
            with open(f"dags/get_price{inputs['dag_id']}.py", "w") as f:
                f.write(template.render(inputs))

# dagimiz altına subdag aç
# main dag'den x veya y dagini açıcaz, verilen parametreye göre