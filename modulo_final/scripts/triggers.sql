CREATE OR REPLACE FUNCTION atualiza_capacidade_carregamento()
RETURNS trigger AS
$$
DECLARE
	id_personagem INT;
	skill TEXT;
	vvalue INT;
BEGIN
	id_personagem=(SELECT DISTINCT m.id_personagem FROM mochila m INNER JOIN item i ON old.id_mochila = m.id);
	SELECT DISTINCT INTO skill, vvalue
    CASE WHEN dano IS NOT NULL THEN 'dano'
        WHEN valor IS NOT NULL THEN 'valor'
        WHEN defesa IS NOT NULL THEN 'defesa'
        ELSE NULL
       END,
    coalesce(dano,coalesce(valor,defesa))
    FROM item i 
    LEFT join arma aa ON i.id_tipo_item = aa.id_tipo_item 
    LEFT join consumivel co ON i.id_tipo_item = co.id_tipo_item
    LEFT join armadura ar ON i.id_tipo_item = ar.id_tipo_item 
    WHERE i.id_tipo_item = 1 AND i.id_mochila = 1;
	
	raise notice 'valores: "%" / "%"', skill, vvalue;
	-- SE ADICIONA ITEM NA MOCHILA
	IF(new.id_mochila IS NOT NULL) THEN
		UPDATE personagem SET capacidade_carregamento = capacidade_carregamento - new.peso WHERE id=id_personagem;
		
		IF(skill = 'dano') THEN
			UPDATE personagem set ataque = vvalue + ataque WHERE id=id_personagem;
		END IF;
		
		IF(skill = 'valor') THEN
			UPDATE personagem set vida = vvalue + vida WHERE id=id_personagem;
			DELETE FROM item i WHERE i.id = new.id;
		END IF;
		
		IF(skill = 'defesa') THEN
			UPDATE personagem set defesa = vvalue + defesa WHERE id=id_personagem;
		END IF;
	END IF;
	
	-- SE DROPA ITEM
	IF(new.id_mochila IS NULL AND old.id_mochila IS NOT NULL) THEN
		UPDATE personagem SET capacidade_carregamento = capacidade_carregamento + old.peso WHERE id=id_personagem;
		
		IF(skill = 'dano') THEN
			UPDATE personagem set ataque = ataque - vvalue WHERE id=id_personagem;
		END IF;
		
		IF(skill = 'defesa') THEN
			UPDATE personagem set defesa = defesa - vvalue WHERE id=id_personagem;
		END IF;
	END IF;
	
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER  atualiza_capacidade_carregamento_trigger
AFTER INSERT OR UPDATE ON item
FOR EACH ROW 
EXECUTE PROCEDURE atualiza_capacidade_carregamento();