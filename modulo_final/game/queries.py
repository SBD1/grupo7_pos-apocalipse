import database

from dtos.dtoChangeRoom import DtoChangeRoom
from dtos.dtoGetPlayer import DtoGetPlayer
from dtos.dtoGetBackpack import DtoGetBackpack

#Buscar dados ao trocar de sala
def change_room(id_local):
  dados_sala = database.consultar_db('SELECT * FROM local WHERE id = ' + str(id_local) + ';')
  dados_npcs_sala = database.consultar_db('SELECT n.id as id_npc, n.nome, n.e_hostil, n.id_personagem , n.id_local , n.id_dialogo , per.vida , per.nivel , per.caracteristica , per.capacidade_carregamento , per.defesa , per.ataque  FROM npc n INNER JOIN personagem per ON n.id_personagem = per.id WHERE id_local = '+ str(id_local) +';')
  dados_itens_sala = database.consultar_db('SELECT * FROM item WHERE id_local = '+ str(id_local) +' AND id_mochila = null;')
  dados_veiculos_sala = database.consultar_db('SELECT * FROM veiculo WHERE id_local = '+ str(id_local) +';')

  print("executando 4 queries:")
  print('SELECT * FROM local WHERE id = ' + str(id_local) + ';')
  print('SELECT n.id as id_npc, n.nome, n.e_hostil, n.id_personagem , n.id_local , n.id_dialogo , per.vida , per.nivel , per.caracteristica , per.capacidade_carregamento , per.defesa , per.ataque  FROM npc n INNER JOIN personagem per ON n.id_personagem = per.id WHERE id_local = '+ str(id_local) +';')
  print('SELECT * FROM item WHERE id_local = '+ str(id_local) +' AND id_mochila = null;')
  print('SELECT * FROM veiculo WHERE id_local = '+ str(id_local) +';')

  retorno = DtoChangeRoom(dados_sala, dados_npcs_sala, dados_itens_sala, dados_veiculos_sala)
  return retorno

#Buscar dados do player ao inicializar o game
def get_player():
  dados_sobrevivente = database.consultar_db('select s.id as id_sobrevivente,s.nome as nome_sobrevivente,s.furtividade,s.id_personagem,s.coordenadax,s.coordenaday,s.id_local,p.vida,p.nivel,p.caracteristica,p.capacidade_carregamento,p.defesa,p.ataque,m.id as id_mochila from sobrevivente s inner join personagem p on s.id_personagem = p.id inner join mochila m on m.id_personagem = p.id;')
  
  print('Executando query: ' + 'select s.id as id_sobrevivente,s.nome as nome_sobrevivente,s.furtividade,s.id_personagem,s.coordenadax,s.coordenaday,s.id_local,p.vida,p.nivel,p.caracteristica,p.capacidade_carregamento,p.defesa,p.ataque,m.id as id_mochila from sobrevivente s inner join personagem p on s.id_personagem = p.id inner join mochila m on m.id_personagem = p.id;')

  retorno = DtoGetPlayer(
    dados_sobrevivente[0]['id_sobrevivente'],
    dados_sobrevivente[0]['nome_sobrevivente'],
    dados_sobrevivente[0]['furtividade'],
    dados_sobrevivente[0]['id_personagem'],
    dados_sobrevivente[0]['coordenadax'],
    dados_sobrevivente[0]['coordenaday'],
    dados_sobrevivente[0]['id_local'],
    dados_sobrevivente[0]['vida'],
    dados_sobrevivente[0]['nivel'],
    dados_sobrevivente[0]['caracteristica'],
    dados_sobrevivente[0]['capacidade_carregamento'],
    dados_sobrevivente[0]['defesa'],
    dados_sobrevivente[0]['ataque'],
    dados_sobrevivente[0]['id_mochila'])
  return retorno

