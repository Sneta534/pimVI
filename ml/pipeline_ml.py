"""
SaúdePOP — Pipeline de Machine Learning e Análise de Dados
===========================================================
Este script implementa o pipeline completo de análise e modelagem preditiva
para o sistema de prontuário eletrônico e fila inteligente.

Problemas abordados:
1. Previsão de falta (no-show) — Classificação binária
2. Estimativa de tempo de espera — Regressão

Autor: PIM VI — UNIP EaD
"""

import os
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resultados")
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_atendimentos.csv")


def gerar_dataset(n=2000):
    """Gera dataset simulado de atendimentos de clínica popular."""
    np.random.seed(42)

    dias = ["seg", "ter", "qua", "qui", "sex", "sab"]
    tipos = ["clinica_geral", "pediatria", "ginecologia", "ortopedia"]
    sexos = ["M", "F"]

    dados = {
        "id_agendamento": range(1, n + 1),
        "dia_semana": np.random.choice(dias, n, p=[0.20, 0.18, 0.17, 0.17, 0.16, 0.12]),
        "hora_agendamento": np.random.choice(range(7, 19), n),
        "tipo_consulta": np.random.choice(tipos, n, p=[0.40, 0.25, 0.20, 0.15]),
        "idade_paciente": np.random.normal(45, 18, n).clip(1, 95).astype(int),
        "sexo": np.random.choice(sexos, n, p=[0.42, 0.58]),
        "distancia_km": np.random.exponential(5, n).clip(0.5, 30).round(1),
        "consultas_anteriores": np.random.poisson(3, n),
        "faltas_anteriores": np.random.poisson(0.8, n).clip(0, 8),
        "qtd_fila": np.random.poisson(6, n).clip(0, 20),
    }

    df = pd.DataFrame(dados)

    prob_falta = 0.15
    prob_falta += 0.08 * (df["dia_semana"] == "seg")
    prob_falta += 0.05 * (df["hora_agendamento"] >= 16)
    prob_falta += 0.02 * (df["distancia_km"] > 10)
    prob_falta += 0.05 * (df["faltas_anteriores"] >= 2)
    prob_falta -= 0.03 * (df["consultas_anteriores"] >= 5)
    prob_falta = prob_falta.clip(0.05, 0.60)

    df["compareceu"] = (np.random.random(n) > prob_falta).astype(int)

    tempo_base = 15.0
    tempo_base += df["qtd_fila"] * 2.5
    tempo_base += 5.0 * (df["dia_semana"] == "seg")
    tempo_base += 3.0 * (df["hora_agendamento"].between(10, 12))
    tempo_base += np.random.normal(0, 5, n)
    df["tempo_espera_min"] = tempo_base.clip(2, 60).round(1)

    csv_path = DATA_PATH
    df.to_csv(csv_path, index=False)
    print(f"Dataset gerado: {csv_path} ({len(df)} registros)")

    return df


def carregar_dados():
    """Carrega e limpa o dataset."""
    if not os.path.exists(DATA_PATH):
        print("Dataset não encontrado. Gerando dados simulados...")
        return gerar_dataset()

    df = pd.read_csv(DATA_PATH)
    print(f"Dataset carregado: {len(df)} registros")

    n_antes = len(df)
    df = df.drop_duplicates()
    df = df.dropna()
    n_depois = len(df)
    print(f"Limpeza: {n_antes - n_depois} registros removidos")

    return df


