def cart_count(request):
    """Add cart count (number of distinct items) to all template contexts."""
    cart = request.session.get('cart', {})
    count = sum(item.get('quantity', 0) for item in cart.values())
    return {
        'cart_count': count,
    }
