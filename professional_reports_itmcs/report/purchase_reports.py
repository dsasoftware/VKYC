from odoo import api, models


#  purchase order reports 
class ReportPurchaseReport(models.AbstractModel):
    _name = 'report.purchase.report_purchaseorder'
 
    @api.model
    def render_html(self, docids, data=None):
        purchase_obj = self.env['purchase.order'].browse(docids[0])
#         self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
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
            'docs': purchase_obj,
            'data': data,
            'doc' :user,
        }
        return self.env['report'].render('purchase.report_purchaseorder', values=docargs)



