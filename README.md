# Ronda — Visitas de Enfermagem v3.0

## Abrir e atualizar no GitHub

Para testar no computador, abra `index.html`.
Para atualizar o GitHub Pages, substitua na mesma pasta do programa:

- `index.html`
- `sw.js`
- `manifest.webmanifest`
- `icon-192.png` e `icon-512.png` (podem ser mantidos se já existirem iguais)

Nesta versão atualize também `sw.js`, pois o programa de visitas usa cache para
funcionar offline. Não basta atualizar apenas o HTML e deixar um cache antigo sem
atualização. Reabra o site com internet e confira **v3.0.0** no cabeçalho.
`src/`, `tests/`, `package.json` e `build.py` são arquivos opcionais de desenvolvimento;
não são necessários para o funcionamento do HTML.

A atualização procura os dados da v2 no mesmo endereço e navegador e migra os
cadastros para a v3. A chave antiga não é apagada. Após abrir, use **Dados > Exportar
backup JSON**. Outro aparelho, outro navegador ou outro endereço não compartilha
os dados automaticamente. A importação aceita backups v2 e v3.

## Fluxo de uso

1. Adicione ou edite o paciente no painel ou diretamente em Visitas.
2. Confira leito, identificação e, se disponível, registro/prontuário.
3. Assinale apenas o que foi avaliado. Campos vazios não viram achados normais.
4. O rascunho e as pendências são salvos automaticamente neste aparelho.
5. Clique **Salvar visita e gerar evolução**. Esse momento define a hora da evolução.
6. Revise o texto corrido e use **Copiar esta evolução**, ou **Copiar todas as evoluções**.
7. Para uma nova avaliação, use **Nova visita**. Achados e confirmações são reiniciados;
   dispositivos e datas de instalação são mantidos. Pendências anteriores não somem
   por falta de uma nova avaliação. As versões salvas ficam preservadas no backup.

## Copiar todas as evoluções

O botão abre a relação dos pacientes ativos com visita salva. Selecione quais deseja
incluir, prepare a prévia e copie o bloco revisado. Cada trecho tem:

- marcador de início;
- leito, identificação e registro do paciente;
- data/hora da visita salva;
- evolução em texto corrido;
- marcador de fim, repetindo a identificação.

Rascunhos não salvos não entram no bloco. Visitas de pacientes com alta, transferência
ou óbito ficam fora da seleção em lote; ainda podem ser consultadas individualmente.
A identificação deve ser conferida no prontuário antes de cada colagem. O aplicativo
não envia e-mails nem acessa prontuários. Use o canal autorizado pela instituição para
transferir informações assistenciais.

## Avaliação

- Identificação por botões; alergia abre texto. Sem descrição e sem sinalização positiva,
  registra Alergias não conhecidas. Alergia marcada e não descrita gera pendência.
- Glasgow como padrão, AO/RV/RM e soma somente quando todos são testáveis e preenchidos.
  Alternativas ficam em Trocar escala: AVDI, FOUR e registro de resultado NIHSS.
- Dor numérica, registro FPS-R/Faces, PAINAD e CPOT, com Não foi possível avaliar.
- NIHSS é o registro do resultado obtido com o instrumento completo oficial; o app não
  contém as pranchas nem aplica uma NIHSS abreviada. Faces registra a escolha 0/2/4/6/8/10
  após uso da imagem oficial do serviço. Há links para os instrumentos; as imagens de
  faces não foram redesenhadas ou substituídas por emojis. Referências externas exigem
  internet. Glasgow, AVDI, FOUR, PAINAD e CPOT têm entradas por componentes no aplicativo.
- Respiratório: ruídos por tipo e lobos/lados, múltiplas localizações, murmúrios
  presentes/diminuídos/ausentes. Câmara de falamine removida das opções novas.
- Cardiovascular: edema graduado, pulso, TEC, jugular, bulhas, sopros por focos, clique
  de válvula metálica e localização de marcapasso/CDI.
- Abdome: RH, dor por quadrantes/regiões; mobilidade e dispositivos de auxílio.
- Pele: coloração e hipocoração graduada; lesões por pressão, outras lesões, curativos,
  flebite e tabela de apoio Maddox; prevenção sacral, trocantérica e de calcanhares por lado.
