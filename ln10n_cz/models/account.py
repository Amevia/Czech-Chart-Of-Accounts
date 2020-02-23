from odoo import api, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _prepare_liquidity_account(self, name, company, currency_id, type):
        res = super(AccountJournal, self)._prepare_liquidity_account(name, company, currency_id, type)
        if company.chart_template_id.get_external_id()[1] == 'l10n_cz.czech_chart_template':
            if res['code'] == '211':
                res['name'] = 'Pokladna'
                res.update({
                    'group_id': self.env.ref('l10n_cz.account_group_21').id,
                    })
            elif res['code'] == '221':
                res['name'] = 'Bankovní účty'
                res.update({
                    'group_id': self.env.ref('l10n_cz.account_group_22').id,
                    })
        return res
