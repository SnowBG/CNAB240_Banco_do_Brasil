'''
Autor: Emerson Lara
Título: Procesa Arquivo de Retorno Banco do Brasil
Descrição: Este script interpreta o Arquivo de Remessa de retorno referente aos
boletos provenientes do Banco do Brasil e grava os dados em uma planilha.
'''

class Retorno():
    def __init__(self):
        self.file = "retorno.txt"
        self.path = "c:/Users/emerson/Documents/Nova pasta/"

    def obter_dados(self):
        with open(self.path + self.file, 'r') as f:
            self.retorno = f.readlines()
            self.retorno.remove('\n')
            self.header_arquivo(self.retorno[0])
            self.header_lote(self.retorno[1])

    def header_arquivo(self, linha):
        """
        Interpreta o Header do arquivo.
        Args:
            - linha: string com a linha referente ao header do arquivo.

        """
        codigo_banco = linha[:3]
        lote_servico = linha[3:7]
        tipo_registro = linha[7:8]
        febraban1 = linha[8:17]
        tipo_inscricao = linha[17:18]
        numero_inscricao = linha[18:32]
        nr_convenio_cobrancaBB = linha[32:41]
        cobranca_cedenteBB = linha[41:45]
        nr_carteira_cobrancaBB = linha[45:47]
        nr_variacao_carteira_cobrancaBB = linha[47:50]
        reservadoBB1 = linha[50:52]
        agencia_mantenedora = linha[52:57]
        dig_verificador_agencia = linha[57:58]
        numero_conta_corrente = linha[58:70]
        dig_verificador_conta = linha[70:71]
        dig_verificador_ag_conta = linha[72:72]
        nome_empresa = linha[72:102]
        nome_banco = linha[102:132]
        febraban2 = linha[132:142]
        cod_remessa_retorno = linha[142:143]
        data_geracao_arquivo = linha[143:151]
        hora_geracao_arquivo = linha[151:157]
        numero_seq_arquivo = linha[157:163]
        nm_ver_layout_arquivo = linha[163:166]
        densidade_gravacao_arquivo = linha[166:171]
        reservadoBB2 = linha[171:191]
        reservadoEmp1 = linha[191:211]
        febraban3 = linha[211:240]

        print(codigo_banco,
              lote_servico,
              tipo_registro,
              febraban1,
              tipo_inscricao,
              numero_inscricao,
              nr_convenio_cobrancaBB,
              cobranca_cedenteBB,
              nr_carteira_cobrancaBB,
              nr_variacao_carteira_cobrancaBB,
              reservadoBB1,
              agencia_mantenedora,
              dig_verificador_agencia,
              numero_conta_corrente,
              dig_verificador_conta,
              dig_verificador_ag_conta,
              nome_empresa,
              nome_banco,
              febraban2,
              cod_remessa_retorno,
              data_geracao_arquivo,
              hora_geracao_arquivo,
              numero_seq_arquivo,
              nm_ver_layout_arquivo,
              densidade_gravacao_arquivo,
              reservadoBB2,
              reservadoEmp1,
              febraban3
              )
    def header_lote(self, linha):
        """
        Interpreta o Header do arquivo.
        Args:
            - linha: string com a linha referente ao header do lote.

        """
        codigo_banco_comp = linha[0:3]
        lote_servico = linha[3:7]
        tipo_registro = linha[7:8]
        tipo_operacao = linha[8:9]
        tipo_servico = linha[9:11]
        febraban1 = linha[11:13]
        nm_ver_layout_lote = linha[13:16]
        febraban2 = linha[16:17]
        tipo_inscricao = linha[17:18]
        nr_inscricao_empresa = linha[18:33]
        nr_convenio_cobrancaBB = linha[33:42]
        cobranca_cedenteBB = linha[42:46]
        nr_carteira_cobrancaBB = linha[46:48]
        nr_variacao_carteira_cobrancaBB = linha[48:51]
        id_remessa_testes = linha[51:53]


        print(
            codigo_banco_comp,
            lote_servico,
            tipo_registro,
            tipo_operacao,
            tipo_servico,
            febraban1,
            nm_ver_layout_lote,
            febraban2,
            tipo_inscricao,
            nr_inscricao_empresa,
            nr_convenio_cobrancaBB,
            cobranca_cedenteBB,
            nr_carteira_cobrancaBB,
            nr_variacao_carteira_cobrancaBB,
            id_remessa_testes
            )

if __name__ == '__main__':
    r = Retorno()
    r.obter_dados()
