CREATE OR REPLACE FUNCTION atualiza_capacidade_carregamento()
RETURNS trigger AS
$$
DECLARE
	id_personagem INT;
BEGIN
	id_personagem=(SELECT DISTINCT m.id_personagem FROM mochila m INNER JOIN item i ON old.id_mochila = m.id);
	-- SE ADICIONA ITEM NA MOCHILA
	IF(new.id_mochila IS NOT NULL) THEN
		UPDATE personagem SET capacidade_carregamento = capacidade_carregamento - new.peso WHERE id=id_personagem;
	END IF;
	
	-- SE DROPA ITEM
	IF(new.id_mochila IS NULL AND old.id_mochila IS NOT NULL) THEN
		UPDATE personagem SET capacidade_carregamento = capacidade_carregamento + old.peso WHERE id=id_personagem;
	END IF;
	
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER  atualiza_capacidade_carregamento_trigger
AFTER INSERT OR UPDATE ON item
FOR EACH ROW 
EXECUTE PROCEDURE atualiza_capacidade_carregamento();