from odoo import api, models


#  stock  reports 
class ReportStockReport(models.AbstractModel):
    _name = 'report.stock.report_picking'
 
    @api.model
    def render_html(self, docids, data=None):
        sale_obj = self.env['stock.picking'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data=user.company_id
        data = {'sale_header_footer':user.company_id.sale_header_footer ,
                'primary_color': company_data.primary_color ,
                'secondary_color':  company_data.secondary_color,
                'sale_font_color': company_data.sale_font_color}
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': sale_obj,
            'data': data,
            'doc' :user,
        }
        return self.env['report'].render('stock.report_picking', values=docargs)


#  stock  delivery  
class ReportStockDeliveryReport(models.AbstractModel):
    _name = 'report.stock.report_deliveryslip'
 
    @api.model
    def render_html(self, docids, data=None):
        sale_obj = self.env['stock.picking'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data=user.company_id
        data = {'sale_header_footer':user.company_id.sale_header_footer ,
                'primary_color': company_data.primary_color ,
                'secondary_color':  company_data.secondary_color,
                'sale_font_color': company_data.sale_font_color}
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': sale_obj,
            'data': data,
            'doc' :user,
        }
        return self.env['report'].render('stock.report_deliveryslip', values=docargs)


