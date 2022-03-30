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