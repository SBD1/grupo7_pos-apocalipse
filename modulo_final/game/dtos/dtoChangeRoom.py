from dtos.dtoDadosSala import DtoDadosSala
from dtos.dtoDadosNpcsSala import DtoDadosNpcsSala
from dtos.dtoDadosItensSala import DtoDadosItensSala
from dtos.dtoDadosVeiculosSala import DtoDadosVeiculosSala


class DtoChangeRoom:
  def __init__(self, dados_sala, dados_npcs_sala, dados_itens_sala, dados_veiculos_sala):
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
          npc['ataque']))
    self.dados_itens_sala = []
    for item in dados_itens_sala:
      self.dados_itens_sala.append(
        DtoDadosItensSala(
          item['id'],
          item['peso'],
          item['nivel'],
          item['id_mochila'],
          item['coordenadax'],
          item['coordenaday'],
          item['id_local'],
          item['id_tipo_item']))
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