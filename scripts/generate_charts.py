from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Definir caminhos relativos ao script
BASE = Path(__file__).resolve().parents[1]
data_file = BASE / "data" / "tasks.csv"
out_dir = BASE / "docs" / "dashboards" / "graficos"
out_dir.mkdir(parents=True, exist_ok=True)

if not data_file.exists():
    print(f"Arquivo de dados não encontrado: {data_file}")
    exit(1)

df = pd.read_csv(data_file)

# Estilo visual
plt.style.use('ggplot')

# Gráfico 1: Tarefas por Status
status_counts = df["status"].value_counts()
plt.figure(figsize=(10, 6))
status_counts.plot(kind="bar", color='skyblue')
plt.title("Tarefas por Status", fontsize=14, fontweight='bold')
plt.xlabel("Status", fontsize=12)
plt.ylabel("Quantidade", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(out_dir / "por-status.png", dpi=300)
plt.close()

# Gráfico 2: Tarefas por Área
area_counts = df["area"].value_counts()
plt.figure(figsize=(10, 6))
area_counts.plot(kind="pie", autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Distribuição de Tarefas por Área", fontsize=14, fontweight='bold')
plt.ylabel("") # Remover o label do eixo Y
plt.tight_layout()
plt.savefig(out_dir / "por-area.png", dpi=300)
plt.close()

# Gráfico 3: Entregas (Volume)
df["closed_at"] = pd.to_datetime(df["closed_at"], errors="coerce")
done = df[df["status"] == "Concluído"].copy()
if not done.empty:
    done["mes"] = done["closed_at"].dt.to_period("M").astype(str)
    monthly = done["mes"].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    monthly.plot(kind="line", marker="o", color='green', linewidth=2)
    plt.title("Histórico de Entregas (Throughput)", fontsize=14, fontweight='bold')
    plt.xlabel("Mês", fontsize=12)
    plt.ylabel("Quantidade Concluída", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(out_dir / "throughput.png", dpi=300)
    plt.close()
else:
    print("Nenhuma tarefa concluída para gerar o gráfico de entregas.")

print("Gráficos gerados com sucesso em docs/dashboards/graficos/")
