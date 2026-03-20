import xml.etree.ElementTree as ET
from jinja2 import Template

tree = ET.parse('resultado_testes.xml')
root = tree.getroot()

testes = []

for testcase in root.iter('testcase'):
    nome_tecnico = testcase.get('name')
    nome_amigavel = nome_tecnico.replace('test_', '').replace('_', ' ').title()

    status = "APROVADO" if len(list(testcase)) == 0 else "REPROVADO"

    testes.append({
        "item": nome_amigavel,
        "status": status
    })

html_template = """
<html>
<head>
    <title>Termo de Aceite Técnico</title>
</head>
<body>
    <h1>Termo de Aceite Técnico</h1>
    <p>Resultado dos testes executados:</p>

    <ul>
    {% for t in testes %}
        <li>{{ t.item }}: <b>{{ t.status }}</b></li>
    {% endfor %}
    </ul>

    <br><br>
    __________________________________________<br>
    Assinatura do Stakeholder
</body>
</html>
"""