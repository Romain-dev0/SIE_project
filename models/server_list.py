from odoo import fields, models
import requests


class ServerStatusLog(models.Model):
    _name = "server_status"
    _description = "log the status of servers"

    name = fields.Char('Server name')
    ip_addr = fields.Char('Ip address')
    is_online = fields.Boolean('Status')
    num_player = fields.Integer('Number player')

    def fetch_external_data(self):
            if not self.ip_addr:
                print("no_ip_addr")
                return
            url = f"https://api.mcsrvstat.us/3/{self.ip_addr}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.update_data(data)
            else:
                _logger.error(f"Failed to fetch data for IP {self.ip_addr}: {response.status_code}")


    def update_data(self, data):
            #updating data
            self.is_online = data.get('online', False)
            self.num_player = data.get('players', {}).get('online', 0)
            self.name = data.get('motd', {}).get('clean', [self.name])[0] 
