import data
import helpers


class TestUrbanRoutes:
    #Verificar se esta conectado a plataforma da Urban
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

#Definir funções
    def test_set_route(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
         # Adicionar em S8
         print("função criada para selecionar o plano")
         pass

    def test_fill_phone_number(self):
         # Adicionar em S8
         print("função criada preencher o número de telefone")
         pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para preencher o método de pagamento")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para deixar um comentario para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para solicitar cobertor e lenços ")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
         print("função criada para solicitar 2 sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para testar se o modelo aparece na busca de carros")
        pass
