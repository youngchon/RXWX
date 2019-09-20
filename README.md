# RXWX
Receive aviation weather and airport information

## Planning

Inital thoughts on using this is to setup a domain to receive emails (or sms) containing the metars/ATIS of a particular airport.

This would be using the FAA approved weather breifing tools from the AWC.


## Examples Text/inputs
KRNT; S50; KPWU;  <-- should only show metars
KRNT; KPWT; 50; TAF <-- should show a Flight plan in the order and 50 miles of. TAF provided as well
KRNT; GRAPHICAL; <-- ascii of the metar.


## Responses
SMS capable responses
