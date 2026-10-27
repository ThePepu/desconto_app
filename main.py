from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService


if __name__ == "__main__":
    service = PedidoService()

    pedido1 = Pedido("Leonardo", DescontoVIP())
    pedido1.valor_original = 100

    pedido2 = Pedido("Maria", DescontoNormal())
    pedido2.valor_original = 200

    pedido3 = Pedido("João", DescontoPremium())
    pedido3.valor_original = 300

    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()
