-- SALVA ULTIMA POSICAO DO SOBREVIVENTE (checkpoint)
UPDATE sobrevivente
    SET coordenadaX = '?', coordenadaY = '?', id_local = '?'
    WHERE sobrevivente.id = '?';


-- DROPA ITEM 
UPDATE item
    SET id_mochila = null, coordenadaX = '?', coordenadaY = '?', id_local = '?'
    WHERE item.id = '?';

-- DROPA ITEM (ALTERNATIVA)
UPDATE item
    SET id_mochila = null, coordenadaX = subquery.x, coordenadaY = subquery.y
    FROM (SELECT s.coordenadaX x, s.coordenadaY y FROM sobrevivente s WHERE s.id = '?') AS subquery
    WHERE item.id = '?';

-- PEGA ITEM
UPDATE item
    SET id_mochila = subquery.id_mochila, coordenadaX = null, coordenadaY = null, id_local = null
    FROM (SELECT m.id id_mochila FROM mochila m INNER JOIN sobrevivente s ON m.id_personagem = s.id_personagem WHERE s.id = '?') AS subquery
    WHERE item.id = '?';

-- DIRIGE VEICULO
UPDATE veiculo
    SET id_motorista = '?'
    WHERE veiculo.id = '?';

-- LARGA VEICULO
UPDATE veiculo
    SET id_motorista = null, coordenadaX = '?', coordenadaY = '?', id_local = '?'
    WHERE veiculo.id = '?';

-- TROCAR DE SALA
    -- DADOS DA SALA
    SELECT * FROM local WHERE id = '?';

    -- DADOS DOS NPCS
    SELECT * FROM npc n INNER JOIN personagem per ON n.id_personagem = per.id WHERE id_local = '?';

    -- DADOS DOS ITENS
    SELECT * FROM item WHERE id_local = '?' AND id_mochila = null;

    -- DADOS DOS VEICULOS
    SELECT * FROM veiculo WHERE id_local = '?';

-- GET DADOS PLAYER
select
	s.id as id_sobrevivente,
	s.nome as nome_sobrevivente,
	s.furtividade,
	s.id_personagem,
	s.coordenadax,
	s.coordenaday,
	s.id_local,
	p.vida,
	p.nivel,
	p.caracteristica,
	p.capacidade_carregamento,
	p.defesa,
	p.ataque,
	m.id as id_mochila
from
	sobrevivente s
inner join personagem p on
	s.id_personagem = p.id
inner join mochila m on
	m.id_personagem = p.id;

-- SET DADOS PLAYER (salvar)
-- start a transaction
BEGIN;

    UPDATE sobrevivente s
        SET s.furtividade = '?', s.coordenadax = '?', s.coordenaday = '?', s.id_local = '?'
        WHERE s.id_personagem = '?';
        
    UPDATE personagem p
        SET p.vida = '?', p.nivel = '?', p.caracteristica = '?', p.capacidade_carregamento = '?', p.defesa = '?', p.ataque = '?'
        WHERE p.id = '?';

-- commit the transaction
COMMIT;

-- VISUALIZA MOCHILA
select
	distinct
	case
		when dano is not null then 'dano'
		when valor is not null then 'valor'
		when defesa is not null then 'defesa'
		else null
	end as tipo,
	coalesce(dano, coalesce(valor, defesa)) as value,
	i.id,
	i.peso,
	i.nivel,
	i.id_mochila,
	i.coordenadax,
	i.coordenaday,
	i.id_local,
	i.id_tipo_item,
	aa.dano,
	aa.descricao as descricao_arma,
	aa.durabilidade as durabilidade_arma,
	aa.municao,
	co.descricao as descricao_consumivel,
	co.efeito,
	co.valor as valor_consumivel,
	ar.defesa,
	ar.material,
	ar.durabilidade as durabilidade_armadura
from
	item i
left join arma aa on
	i.id_tipo_item = aa.id_tipo_item
left join consumivel co on
	i.id_tipo_item = co.id_tipo_item
left join armadura ar on
	i.id_tipo_item = ar.id_tipo_item
where
	i.id_tipo_item = '?'
	and i.id_mochila = '?';