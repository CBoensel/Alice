from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api")

from . import (
    orders,
    orders_form,
    billing_form,
    identity,
    partner,
    webhooks,
)

from . import orders_merchant

bp.register_blueprint(identity.bp)
bp.register_blueprint(orders.bp)
bp.register_blueprint(partner.bp)

bp.register_blueprint(webhooks.bp)

bp.register_blueprint(orders_merchant.bp)

bp.register_blueprint(orders_form.bp)
bp.register_blueprint(billing_form.bp)