#Altera as informacoes do player quando o jogo é salvo
def update_player(id_personagem, furtividade, coordenada_x, coordenada_y, id_local, vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque):
  database.inserir_db('BEGIN; UPDATE sobrevivente s SET furtividade = '+ str(furtividade) 
  +', coordenadax = '+ str(coordenada_x) 
  +', coordenaday = '+ str(coordenada_y) 
  +', id_local = '+ str(id_local) 
  +' WHERE s.id_personagem = '+ str(id_personagem) 
  +'; UPDATE personagem p SET vida = '+ str(vida) 
  +', nivel = '+ str(nivel) 
  +', caracteristica =  \''+ caracteristica +'\', capacidade_carregamento = '+ str(capacidade_carregamento) 
  +', defesa = '+ str(defesa) 
  +', ataque = '+ str(ataque) 
  +' WHERE p.id = '+ str(id_personagem) 
  +'; COMMIT;');

  print('executando query: ')
  print('BEGIN; UPDATE sobrevivente s SET furtividade = '+ str(furtividade) 
  +', coordenadax = '+ str(coordenada_x) 
  +', coordenaday = '+ str(coordenada_y) 
  +', id_local = '+ str(id_local) 
  +' WHERE s.id_personagem = '+ str(id_personagem) 
  +'; UPDATE personagem p SET vida = '+ str(vida) 
  +', nivel = '+ str(nivel) 
  +', caracteristica =  \''+ caracteristica +'\', capacidade_carregamento = '+ str(capacidade_carregamento) 
  +', defesa = '+ str(defesa) 
  +', ataque = '+ str(ataque) 
  +' WHERE p.id = '+ str(id_personagem) 
  +'; COMMIT;')

#Visualiza mochila
def get_backpack(id_tipo_item, id_mochila):
  dados_mochila = database.consultar_db('select distinct case when dano is not null then \'dano\' when valor is not null then \'valor\' when defesa is not null then \'defesa\' else null end as tipo, coalesce(dano, coalesce(valor, defesa)) as value, i.id, i.peso, i.nivel, i.id_mochila, i.coordenadax, i.coordenaday, i.id_local, i.id_tipo_item, aa.dano, aa.descricao as descricao_arma, aa.durabilidade as durabilidade_arma, aa.municao, co.descricao as descricao_consumivel, co.efeito, co.valor as valor_consumivel, ar.defesa, ar.material, ar.durabilidade as durabilidade_armadura from item i left join arma aa on i.id_tipo_item = aa.id_tipo_item left join consumivel co on i.id_tipo_item = co.id_tipo_item left join armadura ar on i.id_tipo_item = ar.id_tipo_item where i.id_tipo_item = '+ str(id_tipo_item) +' and i.id_mochila = '+ str(id_mochila)+';')
  retorno = [];
  print('executando query: ' + 'select distinct case when dano is not null then \'dano\' when valor is not null then \'valor\' when defesa is not null then \'defesa\' else null end as tipo, coalesce(dano, coalesce(valor, defesa)) as value, i.id, i.peso, i.nivel, i.id_mochila, i.coordenadax, i.coordenaday, i.id_local, i.id_tipo_item, aa.dano, aa.descricao as descricao_arma, aa.durabilidade as durabilidade_arma, aa.municao, co.descricao as descricao_consumivel, co.efeito, co.valor as valor_consumivel, ar.defesa, ar.material, ar.durabilidade as durabilidade_armadura from item i left join arma aa on i.id_tipo_item = aa.id_tipo_item left join consumivel co on i.id_tipo_item = co.id_tipo_item left join armadura ar on i.id_tipo_item = ar.id_tipo_item where i.id_tipo_item = '+ str(id_tipo_item) +' and i.id_mochila = '+ str(id_mochila)+';')
  for item in dados_mochila:
    retorno.append(
      DtoGetBackpack(
        item['tipo'],
        item['value'],
        item['id'],
        item['peso'],
        item['id_mochila'],
        item['coordenadax'],
        item['coordenaday'],
        item['id_local'],
        item['id_tipo_item'],
        item['dano'],
        item['descricao_arma'],
        item['durabilidade_arma'],
        item['municao'],
        item['descricao_consumivel'],
        item['efeito'],
        item['valor_consumivel'],
        item['defesa'],
        item['material'],
        item['durabilidade_armadura']))
  return retorno