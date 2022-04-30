UPDATE local SET id_norte = 2 ,id_sul = 3 WHERE id = 1;
UPDATE local SET id_sul = 1 WHERE id = 2;
UPDATE local SET id_norte = 1, id_leste = 5, id_oeste = 4 WHERE id = 3;
UPDATE local SET id_leste = 3 WHERE id = 4;
UPDATE local SET id_oeste = 3 ,id_norte = 6 ,id_sul = 7 WHERE id = 5;
UPDATE local SET id_sul = 5 WHERE id = 6;
UPDATE local SET id_norte = 5 WHERE id = 7;

UPDATE sobrevivente SET id_personagem = 1, id_local = 1 WHERE id = 1;

UPDATE npc SET id_personagem = 2, id_local = 3 WHERE id = 1;
UPDATE npc SET id_personagem = 3, id_local = 5 WHERE id = 2;
UPDATE npc SET id_personagem = 4, id_local = 6 WHERE id = 3;
UPDATE npc SET id_personagem = 5, id_local = 6 WHERE id = 4;
UPDATE npc SET id_personagem = 6, id_local = 7 WHERE id = 5;
UPDATE npc SET id_personagem = 7, id_local = 1 WHERE id = 6;
UPDATE npc SET id_personagem = 8, id_local = 1 WHERE id = 7;
UPDATE npc SET id_personagem = 9, id_local = 2 WHERE id = 8;
UPDATE npc SET id_personagem = 10, id_local = 4 WHERE id = 9;

UPDATE armadura SET id_tipo_item = 3 WHERE id = 1;

UPDATE consumivel SET id_tipo_item = 4 WHERE id = 1;

UPDATE arma SET id_tipo_item = 1 WHERE id = 1;
UPDATE arma SET id_tipo_item = 2 WHERE id = 2;

UPDATE item SET id_tipo_item = 1, id_local = 2 WHERE id = 1;
UPDATE item SET id_tipo_item = 2, id_local = 6 WHERE id = 2;
UPDATE item SET id_tipo_item = 3, id_local = 4 WHERE id = 3;
UPDATE item SET id_tipo_item = 4, id_local = 2 WHERE id = 4;

UPDATE mochila SET id_personagem = 1 WHERE id = 1;