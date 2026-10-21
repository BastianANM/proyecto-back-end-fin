def carrito_context(request):
    """permite agregar al numero de figuras en el carrito desde cualquier plantilla"""
    carrito = request.session.get('carrito', {})
    total_items = sum(item.get('cantidad', 0) for item in carrito.values())
    return {
        'total_items': total_items
    }