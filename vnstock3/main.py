
from common.vnstock import Vnstock


stock = Vnstock().stock(symbol='ACB', source='TCBS')

# VCI là nguồn dữ liệu từ CK Vietcap bên cạnh nguồn từ TCBS
stock.listing.all_symbols()