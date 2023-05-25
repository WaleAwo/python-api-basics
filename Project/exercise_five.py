import xml.etree.ElementTree as et

import requests


def test_xml():
    response = requests.get("https://parabank.parasoft.com/parabank/services/bank/customers/12212")
    xml = et.ElementTree(et.fromstring(response.content))

    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/xml'
    assert xml.getroot().tag == 'customer'
    assert xml.find('phoneNumber').text == '310-447-4121'
    assert len(xml.findall('.//address/*')) == 4
