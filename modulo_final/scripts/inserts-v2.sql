INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Aquático', false);

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 1, 'Guerreiro incansável', 10, 1, 2, 96, 24, 'Venon');

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Alienigena estranho', 10, 99, 99, 96, 24, 'Carlos');

INSERT INTO sobrevivente(
    furtividade, id_personagem, id_local)
    VALUES (1, 1, 1);

INSERT INTO dialogo(
    descricao)
    VALUES ('Hello World !');

INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, 2, 1, 1);

INSERT INTO mochila(id_personagem)
VALUES (1);

INSERT INTO mochila(id_personagem)
VALUES (2);

INSERT INTO missao(nivel, historia, id_npc, id_sobrevivente)
VALUES (1, 'História Missão 1', 1, 1);

INSERT INTO objetivo(descricao, progresso, id_missao)
VALUES ('Descrição Objetivo 1 Missão 1', 0, 1);

INSERT INTO objetivo(descricao, progresso, id_missao)
VALUES ('Descrição Objetivo 2 Missão 1', 0, 1);

INSERT INTO missao(nivel, historia, id_npc, id_sobrevivente)
VALUES (1, 'História Missão 2', 1, 1);

INSERT INTO objetivo(descricao, progresso, id_missao)
VALUES ('Descrição Objetivo 1 Missão 2', 0, 2);

INSERT INTO objetivo(descricao, progresso, id_missao)
VALUES ('Descrição Objetivo 2 Missão 2', 0, 2);

INSERT INTO tipo_item(descricao)
VALUES ('Capacete');

INSERT INTO tipo_item(descricao)
VALUES ('Colete');

INSERT INTO tipo_item(descricao)
VALUES ('Poção de vida');

INSERT INTO tipo_item(descricao)
VALUES ('Poção de furtividade');

INSERT INTO tipo_item(descricao)
VALUES ('Arma de Fogo');

INSERT INTO tipo_item(descricao)
VALUES ('Arma Branca');

INSERT INTO armadura(defesa, material, durabilidade, id_tipo_item)
VALUES (2, 'Folha', 50, 1);

INSERT INTO armadura(defesa, material, durabilidade, id_tipo_item)
VALUES (10, 'Couro', 50, 2);

INSERT INTO consumivel(descricao, efeito, valor, id_tipo_item)
VALUES ('Regenera a vida', 'vida', 25, 3);

INSERT INTO consumivel(descricao, efeito, valor, id_tipo_item)
VALUES ('Aumenta a furtividade', 'furtividade', 10, 4);

INSERT INTO arma(dano, descricao, durabilidade, municao, id_tipo_item)
VALUES (50, 'Revólver', 50, 6, 3);

INSERT INTO arma(dano, descricao, durabilidade, municao, id_tipo_item)
VALUES (100, 'Espingarda', 50, 3, 5);

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (5, 1, 1, 10, 10, 1, 1);

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (6, 1, 1, 10, 10, 1, 2);

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (3, 1, 1, 10, 10, 1, 2);

INSERT INTO tipo_veiculo(vel_max, descricao, durabilidade, tipo)
VALUES (100, 'Carro 1', 500, 'Terrestre');

INSERT INTO tipo_veiculo(vel_max, descricao, durabilidade, tipo)
VALUES (150, 'Carro 2', 300, 'Terrestre');

INSERT INTO veiculo(nivel_gasolina, id_tipo_veiculo, id_motorista, coordenadaX, coordenadaY, id_local)
VALUES (50, 1, 1, 10, 10, 1);