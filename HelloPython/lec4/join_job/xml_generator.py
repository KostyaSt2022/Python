from user_interface import preassure_view
from user_interface import wind_speed_view
from user_interface import temperature_view

def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(temperature_view(device))
    xml += '    <preassure units = "mmHg">{}</preassure>\n'\
        .format(temperature_view(device))
    
    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml