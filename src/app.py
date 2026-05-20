"""
SaúdePOP — Aplicação Web Principal
Sistema ágil de prontuário eletrônico e fila inteligente para clínicas populares.
"""

from datetime import datetime

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# Armazenamento em memória para demonstração
pacientes = {}
profissionais = {}
agendamentos = {}
fila = []
atendimentos = {}

CONTADOR = {"paciente": 0, "profissional": 0, "agendamento": 0, "atendimento": 0, "fila": 0}


def proximo_id(tipo):
    CONTADOR[tipo] += 1
    return CONTADOR[tipo]


# ---- Rotas da API ----

@app.route("/")
def index():
    return render_template_string(HOME_HTML)


@app.route("/api/pacientes", methods=["GET", "POST"])
def api_pacientes():
    if request.method == "POST":
        dados = request.get_json()
        cpf = dados.get("cpf", "")
        if not cpf:
            return jsonify({"erro": "CPF é obrigatório"}), 400
        for p in pacientes.values():
            if p["cpf"] == cpf:
                return jsonify({"erro": "CPF já cadastrado"}), 409
        id_pac = proximo_id("paciente")
        paciente = {
            "id_paciente": id_pac,
            "nome": dados.get("nome", ""),
            "cpf": cpf,
            "data_nascimento": dados.get("data_nascimento", ""),
            "telefone": dados.get("telefone", ""),
            "email": dados.get("email", ""),
            "endereco": dados.get("endereco", ""),
            "created_at": datetime.now().isoformat(),
        }
        pacientes[id_pac] = paciente
        return jsonify(paciente), 201
    return jsonify(list(pacientes.values()))


@app.route("/api/pacientes/<int:id_paciente>")
def api_paciente_detalhe(id_paciente):
    paciente = pacientes.get(id_paciente)
    if not paciente:
        return jsonify({"erro": "Paciente não encontrado"}), 404
    return jsonify(paciente)


@app.route("/api/pacientes/busca")
def api_paciente_busca():
    cpf = request.args.get("cpf", "")
    for p in pacientes.values():
        if p["cpf"] == cpf:
            return jsonify(p)
    return jsonify({"erro": "Paciente não encontrado"}), 404


@app.route("/api/profissionais", methods=["GET", "POST"])
def api_profissionais():
    if request.method == "POST":
        dados = request.get_json()
        id_prof = proximo_id("profissional")
        profissional = {
            "id_profissional": id_prof,
            "nome": dados.get("nome", ""),
            "crm": dados.get("crm", ""),
            "especialidade": dados.get("especialidade", ""),
            "ativo": True,
            "created_at": datetime.now().isoformat(),
        }
        profissionais[id_prof] = profissional
        return jsonify(profissional), 201
    return jsonify(list(profissionais.values()))


@app.route("/api/agendamentos", methods=["GET", "POST"])
def api_agendamentos():
    if request.method == "POST":
        dados = request.get_json()
        data_hora = dados.get("data_hora", "")
        id_prof = dados.get("id_profissional")
        id_cons = dados.get("id_consultorio")
        for a in agendamentos.values():
            if (a["data_hora"] == data_hora and
                a["id_profissional"] == id_prof and
                a["id_consultorio"] == id_cons and
                a["status"] != "cancelado"):
                return jsonify({"erro": "Horário indisponível"}), 409
        id_ag = proximo_id("agendamento")
        agendamento = {
            "id_agendamento": id_ag,
            "id_paciente": dados.get("id_paciente"),
            "id_profissional": id_prof,
            "id_consultorio": id_cons,
            "data_hora": data_hora,
            "status": "agendado",
            "observacoes": dados.get("observacoes", ""),
            "created_at": datetime.now().isoformat(),
        }
        agendamentos[id_ag] = agendamento
        return jsonify(agendamento), 201
    return jsonify(list(agendamentos.values()))


@app.route("/api/fila", methods=["GET", "POST"])
def api_fila():
    if request.method == "POST":
        dados = request.get_json()
        posicao = len([f for f in fila if f["status"] == "aguardando"]) + 1
        id_f = proximo_id("fila")
        item_fila = {
            "id_fila": id_f,
            "id_paciente": dados.get("id_paciente"),
            "id_consultorio": dados.get("id_consultorio"),
            "posicao": posicao,
            "status": "aguardando",
            "hora_entrada": datetime.now().isoformat(),
            "hora_chamada": None,
            "prioridade": dados.get("prioridade", "normal"),
        }
        PRIO_MAP = {"emergencia": 3, "prioritario": 2, "normal": 1}
        fila.append(item_fila)
        fila.sort(key=lambda x: (-PRIO_MAP.get(x["prioridade"], 0), x["posicao"]))
        return jsonify(item_fila), 201
    return jsonify(fila)


@app.route("/api/fila/chamar", methods=["POST"])
def api_chamar_proximo():
    for item in fila:
        if item["status"] == "aguardando":
            item["status"] = "chamado"
            item["hora_chamada"] = datetime.now().isoformat()
            return jsonify(item)
    return jsonify({"erro": "Fila vazia"}), 404


@app.route("/api/atendimentos", methods=["GET", "POST"])
def api_atendimentos():
    if request.method == "POST":
        dados = request.get_json()
        id_at = proximo_id("atendimento")
        atendimento = {
            "id_atendimento": id_at,
            "id_paciente": dados.get("id_paciente"),
            "id_profissional": dados.get("id_profissional"),
            "id_agendamento": dados.get("id_agendamento"),
            "data_hora_inicio": datetime.now().isoformat(),
            "data_hora_fim": None,
            "anamnese": dados.get("anamnese", ""),
            "prescricao": dados.get("prescricao", ""),
            "observacoes": dados.get("observacoes", ""),
        }
        atendimentos[id_at] = atendimento
        return jsonify(atendimento), 201
    return jsonify(list(atendimentos.values()))


@app.route("/api/atendimentos/paciente/<int:id_paciente>")
def api_atendimentos_paciente(id_paciente):
    hist = [a for a in atendimentos.values() if a["id_paciente"] == id_paciente]
    return jsonify(sorted(hist, key=lambda x: x["data_hora_inicio"], reverse=True))


@app.route("/painel")
def painel_fila():
    return render_template_string(PAINEL_HTML)


# ---- Templates HTML ----

HOME_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SaúdePOP — Sistema de Gestão Clínica</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f4f8; color: #333; }
        .header { background: #2563eb; color: white; padding: 20px 40px; }
        .header h1 { font-size: 28px; }
        .header p { opacity: 0.9; margin-top: 5px; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 8px; padding: 24px; margin-bottom: 20px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .card h2 { color: #2563eb; margin-bottom: 15px; font-size: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
        .stat { text-align: center; padding: 20px; background: #f8fafc; border-radius: 8px; }
        .stat .num { font-size: 36px; font-weight: bold; color: #2563eb; }
        .stat .label { color: #64748b; margin-top: 5px; }
        .endpoints { list-style: none; }
        .endpoints li { padding: 10px 0; border-bottom: 1px solid #e2e8f0; }
        .endpoints code { background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-size: 14px; }
        .method { display: inline-block; width: 60px; font-weight: bold; font-size: 12px;
                  padding: 2px 8px; border-radius: 4px; text-align: center; margin-right: 8px; }
        .get { background: #dcfce7; color: #166534; }
        .post { background: #dbeafe; color: #1e40af; }
        a { color: #2563eb; }
    </style>
</head>
<body>
    <div class="header">
        <h1>SaúdePOP</h1>
        <p>Sistema Ágil de Prontuário Eletrônico e Fila Inteligente</p>
    </div>
    <div class="container">
        <div class="card">
            <h2>Painel do Sistema</h2>
            <div class="grid">
                <div class="stat">
                    <div class="num" id="total-pacientes">0</div>
                    <div class="label">Pacientes</div>
                </div>
                <div class="stat">
                    <div class="num" id="total-agendamentos">0</div>
                    <div class="label">Agendamentos</div>
                </div>
                <div class="stat">
                    <div class="num" id="total-fila">0</div>
                    <div class="label">Na Fila</div>
                </div>
                <div class="stat">
                    <div class="num" id="total-atendimentos">0</div>
                    <div class="label">Atendimentos</div>
                </div>
            </div>
        </div>
        <div class="card">
            <h2>Endpoints da API</h2>
            <ul class="endpoints">
                <li><span class="method get">GET</span> <code>/api/pacientes</code> — Listar pacientes</li>
                <li><span class="method post">POST</span> <code>/api/pacientes</code> — Cadastrar paciente</li>
                <li><span class="method get">GET</span> <code>/api/pacientes/busca?cpf=</code> — Buscar por CPF</li>
                <li><span class="method get">GET</span> <code>/api/profissionais</code> — Listar profissionais</li>
                <li><span class="method post">POST</span> <code>/api/profissionais</code> — Cadastrar profissional</li>
                <li><span class="method get">GET</span> <code>/api/agendamentos</code> — Listar agendamentos</li>
                <li><span class="method post">POST</span> <code>/api/agendamentos</code> — Criar agendamento</li>
                <li><span class="method get">GET</span> <code>/api/fila</code> — Ver fila de espera</li>
                <li><span class="method post">POST</span> <code>/api/fila</code> — Adicionar à fila</li>
                <li><span class="method post">POST</span> <code>/api/fila/chamar</code> — Chamar próximo</li>
                <li><span class="method get">GET</span> <code>/api/atendimentos</code> — Listar atendimentos</li>
                <li><span class="method post">POST</span> <code>/api/atendimentos</code> — Registrar atendimento</li>
                <li><span class="method get">GET</span> <code><a href="/painel">/painel</a></code> — Painel da sala de espera</li>
            </ul>
        </div>
        <div class="card">
            <h2>Sobre</h2>
            <p>PIM VI — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas — UNIP EaD</p>
            <p style="margin-top:8px">Sistema desenvolvido com Python (Flask), SQL Server e MongoDB.</p>
        </div>
    </div>
    <script>
        async function atualizarStats() {
            try {
                const [pac, ag, fi, at] = await Promise.all([
                    fetch('/api/pacientes').then(r => r.json()),
                    fetch('/api/agendamentos').then(r => r.json()),
                    fetch('/api/fila').then(r => r.json()),
                    fetch('/api/atendimentos').then(r => r.json())
                ]);
                document.getElementById('total-pacientes').textContent = pac.length;
                document.getElementById('total-agendamentos').textContent = ag.length;
                document.getElementById('total-fila').textContent = fi.filter(f => f.status === 'aguardando').length;
                document.getElementById('total-atendimentos').textContent = at.length;
            } catch(e) { console.error(e); }
        }
        atualizarStats();
        setInterval(atualizarStats, 5000);
    </script>
</body>
</html>
"""

PAINEL_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SaúdePOP — Painel de Chamada</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #1e293b; color: white;
               display: flex; flex-direction: column; align-items: center; min-height: 100vh;
               padding: 40px 20px; }
        h1 { font-size: 36px; margin-bottom: 10px; }
        .subtitle { color: #94a3b8; font-size: 18px; margin-bottom: 40px; }
        .chamando { background: #2563eb; border-radius: 16px; padding: 40px; text-align: center;
                    width: 100%; max-width: 700px; margin-bottom: 30px; }
        .chamando .label { font-size: 18px; color: #93c5fd; margin-bottom: 10px; }
        .chamando .nome { font-size: 42px; font-weight: bold; }
        .chamando .consultorio { font-size: 20px; color: #bfdbfe; margin-top: 10px; }
        .proximos { width: 100%; max-width: 700px; }
        .proximos h2 { font-size: 20px; color: #94a3b8; margin-bottom: 15px; }
        .proximo-item { display: flex; align-items: center; padding: 15px 20px;
                       background: #334155; border-radius: 8px; margin-bottom: 8px; }
        .proximo-item .pos { font-size: 24px; font-weight: bold; margin-right: 20px; color: #60a5fa; }
        .proximo-item .info { flex: 1; }
        .proximo-item .info .nome { font-size: 18px; }
        .proximo-item .info .cons { font-size: 14px; color: #94a3b8; }
        .footer { margin-top: 40px; color: #64748b; font-size: 16px; }
        .vazio { text-align: center; color: #64748b; font-size: 20px; padding: 40px; }
    </style>
</head>
<body>
    <h1>SaúdePOP</h1>
    <div class="subtitle">Painel de Chamada</div>
    <div id="conteudo">
        <div class="vazio">Nenhum paciente na fila</div>
    </div>
    <div class="footer">
        <span id="hora"></span> &nbsp;|&nbsp; Atualização automática a cada 5 segundos
    </div>
    <script>
        async function atualizar() {
            document.getElementById('hora').textContent = new Date().toLocaleTimeString('pt-BR');
            try {
                const filaResp = await fetch('/api/fila');
                const fila = await filaResp.json();
                const pacResp = await fetch('/api/pacientes');
                const pacientes = await pacResp.json();
                const pacMap = {};
                pacientes.forEach(p => pacMap[p.id_paciente] = p.nome);

                const chamado = fila.find(f => f.status === 'chamado');
                const aguardando = fila.filter(f => f.status === 'aguardando');
                let html = '';
                if (chamado) {
                    html += '<div class="chamando">';
                    html += '<div class="label">CHAMANDO</div>';
                    html += '<div class="nome">' + (pacMap[chamado.id_paciente] || 'Paciente') + '</div>';
                    html += '<div class="consultorio">Consultório ' + chamado.id_consultorio + '</div>';
                    html += '</div>';
                }
                if (aguardando.length > 0) {
                    html += '<div class="proximos"><h2>Próximos na fila</h2>';
                    aguardando.slice(0, 5).forEach((item, i) => {
                        html += '<div class="proximo-item">';
                        html += '<div class="pos">' + (i + 1) + '</div>';
                        html += '<div class="info"><div class="nome">' + (pacMap[item.id_paciente] || 'Paciente') + '</div>';
                        html += '<div class="cons">Consultório ' + item.id_consultorio + '</div></div></div>';
                    });
                    html += '</div>';
                }
                if (!chamado && aguardando.length === 0) {
                    html = '<div class="vazio">Nenhum paciente na fila</div>';
                }
                document.getElementById('conteudo').innerHTML = html;
            } catch(e) { console.error(e); }
        }
        atualizar();
        setInterval(atualizar, 5000);
    </script>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
