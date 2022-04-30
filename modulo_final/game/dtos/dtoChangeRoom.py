from dtos.dtoDadosSala import DtoDadosSala
from dtos.dtoDadosNpcsSala import DtoDadosNpcsSala
from dtos.dtoDadosArmasSala import DtoDadosArmasSala
from dtos.dtoDadosArmadurasSala import DtoDadosArmadurasSala
from dtos.dtoDadosConsumiveisSala import DtoDadosConsumiveisSala
from dtos.dtoDadosVeiculosSala import DtoDadosVeiculosSala


class DtoChangeRoom:
  def __init__(self, dados_sala, dados_npcs_sala, dados_veiculos_sala, dados_armas_sala, dados_armaduras_sala, dados_consumiveis_sala):
    self.dados_sala = DtoDadosSala(
      dados_sala[0]['id'],
      dados_sala[0]['id_norte'],
      dados_sala[0]['id_sul'],
      dados_sala[0]['id_leste'],
      dados_sala[0]['id_oeste'],
      dados_sala[0]['e_hostil'],
      dados_sala[0]['nivel'],
      dados_sala[0]['terreno'],
      dados_sala[0]['precisa_veiculo'])
    self.dados_npcs_sala = []
    for npc in dados_npcs_sala:
      self.dados_npcs_sala.append(
        DtoDadosNpcsSala(
          npc['id_npc'],
          npc['nome'],
          npc['e_hostil'],
          npc['id_personagem'],
          npc['id_local'],
          npc['id_dialogo'],
          npc['vida'],
          npc['nivel'],
          npc['caracteristica'],
          npc['capacidade_carregamento'],
          npc['defesa'],
          npc['ataque'],
          npc['x'],
          npc['y']))

    self.dados_armas_sala = []
    for arma in dados_armas_sala:
      self.dados_armas_sala.append(
        DtoDadosArmasSala(
          arma['id_arma'],
          arma['dano'],
          arma['descricao'],
          arma['durabilidade'],
          arma['id_tipo_item'],
          arma['municao'],
          arma['id'],
          arma['peso'],
          arma['nivel'],
          arma['id_mochila'],
          arma['coordenadax'],
          arma['coordenaday'],
          arma['id_local'],
        )
      )

    self.dados_armaduras_sala = []
    for armadura in dados_armaduras_sala:
      self.dados_armaduras_sala.append(
        DtoDadosArmadurasSala(
          armadura['id_armadura'],
          armadura['defesa'],
          armadura['material'],
          armadura['durabilidade'],
          armadura['id_tipo_item'],
          armadura['id'],
          armadura['peso'],
          armadura['nivel'],
          armadura['id_mochila'],
          armadura['coordenadax'],
          armadura['coordenaday'],
          armadura['id_local'],
        )
      )

    self.dados_consumiveis_sala = []
    for consumivel in dados_consumiveis_sala:
      self.dados_consumiveis_sala.append(
        DtoDadosConsumiveisSala(
          consumivel['id_consumivel'],
          consumivel['descricao'],
          consumivel['efeito'],
          consumivel['valor'],
          consumivel['id_tipo_item'],
          consumivel['id'],
          consumivel['peso'],
          consumivel['nivel'],
          consumivel['id_mochila'],
          consumivel['coordenadax'],
          consumivel['coordenaday'],
          consumivel['id_local'],
        )
      )
    self.dados_veiculos_sala = []
    for veiculo in dados_veiculos_sala:
      self.dados_veiculos_sala.append(
        DtoDadosVeiculosSala(
          veiculo['id'],
          veiculo['nivel_gasolina'],
          veiculo['id_tipo_veiculo'],
          veiculo['id_motorista'],
          veiculo['coordenadax'],
          veiculo['coordenaday'],
          veiculo['id_local']))