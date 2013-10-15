import time
from openerp.report import report_sxw

class stock_quality_report(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(stock_quality_report, self).__init__(cr, uid, name, context=context)
        print 'stock_quality_report parser'
        self.localcontext.update({
            'time': time,
        })

report_sxw.report_sxw(
    'stock_move_quality',
    'stock.move',
    'addons/stock_quality_report/stock_quality_report.rml',
    parser=stock_quality_report
)