def analise_exploratoria(df):
    """Realiza análise exploratória dos dados."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n" + "=" * 60)
    print("ANÁLISE EXPLORATÓRIA DE DADOS")
    print("=" * 60)

    print(f"\nTotal de registros: {len(df)}")
    print(f"Variáveis: {len(df.columns)}")
    print(f"\nTaxa de comparecimento: {df['compareceu'].mean():.1%}")
    print(f"Taxa de falta: {1 - df['compareceu'].mean():.1%}")

    print("\n--- Taxa de falta por dia da semana ---")
    taxa_dia = df.groupby("dia_semana")["compareceu"].apply(lambda x: 1 - x.mean())
    for dia in ["seg", "ter", "qua", "qui", "sex", "sab"]:
        if dia in taxa_dia.index:
            print(f"  {dia}: {taxa_dia[dia]:.1%}")

    print("\n--- Tempo médio de espera ---")
    print(f"  Média: {df['tempo_espera_min'].mean():.1f} min")
    print(f"  Mediana: {df['tempo_espera_min'].median():.1f} min")
    print(f"  Máximo: {df['tempo_espera_min'].max():.1f} min")

    print("\n--- Correlações com 'compareceu' ---")
    numericas = df.select_dtypes(include=[np.number])
    corr = numericas.corr()["compareceu"].drop("compareceu").sort_values(key=abs, ascending=False)
    for var, val in corr.head(5).items():
        print(f"  {var}: {val:.3f}")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Análise Exploratória — SaúdePOP", fontsize=14)

    ordem_dias = ["seg", "ter", "qua", "qui", "sex", "sab"]
    taxa_dia_ordenada = taxa_dia.reindex(ordem_dias)
    axes[0, 0].bar(taxa_dia_ordenada.index, taxa_dia_ordenada.values, color="coral")
    axes[0, 0].set_title("Taxa de Falta por Dia da Semana")
    axes[0, 0].set_ylabel("Taxa de Falta")

    axes[0, 1].hist(df["tempo_espera_min"], bins=20, color="steelblue", edgecolor="white")
    axes[0, 1].set_title("Distribuição do Tempo de Espera")
    axes[0, 1].set_xlabel("Minutos")
    axes[0, 1].set_ylabel("Frequência")

    taxa_hora = df.groupby("hora_agendamento")["compareceu"].apply(lambda x: 1 - x.mean())
    axes[1, 0].plot(taxa_hora.index, taxa_hora.values, marker="o", color="darkred")
    axes[1, 0].set_title("Taxa de Falta por Horário")
    axes[1, 0].set_xlabel("Hora")
    axes[1, 0].set_ylabel("Taxa de Falta")

    axes[1, 1].boxplot(
        [
            df[df["compareceu"] == 1]["distancia_km"],
            df[df["compareceu"] == 0]["distancia_km"],
        ],
        labels=["Compareceu", "Faltou"],
    )
    axes[1, 1].set_title("Distância por Comparecimento")
    axes[1, 1].set_ylabel("Distância (km)")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, "analise_exploratoria.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"\nGráficos salvos em: {fig_path}")


def preparar_features(df):
    """Prepara features para modelagem."""
    df_ml = df.copy()

    df_ml = pd.get_dummies(df_ml, columns=["dia_semana", "tipo_consulta", "sexo"], drop_first=True)

    colunas_excluir = ["id_agendamento", "compareceu", "tempo_espera_min"]
    feature_cols = [c for c in df_ml.columns if c not in colunas_excluir]

    X = df_ml[feature_cols]
    y_class = df_ml["compareceu"]
    y_reg = df_ml["tempo_espera_min"]

    return X, y_class, y_reg, feature_cols


def modelo_noshow(X, y, feature_cols):
    """Treina e avalia modelos de previsão de no-show."""
    print("\n" + "=" * 60)
    print("MODELO 1: PREVISÃO DE FALTA (NO-SHOW)")
    print("=" * 60)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\n--- Regressão Logística ---")
    lr = LogisticRegression(random_state=42, max_iter=1000)
    lr.fit(X_train_scaled, y_train)
    y_pred_lr = lr.predict(X_test_scaled)
    y_prob_lr = lr.predict_proba(X_test_scaled)[:, 1]

    print(f"Acurácia: {accuracy_score(y_test, y_pred_lr):.3f}")
    print(f"AUC-ROC: {roc_auc_score(y_test, y_prob_lr):.3f}")
    print(classification_report(y_test, y_pred_lr, target_names=["Falta", "Compareceu"]))

    print("\n--- Random Forest ---")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    y_prob_rf = rf.predict_proba(X_test)[:, 1]

    print(f"Acurácia: {accuracy_score(y_test, y_pred_rf):.3f}")
    print(f"AUC-ROC: {roc_auc_score(y_test, y_prob_rf):.3f}")
    print(classification_report(y_test, y_pred_rf, target_names=["Falta", "Compareceu"]))

    print("\n--- Feature Importance (Random Forest) ---")
    importances = pd.Series(rf.feature_importances_, index=feature_cols)
    importances = importances.sort_values(ascending=False)
    for feat, imp in importances.head(5).items():
        print(f"  {feat}: {imp:.3f}")

    print("\n--- Ajuste de Hiperparâmetros (Grid Search) ---")
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [5, 10, 15],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid,
        cv=5,
        scoring="roc_auc",
        n_jobs=-1,
        verbose=0,
    )
    grid_search.fit(X_train, y_train)
    print(f"Melhores parâmetros: {grid_search.best_params_}")
    print(f"Melhor AUC-ROC (CV): {grid_search.best_score_:.3f}")

    best_rf = grid_search.best_estimator_
    y_pred_best = best_rf.predict(X_test)
    y_prob_best = best_rf.predict_proba(X_test)[:, 1]
    print(f"AUC-ROC (teste): {roc_auc_score(y_test, y_prob_best):.3f}")
    print(f"F1-Score (teste): {f1_score(y_test, y_pred_best):.3f}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    top_feat = importances.head(8)
    axes[0].barh(top_feat.index[::-1], top_feat.values[::-1], color="forestgreen")
    axes[0].set_title("Feature Importance — Random Forest")
    axes[0].set_xlabel("Importância")

    cm = confusion_matrix(y_test, y_pred_best)
    im = axes[1].imshow(cm, cmap="Blues")
    axes[1].set_title("Matriz de Confusão — Random Forest (otimizado)")
    axes[1].set_xlabel("Predito")
    axes[1].set_ylabel("Real")
    axes[1].set_xticks([0, 1])
    axes[1].set_yticks([0, 1])
    axes[1].set_xticklabels(["Falta", "Compareceu"])
    axes[1].set_yticklabels(["Falta", "Compareceu"])
    for i in range(2):
        for j in range(2):
            axes[1].text(j, i, str(cm[i, j]), ha="center", va="center", fontsize=14)
    plt.colorbar(im, ax=axes[1])

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, "modelo_noshow.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"\nGráficos salvos em: {fig_path}")

    return best_rf


def modelo_tempo_espera(X, y, feature_cols):
    """Treina e avalia modelos de estimativa de tempo de espera."""
    print("\n" + "=" * 60)
    print("MODELO 2: ESTIMATIVA DE TEMPO DE ESPERA")
    print("=" * 60)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\n--- Regressão Linear ---")
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    y_pred_lr = lr.predict(X_test_scaled)

    rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    mae_lr = mean_absolute_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    print(f"RMSE: {rmse_lr:.1f} min")
    print(f"MAE: {mae_lr:.1f} min")
    print(f"R²: {r2_lr:.3f}")

    print("\n--- Gradient Boosting Regressor ---")
    gb = GradientBoostingRegressor(n_estimators=200, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)
    y_pred_gb = gb.predict(X_test)

    rmse_gb = np.sqrt(mean_squared_error(y_test, y_pred_gb))
    mae_gb = mean_absolute_error(y_test, y_pred_gb)
    r2_gb = r2_score(y_test, y_pred_gb)
    print(f"RMSE: {rmse_gb:.1f} min")
    print(f"MAE: {mae_gb:.1f} min")
    print(f"R²: {r2_gb:.3f}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].scatter(y_test, y_pred_lr, alpha=0.4, s=10, label="Reg. Linear", color="blue")
    axes[0].scatter(y_test, y_pred_gb, alpha=0.4, s=10, label="Gradient Boosting", color="red")
    lims = [0, 65]
    axes[0].plot(lims, lims, "k--", alpha=0.5)
    axes[0].set_xlabel("Tempo Real (min)")
    axes[0].set_ylabel("Tempo Predito (min)")
    axes[0].set_title("Real vs Predito")
    axes[0].legend()

    modelos = ["Reg. Linear", "Gradient Boosting"]
    rmses = [rmse_lr, rmse_gb]
    maes = [mae_lr, mae_gb]
    x_pos = np.arange(len(modelos))
    width = 0.35
    axes[1].bar(x_pos - width / 2, rmses, width, label="RMSE", color="steelblue")
    axes[1].bar(x_pos + width / 2, maes, width, label="MAE", color="coral")
    axes[1].set_xticks(x_pos)
    axes[1].set_xticklabels(modelos)
    axes[1].set_ylabel("Minutos")
    axes[1].set_title("Comparação de Modelos")
    axes[1].legend()

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, "modelo_tempo_espera.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"\nGráficos salvos em: {fig_path}")

    return gb


def main():
    """Executa o pipeline completo de ML."""
    print("=" * 60)
    print("SaúdePOP — Pipeline de Machine Learning")
    print("=" * 60)

    df = carregar_dados()

    analise_exploratoria(df)

    X, y_class, y_reg, feature_cols = preparar_features(df)

    modelo_noshow(X, y_class, feature_cols)

    modelo_tempo_espera(X, y_reg, feature_cols)

    print("\n" + "=" * 60)
    print("PIPELINE CONCLUÍDO COM SUCESSO")
    print(f"Resultados salvos em: {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    main()
