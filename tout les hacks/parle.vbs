Dim message, sapi
message=InputBox("Entez le texte que vous voulez parlez)","Speak This")
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message