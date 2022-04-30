INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 1

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 2

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 3

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 4

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 5

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 6

INSERT INTO local(
    id_norte, id_sul, id_leste, id_oeste, e_hostil, nivel, terreno, precisa_veiculo)
    VALUES (null, null, null, null, true, 4, 'Terrestre', false); -- 7

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 1, 'Guerreiro incansável', 10, 1, 1, 96, 24, 'Jogador'); -- 1

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bandido', 10, 1, 20, 45, 65, 'Carlos'); -- 2

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bandido', 10, 1, 25, 18, 23, 'Walter'); -- 3

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bandido', 10, 1, 22, 19, 38, 'Walter'); -- 4

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bandido', 10, 1, 23, 78, 51, 'Walter'); -- 5

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bandido Chefe', 10, 1, 42, 100, 28, 'Walter'); -- 6

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bonzinho', 10, 99, 33, 69, 37, 'Walter'); -- 7

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bonzinho', 10, 99, 33, 85, 60, 'Walter'); -- 8

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bonzinho', 10, 99, 33, 35, 66, 'Walter'); -- 9

INSERT INTO personagem(
    vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, coordenadax, coordenaday, nome)
    VALUES (100, 100, 'Bonzinho', 10, 99, 33, 81, 49, 'Walter'); -- 10

INSERT INTO sobrevivente(
    furtividade, id_personagem, id_local)
    VALUES (1, null, null);

INSERT INTO dialogo(
    descricao)
    VALUES ('Hello World !');

INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (true, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (false, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (false, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (false, null, null, null);
INSERT INTO npc(
    e_hostil, id_personagem, id_local, id_dialogo)
    VALUES (false, null, null, null);

INSERT INTO mochila(id_personagem)
VALUES (null);

INSERT INTO tipo_item(descricao)
VALUES ('Pistola'); -- 1

INSERT INTO tipo_item(descricao)
VALUES ('Arma Grande'); -- 2

INSERT INTO tipo_item(descricao)
VALUES ('armadura'); -- 3

INSERT INTO tipo_item(descricao)
VALUES ('poção'); -- 4

INSERT INTO armadura(defesa, material, durabilidade, id_tipo_item)
VALUES (20, 'Peitoral de Aço', 50, null);

INSERT INTO consumivel(descricao, efeito, valor, id_tipo_item)
VALUES ('Recupera vida', 'vida', 100, null);

INSERT INTO arma(dano, descricao, durabilidade, municao, id_tipo_item)
VALUES (20, 'Revólver', 50, 60, null);

INSERT INTO arma(dano, descricao, durabilidade, municao, id_tipo_item)
VALUES (40, 'Espingarda', 50, 25, null);

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (5, 1, null, 30, 35, null, null); -- revolver

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (5, 1, null, 65, 20, null, null); -- espingarda

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (6, 1, null, 20, 40, null, null); -- armadura

INSERT INTO item(peso, nivel, id_mochila, coordenadaX, coordenadaY, id_local, id_tipo_item)
VALUES (3, 1, null, 64, 64, null, null); --poção