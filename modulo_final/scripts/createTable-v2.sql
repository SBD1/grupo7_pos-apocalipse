CREATE TABLE IF NOT EXISTS local(
	id SERIAL PRIMARY KEY,
	id_norte INT,
	id_sul INT,
	id_leste INT,
	id_oeste INT,
	e_hostil BOOLEAN,
	nivel INT,
	terreno VARCHAR(255),
	precisa_veiculo BOOLEAN,
	CONSTRAINT fk_norte
      FOREIGN KEY(id_norte) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_sul
      FOREIGN KEY(id_sul) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_leste
      FOREIGN KEY(id_leste) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_oeste
      FOREIGN KEY(id_oeste) 
	  REFERENCES local(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS personagem(
    id SERIAL PRIMARY KEY,
    vida INT,
    nivel INT,
    caracteristica VARCHAR(255),
    capacidade_carregamento INT,
	defesa INT,
	ataque INT
);

CREATE TABLE IF NOT EXISTS sobrevivente(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
	furtividade INT,
	id_personagem INT,
	coordenadaX INT,
	coordenadaY INT,
	id_local INT,
	CONSTRAINT fk_personagem
      FOREIGN KEY(id_personagem) 
	  REFERENCES personagem(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_local
      FOREIGN KEY(id_local) 
	  REFERENCES local(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS dialogo(
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS npc(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
	e_hostil BOOLEAN,
	id_personagem INT,
	id_local INT,
	id_dialogo INT,
	CONSTRAINT fk_personagem
      FOREIGN KEY(id_personagem) 
	  REFERENCES personagem(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_local
      FOREIGN KEY(id_local) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_dialogo
      FOREIGN KEY(id_dialogo) 
	  REFERENCES dialogo(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS tipo_veiculo(
    id SERIAL PRIMARY KEY,
    vel_max INT,
    descricao VARCHAR(255),
    durabilidade INT,
    tipo VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS veiculo(
    id SERIAL PRIMARY KEY,
    nivel_gasolina INT,
	id_tipo_veiculo INT,
	id_motorista INT,
	coordenadaX INT,
	coordenadaY INT,
	id_local INT,
	CONSTRAINT fk_local
      FOREIGN KEY(id_local) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_tipo_veiculo
      FOREIGN KEY(id_tipo_veiculo) 
	  REFERENCES tipo_veiculo(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_motorista
      FOREIGN KEY(id_motorista) 
	  REFERENCES sobrevivente(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS mochila(
	id SERIAL PRIMARY KEY,
	id_personagem INT,
	CONSTRAINT fk_personagem
      FOREIGN KEY(id_personagem)
	  REFERENCES personagem(id)
	  ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS tipo_item(
    id SERIAL PRIMARY KEY,
	descricao VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS item(
    id SERIAL PRIMARY KEY,
    peso INT,
    nivel INT,
	id_mochila INT,
	coordenadaX INT,
	coordenadaY INT,
	id_local INT,
	id_tipo_item INT,
	CONSTRAINT fk_mochila
      FOREIGN KEY(id_mochila) 
	  REFERENCES mochila(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_local
      FOREIGN KEY(id_local) 
	  REFERENCES local(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_tipo_item
      FOREIGN KEY(id_tipo_item) 
	  REFERENCES tipo_item(id)
	  ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS arma(
    id SERIAL PRIMARY KEY,
	dano INT,
	descricao VARCHAR(50),
	durabilidade INT,
	municao INT,
	id_tipo_item INT,
	CONSTRAINT fk_tipo_item
      FOREIGN KEY(id_tipo_item) 
	  REFERENCES tipo_item(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS consumivel(
    id SERIAL PRIMARY KEY,
	descricao VARCHAR(50),
	efeito VARCHAR(255),
	valor INT,
	id_tipo_item INT,
	CONSTRAINT fk_tipo_item
      FOREIGN KEY(id_tipo_item) 
	  REFERENCES tipo_item(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS armadura(
    id SERIAL PRIMARY KEY,
	defesa INT,
	material VARCHAR(50),
	durabilidade VARCHAR(255),
	id_tipo_item INT,
	CONSTRAINT fk_tipo_item
      FOREIGN KEY(id_tipo_item) 
	  REFERENCES tipo_item(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS missao(
    id SERIAL PRIMARY KEY,
    nivel INT,
    historia VARCHAR(255),
	id_npc INT,
	id_sobrevivente INT,
	CONSTRAINT fk_npc
      FOREIGN KEY(id_npc) 
	  REFERENCES npc(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_sobrevivente
      FOREIGN KEY(id_sobrevivente) 
	  REFERENCES sobrevivente(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS sobrevivente_completa_missao(
    id SERIAL PRIMARY KEY,
    id_sobrevivente INT,
    id_missao INT,
	id_item_recompensa INT,
	CONSTRAINT fk_sobrevivente
      FOREIGN KEY(id_sobrevivente) 
	  REFERENCES sobrevivente(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_missao
      FOREIGN KEY(id_missao) 
	  REFERENCES missao(id)
	  ON DELETE SET NULL,
	CONSTRAINT fk_item_recompensa
      FOREIGN KEY(id_item_recompensa) 
	  REFERENCES item(id)
	  ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS objetivo(
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255),
    progresso INT,
	id_missao INT,
	CONSTRAINT fk_missao
      FOREIGN KEY(id_missao) 
	  REFERENCES missao(id)
	  ON DELETE SET NULL
);

