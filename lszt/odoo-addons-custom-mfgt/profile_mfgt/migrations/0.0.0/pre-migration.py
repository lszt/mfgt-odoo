def migrate(cr, version):
    cr.execute("UPDATE public.ir_ui_view set active='f' where key like 'profile_mfgt.%'")
    cr.execute("UPDATE public.ir_ui_view set active='f' where key like 'account_payment_sale.%'")
    cr.execute("UPDATE public.ir_ui_view set active='f' where key like 'account_payment_partner.%'")