- Flebite gera conferência de indicação/prescrição de Hirudoid/camomila quando não
  confirmados; não gera indicação de tratamento ou prescrição automaticamente.
- Eliminações: volume/período, papagaio ou sonda vesical; cor, grumos e sangramento.
  Evacuação e Bristol, diarreia em dias e episódios/24h, isolamento instituído por
  C. difficile e data da última evacuação ou data desconhecida.
- Nutrição oral/enteral, aceitação e jejum com motivo. Jejum é exclusivo; oral e enteral
  podem coexistir. Achados relevantes e cuidados paliativos são registrados quando marcados.

## Dispositivos e infusões

É possível adicionar vários dispositivos do mesmo tipo. Cada item tem identidade
própria, local, lateralidade, calibre e inserção, com Sem informação. Outro local
abre texto. Sondas de Nutrição/Eliminações e Dispositivos são o mesmo registro;
as correções são compartilhadas, sem duplicação. O calibre deve incluir a unidade
correta, por exemplo **12 Fr** ou **20 G**.

PICC/CVC: mono, duplo ou triplo lúmen. Shilley: 2 ou 3 vias.
Drenos: tipo, local/lado, data, débito/período, aspecto, cor e oscilação para tórax.
Infusões: data no calendário, hora digitada e acesso escolhido entre os venosos
instalados. Sinais flogísticos e extravasamento do AVP são compartilhados entre
Infusões e Dispositivos.

A sonda enteral exige os dados acordados para finalizar a visita: local, lateralidade,
calibre, fixação, decúbito/cabeceira, situação da infusão, taxa e dieta se infundindo,
data ou Sem informação e situação da verificação de posicionamento. Se a verificação
foi realizada, é necessário registrar método e resultado. O aplicativo não inventa
procedimento nem confirma posição por inferência. Resultado inconclusivo ou não
confirmado mantém a pendência. A sonda vesical não exige calibre e data para salvar.

## Pendências

São mostradas diretamente por leito e identificação. Não há seleção de paciente
para visualizar. Pendências automáticas são atualizadas sem duplicação e ficam
vinculadas ao dispositivo ou à lesão correspondente. Concluir registra execução;
uma condição que deixou de existir é arquivada como condição atualizada, sem
falsamente declarar que o cuidado foi realizado. Nova ocorrência reabre a pendência.
Uma pendência manual entra ao digitar na visita ou ao sair do campo no cartão do leito.

Curativo sujo, com sangue, úmido ou descolando gera pendência antes de qualquer prazo.
Valores iniciais solicitados: **48h para avaliação do AVP** e **7 dias para curativos
dos demais acessos venosos**. Os prazos são configuráveis em Dados e devem corresponder
ao protocolo e ao tipo de cobertura. Não são uma validade universal nem ordem automática
de retirada. Data/hora desconhecida gera conferência, sem assumir a data atual.
ACESSO DIFÍCIL mantém o alerta. Cateter longo não vence por tempo de permanência;
seu curativo segue o prazo configurado.

## Evolução

Texto corrido na sequência acordada, com hora de salvamento, dados neurológicos,
exame físico, nutrição, dispositivos, infusões, eliminações, lesões, intervenções,
respostas e pendências. Destaques aparecem na prévia dos achados relevantes, sem
criar tópicos no texto copiado. Metas, pulseiras, medidas de segurança, orientações
e confirmação de sonda só são descritas como realizadas se assinaladas.

## Verificação e limitações

36 testes automatizados passaram, cobrindo migração, edição de paciente, dispositivos
repetidos, sondas vinculadas, prazos, persistência, cálculos de escalas, pendências,
relatórios e cópia em lote. Os testes de interface simulam eventos e verificam o HTML.
O HTML independente foi comparado ao código testado, sem divergências.

O ambiente não permitiu abrir o arquivo no navegador para inspeção visual. Não houve
teste em iPad/iPhone real nem validação clínica institucional. Antes do plantão,
faça um teste com paciente fictício no aparelho: cadastrar, preencher, salvar, copiar,
imprimir e reabrir. Não use os resultados como confirmação automática de segurança
assistencial. O armazenamento local não tem autenticação, criptografia de aplicação
ou sincronização. A instituição define os requisitos de sigilo e documentação.

Para desenvolvimento: `npm test`; após editar `src/`, executar `python3 build.py`.
As referências consultadas constam na aba Dados e no código `src/data.js`.
