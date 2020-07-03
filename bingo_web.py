from jinja2 import Template
from src.bingo import elegirCarton

x = elegirCarton()

template = Template(open('HTML/template.j2').read())

file = open("bingo.html", "w")
file.write(template.render(carton = elegirCarton()))
file.close()
print("Generado \"bingo.html\".")
