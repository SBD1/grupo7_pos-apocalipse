class DtoGetPlayer:
  def __init__(self,
    id_sobrevivente,
    nome_sobrevivente,
    furtividade,
    id_personagem,
    coordenadax,
    coordenaday,
    id_local,
    vida,
    nivel,
    caracteristica,
    capacidade_carregamento,
    defesa,
    ataque,
    id_mochila):
    self.id_sobrevivente = id_sobrevivente
    self.nome_sobrevivente = nome_sobrevivente
    self.furtividade = furtividade
    self.id_personagem = id_personagem
    self.coordenadax = coordenadax
    self.coordenaday = coordenaday
    self.id_local = id_local
    self.vida = vida
    self.nivel = nivel
    self.caracteristica = caracteristica
    self.capacidade_carregamento = capacidade_carregamento
    self.defesa = defesa
    self.ataque = ataque
    self.id_mochila = id_mochila