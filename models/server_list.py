from odoo import fields, models


class ServerStatusLog(models.Model):
    _name = "server_status"
    _description = "log the status of servers"

    name = fields.Char('Server name')
    ip_addr = fields.Char('Ip address')
    is_online = fields.Boolean('Status')
    num_player = fields.Integer('Number player')

    def fetch_external_data(self):
        url = "http://api.example.com/data"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.update_data(data)

    def update_data(self, data):
        ...