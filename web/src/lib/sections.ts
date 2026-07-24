import type { CollectionKey } from 'astro:content';

export type Section = {
  key: CollectionKey;
  label: string;
  href: string;
  icon: string;
  editDir: string;   // pasta em docs/
  intro: string;
  dateSort?: boolean; // ordenar por data desc
};

export const sections: Record<string, Section> = {
  atas: {
    key: 'atas', label: 'Atas', href: '/atas', icon: 'atas', editDir: 'atas', dateSort: true,
    intro: 'Registros deliberativos de todas as reuniões da diretoria — o histórico versionado do que foi discutido e decidido.',
  },
  decisoes: {
    key: 'decisoes', label: 'Decisões', href: '/decisoes', icon: 'decisoes', editDir: 'decisoes',
    intro: 'Diretrizes formalizadas no modelo ADR (Architecture/Action Decision Records): contexto, decisão, responsáveis e vigência.',
  },
  comissoes: {
    key: 'comissoes', label: 'Comissões', href: '/comissoes', icon: 'comissoes', editDir: 'comissao',
    intro: 'As frentes de trabalho do campus e seus responsáveis — energia, laboratórios, eventos, SBF, SNCT e impacto.',
  },
  processos: {
    key: 'processos', label: 'Processos', href: '/processos', icon: 'processos', editDir: 'processo',
    intro: 'Editais, acordos de PD&I e declarações — os fluxos formais da pesquisa e extensão do campus.',
  },
  pautas: {
    key: 'pautas', label: 'Pautas', href: '/pautas', icon: 'pautas', editDir: 'pautas',
    intro: 'Planejamento das reuniões e o calendário anual — reuniões quinzenais às sextas-feiras.',
  },
  atividades: {
    key: 'atividades', label: 'Atividades', href: '/atividades', icon: 'reports', editDir: 'atividades', dateSort: true,
    intro: 'Log mensal automático de tarefas e demandas ad-hoc, fora das reuniões deliberativas.',
  },
};
