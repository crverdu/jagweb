
class Carrito:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get("carrito")
        if not cart:
            # save an empty cart in the session
            cart = self.session['carrito'] = {}
        self.cart = cart

    def agregarProd(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminarProd(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()

    def restar_prod(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.eliminarProd(producto)
                break
        self.guardar_carrito()
    
    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True
