def migrate(cr, version):
    cr.execute('UPDATE public.ir_ui_view set active='f' where id=1035')