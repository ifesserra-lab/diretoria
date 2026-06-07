#!/usr/bin/env python3
"""Generate a Markdown catalog of GitHub repositories."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = BASE_DIR / "docs" / "tools" / "README.md"
DEFAULT_ORG = "ifesserra-lab"
API_URL = "https://api.github.com"

FALLBACK_DESCRIPTIONS = {
    ".github": "Configurações comunitárias e arquivos padrão da organização ifesserra-lab.",
    "dgp.cnqp_lib": "Biblioteca Python para coleta e tratamento de dados do Diretório dos Grupos de Pesquisa do CNPq.",
    "diretoria": "Portal de governança e documentação operacional da DPPGE do IFES Campus Serra.",
    "research_domain_lib": "Biblioteca Python para modelagem e análise de domínios de pesquisa.",
}


def fetch_json(url: str, token: str | None) -> tuple[Any, str | None]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "diretoria-repository-sync",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data, response.headers.get("Link")
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {exc.code}: {body}") from exc


def has_next_page(link_header: str | None) -> bool:
    if not link_header:
        return False
    return any('rel="next"' in part for part in link_header.split(","))


def fetch_repositories(org: str, token: str | None, include_private: bool) -> list[dict[str, Any]]:
    repos: list[dict[str, Any]] = []
    page = 1
    repo_type = "all" if include_private else "public"

    while True:
        query = urlencode(
            {
                "type": repo_type,
                "sort": "full_name",
                "direction": "asc",
                "per_page": 100,
                "page": page,
            }
        )
        data, link_header = fetch_json(f"{API_URL}/orgs/{org}/repos?{query}", token)
        repos.extend(data)

        if not has_next_page(link_header):
            break
        page += 1

    return sorted(repos, key=lambda repo: repo.get("full_name", "").lower())


def markdown_escape(value: Any) -> str:
    text = str(value or "").strip()
    return text.replace("|", "\\|").replace("\n", " ")


def format_bool(repo: dict[str, Any]) -> str:
    if repo.get("archived"):
        return "Arquivado"
    if repo.get("private"):
        return "Privado"
    return "Publico"


def render_markdown(org: str, repos: list[dict[str, Any]]) -> str:
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Ferramentas e repositórios",
        "",
        f"Lista de repositórios da organização GitHub `{org}`, gerada automaticamente uma vez por semana.",
        "",
        f"Última atualização: {updated_at}",
        "",
        f"Total de repositórios: {len(repos)}",
        "",
        "| Repositório | Descrição | Linguagem | Estado | Atualizado em |",
        "| --- | --- | --- | --- | --- |",
    ]

    for repo in repos:
        name = markdown_escape(repo.get("name"))
        url = repo.get("html_url") or "#"
        description = markdown_escape(
            repo.get("description") or FALLBACK_DESCRIPTIONS.get(repo.get("name"), "Sem descrição informada.")
        )
        language = markdown_escape(repo.get("language") or "-")
        state = format_bool(repo)
        updated = str(repo.get("updated_at") or "").split("T")[0] or "-"
        lines.append(f"| [{name}]({url}) | {description} | {language} | {state} | {updated} |")

    lines.extend(
        [
            "",
            "## Manutenção",
            "",
            "Esta página é atualizada pelo workflow semanal `Weekly Repository Catalog`, que executa `scripts/sync_repositories.py` e commita alterações quando a lista muda.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate docs/tools/README.md from GitHub repositories.")
    parser.add_argument("--org", default=os.getenv("GITHUB_ORG", DEFAULT_ORG), help="GitHub organization name.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Markdown output path.")
    parser.add_argument(
        "--include-private",
        action="store_true",
        default=os.getenv("INCLUDE_PRIVATE_REPOS", "").lower() in {"1", "true", "yes"},
        help="Include private repositories visible to the provided token.",
    )
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    repos = fetch_repositories(args.org, token, args.include_private)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(args.org, repos), encoding="utf-8")
    print(f"Generated {output_path} with {len(repos)} repositories.")


if __name__ == "__main__":
    main()
